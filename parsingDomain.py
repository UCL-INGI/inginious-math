def is_integer(n):
    try:
        int(n)
        return True, "correct"
    except:
        return False, "{} n'est pas un nombre correct".format(n)


def is_subset(set):
    # @set is a string containing information about the subset
    # returns True if it is a subset or False if not

    if set == "":
        return False, "Vous n'avez rien répondu"

    set = set.replace(" ", "")

    intervals = set.split('U')

    for interval in intervals:
        if interval == "":
            return False, "Il y a trop de symboles 'U' dans votre expression"

        if len(interval) <= 2:
            return False, "{} n'est pas un intervalle correct".format(interval)

        if interval[0] == '{' and interval[-1] == '}': # si c'est un singleton
            if not is_integer(interval[1:-1])[0]:
                return False, "{} n'est pas un nombre correct".format(interval[1:-1])

        elif interval[0] in '[]' and interval[-1] in '[]': # si c'est un intervalle
            if not ';' in interval:
                return False, "l'intervalle {} ne contient pas le séparateur ';'".format(interval)

            numbers = interval[1:-1].split(';')

            if len(numbers) != 2:
                return False, "{} contient trop de nombres".format(interval)

            if not is_integer(numbers[0])[0]:
                return False, "{} n'est pas un nombre correct".format(numbers[0])
            if not is_integer(numbers[1])[0]:
                return False, "{} n'est pas un nombre correct".format(numbers[1])
            if int(numbers[0]) > int(numbers[1]):
                return False, "{}: la première borne est plus grande que la deuxième!".format(interval)
            elif int(numbers[0]) == int(numbers[1]):
                return False, "{}: les deux bornes sont égales! Utiliser un singleton ({}) à la place peut-être".format(interval, "{}")

        else:
            return False, "{} n'est pas un intervalle correct".format(interval)

    return True, "correct"

def compareDomains(answer, expected):

    result = is_subset(answer)
    if not result[0]:
        return False, result[1]

    answer = answer.replace(" ", "")
    expected = expected.replace(" ", "")

    answer = answer.split("U")
    expected = expected.split("U")

    for e in answer:
        if not e in expected:
            return False, "{} ne fait pas partie de la réponse".format(e)
    for e in expected:
        if not e in answer:
            return False, "Il vous manque des intervalles dans la réponse"

    return True, "correct"
