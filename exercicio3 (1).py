'''
Considere que você é um orientador acadêmico e deseja criar um sistema especialista que recomende cursos universitários com base nas áreas de interesse e objetivos profissionais dos estudantes. O sistema deve levar em consideração a área de conhecimento de interesse do estudante (como ciências exatas, humanas, biológicas, etc.) e seus objetivos profissionais (como trabalhar em pesquisa, indústria, docência, etc.). Elabore um conjunto de regras e uma base de conhecimento para esse sistema, considerando os seguintes cursos: Engenharia Civil, Psicologia, Biologia, Administração e Matemática.
'''

class Interessados():
	exatas = False 
	humanas = False 
	biologicas = False 
	administracao = False 
	engenharia = False 
aluno = Interessados()



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

def perguntas(interessados):
	interessados.exatas = input_bool("Você possui interesse em ciências exatas? (s/n)")
	if interessados.exatas == True: 
		interessados.engenharia = input_bool("\nVocê possui interesse em ciências da engenharia? (s/n)")
		interessados.biologicas = input_bool("\nVocê possui interesse em ciências biológicas? (s/n)")
	interessados.humanas = input_bool("\nVocê possui interesse em ciências humanas? (s/n)")
	if interessados.humanas == True: 
		interessados.administracao = input_bool("\nVocê possui interesse em ciências administrativas? (s/n)")

perguntas(aluno)

def recomendar_cursos(aluno):
	recomendacoes = []
	if aluno.exatas == True:
		recomendacoes.append("Matemática")
	if aluno.engenharia == True:
		recomendacoes.append("Engenharia Civil")
	if aluno.biologicas == True:
		recomendacoes.append("Biologia")
	if aluno.humanas == True:
		recomendacoes.append("Psicologia")
	if aluno.administracao == True:
		recomendacoes.append("Administração")
	print(f"\nAs recomendações para você são: {recomendacoes}")

recomendar_cursos(aluno)



	

#cursos: Engenharia Civil, Psicologia, Biologia, Administração e Matemática.
	
		
	
	
