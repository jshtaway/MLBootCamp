import pandas as pd

movements = ['Gothic', 'Renaissance', 'Mannerism', 'Baroque',
             'Rococo', 'Neoclassical', 'Romanticism', 'Academic',
             'Impressionism', 'Pointillism', 'Symbolism',
             'Art Nouveau', 'Tonalism', 'Expressionism',
             'Cubism', 'Futurism', 'Dada', 'Surrealism']


def get_dummies(ds):
    data = {}
    for m in movements:
        data[m] = []
    for row in ds:
        N = 0.
        for m in movements:
            if m in row:
                N += 1
                data[m].append(1)
            else:
                data[m].append(0)
        if N > 0:
            for m in movements:
                data[m][-1] /= N
                data[m][-1] /= N

    return pd.DataFrame(data)
