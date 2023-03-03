import logging

logger = logging.getLogger('example_logger')
handler = logging.FileHandler('logs/error.log')
fileFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(fileFormat)
logger.addHandler(handler)
