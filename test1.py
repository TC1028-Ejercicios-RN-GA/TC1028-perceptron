#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import perceptron


class Testprueba (unittest.TestCase):

    def test_codificacion(self):
        self.assertEqual(perceptron.salida_neurona(
            [1,3],[2,-4]), 4.5397868702434395e-05)
        self.assertEqual(perceptron.salida_neurona(
            [-1,2],[-0.52,-.4]), 0.43045377606077095)
       



if __name__ == '__main__':
    unittest.main()
