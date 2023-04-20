salario = float(input("Digite o salário: "))
aumento = int(input("Digite a porcentagem de aumento:"))

print(salario)
print(aumento)

salario_atual = salario + (salario * (aumento/100))

print(salario_atual)