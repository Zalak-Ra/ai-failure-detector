import logging
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("app.log")
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def add(a, b):
    logger.info("add called: %s/%s", a, b)
    return a+b


def mul(a, b):
    logger.info("mul called: %s/%s", a, b)
    return a*b


def div(a, b):
    logger.info("div called: %s/%s", a, b)
    return a/b

def slow_function(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

def crash():
    return 1 / 0