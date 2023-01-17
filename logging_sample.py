
import pprint
import logging
from rich.logging import RichHandler
import structlog
# Press the green button in the gutter to run the script.

def regular_logging(some_dict):

    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logger.info(f"Regular logging")

    logger.critical("Something critical")
    logger.error("An error")
    logger.warning("A warning")
    logger.info(f"My info is that you are here {some_dict}")
    logger.debug("I'm debugging")

def pprint_logging(some_dict):
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logger.info("pprint")
    logger.info(f"pprint {pprint.pformat(some_dict,width=20,depth=10,compact=False)}")


def structured_logging():
    from dataclasses import dataclass

    import structlog


    @dataclass
    class SomeClass:
        x: int
        y: str


    log = structlog.get_logger("some_logger")
    log.info("structlog")
    log.debug("debugging is hard", a_list=[1, 2, 3])
    log.info("informative!", some_key="some_value")
    log.warning("uh-uh!")
    log.error("omg", a_dict={"a": 42, "b": "foo"})
    log.critical("wtf", what=SomeClass(x=1, y="z"))


    log2 = structlog.get_logger("another_logger")


    try:
        d = {"x": 42}
        print(SomeClass(d["y"], "foo"))
    except Exception:
        log2.exception("poor me")
    log.info("all better now!", stack_info=True)

if __name__ == '__main__':
    some_dict={}
    some_dict['key_1']="1111"
    some_dict['key_2'] = "2222"
    some_dict['nested'] = ["n1","n2","n3"]
    some_dict['nested_2'] = {"k1":6,"k2":7}


    regular_logging(some_dict)
    pprint_logging(some_dict)
    structured_logging()
