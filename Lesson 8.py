import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="We have new logging message: %(asctime)s:%(levelname)s - %(message)s"
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception as err:

    logging.exception(f"16 рядок. Ошыбка - {err}")
