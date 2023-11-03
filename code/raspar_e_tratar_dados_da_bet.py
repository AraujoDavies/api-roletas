import logging
import sys
from os import getenv
from time import sleep

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from splinter import Browser, driver
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv('config.env')


def trata_html(input):
    return ' '.join(input.split()).replace('> <', '><')


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


    Example:
        > chrome_browser('local')

        > chrome_browser('remoto', 'http://127.0.0.1:4444')
    """
    options = Options()
    options.add_argument('--start-maximized')

    if type_browser == 'local':
        service = Service(ChromeDriverManager().install())
        driver = Browser('chrome', service=service, options=options)

    elif type_browser == 'remoto':
        driver = Browser(
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

    return driver


def raspar_dados_da_bet(
    driver: driver, url=getenv('URL_BET')
) -> BeautifulSoup | str:
    """
    Acessa a bet e raspa os dados das roletas.

    Args:
        driver: Navegador de manipulação do chrome.

    Returns:
        OK: dados em soup

        ERRO: TIMEOUT

    Example:
        > raspar_dados_da_bet(webdriver)
    """
    if driver.url != url:   # visit correct route
        driver.visit(url)

    count = 0   # wait page loading
    while driver.is_element_not_present_by_text(getenv('ULTIMA_ROLETA')):
        logging.warning('...')
        count += 1
        sleep(1)
        if count > 5:   # some seconds to timeout
            logging.error('roulettes not loading, check env -> ULTIMA_ROLETA')
            return 'TIMEOUT'

    html = trata_html(driver.html)

    soup = BeautifulSoup(html, 'html.parser')

    return soup


def tratar_dados(soup: BeautifulSoup) -> list:
    """
    Recebe o objeto soup e trata os valores para uma lista de dicts python (list of dicst).

    Args:
        soup: html convertido em beautifulsoup

    Returns:
        dict: dados transformados para melhor manipulação.

    Example:
        > tratar_dados(soup)
    """
    divs_rouletts = soup.find_all(
        'div',
        class_='live-casino-static-games-grid-game-pod__content-container',
    )

    return_dicts = []
    for soup_roulett in divs_rouletts:
        nome = soup_roulett.find(
            'div', class_='live-casino-static-games-grid-game-pod__header'
        ).text
        numeros = []
        soup_numeros = soup_roulett.find_all(
            'div', class_='live-casino-roulette-rounds__round'
        )
        for numero in soup_numeros:
            if numero.text != '':
                numeros.append(numero.text)

        numeros.reverse()   # alter order list to DESC
        if len(numeros) > 5:
            numeros.remove(numeros[-1])   # have to be 5 number by list

        modelo = {'roleta': nome, 'numeros': numeros}
        return_dicts.append(modelo)

    return return_dicts
