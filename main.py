from argparse import ArgumentParser, Namespace
from pathlib import Path

import yaml

from util.Logger import Logger


def parse_arguments() -> Namespace:
    """
    Register and parse all arguments, returning a Namespace containing all arguments.

    :return: Namespace containing all arguments.
    """
    parser: ArgumentParser = ArgumentParser(description="Simulate a Wi-Fi network with video and tactile data on the "
                                                        "up-link and haptic data on the down-link.")
    parser.add_argument("-c", nargs=1, default="./config.yml", type=Path,
                        help="Location of configuration YAML file. Defaults to ./config.yml", required=False,
                        dest="config_path")
    parser.add_argument("-o", nargs=1, default="./output", type=Path,
                        help="Location of output files. Defaults to ./output", required=False,
                        dest="output_path")

    return parser.parse_args()


def parse_config(config_path: Path):
    """
    Parse configuration file and return contents.

    :param config_path: Path to configuration file.
    :return: Contents of configuration file.
    """
    with open(config_path, 'r') as file:
        return yaml.unsafe_load(file)


def main():
    """
    Run the simulator.
    """
    arguments: Namespace = parse_arguments()
    config = parse_config(arguments.config_path)
    print(config)
    Logger(arguments.output_path)


if __name__ == '__main__':
    main()
