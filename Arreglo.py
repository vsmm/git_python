#!/usr/bin/python3
#-*-coding: utf-8 -*-
from array import array

miArreglo = array("i", [10,20,30])
i = 0
print("hola")
for value in miArreglo:
	print("miArreglo[{0}] es {1}" .format(i,value))
	i += 1
