from random import random
from typing import Dict

from ABCPacketGenerator import ABCPacketGenerator


class RandomPacketGenerator(ABCPacketGenerator):

    def __init__(self, configuration: Dict):
        if configuration["type"] != "random":
            raise ValueError("Attempted to create a RandomPacketGenerator with non-random configuration")

        super(RandomPacketGenerator, self).__init__(configuration)
        rate_min, rate_max = 1 / configuration["rate"]
        self.inter_packet_time_min = 1 / rate_max
        self.inter_packet_time_max = 1 / rate_min

        if configuration["start_time"] == "random":
            self.start_time = random() * self.inter_packet_time_min
        else:
            self.start_time = configuration["start_time"]

    def generate(self, simulator_time):
        packets = []
        while self.next_generate_time <= simulator_time:
            # TODO: Append some kind of packet to packets
            packets.append(self.packet_size)
            self.next_generate_time += self.inter_packet_time_min + (
                    self.inter_packet_time_max - self.inter_packet_time_min) * random()
        return packets
