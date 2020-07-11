from bioinfo.molecules.bases import (
    Adenine, 
    Thymine,
    Cytosine,
    Guanine,
    Uracil,
)
from bioinfo.molecules.nucleotide import Nucleotide
from bioinfo.molecules.sugars import (
    Deoxyribose,
    Ribose, 
)

class Sequence:
    mapping = {
        'a': Adenine,
        't': Thymine,
        'c': Cytosine,
        'g': Guanine,
        'u': Uracil,
    }

    def __init__(self, seq_str, is_dna = True):
        self.seq_str = seq_str
        self.is_dna = is_dna
        self.nucleotides = self.get_nucleotides(self.seq_str)

    def __len__(self):
        return len(self.seq_str)

    def get_nucleotides(self, seq_str):
        nucleotides = [
            self.get_nucleotide(c)
            for c in seq_str
        ]
        return nucleotides

    def get_nucleotide(self, c):
        get_base = self.mapping[c]
        base = get_base()
        sugar = Deoxyribose() if self.is_dna else Ribose()
        nucleotide = Nucleotide(base, sugar)
        return nucleotide

    def __str__(self):
        s = ''.join(
            str(nucleotide.base) 
            for nucleotide in self.nucleotides
        )
        prefix = "DNA" if self.is_dna else "RNA"
        s = f"{prefix}: {s}"
        return s

