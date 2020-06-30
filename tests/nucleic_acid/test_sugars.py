from assembler.nucleic_acid.sugars import (
    Deoxyribose,
    Ribose, 
)

class TestRibose:
    def test_eq(self):
        # Same object, and equal.
        sugar = Ribose()
        assert sugar is sugar
        assert sugar == sugar

        # Different objects, but still equal.
        another_sugar = Ribose()
        assert sugar is not another_sugar
        assert sugar == sugar

class TestDeoxyribose:
    def test_eq(self):
        # Same object, and equal.
        sugar = Deoxyribose()
        assert sugar is sugar
        assert sugar == sugar

        # Different objects, but still equal.
        another_sugar = Deoxyribose()
        assert sugar is not another_sugar
        assert sugar == sugar

class TestPentoseSugar:
    def test_eq(self):
        ribose = Ribose()
        deoxyribose = Deoxyribose()
        assert ribose is not deoxyribose
        assert ribose != deoxyribose

