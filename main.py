import json


def carregar_sensores():
    with open('sensores.json', 'r') as file:
        dados = json.load(file)
    return dados


def salvar_sensores(dados):
    with open('sensores.json', 'w') as file:
        json.dump(dados, file, indent=2)


def mostrar_menu():
    print("\nMenu:")
    print("--------------")
    print("1. Visualizar condições das salas")
    print("--------------")
    print("2. Atualizar condições de uma sala")
    print("--------------")
    print("3. Adicionar nova sala")
    print("--------------")
    print("4. Excluir sala existente")
    print("--------------")
    print("5. Sair")
    print("--------------")


def visualizar_condicoes(dados):
    print("\nCondições das Salas: ")
    for sala, condicoes in dados['salas'].items():
        print(f"{sala}: Temperatura {condicoes['temperatura']}°C, Umidade {condicoes['umidade']}%")


def atualizar_condicoes(dados):
    sala = input("Digite o nome da sala: ")
    if sala in dados['salas']:
        temperatura = float(input("Digite a nova temperatura: "))
        umidade = float(input("Digite a nova umidade: "))

        dados['salas'][sala]['temperatura'] = temperatura
        dados['salas'][sala]['umidade'] = umidade

        salvar_sensores(dados)
        print(f"As condições da {sala} foram atualizadas.")
    else:
        print(f"A sala {sala} não foi encontrada.")


def adicionar_sala(dados):
    try:
        nova_sala = input("Digite o nome da nova sala: ")
        temperatura = float(input("Digite a temperatura inicial: "))
        umidade = float(input("Digite a umidade inicial: "))
    except ValueError:
        print("Erro: Certifique-se de digitar um valor numérico para temperatura e umidade.")
        return

    dados['salas'][nova_sala] = {'temperatura': temperatura, 'umidade': umidade}

    salvar_sensores(dados)
    print(f"A nova sala {nova_sala} foi adicionada com sucesso.")


def excluir_sala(dados):
    try:
        sala = input("Digite o nome da sala a ser excluída: ")
    except Exception as e:
        print(f"Erro: {e}")
        return

    if sala in dados['salas']:
        del dados['salas'][sala]
        salvar_sensores(dados)
        print(f"A sala {sala} foi excluída com sucesso.")
    else:
        print(f"A sala {sala} não foi encontrada.")



def main():
    try:
        dados_sensores = carregar_sensores()

        while True:
            mostrar_menu()

            opcao = input("Escolha uma opção (1-5): ")

            if opcao == '1':
                visualizar_condicoes(dados_sensores)
            elif opcao == '2':
                atualizar_condicoes(dados_sensores)
            elif opcao == '3':
                adicionar_sala(dados_sensores)
            elif opcao == '4':
                excluir_sala(dados_sensores)
            elif opcao == '5':
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()