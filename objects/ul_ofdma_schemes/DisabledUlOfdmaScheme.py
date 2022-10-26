from typing import List, Tuple, Dict

from objects.Station import Station
from objects.ul_ofdma_schemes.ABCUlOfdmaScheme import ABCUlOfdmaScheme


class DisabledUlOfdmaScheme(ABCUlOfdmaScheme):
    """
    UL-OFDMA scheme that schedules no stations for UL-OFDMA.
    """

    def __init__(self, configuration: Dict):
        super(DisabledUlOfdmaScheme, self).__init__(configuration)

    def allocate(self, stations: List[Station]) -> List[Tuple[Station, int]]:
        return []
