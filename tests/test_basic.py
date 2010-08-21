from bm_nose import BitVectorTest
from bm import BitVector

class TestClass(BitVectorTest):
	def test_setget(self):
		v = BitVector()
		assert v.any() == False
		assert v.none() == True
		v[0] = 1
		v[2] = True
		assert v.any() == True
		assert v.none() == False
		assert v[0] == True
		assert v[1] == False
		assert v[2] == True
		assert v[3] == False

	def test_setclear(self):
		v = BitVector()
		v.resize(100)

		assert v.any() == False
		assert v.none() == True

		v.set()

		assert v.any() == True
		assert v.none() == False
		assert v.count() == len(v)

		v.clear()

		assert v.any() == False
		assert v.none() == True
		assert v.count() == 0

	def test_iter(self):
		v = BitVector()
		for i in range(500):
			v[i*2] = True
		i = 0
		for j in v:
			assert i == j
			i = i + 2
		assert i == 1000

	def test_cmp(self):
		u = self.random_vector()
		v = ~u
		assert u != v
		assert v == ~u

	def test_serialize(self):
		v = self.random_vector()
		u = BitVector()
		assert u != v
		s = v.serialize()
		u.deserialize(s)
		assert u == v

	def test_size(self):
		v = BitVector()
		v.resize(10)
		for i in range(5):
			v[i*2] = True
		assert len(v) == 10
		assert v.count() == 5
