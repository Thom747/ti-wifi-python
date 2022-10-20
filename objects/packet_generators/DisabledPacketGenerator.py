from typing import List

from objects.packet_generators.ABCPacketGenerator import ABCPacketGenerator


class DisabledPacketGenerator(ABCPacketGenerator):
    def __init__(self, configuration):
        if configuration["type"] != "disabled":
            raise ValueError("Attempted to create a DisabledPacketGenerator with non-disabled configuration")
        super(DisabledPacketGenerator, self).__init__(configuration)

    def generate(self, simulator_time) -> List:
        return []
