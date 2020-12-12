# Projeto Final Automação Mobile

**Projeto de automação para o aplicativo Resultados do TSE.**

Objetivo: Automatizar fluxos para o aplicativo Resultados

Aluna: Maria Eduarda Parahyba
___

**Estrutura do projeto:**

Estou usando a estrutura do Pytest para este projeto. Segue abaixo visão geral do projeto: 

```
projetofinalmobile/
  pages/
      locators /
          resultados_locators.py
      base.py
      home.py
      resultados.py
  resources/
      apk/
          br.jus.tse.resultados.apk
  tests /
      test_resultados.py
```

🗂 **Explicação para cada pasta:**

Pages >> PageObjects relacionados, um arquivo .py para cada pasta e suas funcionalidades.

Resources >> Indica a apk que está sendo utilizada

Tests >> Fluxo de teste para a execução.
___

**Recursos**

🎯 Estou utilizando:

Python <br>
Pytest <br>
Appium-Python-Client <br>
Selenium <br>

🛠 Como instalar?

Basta executar o arquivo requirements.txt usando o seguinte comando no caminho raiz:

```
pip install -r requirements.txt
```
___


💻 **Configuração do ambiente de teste**

A pasta do aplicativo e o número de série do produto Android estão registrados na raiz do projeto.
Basta inserir seu número de série (dispositivos adb) em conftest.py.

Para executar o projeto, basta chamar pytest no terminal:

```
pytest
```
___

📝 **Execução de relatório**

Para realizar a execução e também gerar um relatório para isso, basta usar o seguinte comando ao chamar o pytest:

```
pytest --html = report.html
```

Após a execução, um arquivo denominado "report.html" será gerado no caminho raiz do projeto. Clique nele e ele será aberto como um arquivo de texto. Execute-o indicando um navegador para renderizar o arquivo html. O relatório será exibido.

Além disso, um link será exibido após a execução, para que você possa acessá-lo diretamente a partir dele.

___
