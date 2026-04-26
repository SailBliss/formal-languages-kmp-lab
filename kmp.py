from failure import compute_failure


def kmp_search(text, pattern):
    if not pattern:
        return []

    failure = compute_failure(pattern)
    matches = []

    i = 0  # index in text
    j = 0  # index in pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                # retrocede en el patrón usando failure, no en el texto
                j = failure[j - 1]
            else:
                i += 1

        if j == len(pattern):
            matches.append(i - j)
            j = failure[j - 1]  # busca siguiente ocurrencia posible

    return matches
