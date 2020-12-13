import os

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators.resultados_locators import ResultadosSeletores
from pages.base import Base


class Resultados(Base):

    def selecionar_eleicoes_segundo_turno(self):
        """
        Método seleciona o segundo turno da eleições do segundo turno do dia 29/11
        :return: None
        """
        btn_seleciona_eleicao = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_MENU_SELECIONA_ELEICAO)
        btn_seleciona_eleicao.click()
        btn_seleciona_segundo_turno = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_ELEICAO_29_NOVEMBRO)
        btn_seleciona_segundo_turno.click()

    def selecionar_local(self):
        """
        Método clica na escolha de um local de votação
        :return: None
        """
        btn_escolher_local = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_ESCOLHER_LOCAL)
        btn_escolher_local.click()

    def seleciona_estado_municipio(self, estado, municipio):
        """
        Método seleciona o estado e municipio de votação
        :param estado: estado value
        :param municipio: municipio value
        :return: None
        """
        btn_estado = Base.encontra_elemento(self.drive, ResultadosSeletores.DROP_DOWN_ESTADO)
        btn_estado.click()
        os.system('adb shell input swipe 500 1000 500 0')
        drop_seleciona_estado = Base.encontra_elemento(self.drive, estado)
        drop_seleciona_estado.click()
        btn_confirma = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_CONFIRMAR_LOCAL)
        btn_confirma.click()
        drop_seleciona_municipio = Base.encontra_elemento(self.drive, ResultadosSeletores.DROP_DOWN_MUNICIPIO)
        drop_seleciona_municipio.click()
        btn_municipio = Base.encontra_elemento(self.drive, municipio)
        btn_municipio.click()
        btn_confirma.click()
        btn_confirma.click()

    def recife_pernambuco_segundo_turno_validacao(self):
        """
        Método verifica se o municipio escolhido foi exibido corretamente
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.HOME_TEXTO_RECIFE_PE))
        except NoSuchElementException:
            return False
        return True

    def favoritar_candidato(self):
        """
        Método favorita um candidato
        :return: None
        """
        texto_favorito = Base.encontra_elemento(self.drive, ResultadosSeletores.CANDIDATO_TEXTO)
        texto_favorito.click()
        btn_favoritar = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_FAVORITAR)
        btn_favoritar.click()

    def validar_favorito_tab(self):
        """
        Método valida se na tab de favoritos o candidato está aparecendo
        :return: boolean
        """
        try:
            btn_fechar = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_FECHAR)
            btn_fechar.click()
            tab_favoritos = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_FAVORITOS_TAB)
            tab_favoritos.click()
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.CANDIDATO_TEXTO))
        except NoSuchElementException:
            return False
        return True

    def validar_recife_pe_tab_totalizacao(self):
        """
        Método verifica se foi exibido na tab de totalizacao o municipio escolhido
        :return: boolean
        """
        try:
            btn_tab_totalizacao = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_TOTALIZACAO_TAB)
            btn_tab_totalizacao.click()
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.HOME_TEXTO_RECIFE_PE))
        except NoSuchElementException:
            return False
        return True

    def validar_tab_totalizacao(self):
        """
        Método responsável por validar se a pagina de totalização tem informações da votação
        :return: valor do elemento
        """
        try:
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.ELEITORADO_TEXTO))
        except NoSuchElementException:
            return False
        return True

    def validar_pesquisa_candidato(self):
        """
        Método valida se o candidato está aparecendo após pesquisa
        :return: boolean
        """
        try:
            btn_tab_resultados = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_RESULTADOS_TAB)
            btn_tab_resultados.click()
            btn_seg_turno = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_MENU_SELECIONA_ELEICAO)
            btn_seg_turno.click()
            opcao_primeiro_turno = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_ELEICAO_PRIMEIRO_TURNO)
            opcao_primeiro_turno.click()
            btn_pesquisar = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_PESQUISAR_CANDIDATO)
            btn_pesquisar.click()
            barra_pesquisa = Base.encontra_elemento(self.drive, ResultadosSeletores.BARRA_PESQUISA)
            barra_pesquisa.send_keys("carlinhos bala")
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.RESULTADO_PESQUSA))
        except NoSuchElementException:
            return False
        return True

    def validar_duvidas_frequentes(self):
        """
        Método responsável por validar se a pagina de dúvidas frequentes está retornando as informações
        :return: valor do elemento
        """
        try:
            btn_fechar = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_FECHAR)
            btn_fechar.click()
            btn_tab_informacoes = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_INFORMACOES_TAB)
            btn_tab_informacoes.click()
            btn_duvidas = Base.encontra_elemento(self.drive, ResultadosSeletores.BTN_DUVIDAS_FREQUENTES)
            btn_duvidas.click()
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.DUVIDAS_TEXTO))
        except NoSuchElementException:
            return False
        return True
