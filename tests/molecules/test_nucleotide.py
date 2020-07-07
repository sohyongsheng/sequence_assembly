import pytest

from bioinfo.molecules.bases import (
    Adenine, 
    Thymine,
    Cytosine,
    Guanine,
    Uracil,
)
from bioinfo.molecules.errors import InvalidNucleotide
from bioinfo.molecules.nucleotide import Nucleotide
from bioinfo.molecules.sugars import (
    Deoxyribose,
    Ribose, 
)

@pytest.fixture
def adenine():
    return Adenine()

@pytest.fixture
def thymine():
    return Thymine()

@pytest.fixture
def uracil():
    return Uracil()

@pytest.fixture
def deoxyribose():
    return Deoxyribose()

@pytest.fixture
def ribose():
    return Ribose()

class TestNucleotide:
    def test_init(self,
        adenine, thymine, uracil, 
        deoxyribose, ribose,
    ):
        # Thymine for DNA, okay.
        nucleotide = Nucleotide(thymine, deoxyribose)

        # Uracil for RNA, okay.
        nucleotide = Nucleotide(uracil, ribose)

        # Uracil for DNA, no such nucleotide.
        with pytest.raises(InvalidNucleotide):
            nucleotide = Nucleotide(uracil, deoxyribose)

        # Thymine for RNA, no such nucleotide.
        with pytest.raises(InvalidNucleotide):
            nucleotide = Nucleotide(thymine, ribose)

    def test_eq(self, 
        adenine, thymine, uracil, 
        deoxyribose, ribose,
    ):
        # Compare object with itself.
        nucleotide = Nucleotide(adenine, deoxyribose)
        assert nucleotide == nucleotide
        assert nucleotide is nucleotide

        # Same base and sugar.
        first = Nucleotide(adenine, deoxyribose)
        second = Nucleotide(adenine, deoxyribose)
        assert first == second
        assert first is not second

        # Same base but different sugar.
        first = Nucleotide(adenine, deoxyribose)
        second = Nucleotide(thymine, deoxyribose)
        assert first != second
        assert first is not second

        # Same sugar but different base.
        first = Nucleotide(adenine, ribose)
        second = Nucleotide(adenine, deoxyribose)
        assert first != second
        assert first is not second
        
        # Different sugar and different base.
        first = Nucleotide(adenine, ribose)
        second = Nucleotide(thymine, deoxyribose)
        assert first != second
        assert first is not second
        
