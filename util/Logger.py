from enum import Enum, unique
from pathlib import Path
from typing import Any


@unique
class Logfiles(Enum):
    """
    Enumeration of output files.
    Files are backwards compatible with original simulator.
    """
    ACCESS_COLLISION = "access_collision.txt"
    AP_INTERARRIVAL = "AP-interarrival.txt"
    AP_INTERARRIVAL_VID = "AP-interarrival_vid.txt"
    AP_DELAYS = "APdelays.txt"
    AP_DELAYS_COLLECT_HA = "APdelaysCollect_HA.txt"
    CONFIGURATIONS = "configurations.csv"
    CW_PSI = "cw_psi.csv"
    DELAY_DL_ISOLATED = "delay-DL-isolated.txt"
    DELAY_FILE = "delayFile.txt"
    FRAG_THRESH = "frag_thresh.txt"
    GLOBAL = "global.txt"
    GLOBAL_BUFFER = "global_buffer.txt"
    HAP_DELAY_P = "hap_delay_p.txt"
    KIN_DELAY_P = "kin_delay_p.txt"
    LOGGING = "logging.csv"
    STA_AMPDU = "STA-AMPDU.txt"
    STA_INTERARRIVAL = "STA-interarrival.txt"
    STA_INTERARRIVAL_MU_NOVID = "STA-interarrival-MU-novid.txt"
    STA_INTERARRIVAL_MU_VID = "STA-interarrival-MU-vid.txt"
    STA_INTERARRIVAL_SU_NOVID = "STA-interarrival-SU-novid.txt"
    STA_INTERARRIVAL_SU_VID = "STA-interarrival-SU-vid.txt"
    STA_FILE = "sta_file.txt"
    STA_DELAYS_COLLECT_HA = "STAdelaysCollect_HA.txt"
    STA_DELAYS_COLLECT_VI = "STAdelaysCollect_VI.txt"
    THROUGHPUT_TRACK = "throughput_track.txt"
    VID_DELAY = "vid_delay.txt"
    VID_DELAY_P = "vid_delay_p.txt"
    VID_METADATA_FILE = "vid_metadata_file.txt"


class Logger:
    """
    Singleton logger
    """
    __instance = None

    def __init__(self, output_dir: str = None):
        """
        Return the singleton Logger.

        :param output_dir: If supplied, sets the output directory. Required on first instantiation.
        """
        try:
            self.output_dir: Path = Path(output_dir).resolve()
            self.output_dir.mkdir(parents=True, exist_ok=True)
        except AttributeError:
            try:
                # output_dir is None
                self.output_dir: Path = self.output_dir
            except AttributeError as e:
                raise AttributeError("output_dir is required on first instantiation of Logger") from e

    def __new__(cls, *args, **kwargs):
        # Make Logger a singleton so the output directory can be set once
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    def log(self, file: Logfiles, message: str, additional_file_parameter: Any = None, newline: bool = True):
        """
        Append the message to the specified file.
        If file is Logfiles.ACCESS_COLLISION, additional_file_parameter is required, otherwise it is ignored.

        :param file: File to log to.
        :param message: Message to log.
        :param additional_file_parameter: Extension of basename for ACCESS_COLLISION files.
        :param newline: If True, print a newline after the message. Default True.
        """
        filename = self.resolve_filename(file, additional_file_parameter)
        self.log_to_filename(filename)

    def log_to_filename(self, filename: str, message: str, newline: bool = True):
        """
        Append the message to the specified file.
        In general, it is recommended to use either Logger.log or FileLogger.log instead, to prevent typos.

        :param filename: Filename of file to log to.
        :param message: Message to log.
        :param newline: If True, print a newline after the message. Default True.
        """
        with open(self.output_dir / filename, 'a') as f:
            f.write(message)
            if newline:
                f.write('\n')

    @staticmethod
    def resolve_filename(file: Logfiles, additional_file_parameter) -> str:
        """
        Resolve a Logfiles enum to a filename.
        If file is Logfiles.ACCESS_COLLISION, additional_file_parameter is required, otherwise it is ignored.

        :param file: File to log to.
        :param additional_file_parameter: Extension of basename for ACCESS_COLLISION files.
        :return: Filename of file.
        """
        if file == Logfiles.ACCESS_COLLISION:
            if not additional_file_parameter:
                raise AttributeError("Additional file parameter is required for logging to access_collision files")
            else:
                (basename, extension) = file.value.split(".")
                filename = f"{basename}_{str(additional_file_parameter)}.{extension}"
        else:
            if additional_file_parameter:
                print(f"Ignoring additional file parameter {str(additional_file_parameter)} for file {file.value}.")
            filename = file.value
        return filename
