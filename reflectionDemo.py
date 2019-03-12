#!/user/bin/python

import os, sys, re, importlib

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
	modulesStr = raw_input("Modules to load:")
	modules = modulesStr.split(' ')

	search = raw_input("Search: ")
	
	print("Search for %s in %s" % (search, modules))
	
	while (len(search) > 0):
		for moduleName in modules:
			try:
				module = importlib.import_module(moduleName)
				print('%s results: ' % moduleName)
				printDetails(module, search)
				print('\n')
			except ImportError:
				print('Module %s not found' % moduleName)
	
		search = raw_input("Search: ")

if __name__ == '__main__':
	main()
	
