import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def add(a, b):
    logger.info("add called: %s/%s", a, b)
    return a+b


def mul(a, b):
    logger.info("mul called: %s/%s", a, b)
    return a*b


def div(a, b):
    logger.info("div called: %s/%s", a, b)
    return a/b