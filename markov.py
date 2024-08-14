def gen_markov_model(text: str):
    t = list(text)
    t.append("<eos>")

    d: dict[str, list] = {}

    for i in range(1, len(t)):
        c0 = t[i - 1]
        c1 = t[i]
        if c0 in d:
            d[c0].append(c1)
    return d
