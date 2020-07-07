import pytest

from bioinfo.assembly.errors import InvalidPair
from bioinfo.assembly.overlap import Pair
from bioinfo.molecules.sequence import Sequence

class TestPair:
    def test_init(self):
        # Can compare between DNA fragments.
        first = Sequence('acg')
        second = Sequence('acg')
        pair = Pair(first, second)

        # Can also compare between RNA fragments.
        first = Sequence('acg', is_dna = False)
        second = Sequence('acg', is_dna = False)
        pair = Pair(first, second)

        # Comparing between DNA and RNA fragments 
        # will raise an exception.
        first = Sequence('acg', is_dna = True)
        second = Sequence('acg', is_dna = False)
        with pytest.raises(InvalidPair):
            pair = Pair(first, second)



