from appium.webdriver.common.mobileby import MobileBy


class ResultadosSeletores(object):
    """
    Essa classe contém todos os seletores do aplicativo
    """
    BTN_PROX = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Próximo\")')
    BTN_ENTENDI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Entendi\")')
    BTN_LI_ACEITO = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android"
                                      ".view.View/android.view.View/android.view.View/android.view.View/android.view"
                                      ".View[2]/android.view.View[2]/android.view.View[3]/android.widget.Button"))
    EXPRESSION_SELECIONE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione\")')
    BTN_ESCOLHER_LOCAL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Escolher local\")')
    HOME_TEXTO_RECIFE_PE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife, PE\")')
    DROP_DOWN_ESTADO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione o estado\")')
    BTN_CONFIRMAR_LOCAL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Confirmar\")')
    DROP_DOWN_MUNICIPIO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione o município\")')
    BTN_SELECIONA_PERNAMBUCO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pernambuco\")')
    BTN_SELECIONA_RECIFE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife\")')
    BTN_MENU_SELECIONA_ELEICAO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Eleições 2020\")')
    BTN_ELEICAO_29_NOVEMBRO = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView"
                                                "/android.webkit.WebView/android.view.View/android.view.View/android"
                                                ".view.View/android.app.Dialog/android.view.View/android.view.View[2]"
                                                "/android.view.View[2]/android.view.View[5]/android.view.View[2]/"
                                                "android.widget.ListView/android.view.View[4]/android.widget.Button"))
    CANDIDATO_TEXTO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"MARILIA ARRAES\")')
    BTN_FAVORITAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritar\")')
    FAVORITO_TEXTO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favorito\")')
    BTN_FECHAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Fechar\")')
    BTN_FAVORITOS_TAB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritos\")')
    BTN_TOTALIZACAO_TAB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Totalização\")')
    ELEITORADO_TEXTO = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                         "android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/"
                                         "android.webkit.WebView/android.view.View/android.view.View/android"
                                         ".view.View/android.view.View/android.view.View/android.view.View/"
                                         "android.view.View/android.view.View/android.view.View[2]/android"
                                         ".view.View[2]/android.view.View[8]/android.widget.ListView/android"
                                         ".view.View[1]/android.view.View[2]"))
    BTN_INFORMACOES_TAB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Informações\")')
    BTN_DUVIDAS_FREQUENTES = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                               "android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/"
                                               "android.webkit.WebView/android.view.View/android.view.View/android.view"
                                               ".View/android.view.View/android.view.View/android.view.View/android"
                                               ".view.View/android.view.View/android.view.View[2]/android.view"
                                               ".View[2]/android.widget.ListView/android.view.View[2]/android.view"
                                               ".View[2]"))
    DUVIDAS_TEXTO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Dúvidas frequentes\")')
    BTN_RESULTADOS_TAB = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                           ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                           "android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView"
                                           "/android.view.View/android.view.View/android.view.View/android.view"
                                           ".View/android.view.View/android.widget.TabWidget/android.view"
                                           ".View[1]/android.view.View"))
    BTN_VOLTAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"back\")')
    BTN_ELEICAO_SEGUNDO_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"2º TURNO\")')
    BTN_ELEICAO_PRIMEIRO_TURNO = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                                   "android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.view.ViewGroup/android.webkit"
                                                   ".WebView/android.webkit.WebView/android.view.View/android.view"
                                                   ".View/android.view.View/android.app.Dialog/android.view.View"
                                                   "/android.view.View[2]/android.view.View[2]/android.view.View[5]"
                                                   "/android.view.View[2]/android.widget.ListView/android.view.View[5]"
                                                   "/android.widget.Button"))
    BTN_CONFIRMAR_OPCAO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"CONFIRMAR\")')
    BTN_PESQUISAR_CANDIDATO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pesquisar candidato\")')
    BARRA_PESQUISA = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView"
                                       "/android.view.View/android.view.View/android.view.View/android.app.Dialog"
                                       "/android.view.View/android.view.View[1]/android.view.View[2]/android.view"
                                       ".View[2]/android.view.View/android.view.View/android.widget.EditText"))
    RESULTADO_PESQUSA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"CARLINHOS BALA\")')
