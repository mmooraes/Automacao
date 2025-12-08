# 🤖 RPA para Automação de Liberação de Documentação

> Automação desenvolvida em Python para eliminar tarefas manuais repetitivas na liberação de documentações, reduzindo aproximadamente 400 ações manuais por ciclo.

## 📄 Sobre o Projeto

Este projeto consiste em um script de **RPA (Robotic Process Automation)** desenvolvido para interagir com uma interface de sistema legado ou web. O objetivo principal foi resolver o problema de excesso de cliques e digitação repetitiva (teclas `TAB` e `ENTER`) necessários para liberar lotes de documentos.

### 🎯 Problema vs. Solução

* **O Problema:** O processo manual exigia uma sequência exaustiva de navegação via teclado, totalizando cerca de 400 ações manuais (keystrokes) para processar pequenos lotes, gerando fadiga e risco de LER (Lesão por Esforço Repetitivo).
* **A Solução:** Um script Python utilizando a biblioteca `PyAutoGUI` que replica a interação humana com precisão, controlando o fluxo de navegação e preenchimento automaticamente.

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - Para controle programático de teclado e mouse.
* Biblioteca `time` (nativa) - Para controle de fluxo e espera de carregamento de interface.

## ⚙️ Funcionalidades

* **Loop Configurável:** Definição fácil do número de documentos a serem processados (`repeticoes`).
* **Foco Automático:** Inicia alternando para a janela do sistema alvo (`Alt + Tab`).
* **Logica Condicional de Navegação:** Identifica a primeira execução para ajustar a quantidade de `TABs` necessários (38 na primeira, 39 nas subsequentes), adaptando-se à mudança de foco da interface após o primeiro registro.
* **Delays Estratégicos:** Pausas programadas (`sleep`) para garantir que o sistema processe as entradas antes do próximo comando.

## 🚀 Como executar

### Pré-requisitos

Certifique-se de ter o Python instalado e instale a dependência do projeto:

## 🚀 Como Executar

Para garantir o funcionamento correto do script, siga a ordem abaixo:

1.  **Prepare o Ambiente:** Abra o sistema ou navegador onde a tarefa será realizada e deixe-o na tela inicial do processo.
2.  **Posicione as Janelas:**
    * Vá para o seu editor de código (VS Code, Terminal, etc).
    * *Atenção:* O script executa um `Alt + Tab` logo no início. Certifique-se de que a **última janela acessada** antes de ir para o código foi a do sistema alvo.
3.  **Execute o Script:**
    No terminal, rode o comando:
    ```bash
    python nome_do_script.py
    ```
4.  **Aguarde:** Não mexa no mouse ou teclado enquanto o script estiver rodando para evitar interferência nos comandos.

## 🔧 Personalização

Você pode adaptar o comportamento do robô alterando as variáveis no início do arquivo `nome_do_script.py`:

* **Definir quantidade de execuções:**
    Altere a variável `repeticoes` para o número exato de documentos que deseja processar no lote atual.
    ```python
    repeticoes = 7  # Ex: Troque para 50 se tiver 50 documentos
    ```

* **Ajustar velocidade:**
    Se o sistema estiver lento, aumente o `pyautogui.PAUSE` ou os tempos de `sleep()` para evitar que o robô "atropele" o carregamento da página.
    ```python
    pyautogui.PAUSE = 0.5  # Tempo de espera padrão entre cada comando
    ```

## ⚠️ Cuidados (Fail-Safe)

Como este RPA assume o controle dos periféricos (mouse e teclado), foi implementado o recurso de segurança nativo da biblioteca PyAutoGUI:

* **Parada de Emergência:** Se precisar interromper o script imediatamente, mova o cursor do mouse **bruscamente para qualquer um dos quatro cantos da tela**.
* Isso acionará uma exceção `FailSafeException`, parando a execução na hora.
* 
