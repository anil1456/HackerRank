import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.debug("this is will display in debug")
#logging.info("hii, this is basics")

logger=logging.getLogger("Sample")
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler("ex.log")
an=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(an)
logger.addHandler(fh)
logger.debug("this is will display in debug")
logger.info("hii, this is basics")
