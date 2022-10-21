from abc import ABC, abstractmethod
from typing import Dict, List
from objects.packet_generators.PeriodicPacketGenerator import PeriodicPacketGenerator
from objects.packet_generators.RandomPacketGenerator import RandomPacketGenerator
from objects.packet_generators.DisabledPacketGenerator import DisabledPacketGenerator


def create_packet_generator(configuration: Dict) -> "ABCPacketGenerator":
    """
    Return a packet generator conforming to the specified configuration.

    :param configuration: Dictionary containing configuration of packet generator. See config.yml for an example.
    :return: a packet generator conforming to the specified configuration.
    """
    type = configuration["type"]
    if type == "periodic":
        return PeriodicPacketGenerator(configuration)
    elif type == "random":
        return RandomPacketGenerator(configuration)
    elif type == "disabled":
        return DisabledPacketGenerator(configuration)
    elif type == "correlated":
        # TODO: Implement correlated packet generator
        raise NotImplementedError("Correlated packet generator is not implemented yet")
    else:
        raise ValueError(f"Value {type} is not a valid type of packet generator")


class ABCPacketGenerator(ABC):
    """
    Abstract base class for Packet Generators
    """
    @abstractmethod
    def __init__(self, configuration: Dict):
        """
        Create a Packet Generator conforming to the specified configuration.

        :param configuration: Dictionary containing configuration of Packet Generator. See config.yml for an example.
        """
        self.next_generate_time = 0
        self.packet_size = configuration["size"]
        self.start_time = 0

    @abstractmethod
    def generate(self, simulator_time) -> List:
        """
        Generate new packets until the simulator time is < the next generation time.

        :param simulator_time: Time of simulator
        :return: List of packets
        """
        raise NotImplementedError
