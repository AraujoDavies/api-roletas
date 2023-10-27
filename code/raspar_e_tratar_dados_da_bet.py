import logging

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from splinter import Browser, driver
from webdriver_manager.chrome import ChromeDriverManager


def chrome_browser(
    type_browser: str = 'local' or 'remoto',
    ip_remoto: str = 'http://127.0.0.1:4444',
) -> driver:
    """
    Instancia o chrome para fazer as raspagens.


    Args:
        type_browser:
            local: roda na maquina que está executando o script;

            remote: roda em outra maquina/container.

        ip_remoto: endereço ip do chrome que vamos manipular.


    Returns:
        chrome
    """
    options = Options()
    options.add_argument('--start-maximized')

    if type_browser == 'local':
        service = Service(ChromeDriverManager().install())
        return Browser('chrome', service=service, options=options)

    elif type_browser == 'remoto':
        return Browser(
            driver_name='remote',
            browser='chrome',
            command_executor=ip_remoto,
            options=options,
        )
    else:
        logging.critical(
            'Especifique o tipo de browser desejado como "local" ou "remoto" no arquivo de variáveis de ambiente'
        )
        return False


def raspar_dados_da_bet(driver: driver) -> dict:
    """
    Acessa a bet e raspa os dados das roletas.

    Args:
        driver: Navegador de manipulação do chrome.

    Returns:
        Todas roletas com as últimas 5 jogadas
    """
    return {}
