import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [5, 2, -3, -7, 0, -5]
    right = [9, -4, 0, -8, 0, 15]
    expected = [14, -2, -3, -15, 0, 10]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)

def test_multiply(self):
    left = [5, 2, -3, -7, 0, -5]
    right = [9, -4, 0, -8, 0, 15]
    expected = [45, -8, 0, 56, 0, -75]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.multiply(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()
