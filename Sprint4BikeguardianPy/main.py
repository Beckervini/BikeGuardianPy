#Rm945679 Vinicius Becker, rm550562 Larissa Akemi, rm552292 Julia Nery, 
#rm552389 Isabelli Heloiza, rm98163 Julia Martins

import funcoes

while True:
    try:
        print("- - - Menu Inicial - - -")
        print("1 - Cadastrar-se como psicologo")
        print("2 - Cadastrar-se como psiquiatra")
        print("3 - Cadastrar-se como paciente")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcoes.cadastrar_cliente()

        elif opcao == '2':
            funcoes.cadastrar_bike()

        elif opcao == '3':
            funcoes.visualizar_cadastros()
            input("Pressione ENTER para continuar...")

        elif opcao == '4':
            break

        else:
            print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")