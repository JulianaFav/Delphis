from ui.subject_view import tela_materia


def iniciar():
    while True:
        print("\n=== DELPHIS ===")
        print("1 - Matérias")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            tela_materia()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    iniciar()
