def compute_failure(pattern):
    n = len(pattern)
    failure = [0] * n

    length = 0
    i = 1

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            failure[i] = length
            i += 1
        else:
            if length != 0:
                # retrocede al prefijo-sufijo más corto anterior
                length = failure[length - 1]
            else:
                failure[i] = 0
                i += 1

    return failure
