def test_parametro_errado_ao_instanciar_browser(browser):
    chrome = browser('invalid')
    assert chrome == False


def test_se_esta_instanciando_chrome_local(browser):
    chrome = browser('local')
    chrome.quit()
    assert 'splinter.driver.webdriver.chrome.WebDriver' in str(chrome)


def test_se_esta_instanciando_chrome_remoto(browser):
    chrome = browser('remoto')
    chrome.quit()
    assert 'splinter.driver.webdriver.remote.WebDriver' in str(chrome)
