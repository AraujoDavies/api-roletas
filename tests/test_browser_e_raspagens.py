from code.raspar_e_tratar_dados_da_bet import raspar_dados_da_bet


def test_parametro_errado_ao_instanciar_browser(browser_invalid):
    assert browser_invalid == False


def test_se_esta_instanciando_chrome_local(browser_local):
    assert 'splinter.driver.webdriver.chrome.WebDriver' in str(browser_local)


def test_se_esta_instanciando_chrome_remoto(browser_remoto):
    assert 'splinter.driver.webdriver.remote.WebDriver' in str(browser_remoto)


def test_se_raspou_dados_de_todas_roletas(raspagem_de_dados):
    assert len(raspagem_de_dados) == 31


def test_se_todas_roletas_estao_trazendo_5_numeros(raspagem_de_dados):
    for roleta in raspagem_de_dados:
        print(roleta['roleta'])
        assert len(roleta['numeros']) == 5


def test_timeout_na_raspagem(browser_local):
    assert (
        raspar_dados_da_bet(browser_local, 'https://www.google.com')
        == 'TIMEOUT'
    )
