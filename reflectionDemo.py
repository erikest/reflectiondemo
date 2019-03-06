#!/user/bin/python

import os, sys, re

def printDetails(module, search):
	functions = []
	for f in dir(module):
		if search in f:
			functions.append(f)

	functionsSorted = sorted(functions)

	for function in functionsSorted:
		print("Function: %s\nHelp: " % function)
		help(function)

def main():
	search = raw_input("Search for: ")
	print("Search for %s in os, sys, re" % search)
	while (len(search) > 0):
		print("os results: ")
		printDetails(os, search)
		print("\n\nsys results: ")
		printDetails(sys, search)
		print("\n\nre results: ")
		printDetails(re, search)
		print("\n\n")
		search = raw_input("Search for: ")

if __name__ == '__main__':
	main()
	
