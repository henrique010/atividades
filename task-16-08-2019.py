
#Exercicio 1
def verifyPairs(n, vet):
    if(n < 1):
        return 'ERRO: n deve ser maior que 1'

    result = True
    i = 0
    while n > 0:
        if(vet[i] % 2 != 0):
            result = False
        
        i = i + 1
        n = n - 1

        if(not result):
            return 'ERRO: existe numero impar na sequencia'
    
    return result

#Exercicio 2
def isCousin(n):
    result = 0
    i = 1
    while i <= n:
        if(n % i == 0):
            result = result + 1

        if(result > 2):
            return False
        
        i = i + 1

    return True 

#Exercicio 3
def isAdjoining(n):
    result = False
    a = 0
    b = 0
    while n > 0:
        a = n % 10
        n = n / 10
        b = n % 10

        if(a == b):
            result = True
        
        if(result):
            return result
    
    return result

#Exercicio 4
def isPa(n, vet):
    result = True
    r = vet[1] - vet[0]
    i = 2
    while i < n - 1:
        tmp = vet[i+1] - vet[i]
        if(r != tmp):
            print(vet[i+1], vet[i])
            result = False
        if(not result):
            return result
        
        i = i + 1
    
    return result


#Exercicio 1
def decompositionIntoPrimeFactors(n):
    factor = 2
    while n > 1:
        mult = 0
        while n % factor == 0:
            mult = mult + 1
            n = n / factor
        
        if(mult != 0):
            print("fator ", factor, "multiplicidade: ", mult)
    
        factor = factor + 1


#Exercicio 3
def sequenceFatorial(n, vet):
    v = []
    i = 0
    result = 0
    while i != n:
        result = 1
        while vet[i] != 0:
            result = result * vet[i]
            vet[i] = vet[i] - 1

        v.append(result)
        i = i + 1
    
    return v

#Exercicio 4
def sequencePrimos(n, vet):
    i = 0
    result = 0
    while i != n:
        if(isCousin(vet[i])):
            result = result + 1
        
        i = i + 1
    
    return result

#Exercicio 6
def tabuada(n):
    v = []
    i = 1
    j = 0
    while i <= n:
        j = 1
        while j <= n:
            v.append(i * j)
            j = j + 1
        
        i = i + 1
    
    return v


#Exercicio 1, 2 e 3
def fatorial(n):
    if(n < 0):
        return 'ERROR: O expoente deve ser maior ou igual a 0'

    result = 1
    while n != 0:
        result = result * n
        n = n - 1
    
    return result

def combination(n, m):
    if(n > m):
        return 'ERRO: n deve ser menor ou igual a m'
    
    return fatorial(m)/(fatorial(m-n) * fatorial(n))

#Exercicio 4
def coefficientsExpansion(n):
    cont = 0
    while cont <= n:
        print("Coeficiente de x^%d y^%d: %d"%(n-cont, cont, combination(cont, n)))
        cont += 1

    return 0

if __name__ == '__main__':

    #print(verifyPairs(6, [2, 6, 8, 20, 10, 4]))

    #print(isCousin(24))

    #print(isAdjoining(21212))

    #print(isPa(9, [1, 2, 3, 4, 6, 6, 7, 8, 9]))

    #decompositionIntoPrimeFactors(600)

    #print(sequenceFatorial(3, [5, 5, 5]))

    #print(sequencePrimos(5, [2, 4, 8, 7, 10]))

    #print(tabuada(13))

    #print(combination(2, 4))

    coefficientsExpansion(5)