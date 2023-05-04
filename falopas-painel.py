#!/bin/python3

from utils import *

while True:
	try:
		clear()
		print(f"""{green}
OOooOoO    Oo     o       .oOOOo.  OooOOo.     Oo    .oOOOo.  
o         o  O   O       .O     o. O     `O   o  O   o     o  
O        O    o  o       O       o o      O  O    o  O.       
oOooO   oOooOoOo o       o       O O     .o oOooOoOo  `OOoo.  
O       o      O O       O       o oOooOO'  o      O       `O 
o       O      o O       o       O o        O      o        o 
o       o      O o     . `o     O' O        o      O O.    .O 
O'      O.     O OOoOooO  `OoooO'  o'       O.     O  `oooO' 
															
	{yellow} P A I N E L  D E  C O N S U L T A S
{red}             By  OnlyFalopas
{green}
-----------
|  MENU   |
-----------

{red}[{yellow}1{red}]{white} Consulta CEP
{red}[{yellow}2{red}]{white} Consulta CPF
{red}[{yellow}3{red}]{white} Consulta IP
{red}[{yellow}4{red}]{white} Consulta NOME
{red}[{yellow}5{red}]{white} Consulta COVID
{red}[{yellow}6{red}]{white} Consulta CNPJ
{red}[{yellow}7{red}]{white} Consulta PLACA
{red}[{yellow}8{red}]{white} Consulta DDD
{green}
-----------
| OUTROS  |
-----------

{red}[{yellow}D{red}]{white} DEVS
{red}[{yellow}S{red}]{white} SAIR
""")
		user = input(red + "~> " + f).strip().lower()[0]

		match user:
			case '1':
				cep()
			case '2':
				cpf()
			case '3':
				ip()
			case '4':
				nome()
			case '5':
				covid()
			case '6':
				cnpj()
			case '7':
				placa()
			case '8':
				ddd()
			case 's':
				clear()
				print(green + 'Obrigado por usar o nosso painel, até mais :)' + f)
				break
			case 'd':
				devs()

	except:
		continue
