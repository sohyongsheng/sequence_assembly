import numpy as np

from bioinfo.assembly.errors import InvalidPair
from bioinfo.molecules.sequence import Sequence

class LargestOverlapFinder:
    def __init__(self):
        pass

    def find(self, first, second):
        # Modified from longest common substring problem.
        # See following for tutorial on dynamic programming 
        # solution:
        # https://www.youtube.com/watch?v=BysNXJHzCEs
        num_rows = len(first) + 1
        num_cols = len(second) + 1
        array = np.zeros((num_rows, num_cols), dtype = int)
        for i, m in enumerate(first, start = 1):
            for j, n in enumerate(second, start = 1):
                if m == n:
                    array[i, j] = array[i - 1, j - 1] + 1

        # Where finding longest overlap differs from finding
        # longest common substring: finding overlap requires
        # substring to be at the end of the sequence. This means
        # we need to search for numbers that run diagonally from
        # first row to last column, or first column to last row.
        last_row = array[-1, 1:]
        last_col = array[1:, -1]
        p = self.get_largest_overlap(last_row)
        q = self.get_largest_overlap(last_col)
        if p >= q:
            to_swap = False
            overlap_len = p
        else:
            to_swap = True
            overlap_len = q
        return to_swap, overlap_len

    def get_largest_overlap(self, x):
        expected = np.arange(1, len(x) + 1)
        is_overlap = (x == expected)
        (indices,) = is_overlap.nonzero()
        if indices:
            last_occurred = indices[-1]
            overlap_len = last_occurred + 1
        else:
            overlap_len = 0
        return overlap_len

class Pair:
    finder = LargestOverlapFinder()

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if self.first.is_dna != self.second.is_dna:
            raise InvalidPair(
                "Cannot compare DNA with RNA sequences."
            )
        self.to_swap, self.overlap_len = self.finder.find(
            self.first.nucleotides, 
            self.second.nucleotides,
        )

    def combine(self):
        if self.to_swap:
            first, second = self.second, self.first
        else:
            first, second = self.first, self.second
        k = self.overlap_len
        prefix = first.seq_str[: -k]
        overlap = first.seq_str[-k: ]
        suffix = second.seq_str[k: ]
        combined = Sequence(prefix + overlap + suffix)
        return combined

    def __str__(self):
        if self.to_swap:
            first, second = self.second, self.first
        else:
            first, second = self.first, self.second
        k = self.overlap_len
        n = total_len = len(first) + len(second) - k
        prefix = "DNA" if first.is_dna else "RNA"
        prefix = f"{prefix} pair:"
        space, arrow = '.', '^'
        suffix = ''.join([
            space * (len(first) - k),
            arrow * k,
            space * (len(second) - k),
        ])
        s = '\n'.join([
            prefix,
            first.seq_str.ljust(n),
            second.seq_str.rjust(n),
            suffix,
        ])
        return s




