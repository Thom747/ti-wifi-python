from random import random
from typing import Dict

from ABCPacketGenerator import ABCPacketGenerator


class PeriodicPacketGenerator(ABCPacketGenerator):

    def __init__(self, configuration: Dict):
        if configuration["type"] != "periodic":
            raise ValueError("Attempted to create a PeriodicPacketGenerator with non-periodic configuration")

        super(PeriodicPacketGenerator, self).__init__(configuration)
        self.inter_packet_time = 1 / configuration["rate"]

        if configuration["start_time"] == "random":
            self.start_time = random() * self.inter_packet_time
        else:
            self.start_time = configuration["start_time"]

    def generate(self, simulator_time):
        packets = []
        while self.next_generate_time <= simulator_time:
            # TODO: Append some kind of packet to packets
            packets.append(self.packet_size)
            self.next_generate_time += self.inter_packet_time
        return packets
