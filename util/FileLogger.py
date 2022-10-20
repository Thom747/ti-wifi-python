from util.Logger import Logger, Logfiles


class FileLogger:
    """
    Logger that is dedicated to a single file
    """

    def __init__(self, file: Logfiles, additional_file_parameter):
        """
        Return a FileLogger that will log to the specified file.
        Singleton Logger needs to be instantiated before use.

        :param file: File to log to.
        :param additional_file_parameter: Extension of basename for ACCESS_COLLISION files.
        """
        self.logger = Logger()
        self.filename = self.logger.resolve_filename(file, additional_file_parameter)

    def log(self, message: str, newline: bool = True):
        """
        Log message to file.

        :param message: Message to log.
        :param newline: If True, print a newline after the message. Default True.
        """
        self.logger.log_to_filename(self.filename, message, newline)
