from bioinfo.molecules.bases import (
    Adenine, 
    Thymine,
    Cytosine,
    Guanine,
    Uracil,
)

class TestAdenine:
    def test_eq(self):
        # Same object, and equal.
        base = Adenine()
        assert base is base
        assert base == base

        # Different objects, but still equal.
        another_base = Adenine()
        assert base is not another_base
        assert base == another_base

class TestThymine:
    def test_eq(self):
        # Same object, and equal.
        base = Thymine()
        assert base is base
        assert base == base

        # Different objects, but still equal.
        another_base = Thymine()
        assert base is not another_base
        assert base == another_base

class TestCytosine:
    def test_eq(self):
        # Same object, and equal.
        base = Cytosine()
        assert base is base
        assert base == base

        # Different objects, but still equal.
        another_base = Cytosine()
        assert base is not another_base
        assert base == another_base

class TestGuanine:
    def test_eq(self):
        # Same object, and equal.
        base = Guanine()
        assert base is base
        assert base == base

        # Different objects, but still equal.
        another_base = Guanine()
        assert base is not another_base
        assert base == another_base

class TestUracil:
    def test_eq(self):
        # Same object, and equal.
        base = Uracil()
        assert base is base
        assert base == base

        # Different objects, but still equal.
        another_base = Uracil()
        assert base is not another_base
        assert base == another_base

class TestNitrogenousBase:
    def test_eq(self):
        adenine = Adenine()
        thymine = Thymine()
        cytosine = Cytosine()
        guanine = Guanine()
        uracil = Uracil()

        # Adenine vs rest of bases.
        assert adenine != thymine
        assert adenine != cytosine
        assert adenine != guanine
        assert adenine != uracil

        # Thymine vs rest of bases.
        assert thymine != cytosine
        assert thymine != guanine
        assert thymine != uracil

        # Cytosine vs rest of bases.
        assert cytosine != guanine
        assert cytosine != uracil

        # Guanine vs rest of bases.
        assert guanine != uracil

        # Uracil vs rest of bases (none left).
        pass

