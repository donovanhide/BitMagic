from bm import BitVector
from sys import stdout

class TestClass:
	def test_count(self):
		base = 2
		exp = 18
		size = base ** exp

		for e in range(exp+1):
			v = BitVector()
			div = base ** (exp-e)
			nbits = size / div

			stdout.write("%d/%d... " % (nbits, size))
			stdout.flush()

			for i in range(nbits):
				v[i*div] = True

			assert v.count() == nbits
