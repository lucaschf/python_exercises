# Crie uma função que recebe uma lista cujos elementos são strings ou listas de strings e
# a. retorne o elemento com mais caracteres
# b. retorne a média de vogais nos elementos
# (nº de vogais de cada elemento/nº de elementos)
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a palavra lexicograficamente maior
# e. conte o número de ocorrências de palavras compostas
# f. retorne a quantidade de vizinhos iguais

# DESAFIO: exiba todas as sublistas de 2 elementos possíveis

import exercise_4


def execute(items):
    sub_items = []

    for item in items:
        if isinstance(item, str):
            sub_items.append(item)
        elif isinstance(item, list):
            sub_items.extend(item)

    return dict(exercise_4.execute(sub_items))


if __name__ == "__main__":
    list_items = ["Lucas", "bate-papo", "guarda-chuva", ["luis", "jose-cartlos", "sds", 'pica-pau', 'hueheuheuheuheu']]
    print(dict(execute(list_items)))
