from bioinfo.molecules.sequence import Sequence
from bioinfo.assembly.overlap import Pair

if __name__ == '__main__':
    # first = Sequence('tcgat')
    # second = Sequence('atcg')
    first = Sequence('acg', is_dna = False)
    second = Sequence('acg', is_dna = False)
    pair = Pair(first, second)
    pair.combine()

