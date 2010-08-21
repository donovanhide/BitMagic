"""
Illustrate the counting problem where after a certain amount of
bits in the vector have been set, the count() method starts returning
incorrect results.
"""
from bm import BitVector
from math import log10

def test(base, exp):
	size =  base ** exp
	## print out header
	s = [
		"Size / Divisor",
		"Number Bits Set",
		"Count Result",
		"Percent Bits Set"
	]
	print "".join(map(lambda x: x.rjust(25), s))
	print "="*100

	for i in range(exp):
		v = BitVector()
		divisor = base ** (exp-i)
		set = size/divisor
		for i in range(set):
			v[i*divisor] = 1
		count = v.count()
		pct = (100 * float(set) / size)

		### print out status...
		s = [
			"%d / %d" % (size, divisor),
			"%d" % (set,),
			"%d" % (count,),
			"%.08f" % (pct,)
		]
		print "".join(map(lambda x: x.rjust(25), s))
		assert count == set

if __name__ == '__main__':
	from sys import argv, exit
	
	try:
		base = int(argv[1])
		exp = int(argv[2])
	except:
		print """
		Usage: %s base exp

		Run test on vector of size base ** exp, setting more
		bits each iteration.
		""" % (argv[0],)
		
	test(base, exp)
