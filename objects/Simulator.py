from typing import List

from objects.AccessPoint import AccessPoint
from objects.Station import Station, create_stations


class Simulator:

    def __init__(self, configuration):
        self.stas_config = configuration["stas"]
        self.ap_config = configuration["ap"]
        self.sim_config = configuration["simulation"]
        self.channel_config = configuration["channel"]
        self.max_iterations = self.sim_config["iterations"]
        self.max_duration_s = self.sim_config["duration"]
        self.stations: List[Station] = []
        self.time_us = 0

    @property
    def ap(self):
        return self.ap

    @ap.setter
    def ap(self, ap: AccessPoint):
        self.ap = ap
        assert self.stations == ap.stations

    def run(self):
        for i in range(self.max_iterations):
            self.time_us = 0
            self.stations = create_stations(self.stas_config)
            self.ap = AccessPoint(self.ap_config, self.stations)
            self._simulate()

    def _simulate(self):
