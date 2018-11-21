f = {'segitiga' : 'L = 0.5 * a * t', 'persegi' : 'L = s ** 2', 'persegi panjang' : 'L = p * 1', 'lingkaran' : 'L = pi * r ** 2', 'jajar genjang' : 'L = a * t'}
print('''no	| nama bangun	| rumus luas
----|-----------------|-----------------
1    |segitiga	      |'''+f['segitiga'] +
'''\n2   |persegi	   |'''+f['persegi'] +
'''\n3   |persegi panjang  |'''+f['persegi panjang'] +
'''\n4   |lingkaran	   |'''+f['lingkaran'] +
'''\n5   |jajar genjang    |'''+f['jajar genjang'])
