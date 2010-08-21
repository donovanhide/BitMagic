class BitVectorTest:
	def __init__(self, size=1000000, chance=0.10):
		self.size = size
		self.chance = chance

	def setUp(self):
		from random import seed
		from time import time
		seed(time())

	def random_vector(self, quiet=True):
		from random import random
		from bm import BitVector

		v = BitVector()
		def f():
			for i in range(int(self.size * self.chance)):
				j = int(self.size * random())
				if j >= self.size:
					continue
				v[j] = 1
		if not quiet:
			print
			print "="*50
			self.time(f, "Allocate Random Vector")
			v.print_stats()
		else:
			f()
		return v

	def time(self, f, desc, iterations=1):
		from datetime import datetime
		start = datetime.now()
		for i in range(iterations):
			f()
		end = datetime.now()
		delta = end - start
		s = desc.rjust(25)
		s = s + " %s" % (delta,)
		if iterations > 1:
			s = s + " (%s/iteration)" % (delta/iterations)
		print s
