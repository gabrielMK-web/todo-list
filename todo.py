def adicionar_tarefa(tarefas, descricao):
    """
    Adiciona uma nova tarefa à lista.
    Uma tarefa é um dicionário com 'descricao', 'concluida' e 'prioridade'.
    """
    if descricao:
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").strip().capitalize()
        if prioridade not in ['Alta', 'Média', 'Baixa']:
            print("⚠️ Prioridade inválida. Definindo como 'Baixa' por padrão.")
            prioridade = 'Baixa'
        nova_tarefa = {"descricao": descricao, "concluida": False, "priority": prioridade}
        tarefas.append(nova_tarefa)
        print(f"\n✅ Tarefa '{descricao}' adicionada com prioridade {prioridade}!")
    else:
        print("\n❌ A descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
    """Lista todas as tarefas, mostrando o status e a prioridade."""
    print("\n--- Sua Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa na lista. Adicione uma!")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "✅" if tarefa["concluida"] else "◻️"
            prioridade = tarefa.get("priority", "Baixa")
            print(f"{i + 1}. {status} {tarefa['descricao']} (Prioridade: {prioridade})")
    print("----------------------------")

def marcar_como_concluida(tarefas, indice):
    """Marca uma tarefa como concluída com base no seu índice na lista."""
    # O índice do usuário começa em 1, mas o da lista em 0
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        if tarefas[indice_real]["concluida"]:
            print(f"\n⚠️ A tarefa '{tarefas[indice_real]['descricao']}' já estava marcada como concluída.")
        else:
            tarefas[indice_real]["concluida"] = True
            print(f"\n✅ Tarefa '{tarefas[indice_real]['descricao']}' marcada como concluída!")
    else:
        print("\n❌ Índice inválido. Por favor, escolha um número da lista.")

def remover_tarefa(tarefas, indice):
    """Remove uma tarefa da lista com base no seu índice."""
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        tarefa_removida = tarefas.pop(indice_real)
        print(f"\n🗑️ Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print("\n❌ Índice inválido. Por favor, escolha um número da lista.")

def editar_descricao_tarefa(tarefas, indice):
    """Edita a descrição de uma tarefa existente."""
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        print(f"\nDescrição atual: {tarefas[indice_real]['descricao']}")
        nova_descricao = input("Digite a nova descrição: ").strip()
        if nova_descricao:
            tarefas[indice_real]["descricao"] = nova_descricao
            print("✅ Descrição atualizada com sucesso!")
        else:
            print("❌ A nova descrição não pode ser vazia.")
    else:
        print("\n❌ Índice inválido. Escolha um número da lista.")

def exibir_menu():
    """Menu principal."""
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Editar Descrição da Tarefa")
    print("0. Sair")

def main():
    """Função principal que executa o loop do programa."""
    # A lista de tarefas (nosso vetor) é criada vazia aqui.
    # Ela existirá apenas enquanto o programa estiver em execução.
    lista_de_tarefas = []

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Digite um número.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Digite um número.")
        elif escolha == '5':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para editar a descrição: "))
                editar_descricao_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Digite um número.")
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

# Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()