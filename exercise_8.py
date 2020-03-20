# Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores
# da lista.
# Exemplo:
# lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0)
# Valor mais próximo da média = 7.5

import numpy


def closest_to_average(items):
    avg = numpy.mean(items)
    diffs = {value: abs(value - avg) for value in items}

    return min(diffs, key=diffs.get)


if __name__ == "__main__":
    print(closest_to_average([2.5, 7.5, 10.0, 4.0]))
