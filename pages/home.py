import os

from pages.base import Base
from pages.locators.resultados_locators import ResultadosSeletores
import time


class Home(Base):

    def realizar_fluxo_inicial(self):
        """
       Este método executa o fluxo inicial (bem-vindo) do aplicativo
       :return: None
        """
        btn_prox = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_PROX)
        btn_prox.click()
        btn_entendi = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_ENTENDI)
        btn_entendi.click()
        os.system('adb shell input swipe 500 1000 500 0')
        btn_li = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_LI_ACEITO)
        btn_li.click()
        time.sleep(5)
