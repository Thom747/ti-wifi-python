from abc import ABC, abstractmethod
from typing import List, Tuple, Dict

from objects.Station import Station
from objects.ul_ofdma_schemes.DisabledUlOfdmaScheme import DisabledUlOfdmaScheme


def create_ul_ofdma_scheme(configuration: Dict) -> "ABCUlOfdmaScheme":
    """
    Return an UL-OFDMA scheme conforming to the specified configuration.

    :param configuration: Dictionary containing configuration of UL-OFDMA scheme. See config.yml for an example.
    :return: an UL-OFDMA scheme conforming to the specified configuration.
    """
    ul_ofdma_type = configuration["type"]
    if ul_ofdma_type == "disabled":
        return DisabledUlOfdmaScheme(configuration)
    elif ul_ofdma_type == "fixed":
        raise NotImplementedError("Fixed UL-OFDMA scheme is not implemented yet")
    elif ul_ofdma_type == "proportional":
        raise NotImplementedError("Proportional UL-OFDMA scheme is not implemented yet")
    else:
        raise ValueError(f"Value {ul_ofdma_type} is not a valid type of UL-OFDMA scheme")

class ABCUlOfdmaScheme(ABC):
    """
    Abstract base class for UL-OFDMA schemes
    """
    @abstractmethod
    def __init__(self, configuration:Dict):
        """
        Create an UL-OFDMA scheme conforming to the specified configuration.

        :param configuration: Dictionary containing configuration of UL-OFDMA scheme. See config.yml for an example.
        """
        pass

    @abstractmethod
    def allocate(self, stations: List[Station]) -> List[Tuple[Station, int]]:
        """
        Allocate RUs among connected stations.

        :param stations: List of stations.
        :return: List of Station, RU allocations. Stations not listed are not scheduled.
        """
        raise NotImplementedError
