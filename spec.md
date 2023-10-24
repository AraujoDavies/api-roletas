# API Roletas

## Objetivo

Lista as últimas jogadas das roletas disponíves na BET365.

- Facilita na criação de bots.
- Armazenar jogadas para estudar padrões futuramente.

## Como ? 

Uma máquina/container vai ficar monitorando as roletas e salvando o número que sair a cada jogada em um banco de dados e vai haver um endpoint construido em FASTAPI ou Flask que vai receber as requisições e retornar essas jogadas no formato JSON.

## Roletas

Roletas são compostas por 36 números e o zero.

## Dúzia/Coluna

Uma roleta possui 3 dúzias e 3 colunas, exemplo:

- Números de 1 a 12 => 1° duzia
- Números de 13 a 24 => 2° duzia
- Números de 25 a 36 => 3° duzia

## Outras classificações

Além da Dúzia e da coluna o número pode ser classificado como:

- Pretos ou vermelhos
- Ímpares e Pares
- Altos e baixos

