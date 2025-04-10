base, horas_extras, valor_horas_extra= int(input('insira o valor do salário base: ')), int(input('insira o número de horas extras: ')), int(input('insira o valor da hora extra: '))
salario = base + (horas_extras * valor_horas_extra) 
print(f'o salário total é: {salario}')