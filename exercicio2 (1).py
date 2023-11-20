'''
Imagine que você é um mecânico e quer criar um sistema especialista que ajude a diagnosticar problemas em automóveis. O sistema deve ser capaz de fazer perguntas ao usuário sobre os sintomas que o carro está apresentando e, com base nas respostas, diagnosticar o problema. Elabore um conjunto de regras e uma base de conhecimento para esse sistema, considerando os seguintes problemas: bateria descarregada, pneu furado, motor superaquecido e freios desgastados.
'''


class Carro:
    daPartida = False
    DispositivosEletricosFuncionam = False
    luzesInternasFuncionam = False
    CarroInclinaProLado = False
    barulhoContinuoAoDirigir = False
    pneuMurchando = False
    fumaçaExecessiva = False
    odorQueimado = False
    medidorTemperaturaAlto = False
    pedalDoFreioProfundo = False
    CarroDemoraParar = False
    frearRangido = False
    pedalFreioVibrado = False


# Cria uma instância da classe Carro


# Perguntas ao usuário
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


meu_Carro = Carro()


def perguntas(Carro):
    Carro.daPartida = input_bool("O Carro está dando partida? (s/n) ")
    Carro.DispositivosEletricosFuncionam = input_bool(
        "Os dispositivos elétricos estão funcionando? (s/n) ")
    Carro.luzesInternasFuncionam = input_bool(
        "As luzes internas estão funcionando? (s/n) ")
    Carro.CarroInclinaProLado = input_bool(
        "O Carro está inclinando para algum lado? (s/n) ")
    Carro.barulhoContinuoAoDirigir = input_bool(
        "Você escuta um barulho contínuo ao dirigir? (s/n) ")
    Carro.pneuMurchando = input_bool("O pneu parece estar murchando? (s/n) ")
    Carro.fumaçaExecessiva = input_bool(
        "Está saindo fumaça excessiva do Carro? (s/n) ")
    Carro.odorQueimado = input_bool(
        "Você sente um odor de queimado vindo do Carro? (s/n) ")
    Carro.medidorTemperaturaAlto = input_bool(
        "O medidor de temperatura indica nível alto? (s/n) ")
    Carro.pedalDoFreioProfundo = input_bool(
        "O pedal do freio está mais profundo do que o normal? (s/n) ")
    Carro.CarroDemoraParar = input_bool(
        "O Carro demora mais para parar? (s/n) ")
    Carro.frearRangido = input_bool("Você escuta um rangido ao frear? (s/n) ")
    Carro.pedalFreioVibrado = input_bool(
        "O pedal do freio vibra ao ser pressionado? (s/n) ")


perguntas(meu_Carro)


def diagnosticar_problemas(Carro):
    problemas = []

    # Condições para Bateria Descarregada
    if not Carro.daPartida and not Carro.DispositivosEletricosFuncionam and not Carro.luzesInternasFuncionam:
        problemas.append("Bateria Descarregada")

    # Condições para Pneu Furado
    if Carro.CarroInclinaProLado or Carro.barulhoContinuoAoDirigir or Carro.pneuMurchando:
        problemas.append("Pneu Furado")

    # Condições para Motor Superaquecido
    if Carro.fumaçaExecessiva or Carro.odorQueimado or Carro.medidorTemperaturaAlto:
        problemas.append("Motor Superaquecido")

    # Condições para Freios Desgastados
    if Carro.pedalDoFreioProfundo or Carro.CarroDemoraParar or Carro.frearRangido or Carro.pedalFreioVibrado:
        problemas.append("Freios Desgastados")

    return problemas


problemas_identificados = diagnosticar_problemas(meu_Carro)

# Imprimindo os problemas identificados
if problemas_identificados:
    print("\nSeu Carro pode estar apresentando os seguintes problemas:")
    for problema in problemas_identificados:
        print(f"- {problema}")
else:
    print(
        "\nSeu Carro parece estar funcionando bem, sem problemas identificados."
    )
