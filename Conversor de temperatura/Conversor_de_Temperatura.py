print("\n")
print("Conversor de temperatura!")
i = 0
j = 0

while i == 0:
    tipo = input("Selecione um tipo de temperatura: C = Celsius, F = Fahrenheit, K = Kelvin: ").upper()
    if tipo == "C" or tipo == "F" or tipo == "K":
        i += 1
    else:
        print("\nTipo de temperatura inválido. Por favor, selecione novamente.")

t1 = float(input("\nInsira quantos graus em º" + tipo + " de temperatura você deseja converter: "))

while j == 0:
    tipo2 = input("\nDeseja converter o valor " + str(t1) + "º" + tipo + " Para? : C = Celsius, F = Fahrenheit, K = Kelvin: ").upper()
    if tipo2 == "C" or tipo2 == "F" or tipo2 == "K":
        j += 1
    else:
        print("\nTipo de temperatura inválido. Por favor, selecione novamente.")

if tipo == "C" and tipo2 == "F":
    conversao = float(t1 * 1.8 + 32)
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)

elif tipo == "C" and tipo2 == "K": 
    conversao = float(t1 + 273)
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)

elif tipo == "F" and tipo2 == "C": 
    conversao = float((t1 - 32)/1.8)
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)

elif tipo == "F" and tipo2 == "K": 
    conversao = float((t1 - 32)*(5/9)+273)
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)

elif tipo == "K" and tipo2 == "C": 
    conversao = float((t1 - 273))
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)

elif tipo == "K" and tipo2 == "F": 
    conversao = float((t1 - 273)*1.8 +32)
    print("\nA Conversão de " + str(t1) + "º" + tipo + " para º" + tipo2 + " é igual a: " + str(conversao) + "º" + tipo2)