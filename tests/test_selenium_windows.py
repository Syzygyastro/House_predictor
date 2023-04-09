import subprocess
import socket
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture(scope="module")
def flask_port():
    """Ask OS for a free port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        addr = s.getsockname()
        port = addr[1]
        return port


@pytest.fixture(scope="module")
def run_app_win(flask_port):
    """Runs the Flask app for live server testing on Windows"""
    server = subprocess.Popen(
        [
            "flask",
            "--app",
            "house_price_app:create_app('house_price_app.config.TestConfig')",
            "run",
            "--port",
            str(flask_port),
        ]
    )
    try:
        yield server
    finally:
        server.terminate()


def test_data_page_running(run_app_win, chrome_driver, flask_port):
    """
    GIVEN a running app
    WHEN the data page is accessed successfully
    THEN a h1 text 'House price & GDP data from 1952' should pop up
    """
    # localhost has the IP address 127.0.0.1, which refers
    # back to your own server on your local computer
    driver = webdriver.Chrome()
    url = f"http://localhost:{flask_port}/api"
    driver.get(url)
    text = driver.find_element(By.TAG_NAME, 'h1').text
    assert "House price & GDP data from 1952" in text
    driver.quit()


def test_yearly_data_selected(run_app_win, chrome_driver, flask_port):
    """

    GIVEN a running app
    WHEN the data page is accessed
    AND the user clicks on the year with the id="1952"
    THEN a page with the title "Price (All)" should be displayed
    AND should  contain a text value "£1891.0"
    """
    url = f"http://localhost:{flask_port}/api"
    chrome_driver.get(url)
    # Wait until the element with id="1952" is on the page and then click on it
    el_1 = WebDriverWait(chrome_driver, timeout=3).until(
        lambda d: d.find_element(By.ID, "1952")
    )
    el_1.click()
    # Find the text value of the event highlights
    text = chrome_driver.find_element(By.ID, "Price (All)").text
    assert "£1891.0" in text


def test_home_nav_link_switch_to_statistics(run_app_win, chrome_driver, flask_port):
    """
    GIVEN a running app
    WHEN the homepage is accessed
    AND then the user clicks on the event with the id="1952"
    AND then the user clicks on the navbar in the 'Statistics' link
    THEN the page url should be "http://127.0.0.1:5000/stats"

    """
    url = f"http://localhost:{flask_port}/api"
    url_test = f"http://localhost:{flask_port}/stats"
    chrome_driver.get(url)
    # Wait until the element with id="1952" is on the page and then click on it
    el_1 = WebDriverWait(chrome_driver, timeout=3).until(
        lambda d: d.find_element(By.ID, "1952")
    )
    el_1.click()
    nav_home = WebDriverWait(chrome_driver, timeout=3).until(
        EC.element_to_be_clickable((By.ID, "Statistics"))
    )
    nav_home.click()
    current_url = chrome_driver.current_url
    assert current_url == url_test
