class Simulator:

    def __init__(self, configuration):
        self.max_iterations = configuration["general"]["iterations"]
        self.max_duration_s = configuration["general"]["duration"]
        self.ap = None
        self.stations = []

    def add_station(self, station: Station):
        self.stations.append(station)

    def run(self):
