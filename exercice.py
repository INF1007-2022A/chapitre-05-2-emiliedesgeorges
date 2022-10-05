#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from string import digits

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	
	sous_total = 0
	for i in data:
		sous_total += i[1] * i[2]
	sous_total = round(sous_total, 2)

	taxes = sous_total*0.15
	taxes = round(taxes, 2)

	total = taxes + sous_total
	total = round(total, 2) 

	return f"{name}\nSOUS-TOTAL\t {sous_total} $\nTAXES\t\t {taxes : >6} $\nTOTAL\t\t {total} $"


def format_number(number, num_decimal_digits):
	result = ""
	abs_n = int(abs(number))#arrondir vers 0

	if abs_n != 0:
		digits_group = abs_n % 1000
		abs_n //= 1000
		result += f"{abs_n} " + f"{digits_group}"
#cette partie marche pas si nombre est plus grand que 100 000 000 non? genre ça va donner ça 100000 000

	decimal_part = int(abs(number)%1*10**num_decimal_digits)
	result += "." + str(decimal_part)
	
	return result.strip()



def get_triangle(num_rows):
	countA = 0
	lignes_triangle = "x"+" "*(num_rows-1) +"A" + " "*(num_rows-1) + "x" "\n"
	for i in range(1, num_rows):
		lignes_triangle += "x" + (num_rows-1-i)*" " + (2*i+1)*"A" + (num_rows-1-i)*" " + "x" + "\n"
	ligne_x = "x"*(2*num_rows+1)
	return f"{ligne_x}\n{lignes_triangle}{ligne_x}"


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
