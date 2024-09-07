"""
Micro grad implementations
"""

from __future__ import annotations
from collections.abc import Iterable, Callable


class Neuron:
    """
    what does single neuron contains
    """

    def __init__(self, data, _children: Iterable | None = None) -> None:
        self.data = data
        self._prev = set(_children) if _children else set()
        self.grad: int | float = 0
        # its intresting to note backward will be called by output neuron
        self._backward: Callable = lambda: None

    def __str__(self) -> str:
        return f"Data:{self.data} | Grad:{self.grad}"

    def __add__(self, other: Neuron | int | float) -> Neuron:

        if isinstance(other, int):
            other = Neuron(other)
        elif isinstance(other, float):
            other = Neuron(other)
        elif isinstance(other, Neuron):
            pass
        data = self.data + other.data
        out = Neuron(data, _children=(self, other))

        def _backward():
            # local derivative time global derivative
            # for addition local derivative will be 1
            # global derivate will be out.grad
            self.grad = 1.0 * out.grad
            other.grad = 1.0 * out.grad

        out._backward = _backward

        return out

    # def __radd__(self, val: int | float) -> Neuron:
    #     other = Neuron(val)
    #     data = self.data + other.data
    #     out = Neuron(data, _children=(self, other))

    #     def _backward():
    #         self.grad = 1.0 * other.data * out.grad
    #         other.grad = 1.0 * self.data * out.grad

    #     out._backward = _backward
    #     return out

    def __mul__(self, other: Neuron | int | float) -> Neuron:
        if isinstance(other, int):
            other = Neuron(other)
        elif isinstance(other, float):
            other = Neuron(other)
        elif isinstance(other, Neuron):
            pass
        data = self.data * other.data
        out = Neuron(data, _children=(self, other))

        def _backward():
            # local derivative time global derivative
            # for multiplication local derivative will be other.data
            # global derivate will be out.grad
            self.grad = other.data * out.grad
            other.grad = self.data * out.grad

        out._backward = _backward

        return out

    # def __rmul__(self, val: int | float) -> Neuron:
    #     other = Neuron(val)
    #     data = self.data * other.data
    #     return Neuron(data, _children=(self, other))

    @property
    def prev(self):
        """
        Getter property for protected variable _prev
        """
        return self._prev

    def backprop(self):
        """
        Backpropagate
        """
        return self._backward()


def main():
    """
    main function to test things
    """
    x1 = Neuron(2)
    x2 = Neuron(4)
    w1 = Neuron(3)
    w2 = Neuron(5)
    b = Neuron(10)
    x1w1 = x1 * w1
    x2w2 = x2 * w2

    x1w1_x2w2 = x1w1 + x2w2
    x1w1_x2w2_b = x1w1_x2w2 + b

    x1w1_x2w2_b.grad = 1
    x1w1_x2w2_b.backprop()
    x1w1_x2w2.backprop()
    x1w1.backprop()
    x2w2.backprop()

    print("======================================")
    print("after backpropogation")
    print("x1", x1)
    print("w1", w1)
    print("x2", x2)
    print("w2", w2)
    print("x1w1", x1w1)
    print("x2w2", x2w2)
    print("x1w1_x2w2", x1w1_x2w2)
    print("x1w1_x2w2_b", x1w1_x2w2_b)
    print("b", b)


if __name__ == "__main__":
    main()
