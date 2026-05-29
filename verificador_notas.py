nome = input('Digite seu nome completo: ')
nota = input('Digite sua nota: ')

nota_float = float(nota)

if nota_float >= 7:
	print(f'Aluno: {nome}\n Nota: {nota_float:.2f}\n Situação: Aprovada(o)')
elif nota_float >= 5 and nota_float <= 6.9:
	print(f'Aluno: {nome}\n Nota: {nota_float:.2f}\n Situação: Recuperação')
else:
	print(f'Aluno: {nome}\n Nota: {nota_float:.2f}\n Situação: Reprovada(o)')