# Ilha do tesouro! Esse quiz apresenta escolhas para o usuário em um mini game no qual o personagem está buscando o tesouro

desafio1 = input(
        'Você e seu amgio estão em um bar que está afundando. Você observa uma ilha, mas seu amigo não é capaz de nadar, porque está machucado. Digite "Nadar" para seguir sem seu amigo ou "Tentar" para tentar salvar seu amigo:'
    )

lower_desafio1 = desafio1.lower()

if lower_desafio1 == "nadar":
    print("O mar era mais fundo que você imaginava! Game over.")
else:
    desafio2 = input("Você consegue salvar seu amigo! Digite \"Esperar\" para continuar na ilha ou \"Procurar\" para inspecionar a Ilha.")
    lower_desafio2 = desafio2.lower()

    if lower_desafio2 == "esperar":
        print("Um dragão devorou vocês na ilha! Game ouver.")
        
    else:
        desafio3 = input("Na sua busca, você chega em três portas. Digite \"Vermelho\" para abrir a porta da esquerda, digite \"Azul\" para abrir a porta da direita e digite \"Verde\" para abrir a porta do meio.")
        lower_desafio3 = desafio3.lower()

        if lower_desafio3 == "vermelho":
            print("Você caiu em uma porta cheia de fogo! Game over.")

        elif lower_desafio3 == "azul":
            print("Você entrou em um quarto cheio de cobras venenosas! Game over.")

        else:
            print("Você achou o baú! Good game.")