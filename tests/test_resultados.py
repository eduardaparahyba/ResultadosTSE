import pytest
from pages.home import Home
from pages.resultados import Resultados
from pages.locators.resultados_locators import ResultadosSeletores


@pytest.mark.usefixtures('test_setup')
class TestResultados(object):

    def test_fluxo_inicial(self, test_setup):
        """
        Método testa se é possível acessar a tela inicial do app sem erros
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.realizar_fluxo_inicial()
        verifica_home = home.verifica_tela_home()
        assert verifica_home, 'Não acessou a tela inicial'

    def test_estado_municipio_segundo_turno(self, test_setup):
        """
        Método testa se é possível verificar sem erros o resultado do segundo turno
        da eleição para um estado e municipio
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        resultados_inicial = Resultados(test_setup)
        resultados_inicial.selecionar_eleicoes_segundo_turno()
        resultados_inicial.selecionar_local()
        resultados_inicial.seleciona_estado_municipio(ResultadosSeletores.BTN_SELECIONA_PERNAMBUCO,
                                                      ResultadosSeletores.BTN_SELECIONA_RECIFE)
        retorna_recife_pernambuco = resultados_inicial.recife_pernambuco_segundo_turno_validacao()
        assert retorna_recife_pernambuco, 'Resultado Divergente'

    def test_favoritar_candidato(self, test_setup):
        """
        Método testa se o candidato aparece favoritado após realização do procedimento de favoritar
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        resultados_inicial = Resultados(test_setup)
        resultados_inicial.favoritar_candidato()
        valida_favoritos_tab = resultados_inicial.validar_favorito_tab()
        assert valida_favoritos_tab, 'Candidato não foi favoritado'

    def test_tab_totalizacao(self, test_setup):
        """
        Método testa se a tab de totalização está carregando corretamente e com os dados da
        cidade e municipios escolhidos
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        resultados_inicial = Resultados(test_setup)
        valida_municipio_totalizacao = resultados_inicial.validar_recife_pe_tab_totalizacao()
        valida_totalizacao = resultados_inicial.validar_tab_totalizacao()
        assert (valida_municipio_totalizacao) and (valida_totalizacao), 'Resultado Divergente'

    def test_pesquisar_candidato(self, test_setup):
        """
        Método testa se ao pesquisar por um candidato, o mesmo aparece no resultado da pesquisa
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        resultados_inicial = Resultados(test_setup)
        valida_pesquisa_candiato = resultados_inicial.validar_pesquisa_candidato()
        assert valida_pesquisa_candiato, 'Candidato não localizado'

    def test_duvidas_frequentes(self, test_setup):
        """
        Método testa se as dúvidas frequentes (localizada na tab Informações) estão sendo carregadas com sucesso
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        resultados_inicial = Resultados(test_setup)
        valida_duvidas_frequentes = resultados_inicial.validar_duvidas_frequentes()
        assert valida_duvidas_frequentes, 'Resultado Divergente'
