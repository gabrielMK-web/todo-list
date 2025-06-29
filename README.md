# Projeto: Gerenciador de Tarefas v2.0

## 1. Visão Geral

Este é um projeto de um Gerenciador de Tarefas via terminal, desenvolvido em Python. A base do projeto oferece funcionalidades para adicionar, listar, concluir e remover tarefas. O objetivo deste trabalho é estender a funcionalidade do sistema e demonstrar um fluxo de trabalho de desenvolvimento profissional utilizando Git e GitHub.

## 2. Configuração Inicial

1.  **Fork:** Realize um fork deste repositório para a sua conta pessoal no GitHub.
2.  **Clone:** Clone o repositório que você criou (o seu fork) para o seu ambiente de desenvolvimento local.
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    ```

## 3. Especificações da Tarefa

Você deve implementar as **duas** novas funcionalidades descritas abaixo.

### Funcionalidade 1: Prioridade de Tarefas

* **Estrutura de Dados:** A estrutura de dados de cada tarefa deve ser alterada para incluir um campo `prioridade`.
* **Adicionar Tarefa:** A função de adição deve ser modificada para solicitar ao usuário um nível de prioridade (`Alta`, `Média`, `Baixa`). Uma entrada inválida deve resultar na prioridade padrão `Baixa`.
* **Listar Tarefas:** A função de listagem deve ser atualizada para exibir a prioridade de cada tarefa.

### Funcionalidade 2: Edição de Descrição da Tarefa

* **Menu:** Uma nova opção para "Editar Tarefa" deve ser adicionada ao menu principal.
* **Implementação:** Deve ser criada uma função que permita ao usuário:
    1.  Selecionar uma tarefa existente pelo seu índice.
    2.  Visualizar a descrição atual.
    3.  Inserir uma nova descrição para substituí-la.
* **Feedback:** O sistema deve informar ao usuário se a operação foi bem-sucedida.

## 4. Requisitos de Entrega e Fluxo de Trabalho

A avaliação levará em conta a organização do seu repositório e o uso correto das ferramentas.

* **README.md:** Este arquivo deve ser atualizado com a seção "Minhas Contribuições" devidamente preenchida.
* **`.gitignore`:** O repositório precisa conter um arquivo `.gitignore` configurado adequadamente para projetos Python, ignorando arquivos e pastas como `__pycache__` e `venv/`.
* **Fluxo com Branches:** Cada uma das duas funcionalidades deve ser desenvolvida em uma *feature branch* separada (ex: `feature/task-priority` e `feature/edit-task-description`). Após a finalização, cada branch deve ser mesclada (`merge`) de volta à branch `main`.
* **Histórico de Commits:** É exigido um histórico com um mínimo de **8 a 10 commits atômicos**. As mensagens de commit devem ser claras e refletir o trabalho realizado em cada etapa.

## 5. Critérios de Avaliação

* **README:** Clareza e detalhamento da seção "Minhas Contribuições".
* **Git:** Qualidade das mensagens de commit e demonstração do fluxo de trabalho com branches e merges.
* **Funcionalidade:** Implementação correta e funcional das modificações solicitadas.
* **Código:** Legibilidade, organização e qualidade geral do código implementado.

---

## (Template para o Aluno)

## Minhas Contribuições

* **Nome:** `Gabriel Marin Käfer`
* **GitHub:** `https://github.com/gabrielMK-web`

### Modificação 1: Prioridade de Tarefas

**Lógica Implementada:**
* Adicionei um novo campo chamado prioridade à estrutura de dados das tarefas. Na função de adicionar tarefa, o usuário é solicitado a informar a prioridade desejada: Alta, Média ou Baixa. Caso a entrada seja inválida ou deixada em branco, a prioridade padrão "Baixa" é atribuída automaticamente. A exibição das tarefas também foi ajustada para mostrar o nível de prioridade ao lado da descrição.

**Como Testar:**
* Execute o programa.

Selecione a opção de adicionar uma nova tarefa.

Informe a descrição da tarefa normalmente.

Quando solicitado, digite a prioridade desejada (Alta, Média ou Baixa).

Em seguida, use a opção de listar tarefas para verificar se a prioridade está sendo exibida corretamente.

Tente também digitar algo inválido (ex: "urgente") ou deixar em branco, e observe se a prioridade padrão "Baixa" é aplicada.

### Modificação 2: Editar Descrição da Tarefa

**Lógica Implementada:**
* Criei uma nova opção no menu chamada “Editar descrição da tarefa”. Essa funcionalidade solicita ao usuário o ID da tarefa existente, exibe a descrição atual e permite digitar uma nova descrição. Após isso, a tarefa é atualizada e uma mensagem de confirmação é exibida. A função também verifica se o ID digitado existe, e exibe uma mensagem de erro apropriada caso não exista.

**Como Testar:**
* Execute o programa.

Adicione pelo menos uma tarefa para ter um ID disponível.

Selecione a opção "Editar descrição da tarefa" no menu.

Digite o ID da tarefa que deseja editar.

Verifique se a descrição atual é mostrada corretamente.

Digite a nova descrição.

Liste as tarefas para confirmar se a alteração foi salva com sucesso.

Opcional: tente digitar um ID inexistente e observe se o programa trata o erro corretamente.