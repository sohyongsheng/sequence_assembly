import numpy as np

from bioinfo.assembly.errors import InvalidPair
from bioinfo.molecules.sequence import Sequence

class LargestOverlapFinder:
    def __init__(self):
        pass

    # Get indices a, b, c, d of longest substrings first,
    # such that substring == first[a: b] == second[c: d].
    # Also returns length of substring.
    def get_substrings(self, counter):
        while not np.all(counter == 0):
            i, j = np.unravel_index(counter.argmax(), counter.shape)
            length = counter[i, j]
            for k in range(length):
                counter[i - k, j - k] = 0
            b, d = i + 1, j + 1
            a, c = b - length, d - length
            indices = a, b, c, d
            yield indices, length

    def is_overlap(self, indices, first, second):
        a, b, c, d = indices
        # First overlaps with second, e.g.
        # 0123
        #  1234
        #  ^^^
        if b == len(first) and c == 0:
            return True
        # Second overlaps with first, e.g.
        #  1234
        # 0123
        #  ^^^
        elif a == 0 and d == len(second):
            return True
        # First is within second, e.g.
        #  123
        # 01234
        #  ^^^
        elif a == 0 and b == len(first):
            return True
        # Second is within first, e.g.
        # 01234
        #  123
        #  ^^^
        elif c == 0 and d == len(second):
            return True
        else:
            return False

    # Taken from longest common substring problem. See 
    # following for tutorial on dynamic programming solution:
    # https://www.youtube.com/watch?v=BysNXJHzCEs
    def tally_counter(self, first, second):
        num_rows = len(first) + 1
        num_cols = len(second) + 1
        counter = np.zeros((num_rows, num_cols), dtype = int)
        for i, m in enumerate(first, start = 1):
            for j, n in enumerate(second, start = 1):
                if m == n:
                    counter[i, j] = counter[i - 1, j - 1] + 1
        counter = self.remove_first_row_first_col(counter)
        return counter

    def find(self, first, second):
        counter = self.tally_counter(first, second)
        for indices, length in self.get_substrings(counter):
            a, b, c, d = indices
            assert first[a: b] == second[c: d]
            if self.is_overlap(indices, first, second):
                return indices, length
        else:
            indices, length = None, 0
            return indices, length

    def remove_first_row_first_col(self, x):
        return x[1:, 1:]

class Pair:
    finder = LargestOverlapFinder()

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if self.first.is_dna != self.second.is_dna:
            raise InvalidPair(
                "Cannot compare DNA with RNA sequences."
            )
        self.indices, self.overlap_length = self.finder.find(
            self.first.seq_str, 
            self.second.seq_str,
        )

    def combine(self):
        first = self.first.seq_str
        second = self.second.seq_str
        # No overlap, so just concatenate.
        if self.overlap_length == 0:
            combined = first + second
            return Sequence(
                combined, 
                is_dna = self.first.is_dna,
            )
        else:
            a, b, c, d = self.indices
            # First overlaps with second, e.g.
            # 0123
            #  1234
            #  ^^^
            if b == len(self.first) and c == 0:
                prefix = first[:a]
                assert first[a: b] == second[c: d]
                overlap = first[a: b]
                suffix = second[d:]
                combined = prefix + overlap + suffix
                return Sequence(
                    combined, 
                    is_dna = self.first.is_dna,
                )
            # Second overlaps with first, e.g.
            #  1234
            # 0123
            #  ^^^
            elif a == 0 and d == len(self.second):
                prefix = second[:c]
                assert second[c: d] == first[a: b]
                overlap = second[c: d]
                suffix = first[b:]
                combined = prefix + overlap + suffix
                return Sequence(
                    combined, 
                    is_dna = self.first.is_dna,
                )
            # First is within second, e.g.
            #  123
            # 01234
            #  ^^^
            elif a == 0 and b == len(self.first):
                return Sequence(
                    second, 
                    is_dna = self.second.is_dna,
                )
            # Second is within first, e.g.
            # 01234
            #  123
            #  ^^^
            elif c == 0 and d == len(self.second):
                return Sequence(
                    first, 
                    is_dna = self.first.is_dna,
                )


