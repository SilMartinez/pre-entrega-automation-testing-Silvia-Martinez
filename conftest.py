import logging
from pathlib import Path

import pytest

from utils.helpers import get_driver, take_screenshot


def _configure_logger():
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    log_file = logs_dir / "tests.log"

    logger = logging.getLogger("tests")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


@pytest.fixture(scope="session")
def logger():

    return _configure_logger()


@pytest.fixture
def driver(request, logger):

    drv = get_driver(headless=True)

    yield drv

    # En el teardown, verificamos si el test falló
    try:
        rep_call = getattr(request.node, "rep_call", None)
        if rep_call and rep_call.failed:
            test_name = request.node.name
            shot = take_screenshot(drv, name_prefix=test_name)
            logger.error(f"Test '{test_name}' falló. Screenshot: {shot}")
    finally:
        drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
