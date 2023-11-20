'''
Suponha que você é um chef de cozinha e deseja criar um sistema especialista que recomende pratos baseados nas preferências alimentares dos clientes. O sistema deve ser capaz de levar em consideração restrições dietéticas (como vegetarianismo ou alergias) e preferências de sabor (como salgada ou doce). Elabore um conjunto de regras e uma base de conhecimento para esse sistema, considerando os seguintes pratos: salada vegetariana, lasanha, sushi, frango assado e sorvete de chocolate.
'''


class client():
    vegetarian = False
    alergico_peixe = False
    alergico_ave = False
    gosta_salgada = False
    gosta_doce = False
    intolerancia_lactose = False


Cliente = client()


def input_bool(prompt):
    """Solicita ao usuário uma resposta 's' ou 'n' e valida a entrada."""
    while True:
        resposta = input(prompt).lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Por favor, insira 's' ou 'n'.")


def preferencias(Cliente):
    Cliente.vegetarian = input_bool("\nVocê é vegetariano? (s/n) ")
    if Cliente.vegetarian == False:
        Cliente.alergico_peixe = input_bool(
            "\nVocê é alérgico a peixe? (s/n) ")
        Cliente.alergico_ave = input_bool("\nVocê é alérgico a ave? (s/n) ")

    Cliente.gosta_salgada = input_bool(
        "\nVocê gosta de comidas salgadas? (s/n) ")
    Cliente.gosta_doce = input_bool("\nVocê gosta de comidas doces? (s/n) ")
    if Cliente.gosta_doce == True:
        Cliente.intolerancia_lactose = input_bool(
            "\nVocê tem intolerância à lactose? (s/n) ")


preferencias(Cliente)


def recomendar_pratos(Cliente):
    recomendacoes = []

    # Para salada vegetariana
    recomendacoes.append("salada vegetariana")

    # Para lasanha bolonhesa
    if not Cliente.vegetarian and not Cliente.alergico_peixe and not Cliente.alergico_ave and Cliente.gosta_salgada:
        recomendacoes.append("lasanha bolonhesa")

    # Para sushi
    if not Cliente.vegetarian and not Cliente.alergico_peixe and Cliente.gosta_salgada:
        recomendacoes.append("sushi")

    # Para frango assado
    if not Cliente.vegetarian and not Cliente.alergico_ave and Cliente.gosta_salgada:
        recomendacoes.append("frango assado")

    # Para sorvete de chocolate
    if Cliente.gosta_doce and not Cliente.intolerancia_lactose:
        recomendacoes.append("sorvete de chocolate")

    if not recomendacoes:
        return "Desculpe, não temos recomendações para suas preferências no momento."
    else:
        return ", ".join(recomendacoes)


# Após coletar as preferências do cliente, chame a função recomendacao:
print("Recomendamos para você: \n")
print(recomendar_pratos(Cliente))
