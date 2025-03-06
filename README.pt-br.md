# Master Calendar
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/RafaDdS/MasterCalendar/blob/main/README.md)

Script para automatizar e-mails do PESC para o Google Calendar.

Este é um projeto rápido para resolver um problema muito específico. Quero uma automação para converter e-mails sobre apresentações de mestrado e doutorado em eventos no meu Google Calendar.

## Você vai precisar
- Python 3.12
- Chrome Browser
- pipenv

## Como usar
Abra a pasta principal em um terminal e execute:
```
pipenv install
pipenv run python main.py
```
Pergunte-me pelo arquivo credentials.json do Master Calendar e você receberá. Sem ele, você precisará criar seu próprio projeto GCP e gerar novas credenciais. Não parece perigoso compartilhar, mas tentarei mantê-lo seguro do público em geral.

Na primeira vez que você usar o sistema, ele abrirá uma página de login adicional, onde você fará login com a conta na qual deseja salvar os eventos. O link correto também será exibido no terminal, caso a página não abra automaticamente. Você precisará permitir que o sistema faça modificações no seu calendário. As informações são salvas no arquivo token.pickle, que você pode excluir se quiser mudar o calendário que está usando.

Uma sessão de login do Gmail será aberta em uma nova janela do Chrome. Em seguida, você precisará:

- Fazer login com sua conta.
- É sempre uma boa ideia fechar qualquer pop-up que aparecer. Eles podem levar a resultados incorretos.
- Navegar até o e-mail que deseja processar.
- Digitar "Vai" no terminal para indicar ao script que você deseja processar o e-mail atual.
- Digitar "S" para confirmar a criação do evento com as informações capturadas.
- Digitar "Sair" ou fazer um interrupção de teclado (Ctrl + C) no terminal para indicar que deseja interromper o script. Isso também fechará a janela do Chrome.