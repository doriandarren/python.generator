import os
import logging
from datetime import datetime


class DailyFileHandler(logging.FileHandler):
    def __init__(self, log_dir, prefix, encoding=None, delay=False):
        self.log_dir = log_dir
        self.prefix = prefix
        self.current_date = datetime.now().strftime("%Y_%m_%d")

        os.makedirs(self.log_dir, exist_ok=True)

        filename = self._build_filename()
        super().__init__(filename, mode="a", encoding=encoding, delay=delay)

    def _build_filename(self):
        return os.path.join(
            self.log_dir,
            f"{self.prefix}_{self.current_date}.log"
        )

    def emit(self, record):
        new_date = datetime.now().strftime("%Y_%m_%d")

        if new_date != self.current_date:
            self.current_date = new_date

            if self.stream:
                self.stream.close()
                self.stream = None

            self.baseFilename = os.path.abspath(self._build_filename())
            self.stream = self._open()

        super().emit(record)