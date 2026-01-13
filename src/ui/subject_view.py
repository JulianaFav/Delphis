from services.subject_service import SubjectService
from models.subject import Materia

def tela_materia():
    while True:
        print("\n=== MATÉRIAS ===")
        print("1 - Cadastrar matéria")
        print("2 - Listar matérias")
        print("3 - Excluir matéria")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome da matéria: ")
            try:
                materia = Materia(id=None, nome=nome)
                SubjectService.criar(materia)
                print("Matéria cadastrada com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            materias = SubjectService.listar_todas()
            if not materias:
                print("Nenhuma matéria cadastrada.")
            else:
                for m in materias:
                    print(f"- {m.nome}")

        elif opcao == "3":
            id_materia = input("ID da matéria para excluir: ")
            SubjectService.excluir(id_materia)
            print("Operação finalizada.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
