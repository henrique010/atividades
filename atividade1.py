def celciusToFahrenheit(c):
    return (c * 9/5) + 32

def fahrenheitToCelcius(f):
    return (f - 32) * 5/9 

def isLeap(year):
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False

def isCompatible(heigth, weight, age, hair, sexo, schooling):
    if(heigth < 155 or heigth > 170):
         return False
    if(weight < 45 or weight > 65):
         return False
    if(age < 25 or age > 35):
         return False
    if(hair != "loiro"):
        return False
    if(sexo != "feminino"):
         return False
    if(schooling == "Phd"):
         return False
    
    return True

def sequenceSum(vet):
    i = 0
    s = 0
    while vet[i] != 0:
        s = s + vet[i]
        i = i + 1
    
    return s

def potentiation(n, k):
    if(k < 0):
        return 'ERROR: O expoente deve ser maior ou igual a 0'

    result = 1
    while k != 0:
        result = result * n
        k = k - 1

    return result

def fatorial(n):
    if(n < 0):
        return 'ERROR: O expoente deve ser maior ou igual a 0'

    result = 1
    while n != 0:
        result = result * n
        n = n - 1
    
    return result

def firstSixMultiples(n, i, j):
    vet = []
    number = 0
    while n != 0:
        if(number % i == 0 or number % j == 0):
            vet.append(number)
            n = n - 1
        
        number = number + 1
    
    return vet

def MDC(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    
    return a

def sumPairs(n, vet):
    if(n < 0):
        return 'ERROR: O n deve ser maior ou igual a 0'

    i = 0
    result = 0
    while n != 0:
        if(vet[i] % 2 == 0):
            result = result + vet[i]
        n = n - 1
        i = i + 1
    
    return result

def sumPairsAndOdd(n, vet):
    if(n < 0):
        return 'ERROR: O n deve ser maior ou igual a 0'

    i = 0
    result = 0
    result2 = 0
    while n != 0:
        if(vet[i] % 2 == 0):
            result = result + 1
            
        elif(vet[i] % 2 != 0):
            result2 = result2 + 1
        
        n = n - 1
        i = i + 1
    
    return (result, result2)

def numberOfOccurrences(n, d):
    result = 0
    while n != 0:
        if(n % 10 == d):
            result = result + 1
        
        n = n/10

    return result

def triangular(n):
    k = 0
    i = 1
    while k < n:
        if(i * (i+1) * (i+2) == n):
            print(i, i+1, i+2)
            return True

        k = k + 1
        i = i + 1

    return False

def order(a, b, c):
    if(a > b and b > c):
        return (c, b, a)
    elif(a > c and b < c):
        return (b, c, a)
    elif(a > b and a < c):
        return (b, a, c)
    elif(a < b and b < c):
        return (a, b, c)
    elif (a < b and a > c):
        return (c, a, b)
    else:
        return (a, c, b)
    

if __name__ == '__main__':
    '''
    c = float(input("Digite a temperatura em celcius: "))
    print(celciusToFahrenheit(c))

    f = float(input("Digite a temperatura em fahrenheit: "))
    print(fahrenheitToCelcius(f))

    year = int(input("Digite um ano: "))
    print(isLeap(year))
    
    heigth = float(input("Digite sua altura: "))
    weight = float(input("Digite seu peso: "))
    age = int(input("Digite sua idade: "))
    hair = raw_input("Digite sua cor de cabelo: ")
    sexo = raw_input("Digite seu sexo: ")
    schooling = raw_input("Digite sua escolaridade: ")
    print(isCompatible(heigth, weight, age, hair, sexo, schooling))

    sequence = [12, 17, 4, -6, 8, 0]
    print(sequenceSum(sequence))

    n = int(input("Digite a base: "))
    k = int(input("Digite on expoente: "))
    print(potentiation(n, k))

    n = int(input("Digite um numero que deseja saber o fatorial: "))
    print(fatorial(n))

    print(firstSixMultiples(6, 2, 3))

    print(MDC(12, 18))
    
    v = [2, 7, 0, 5, 8, 4]
    print(sumPairs(6, v))

    v = [2, 7, 0, 5, 8, 4]
    pair, odd = sumPairsAndOdd(6, v)
    print(pair, odd)
    
    n = int(input("Digite o valor de n: "))   
    d = int(input("Digite o valor de d: "))
    print("O digito", d, "ocorre ", numberOfOccurrences(n, d), "em n")

    print(triangular(190))

    print(triangular(210))
    '''
    print(order(70, 20, 50))
    




    




