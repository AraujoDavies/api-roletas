from pytest import fixture
from raspar_e_tratar_dados_da_bet import chrome_browser


@fixture
def browser():
    return chrome_browser
