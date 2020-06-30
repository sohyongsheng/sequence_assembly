from assembler.sequence import Sequence
from difflib import SequenceMatcher

if __name__ == '__main__':
    seq_str = 'atcg'
    first = Sequence(seq_str)
    second = Sequence(seq_str)
    print(first.nucleotides[0].base == second.nucleotides[1].base)

