class NitrogenousBase:
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(self, type(other))

class Pyrimidine(NitrogenousBase):
    def __init__(self):
        self.num_rings = 1

class Purine(NitrogenousBase):
    def __init__(self):
        self.num_rings = 2

class Adenine(Purine):
    def __init__(self):
        self.complement = Thymine

    def __str__(self):
        return 'a'

class Thymine(Pyrimidine):
    def __init__(self):
        self.complement = Adenine

    def __str__(self):
        return 't'

class Cytosine(Pyrimidine):
    def __init__(self):
        self.complement = Guanine

    def __str__(self):
        return 'c'

class Guanine(Purine):
    def __init__(self):
        self.complement = Cytosine

    def __str__(self):
        return 'g'

class Uracil(Pyrimidine):
    def __init__(self):
        self.complement = Adenine

    def __str__(self):
        return 'u'


