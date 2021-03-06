import logging
logger=logging.getLogger("Demologger")
logger.setLevel(level=logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(level=logging.WARNING)

file_handler=logging.FileHandler(filename='abc.log',mode='w')
file_handler.setLevel(level=logging.ERROR)

console_formater=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
console_handler.setFormatter(console_formater)
logger.addHandler(console_handler)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.critical("This crictle We Happy to aissit to you shortly")
logger.warning("THE Warning  be care fully next time")
logger.error('we are solveing this error ')
logger.info("Information is sent")
logger.debug("We are debug the program")