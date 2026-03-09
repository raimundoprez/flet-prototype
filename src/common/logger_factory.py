from datetime import datetime
from typing import Optional
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, Logger, getLogger, Formatter, StreamHandler, FileHandler

import os

class LoggerFactory:
    levels = [DEBUG, INFO, WARNING, ERROR, CRITICAL]

    @classmethod
    def create(cls, name: str, level: int, trace_screen: bool, file_path: Optional[str]) -> Logger:
        """
        Creates a logger object with the parameters given.

        Args:
            name (str): The unique name used to identify the logger.
            level (int): The logging level of the logger.
            trace_screen (bool): Print messages on console.
            file_path (Optional[str]): If provided, a file where log messages will be written.
        
        Returns:
            Logger: A customized logger.

        Raises:
            ValueError: If the logging level is out of range.
            Exception: If StreamHandler, FileHandler, exists or makedirs failed with the parameters given.
        """

        try:
            cls.levels.index(level)
        except ValueError:
            raise ValueError(f'Invalid logging {level=}')

        logger = getLogger(name)
        logger.setLevel(level)

        formatter = Formatter("[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d (%(funcName)s) - %(message)s")

        if trace_screen:
            console_handler = StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        if file_path is not None:
            log_dir = os.path.dirname(file_path)

            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)

            now = datetime.now()
            formatted_date = now.strftime("_%Y_%m_%d_%H_%M_%S_%f")

            file_handler = FileHandler(file_path + formatted_date, mode="w")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger