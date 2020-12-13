from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.resultados_locators import ResultadosSeletores


class Base(object):

    def __init__(self, drive):
        self.drive = drive

    def encontra_elemento(self, element):
        """
        Método responsável por encontrar elementos (utilizando presence_of_element_located)
        :param element: elemento a ser procurado
        :return: valor do elemento
        """
        value = WebDriverWait(self, 40).until(EC.presence_of_element_located((
            element
        )))
        return value

    def verifica_tela_home(self):
        """
        Método responsável por validar se está na página principal
        :return: valor do elemento
        """
        resultados = Base.encontra_elemento(self.drive, ResultadosSeletores.EXPRESSION_SELECIONE)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True
