# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET

def extract_poem(index):
	a = []
	tree = ET.parse('Poem.xml')
	root = tree.getroot()
	for poem in root:
		if int(poem.get('name')) == index:
			for beit in poem:
				a.append(beit.text)
	ans = []
	for i in range(len(a)/2):
		ans.append((a[2*i],a[2*i+1]))
	return ans

def extract_beits():
	a = []
	tree = ET.parse('Poem.xml')
	root = tree.getroot()
	for poem in root:
		for beit in poem:
			a.append(beit.text)
			break
	return a
