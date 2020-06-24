from assembler.nucleic_acid.bases import (
    Thymine,
    Uracil,
)
from assembler.nucleic_acid.sugars import (
    Ribose, 
    Deoxyribose,
)

class PhosphateGroup:
    def __init__(self):
        pass

class Nucleotide:
    def __init__(self, base, sugar):
        if isinstance(sugar, Deoxyribose):
            assert not isinstance(base, Uracil)
        if isinstance(sugar, Ribose):
            assert not isinstance(base, Thymine)
        self.base = base
        self.sugar = sugar
        self.phosphate = PhosphateGroup()

