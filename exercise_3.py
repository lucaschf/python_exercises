# a) Faça uma função que receba duas listas e retorne True se são iguais ou False caso contrário.
# Duas listas são iguais se possuem os mesmos valores e na mesma ordem.
# b) Faça uma função que receba duas listas e retorne True se têm os mesmos elementos ou False
# caso contrário
# Duas listas possuem os mesmos elementos quando são compostas pelos mesmos valores, mas não
# obrigatoriamente na mesma ordem.

# DESAFIO: exiba todas as sublistas de 2 elementos possíveis


def are_equals(items, other_items):
    return items == other_items


def has_same_content(items, other_items):
    return len(items) == len(other_items) and set(items) == set(other_items)


if __name__ == "__main__":
    content = [1, 4, 2, 3, 8, 9, 10]
    otherContent = [1, 10, 3, 4, 9, 8, 2]

    print(f"Content\n{content}\n")
    print(f"Other content\n{otherContent}\n")

    print(f"Are equals: {are_equals(content, otherContent)}")
    print(f"Has same content: {has_same_content(content, otherContent)}")
