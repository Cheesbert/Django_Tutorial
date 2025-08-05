from enum import Enum
from ..algorithm_implementations import sorting

"""
Constant accessing implemented algorithm_implementations
"""
class SortMethods(Enum):
    BUBBLE = ("bubble", "Bubblesort", sorting.bubblesort)
    QUICK = ("quick", "Quicksort", sorting.quicksort)
    HEAP = ("heap", "Heapsort", sorting.heapsort)

    def __init__(self, key, label, func):
        self._key = key
        self.label = label
        self.func = func

    @property
    def value(self):
        return self._key

    @classmethod
    def choices(cls):
        return [(member.value, member.label) for member in cls]

    @classmethod
    def get_func(cls, key):
        return {member.value: member.func for member in cls}.get(key)


if __name__ == "__main__":
    print(tuple(SortMethods))

