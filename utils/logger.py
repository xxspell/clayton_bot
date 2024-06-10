
import logging

def setup_logger(log_file="app.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(username)s | %(action)s | %(tokens)s (%(session_tokens)s)')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger