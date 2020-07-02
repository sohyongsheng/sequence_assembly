from assembler.nucleic_acid.sequence import Sequence

class TestSequence:
    def test_init(self):
        # Nucleotides of the same type in a sequence are 
        # different objects and take up their own memory.
        sequence = Sequence('aa')
        first, second = sequence.nucleotides
        assert first == second
        assert first is not second

