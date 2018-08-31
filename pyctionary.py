#!/usr/bin/python3
import nltk
try:
	from nltk.corpus import wordnet
except ImportError:
	nltk.download('wordnet')
import sys

try:
	try:
		word = str(sys.argv[1])
		synsets = wordnet.synsets(word)
	except IndexError:
		print ("Enter Words as parameter to Search \n Ex.$ pyctionary hello")
		exit(0)
except SyntaxError:
	print("Python 3: Incompatible")
	exit(0)
try:
	if synsets == []:
		print ("Word Not available! Sorry!")

	for synset in synsets:
		print "-" * 10
		print "Name\t\t:", synset.name()
		print "Lexical Type\t:", synset.lexname()
		print "Lemmas\t\t:", synset.lemma_names()
		print "Definition\t:", synset.definition()
		print "_"*20
		print "Usage:\n"
		for example in synset.examples():
			print ">",example
except SyntaxError:
	print("Python 3: In-compatible")

