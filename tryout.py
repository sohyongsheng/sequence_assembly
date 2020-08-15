from bioinfo.molecules.sequence import Sequence
from bioinfo.assembly.overlap import Pair

if __name__ == '__main__':
    first = Sequence('atcg')
    second = Sequence('tcgat')
    pair = Pair(first, second)
    combined = pair.combine()
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Combined: {combined}")
    print(f"Overlap length: {pair.overlap_length}")
    print()

    first = Sequence('a')
    second = Sequence('t')
    pair = Pair(first, second)
    combined = pair.combine()
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Combined: {combined}")
    print(f"Overlap length: {pair.overlap_length}")
    print()

    first = Sequence('')
    second = Sequence('')
    pair = Pair(first, second)
    combined = pair.combine()
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Combined: {combined}")
    print(f"Overlap length: {pair.overlap_length}")

