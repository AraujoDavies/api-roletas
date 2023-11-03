from code.raspar_e_tratar_dados_da_bet import (
    chrome_browser,
    raspar_dados_da_bet,
    tratar_dados,
)
from time import sleep

if __name__ == '__main__':
    driver = chrome_browser()

    soup = raspar_dados_da_bet(driver=driver)
    if soup != 'TIMEOUT':
        dados = tratar_dados(soup=soup)
