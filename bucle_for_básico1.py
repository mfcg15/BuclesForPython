# 1. Basico
print("Ejecicio 1")
for i in range(151):
    print(i)

#2. Multiplos de cinco 
print("\nEjecicio 2")
for i in range(5,1001,5):
    print(i)

#3. Contar Dojo
print("\nEjecicio 3")
for i in range(1,101):
    if (i%10==0):
        print("Coding Dojo")
    elif (i%5==0):
        print("Coding")
    else:
        print(i)

#4. whoa
print("\nEjecicio 4")
sumaImpares = 0
for i in range(1,500000,2):
    sumaImpares += i
print(sumaImpares)

#5.Cuenta regresiva de a 4
print("\nEjecicio 5")
for i in range(2018,0,-4):
    print(i)

#6.Contador Flexible
print("\nEjecicio 6")
lowNum = 2 
higNum = 9
mul = 3
sucesivo = ""
for i in range(lowNum,higNum+1):
    if (i%3==0):
        sucesivo += str(i)+" "
print(sucesivo)