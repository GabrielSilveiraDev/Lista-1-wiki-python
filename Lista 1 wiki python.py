#Lista de exercício 1 python wiki
#Questão 1:
""

print("Hello World")


#Questão 2:

x = float(input('Digite um número: '))

print(f'O número digitado foi {x}')

""

#Questão 3:
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

print(f'A soma é:{x+y} ')

""

#Questão 4:

nota1 = int(input('Digite a 1º nota do aluno: '))
nota2 = int(input('Digite a 2º nota do aluno: '))
nota3 = int(input('Digite a 3º nota do aluno: '))
nota4 = int(input('Digite a 4º nota do aluno: '))

print(f'A nota final do aluno é: {(nota1+nota2+nota3+nota4)/4}')

""

#Questão 5:

x = float(input('Digite o valor em metros a ser convertido para centimetros: '))

print(f'{x} metros é igual a {x*100} centimetros')

""

#Questão 6:

x = float(input('Digite o raio do circulo em cm: '))

print(f'A área desse circulo é de: {x**2*3.14}cm²')

""

#Questão 7:

x = float(input('Digite o tamanho do lado do quadrado em cm: '))

print(f'O dobro da área do quadrado é: {2*x**2}cm²')

""

#Questão 8:

x = float(input('Digite quantos R$ você ganha por hora: '))
y = float(input('Digite quantas horas você trabalha por mês: '))

print(f'Sua renda mensal é de: {x*y}')

""

#Questão 9:

x = float(input('Digite a temperatura em graus Farenheit: '))

print(f'A temperatura em graus Celsius e de: {(x-32)*5/9} ºC')

""

#Questão 10:

x = float(input('Digite a temperatura em graus Celsius: '))

print(f'A temperatura em graus Farenheit é de: {(9*x/5 + 32)} ºF')

""

#Questão 11:

x = int(input('Digite o primeiro valor inteiro: '))
y = int(input('Digite o segundo valor inteiro: '))
z = float(input('Digite um número real: '))

print(f'O produto do dobro do primeiro com a metade do segundo é: {(2*x)*(y/2)}'
      f'\nA soma do triplo do primeiro com o terceiro é: {3*x+z}\nO terceiro elevado ao cubo é: {z**3} ')


""
#Questão 12:

x = float(input('Digite sua altura em m: '))
y = float(input('Digite seu peso em kg: '))

print(f'Seu peso ideal é: {72.7*x -58}kg')

""

#Questão 13:

altura = float(input('Digite sua altura em m: '))
sexo = input('Digite f se for mulher e m se for homem: ')

if sexo == 'M':
    
    print(f'O seu peso ideal é de {round(72.7*x -58,2)}kg')
    
if sexo.upper() == 'F':
    
    print(f'O seu peso ideal e de {round(62.1*x -44.7,2)})kg')

""

#Questão 14:

peso = float(input('Digite quantos quilogramas de peixe foram trazidos: '))
excesso = (peso - 40)

if excesso > 0:

    multa = excesso *4
    print(f'O excesso foi de {excesso}kg e a multa foi de {multa}R$')

else:
    print('Nao haverá multa, visto que o peso de peixe trazido está dentro das regras estabelecidas no regulamento.')
    
""

#Questão 15:

x = float(input('Digite quantos reais você ganha por hora: '))
y = float(input('Diite quantas horas você trabalha no mês: '))
salario = x*y

print(f'O salário bruto é de {salario}R$.\nO valor pago ao INSS foi de: {salario*0.08}R$.'
      f'\nO valor pago ao sindicato foi de: {salario*0.05}R$.\nO valor pago de imposto de renda foi de {salario*0.11}R$.'
      f'\nO salário líquido é de {salario*0.76}')

""

#Questão 16:

x = float(input('Quantos m² possui a área a ser pintada: '))

print(f'A quantidade de latas a ser comprada é de: {int((x/3)/18) +1}, e o valor total é de: {int(((x/3)/18)+1)*80}R$')

""

#Questão 17:

x = float(input('Quantos m² possui a área a ser pintada: '))
y = int((((x/108) - int((x/108)))*108)/21.6) +1

print(f'Se você comprar apenas galões de 18L, você tera que comprar {int((x/108)) +1} latas,'
      f' com um custo de {(int((x/108))+1)*80}R$.\nSe você comprar apenas galões de 3.6L,'
      f' você tera que comprar {(int((x/21.6))+1)} latas, com um custo de {(int((x/21.6))+1)*25}R$.'
      f'\nSe você comprar as latas misturadas, terã que comprar {int((x/108))} latas de 18L,'
      f' e {y} latas de 3.6L, com um custo de: {(int((x/108))*80) + (y*25)}R$.')

""

#Questão 18:

x = float(input('Digite quantos MB tem o arquivo: '))
y = float(input('Digite a velocidade de download em MBps: '))

print(f'O tempo aproximado de download deste arquivo é de: {(x/y)/60} minutos')

""