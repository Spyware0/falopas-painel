from os import system
from webbrowser import open

try:
	from requests import get
except:
	print("Instalando dependências")
	system("pip install requests")


def clear():
	system('cls||clear')


def ent():
	input('\nenter para continuar')


def group():
	open('https://chat.whatsapp.com/FhFvqBpRYCV6tsmaBSMclT')


def cpf():
	cpf = int(input("informe o CPF: "))
	url = get(f"http://ghostcenter.xyz/api/cpf/{cpf}").json()
	for item in url:
		if url[item] != '':
			if type(url[item]) == dict:
				print()
				print(f'{green}{item}:{f}')
				for c in url[item]:
					print(f'	{green}{c}:{f}{n} {url[item][c]}{f}')
				print()
			elif type(url[item]) == str or int or float or bool:
				print(f'{green}{item}{f}{n}: {url[item]}{f}')
	ent()


def ip():
	ip = input(f"{green}Informe o IP: (enter para ver seu ip){f} ").strip()
	url = get(f"https://ipwhois.app/json/{ip}").json()
	for item in url:
		if url[item] != '':
			print(f'{green}{item}{f}{n}: {url[item]}{f}')
	ent()


def cep():
	cep = int(input(f'{green}Informe o CEP:{f} '))
	url = get(f'https://viacep.com.br/ws/{cep}').json()
	for i in url:
		if url[i] != '':
			print(f'{green}{i}{f}{n}: {url[i]}{f}')
	ent()


def ddd():
	ddd = int(input(f'{green}Informe o DDD:{f} '))
	url = get(f'https://brasilapi.com.br/api/ddd/v1/{ddd}').json()
	for i in url:
		if url[i] != '':
			if type(url[i]) == list:
				print(green+i+f)
				for c in url[i]:
					print(f'{green}{c}{f}')
			elif type(url[i]) == str or int:
				print(f'{green}{i}{f}{n}: {url[i]}{f}')
	ent()


def cnpj():
	cnpj = input(f'''{n}ex:{f} 03778130000148\nCNPJ: ''').strip()
	url = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').json()
	clear()
	for i in url:
		if url[i] != '':
			if type(url[i]) == dict:
				print()
				print(f'{green}{i}:{f}')
				for c in url[i]:
					print(f'  {green}{c}:{f}{n} {url[i][c]}{f}')
				print()
			elif type(url[i]) == list:
				print()
				print(f'{green}{i}:{f}')
				for ite in url[i]:
					for ij in ite:
						print(f'  {green}{ij}:{f}{n} {ite[ij]}{f}')
				print()
			elif type(url[i]) == str or int or float or bool:
				print(f'{green}{i}:{f}{n} {url[i]}{f}')
	ent()


def placa():
	placa = input(f'{green}PLACA:{f} ').strip().lower()
	url = get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).json()
	clear()
	for i in url:
		if url[i] != '':
			print(f'{green}{i}:{f}{n} {url[i]}{f}')
	ent()


def covid():
	estado = input(f"{green}Informe o ESTADO(ex: sp):{f} ").strip().lower()
	url = get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{estado}").json()
	for item in url:
		if url[item] != '':
			print(f'{green}{item}{f}{n}: {url[item]}{f}')
	ent()


def devs():
	print(f"{red} Equipe OnlyFalopas: {yellow} MrDiniz, Spyware,    Josh washington , Crowley, Swag Baby, Dio brando, Ghosthype{f}")
	ent()


def nome():
	nome = input("informe o NOME: ")
	url = get(f"http://ghostcenter.xyz/api/nome/{nome}").json()
	nomes = url['dados']
	for spyware in nomes:
		print(f"CPF = {spyware['cpf']}")
		print(f"NOME = {spyware['nome']} ")
		print(f"ANIVERSARIO = {spyware['nascimento']} ")
		print(f"SEXO = {spyware['sexo']} ")
	ent()


green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;97m"
f = '\033[m'
n = '\033[1m'
a = '\033[1;94m'
