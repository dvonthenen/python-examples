import logging, verboselogs


def myFunc():
    logger = verboselogs.VerboseLogger(__name__)
    logger.success("from myFunc")
