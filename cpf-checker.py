logo=r"""

              __            _               _             
             / _|          | |             | |            
   ___ _ __ | |_ ______ ___| |__   ___  ___| | _____ _ __ 
  / __| '_ \|  _|______/ __| '_ \ / _ \/ __| |/ / _ \ '__|
 | (__| |_) | |       | (__| | | |  __/ (__|   <  __/ |   
  \___| .__/|_|        \___|_| |_|\___|\___|_|\_\___|_|   
      | |                                                 
      |_|                          by Sudano#7479          

"""

print(logo)
cpf_digitado = input("Digite o CPF para consultar: ").replace(".", "").replace("-", "")

if not cpf_digitado.isdigit():
    print('O CPF digitado é inválido.')
    exit()

backup = 0

for i in range(len(cpf_digitado)):
    backup += int(cpf_digitado[i])

if str(backup)[0] == str(backup)[1]:
    print('O CPF digitado é valido.')
else:
    print('O CPF digitado é inválido.')