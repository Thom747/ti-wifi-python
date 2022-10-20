from typing import Dict
from objects.packet_generators.ABCPacketGenerator import ABCPacketGenerator, create_packet_generator
from collections import deque


class Station:
    def __init__(self, configuration: Dict):
        """
        Create a Station conforming to the specified configuration.

        :param configuration: Dictionary containing configuration of Station. See config.yml for an example.
        """
        self.haptic_config: Dict = configuration["haptic"]
        self.video_config: Dict = configuration["video"]

        self.packet_queue_haptic: deque = deque(maxlen=self.haptic_config["queue_size"])
        self.packet_queue_video: deque = deque(maxlen=self.video_config["queue_size"])

        self.haptic_packet_generator: ABCPacketGenerator = create_packet_generator(
            self.haptic_config["packet_generation"])
        self.video_packet_generator: ABCPacketGenerator = create_packet_generator(
            self.video_config["packet_generation"])

    def generate(self, simulator_time):
        for packet in self.haptic_packet_generator.generate(simulator_time):
            self.packet_queue_haptic.append(packet)
        for packet in self.video_packet_generator.generate(simulator_time):
            self.packet_queue_video.append(packet)

    