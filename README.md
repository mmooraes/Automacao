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

```bash
pip install pyautogui
