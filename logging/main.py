import logging, verboselogs

from tmp.myfunc import myFunc

verboselogs.install()
logger = verboselogs.VerboseLogger(__name__)
logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.SPAM)
# logger.setLevel(logging.VERBOSE)
logger.setLevel(logging.WARNING)

# NOTSET - 0
# SPAM - 5
# DEBUG - 10
# VERBOSE - 15
# NOTICE - 25
# WARNING - 30
# SUCCESS - 35
# ERROR - 40
# CRITICAL - 50

logger.spam("this is spam!")
logger.debug("debug debug debug")
logger.verbose("Can we have verbose logging? %s", "Yes we can!")
logger.info("this is information")
logger.notice("notice!")
logger.warning("warning danger will robinson")
logger.success("success!")
logger.error("Error!")

# single logger instance test
myFunc()
