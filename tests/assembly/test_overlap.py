import pytest

from bioinfo.assembly.errors import InvalidPair
from bioinfo.assembly.overlap import (
    LargestOverlapFinder, 
    Pair,
)
from bioinfo.molecules.sequence import Sequence

class TestLargestOverlapFinder:
    def test_find(self):
        finder = LargestOverlapFinder()

        # First overlaps with second, e.g.
        # 0123
        #  1234
        #  ^^^
        first = '0123'
        second = '1234'
        indices, length = finder.find(first, second)
        a, b, c, d = indices
        assert (a, b, c, d) == (1, 4, 0, 3)
        assert length == 3

        # Second overlaps with first, e.g.
        #  1234
        # 0123
        #  ^^^
        first = '1234'
        second = '0123'
        indices, length = finder.find(first, second)
        a, b, c, d = indices
        assert (a, b, c, d) == (0, 3, 1, 4)
        assert length == 3

        # First is within second, e.g.
        #  123
        # 01234
        #  ^^^
        first = '123'
        second = '01234'
        indices, length = finder.find(first, second)
        a, b, c, d = indices
        assert (a, b, c, d) == (0, 3, 1, 4)
        assert length == 3

        # Second is within first, e.g.
        # 01234
        #  123
        #  ^^^
        first = '01234'
        second = '123'
        indices, length = finder.find(first, second)
        a, b, c, d = indices
        assert (a, b, c, d) == (1, 4, 0, 3)
        assert length == 3

        # First is same as second.
        first = second = '012'
        indices, length = finder.find(first, second)
        a, b, c, d = indices
        assert (a, b, c, d) == (0, 3, 0, 3)
        assert length == 3

        # No overlap between first and second.
        # Completely different first and second strings.
        first = '0'
        second = '1'
        indices, length = finder.find(first, second)
        assert indices is None
        assert length == 0

        # No overlap between first and second, 
        # even though there's a common substring '123'.
        first = 'a123b'
        second = 'c123d'
        indices, length = finder.find(first, second)
        assert indices is None
        assert length == 0

        # First and second are empty strings.
        first = second = ''
        indices, length = finder.find(first, second)
        assert indices is None
        assert length == 0

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

    def test_combine(self):
        # First overlaps with second, e.g.
        # 0123
        #  1234
        #  ^^^
        first = Sequence('atcg')
        second = Sequence('tcga')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'atcga'

        # Second overlaps with first, e.g.
        #  1234
        # 0123
        #  ^^^
        first = Sequence('tcga')
        second = Sequence('atcg')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'atcga'
        
        # First is within second, e.g.
        #  123
        # 01234
        #  ^^^
        first = Sequence('tcg')
        second = Sequence('atcga')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'atcga'
        
        # Second is within first, e.g.
        # 01234
        #  123
        #  ^^^
        first = Sequence('atcga')
        second = Sequence('tcg')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'atcga'
        
        # No overlap at all.
        first = Sequence('a')
        second = Sequence('t')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'at'

        # Also no overlap at all, but slightly trickier.
        first = Sequence('atcg')
        second = Sequence('ctcg')
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'atcgctcg'
        
        # Same as above, but now test for RNAs.
        # First overlaps with second, e.g.
        # 0123
        #  1234
        #  ^^^
        first = Sequence('aucg', is_dna = False)
        second = Sequence('ucga', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'aucga'

        # Second overlaps with first, e.g.
        #  1234
        # 0123
        #  ^^^
        first = Sequence('ucga', is_dna = False)
        second = Sequence('aucg', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'aucga'
        
        # First is within second, e.g.
        #  123
        # 01234
        #  ^^^
        first = Sequence('ucg', is_dna = False)
        second = Sequence('aucga', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'aucga'
        
        # Second is within first, e.g.
        # 01234
        #  123
        #  ^^^
        first = Sequence('aucga', is_dna = False)
        second = Sequence('ucg', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'aucga'
        
        # No overlap at all.
        first = Sequence('a', is_dna = False)
        second = Sequence('u', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'au'

        # Also no overlap at all, but slightly trickier.
        first = Sequence('aucg', is_dna = False)
        second = Sequence('cucg', is_dna = False)
        pair = Pair(first, second)
        combined = pair.combine()
        assert combined.is_dna == first.is_dna
        assert combined.seq_str == 'aucgcucg'
        
