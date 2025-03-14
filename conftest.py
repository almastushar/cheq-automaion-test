from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from loguru import logger
import os
import pytest
import configparser

from utils.common_func import get_latest_log_file, extract_logs


@pytest.fixture(scope='function')
def config():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file_path = os.path.abspath(cur_dir)
    _file = _file_path + "\\" + "config.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def data():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file_path = str(os.path.abspath(cur_dir))
    _file = _file_path + "\\" + "data.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    def fin():
        driver.close()

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="session", autouse=True)
def setup_logger(request):
    log_format = "{time} | {level} | {message} | {file} | {line} | {" \
                 "function} | {exception}"

    path = "logs/log_{time}.log"

    logger.add(
        sink=path,
        colorize=True,
        format=log_format,
        level='DEBUG',
        compression='zip',
        rotation='50 MB',
        encoding='utf-8',
        retention='30 days',
        backtrace=False,
        diagnose=False,
        catch=True
    )
    yield


screenshots_dir = "report/screenshots"
screenshots = "screenshots"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    latest_log = None
    log_data = None
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if report.failed:
            logger.error(f"Test failed: {item.nodeid}")
            latest_log = get_latest_log_file("logs")

        if driver:
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            screenshots_path = os.path.join(screenshots, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            if latest_log:
                with open(latest_log) as f:
                    log_data = extract_logs(item.name, latest_log)

            if isinstance(log_data, (str, bytes)):
                report.extra = getattr(report, 'extras', [])
                report.extra.append(pytest_html.extras.html(f"<div><h2>Logs:</h2><pre>{log_data}</pre></div>"))
                report.extra.append(pytest_html.extras.image(screenshots_path))
            else:
                report.extra = getattr(report, 'extras', [])
                report.extra.append(pytest_html.extras.html(f"<div><h2>Logs:</h2><pre>{str(log_data)}</pre></div>"))
                report.extra.append(pytest_html.extras.image(screenshots_path))
