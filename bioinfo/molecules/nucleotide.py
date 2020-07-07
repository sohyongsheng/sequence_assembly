from bioinfo.molecules.bases import (
    NitrogenousBase,
    Thymine,
    Uracil,
)
from bioinfo.molecules.errors import InvalidNucleotide
from bioinfo.molecules.sugars import (
    Deoxyribose,
    PentoseSugar,
    Ribose, 
)

class PhosphateGroup:
    def __init__(self):
        pass

class Nucleotide:
    def __init__(self, base, sugar):
        assert isinstance(base, NitrogenousBase)
        assert isinstance(sugar, PentoseSugar)
        if (
            isinstance(sugar, Deoxyribose) 
            and isinstance(base, Uracil)
        ):
            raise InvalidNucleotide(
                "Cannot have Uracil in DNA nucleotide."
            ) 
        if (
            isinstance(sugar, Ribose)
            and isinstance(base, Thymine)
        ):
            raise InvalidNucleotide(
                "Cannot have Thymine in RNA nucleotide"
            )
        self.base = base
        self.sugar = sugar

    def __eq__(self, other):
        return all([
            self.base == other.base,
            self.sugar == other.sugar,
        ])

    def __str__(self):
        return str(self.base)
        

