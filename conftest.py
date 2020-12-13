import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def test_setup():
    """
    Configuração de conexão entre Appium e o DUT
    :return: conexão
    """
    desired_cap = {
        'platformName': 'Android',
        'deviceName': '192.168.220.105:5555',
        "app":  'C:\\Users\\duda_\\Documents\\Especialização\\Automação Mobile\\apks\\br.jus.tse.resultado.apk',
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()
