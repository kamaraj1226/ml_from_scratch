'''
Test cases for micro grad
'''
import unittest
from mg import Neuron


class NeuronTests(unittest.TestCase):
    '''
    Tests for Neuron
    '''
    def test_str(self):
        '''
        Check string represntation
        '''
        n1 = Neuron(2)
        assert str(n1) == "Data:2"

    def test_add(self):
        '''
        check if we can add
        '''

        n1 = Neuron(2)
        n2 = Neuron(3)
        result: Neuron = n1 + n2
        assert str(result) == 'Data:5'
        previous = result.prev
        assert n1 in previous and n2 in previous

    def test_mul(self):
        '''
        check if we can add
        '''

        n1 = Neuron(2)
        n2 = Neuron(3)
        result = n1 * n2
        assert str(result) == 'Data:6'
        previous = result.prev
        assert n1 in previous and n2 in previous
