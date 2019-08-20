#Lista: estrutura sequencial indexada
#Exercicio 1
def printInverse(n, vet):
    i = n - 1 
    while i > -1:
        print(vet[i])
        i = i - 1

#Exercicio 2
def printWithoutRepetition(vet):
    present = False
    result = []
    for i in range(0, len(vet)-1):
        if(i > 0):
            for j in range(0, len(result)-1):
                if(result[j] == vet[i]):
                    present = True
                    break
            
            if(not present):
                result.append(vet[i])
                present = False
            else:
                present = False
        
        else:
            result.append(vet[i])
    
    return result

#Exercicio 3
def orderSequence(m, n, s1, s2):
    result = []
    for i in range(0, m-1):
        result.append(s1[i])
    for i in range(0, n-1):
        result.append(s2[i])
    
    result = printWithoutRepetition(result)
    result.sort()

    return result


#Exercicio 4
def highestSum(n, vet):
    if(n != len(vet)):
        return 'ERRO: o valor de n é diferente do tamanho da sequencia'
    
    result = []
    highest = vet[0]
    i = 1
    result.append(highest)

    while i != n:
        tmp = highest + vet[i]

        if(tmp > highest):
            highest = tmp
            result.append(vet[i])
        
        else:

            if(sum(vet[i:]) <= sum(result)):
                print(vet[i])
                highest = tmp
                result.append(vet[i])
            
            else:
                result.clear()
                highest = vet[i]
                

        i = i + 1
    
    return (result, sum(result))


#Funções com listas
#Exercicio 1
def pertence(n, vet):
    for i in range(0, len(vet)):
        if(vet[i] == n):
            return True
        
    return False

#Exercicio 2
def printWithoutRepetition2(n, vet):
    result = []
    for i in range(0, n):
        if(i > 0):
            
            if(not pertence(vet[i], result)):
                result.append(vet[i])
        
        else:
            result.append(vet[i])

    return result

#Exercicio 3
def index(n, vet):
    for i in range(0, len(vet)):
        if(vet[i] == n):
            return i
    
    return None
    

#Exercicio 4
def indexOccurrence(n, vet):
    j = 0
    for i in range(0, n):
        if(index(vet[i], vet) != None):
            print('O valor ', vet[i], ' ocorre ', vet.count(vet[i]), 'vez(es)')

#Exercicio 5
def sumElements(start, end, vet):
    return sum(vet[start:end])

if __name__ == '__main__':

    #printInverse(6, [1, 2, 3, 4, 5, 6])

    #print(printWithoutRepetition([3.6, 2.3, 5.4, 3.6, 9.5, 7.5, 5.4, 2.2, 9.5]))

    #print(orderSequence(4, 3, [4,3,7,3], [1,2,4]))

    #print(highestSum(12, [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]))

    #pertence(False, [0.67, 'Ola', 9, True, False, 'a'])

    #print(printWithoutRepetition2(5, [1, 2, 3, 2, 5]))

    #print(index(10, [1, 2, 5, 7, 8, 9, 3]))

    #indexOccurrence(5, [1, 2, 5, 2, 3])

    print(sumElements(1, 4, [1, 4, 7, 5, 2, 9]))


