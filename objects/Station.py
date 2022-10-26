from typing import Dict, List
from objects.packet_generators.ABCPacketGenerator import ABCPacketGenerator, create_packet_generator
from collections import deque


def create_stations(configuration: Dict) -> List["Station"]:
    """
    Create a list of stations corresponding to the amount and configuration provided.

    :param configuration: Dictionary containing configuration of stations. See config.yml for an example.
    :return: a list of stations corresponding to the amount and configuration provided.
    """
    amount = configuration["amount"]
    stations = []
    for i in range(amount):
        stations.append(Station(configuration))
    return stations


class Station:
    """
    Class representing a station in a Wi-Fi network
    """

    def __init__(self, configuration: Dict):
        """
        Create a Station conforming to the specified configuration.

        :param configuration: Dictionary containing configuration of Station. See config.yml for an example.
        """
        self.haptic_config: Dict = configuration["haptic"]
        self.video_config: Dict = configuration["video"]

        haptic_queue_size = self.haptic_config["queue_size"] if self.haptic_config["queue_size"] > 0 else None
        video_queue_size = self.video_config["queue_size"] if self.video_config["queue_size"] > 0 else None
        self.packet_queue_haptic: deque = deque(maxlen=haptic_queue_size)
        self.packet_queue_video: deque = deque(maxlen=video_queue_size)

        self.haptic_packet_generator: ABCPacketGenerator = create_packet_generator(
            self.haptic_config["packet_generation"])
        self.video_packet_generator: ABCPacketGenerator = create_packet_generator(
            self.video_config["packet_generation"])

    def generate(self, simulator_time):
        """
        Generate new packets since the last time generate was called.

        :param simulator_time: Time of the simulator
        """
        for packet in self.haptic_packet_generator.generate(simulator_time):
            self.packet_queue_haptic.append(packet)
        for packet in self.video_packet_generator.generate(simulator_time):
            self.packet_queue_video.append(packet)
