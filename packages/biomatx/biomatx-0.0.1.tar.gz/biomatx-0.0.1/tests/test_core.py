import asyncio
import os

import pytest

import biomatx
from biomatx import Bus, Packet


class SerialMock:
    def __init__(self, event_loop):
        self.closed = True
        self.master, self.slave = os.openpty()
        self.closed = False
        self.port = os.ttyname(self.slave)

    def close(self):
        if self.closed:
            return
        self.closed = True
        os.close(self.master)
        os.close(self.slave)

    async def send(self, module, switch, released):
        await asyncio.to_thread(
            lambda: os.write(self.master, bytes(Packet(module, switch, released)))
        )

    async def read(self):
        data = await asyncio.to_thread(lambda: os.read(self.master, 2))
        return Packet.from_bytes(data)


@pytest.fixture
def serial_mock(event_loop):
    mock = SerialMock(event_loop)
    yield mock
    mock.close()


@pytest.fixture
def bus(event_loop, serial_mock):
    bus = Bus(2)
    bus.events = []

    async def cb(device):
        bus.events.append(device)

    coro = bus.connect(serial_mock.port, cb, loop=event_loop)
    event_loop.run_until_complete(coro)
    return bus


async def gather(*aws):
    return await asyncio.gather(*aws, return_exceptions=True)


def test_import_package():
    assert isinstance(biomatx.__all__, list)


def test_packet():
    pkt = Packet(1, 7, False)
    assert pkt.pressed
    assert bytes(pkt) == b"\x51\x17"
    assert pkt == Packet.from_bytes(b"\x51\x17")


@pytest.mark.asyncio
async def test_bus_read_send(serial_mock, bus):
    # Check that we can read packet
    packet, _ = await gather(bus.read_packet(), serial_mock.send(1, 2, True))
    assert packet == Packet(1, 2, True)

    # Check that we can send packet
    _, packet = await gather(bus.send_packet(packet), serial_mock.read())
    assert packet == Packet(1, 2, True)


@pytest.mark.asyncio
async def test_bus_process_press(serial_mock, bus):
    """Check that the bus process press packets correctly"""
    tasks, _ = await gather(bus.process_packet(), serial_mock.send(1, 2, False))
    await gather(*tasks)
    assert len(bus.events) == 1
    switch = bus.events[0]
    assert isinstance(switch, biomatx.Switch)
    assert switch.module.address == 1
    assert switch.address == 2
    assert switch.pressed
    relay = bus.relay(1, 2)
    assert relay.off


@pytest.mark.asyncio
async def test_bus_process_release(serial_mock, bus):
    """Check that the bus process release packets correctly"""
    # Check that we can process released packets
    tasks, _ = await gather(bus.process_packet(), serial_mock.send(1, 2, True))
    await gather(*tasks)
    assert len(bus.events) == 2
    switch, relay = bus.events
    assert isinstance(switch, biomatx.Switch)
    assert switch.module.address == 1
    assert switch.address == 2
    assert switch.released
    assert isinstance(relay, biomatx.Relay)
    assert relay.module.address == 1
    assert relay.address == 2
    assert relay.on


@pytest.mark.asyncio
async def test_switch_press(serial_mock, bus):
    """Check that switches can be pressed"""
    switch = bus.switch(1, 2)
    _, packet = await gather(switch.press(), serial_mock.read())
    assert packet == Packet(1, 2, False)
    assert switch.pressed


@pytest.mark.asyncio
async def test_switch_release(serial_mock, bus):
    """Check that switches can be released"""
    switch = bus.switch(1, 2)
    _, packet = await gather(switch.release(), serial_mock.read())
    assert packet == Packet(1, 2, True)
    assert switch.released


@pytest.mark.asyncio
async def test_relay_toggle(serial_mock, bus):
    """Check that relays can be toggled"""
    relay = bus.relay(1, 3)
    assert relay.off
    _, packet1, packet2 = await gather(
        relay.toggle(), serial_mock.read(), serial_mock.read()
    )
    assert packet1 == Packet(1, 3, False)
    assert packet2 == Packet(1, 3, True)
    assert relay.on

    _, packet1, packet2 = await gather(
        relay.toggle(), serial_mock.read(), serial_mock.read()
    )
    assert packet1 == Packet(1, 3, False)
    assert packet2 == Packet(1, 3, True)
    assert relay.off


@pytest.mark.asyncio
async def test_relay_force_toggle(serial_mock, bus):
    """Check that relays can be force toggled"""
    relay = bus.relay(1, 3)
    assert relay.off
    await relay.force_toggle()
    assert relay.on
    await relay.force_toggle()
    assert relay.off


def test_bus_loop(event_loop, serial_mock, bus):
    """Check the bus loop"""
    coro = bus.loop()
    event_loop.call_later(0.001, lambda: bus.stop())
    event_loop.run_until_complete(coro)
