# Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas
# demais pessoas.
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# ' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
# Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
# Faça a função "traduzir", que recebe uma lista com uma mensagem (lSecreta) e "traduz" a sequência
# armazenada em lSecreta de acordo com o código das amigas.
# Teste para lSecreta = [2,15,13,0,4,9,1];
# DICA: crie uma string com as letras na ordem do código


def decrypt(message):
    encryption_key = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted = ''

    for key_code in message:
        decrypted += encryption_key[key_code]

    return decrypted


if __name__ == "__main__":
    encrypted_message = [2, 15, 13, 0, 4, 9, 1]

    print(decrypt(encrypted_message))
