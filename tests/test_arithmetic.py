from bm_nose import BitVectorTest

class TestClass(BitVectorTest):
	def test_and(self):
		u = self.random_vector()
		v = self.random_vector()
		assert u&v == v&u

	def test_or(self):
		u = self.random_vector()
		v = self.random_vector()
		assert u|v == v|u

	def test_not(self):
		v = self.random_vector()
		v.resize(self.size)
		assert (v & ~v).count() == 0
		assert (v | ~v).count() == self.size
