# Crie uma função que recebe uma lista de números e
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos
# e. retorne o valor mais próximo da média dos elementos
# f. retorne a soma dos elementos com valor negativo
# g. retorne a quantidade de vizinhos iguais

# DESAFIO: exiba todas as sublistas de 2 elementos possíveis

import numpy


def execute(items):
    yield "biggest", max(items)  # biggest element
    yield "sum", sum(items)  # sum of elements
    yield "occurrences_first_element", items.count(items[0])  # number of occurrences of an element
    yield "media", numpy.mean(items)  # mean of the elements
    # todo letter e
    yield "negative_sum", sum(filter(lambda n: n < 0, items))  # sum of negative elements
    # todo letter g


if __name__ == "__main__":
    for i in execute([1, 2, 4, 5, 6, 7]):
        print(i)
