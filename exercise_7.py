# Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]],
# ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez
# em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve imprimir na tela:
# a) o total de faltas do campeonato
# b) o time que fez mais faltas
# c) o time que fez menos faltas

# [
#     ['Brasil', 'Italia', [10, 9]],
#     ['Brasil', 'Espanha', [5, 7]],
#     ['Italia', 'Espanha', [7, 8]]
# ]


def execute(championship_result):
    total_faults = 0
    championship_faults = dict()

    more_faults = ""
    less_faults = ""

    for item in championship_result:
        match_faults = item[-1]  # last item is the faults list
        total_faults += sum(match_faults)

        for i in range(2):  # the match has only two teams
            team = item[i]
            team_faults = match_faults[i]

            if not bool(championship_faults):
                more_faults = team
                less_faults = team

            if team in championship_faults:  # checks if the team already had faults com
                team_faults += championship_faults[team]

            championship_faults[team] = team_faults

            if team_faults > championship_faults[more_faults]:
                more_faults = team
            elif team_faults < championship_faults[less_faults]:
                less_faults = team

    yield "total_faults", total_faults
    yield "more_faults", more_faults
    yield "less_faults", less_faults
    yield "championship_faults", championship_faults


if __name__ == "__main__":
    print(dict(
        execute([["Brasil", "Italia", [10, 9]], ["Brasil", "Espanha", [5, 7]], ["Italia", "Espanha", [7, 8]]])
    ))
