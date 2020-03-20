# Crie uma função que recebe uma lista qualquer e
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos
# e. retorne o valor mais próximo da média dos elementos
# f. retorne a soma dos elementos com valor negativo
# g. retorne a quantidade de vizinhos iguais

# DESAFIO: exiba todas as sublistas de 2 elementos possíveis

import exercise_1


# filters the numbers in the list
# @return a list containing all the numbers of the items
def filter_numbers(items):
    return list(filter(lambda x: isinstance(x, (int, float)), items))


def execute(items):
    return exercise_1.execute(filter_numbers(items))


if __name__ == "__main__":
    for i in execute([1, "DASD", 2, 4, 905, 6, 7, 'a', 8006.0]):
        print(i)
