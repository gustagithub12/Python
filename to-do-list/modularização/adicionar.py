def add(concluir=False):
    arq = 'tarefas.txt'

    try:
        adicione = input("Adicione uma Tarefa: ").strip()

        with open(arq, 'a', encoding='utf-8') as file:
            if concluir:
                file.write(adicione + ' ✅ Concluído\n')
            else:
                file.write(adicione + ' ❌ Não concluído\n')

        print('✅ Tarefa adicionada!')

    except Exception as erro:
        print(f'❌ Erro ao adicionar tarefa: {erro}')


def listtarefas():
    arq = 'tarefas.txt'
    try:
        with open(arq, 'r', encoding='utf-8') as file:
            tarefas = file.readlines()

        if not tarefas:
            print("📭 Nenhuma tarefa cadastrada.")
        else:
            print("\n📝 Tarefas cadastradas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f'[{i}] - {tarefa.strip()}')

    except Exception as erro:
        print(f'❌ Erro ao listar tarefas: {erro}')


def conclusao():
    arq = 'tarefas.txt'

    try:
        with open(arq, 'r', encoding='utf-8') as file:
            tarefas = file.readlines()

        if not tarefas:
            print("📭 Nenhuma tarefa cadastrada.")
            return

        print("\n📝 Tarefas cadastradas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"[{i}] - {tarefa.strip()}")

        try:
            op = int(input('Digite o número da tarefa que deseja marcar como concluída: '))

            if 1 <= op <= len(tarefas):
                tarefa_original = tarefas[op - 1].strip()

                if "✅ Concluído" in tarefa_original:
                    print("⚠️ Esta tarefa já está marcada como concluída.")
                    return

                tarefa_sem_status = tarefa_original.split(' ❌')[0]
                tarefas[op - 1] = tarefa_sem_status + ' ✅ Concluído\n'

                with open(arq, 'w', encoding='utf-8') as file:
                    file.writelines(tarefas)

                print("✅ Tarefa marcada como concluída!")
            else:
                print("❌ Número inválido!")

        except ValueError:
            print("❌ Digite um número válido.")

    except Exception as erro:
        print(f'❌ Erro ao concluir tarefa: {erro}')


def remover():
    arq = 'tarefas.txt'

    try:
        with open(arq, 'r', encoding='utf-8') as file:
            tarefas = file.readlines()

        if not tarefas:
            print("📭 Nenhuma tarefa cadastrada.")
            return

        print("\n📝 Tarefas cadastradas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f'{i} - {tarefa.strip()}')

        try:
            op = int(input('Digite o número da tarefa que deseja remover: '))

            if 1 <= op <= len(tarefas):
                tarefa_removida = tarefas.pop()

                with open(arq, 'w', encoding='utf-8') as file:
                    file.writelines(tarefas)

                print(f'✅ Tarefa removida: {tarefa_removida.strip()}')
            else:
                print("❌ Número fora do intervalo.")

        except ValueError:
            print("❌ Digite um número válido.")
        except Exception as erro:
            print(f'❌ Erro ao remover tarefa: {erro}')

    except FileNotFoundError:
        print("❌ Arquivo de tarefas não encontrado.")
