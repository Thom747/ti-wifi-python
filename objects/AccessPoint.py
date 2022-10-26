from typing import Dict, List

from objects.Station import Station
from objects.ul_ofdma_schemes.ABCUlOfdmaScheme import create_ul_ofdma_scheme, ABCUlOfdmaScheme


class AccessPoint(Station):
    def __init__(self, configuration: Dict, stations: List[Station]):
        super().__init__(configuration)

        self.ul_ofdma_config: Dict = configuration["ul_ofdma"]
        self.ul_ofdma_scheme: ABCUlOfdmaScheme = create_ul_ofdma_scheme(self.ul_ofdma_config)

        self.stations: List[Station] = stations
