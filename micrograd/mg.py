"""
Micro grad implementations
"""

from __future__ import annotations
from collections.abc import Iterable


class Neuron:
    """
    what does single neuron contains
    """

    def __init__(self, data, _children: Iterable | None = None) -> None:
        self.data = data
        self._prev = set(_children) if _children else set()

    def test(self):
        """temp method to test"""
        print(3 + self)

    def __str__(self) -> str:
        return f"Data:{self.data}"

    def __add__(self, other: Neuron) -> Neuron:
        data = self.data + other.data

        return Neuron(data, _children=(self, other))

    def __radd__(self, val: int | float) -> Neuron:
        other = Neuron(val)
        data = self.data + other.data
        return Neuron(data, _children=(self, other))

    def __mul__(self, other: Neuron) -> Neuron:
        data = self.data * other.data
        return Neuron(data, _children=(self, other))

    def __rmul__(self, val: int | float) -> Neuron:
        other = Neuron(val)
        data = self.data * other.data
        return Neuron(data, _children=(self, other))

    @property
    def prev(self):
        """
        Getter property for protected variable _prev
        """
        return self._prev


if __name__ == "__main__":
    n1 = Neuron(2)
    n1.test()
