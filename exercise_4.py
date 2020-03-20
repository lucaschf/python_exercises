# Crie uma função que recebe uma lista de strings e
# a. retorne o elemento com mais caracteres
# b. retorne a média de vogais nos elementos (nº de vogais de cada elemento/nº de
# elementos)
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a palavra lexicograficamente maior
# e. conte o número de ocorrências de palavras compostas
# f. retorne a quantidade de vizinhos iguais

# DESAFIO: exiba todas as sublistas de 2 elementos possíveis


def execute(items):
    yield 'biggest', max(items)
    yield 'vowel_media', (vowel_counter(items) / len(items))
    yield 'vowel', (vowel_counter(items))
    yield "occurrences_first_element", items.count(items[0])
    yield "biggest_lexicographically_word", max(items, key=len)
    yield "compound_words", compound_words_counter(items)
    # todo f


def vowel_counter(items):
    vowels = 'aeiouAEIOU'
    return sum([1 for char in ''.join(items) if char in vowels])


def compound_words_counter(items):
    return len(list(filter(lambda word: "-" in word, items)))


if __name__ == "__main__":
    print(dict(execute(["Lucas", "bate-papo", "guarda-chuva"])))
