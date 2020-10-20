""" 4- Crie um programa que receba um valor e mostre seu dobro, seu triplo e sua raiz quadrada """
import math

valor = float(input("Insira um valor:\n"))

print(f"O dobro do valor é: {valor * 2}")
print(f"O triplo do valor é: {valor * 3}")
print(f"A raiz quadrada é: {valor ** 0,5}")

print(f"Metodo pow: {math.pow(valor, 1/2)}")
print(f"Metodo sqrt: {math.sqrt(valor)}")
