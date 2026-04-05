leangth_of_wall = 100
print(leangth_of_wall)

import logging
import loguru
from loguru import logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)

logging.info("Program started")
# logging.warning("This is a warning")
# logging.error("This is an error")
import loguru
logging.info(leangth_of_wall)