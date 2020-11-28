import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def test_setup():
    desired_cap = {
        'platformName': 'Android',
        'deviceName': '192.168.85.101:5555',
        "appPackage": "br.jus.tse.resultados",
        "appActivity": "br.jus.tse.resultados.MainActivity",
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()
