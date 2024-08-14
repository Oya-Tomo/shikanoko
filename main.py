import random
import pprint


def gen_markov_model(text: str):
    t = list(text)
    t.append("<eos>")

    d: dict[str, list] = {}

    for i in range(1, len(t)):
        c0 = t[i - 1]
        c1 = t[i]
        if c0 in d:
            d[c0].append(c1)
        else:
            d[c0] = []
            d[c0].append(c1)

    return d


def gen_text(model: dict[str, list], start_char: str):
    text = [start_char]
    while text[-1] != "<eos>":
        c = text[-1]
        op = model[c]
        cn = random.choice(op)
        text.append(cn)
    return "".join(text[:-1])


input_text = "しかのこのこのここしたんたん"
model = gen_markov_model(input_text)

pprint.pprint(model)
output_text = gen_text(model, "し")
print(output_text)

# {'か': ['の'],
#  'こ': ['の', 'の', 'こ', 'し'],
#  'し': ['か', 'た'],
#  'た': ['ん', 'ん'],
#  'の': ['こ', 'こ', 'こ'],
#  'ん': ['た', '<eos>']}
# しかのこのこのこのこのこここしかのこここのこのこのこのこしたん
