from code.raspar_e_tratar_dados_da_bet import (
    chrome_browser,
    raspar_dados_da_bet,
    tratar_dados,
)

from pytest import fixture


@fixture
def browser_invalid():
    return chrome_browser('invalid')


@fixture
def browser_local():
    chrome = chrome_browser('local')
    yield chrome
    chrome.quit()


@fixture
def browser_remoto():
    chrome = chrome_browser('remoto')
    yield chrome
    chrome.quit()


@fixture()
def raspagem_de_dados(browser_local):
    return tratar_dados(raspar_dados_da_bet(browser_local))
