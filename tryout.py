from bioinfo.molecules.sequence import Sequence
from bioinfo.assembly.overlap import Pair

if __name__ == '__main__':
    first = Sequence('tcgat')
    second = Sequence('atcg')
    pair = Pair(first, second)
    combined = pair.combine()
    print(pair)

