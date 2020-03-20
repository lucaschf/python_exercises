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
import exercise_8


def execute(items):
    yield "biggest", max(items)
    yield "sum", sum(items)
    yield "occurrences_first_element", items.count(items[0])
    yield "media", numpy.mean(items)
    yield "closest_to_average", exercise_8.closest_to_average(items)
    yield "negative_sum", sum(filter(lambda n: n < 0, items))
    # todo letter g


if __name__ == "__main__":
    list_item = [1, 2, 4, 5, 6, 7]

    for i in execute(list_item):
        print(i)
