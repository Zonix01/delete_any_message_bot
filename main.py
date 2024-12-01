import logging

from delete_bot import main

logging.basicConfig(
    level=logging.ERROR,
    filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)


if __name__ == "__main__":
    main()
