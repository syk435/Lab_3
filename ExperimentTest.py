import unittest
import Experiment

class MyTestCase(unittest.TestCase):

  def test_t1(self):
    r1 = Experiment.largest([1,1,1]) 
    self.assertEqual(r1, 1)

  def test_t2(self):
    r1 = Experiment.largest([3,2,1]) 
    self.assertEqual(r1, )

  def test_t7(self):
    self.assertRaises(ValueError, Experiment.largest, [])
	
  def test_logout(self):
    r1 = Experiment.largest([-1,-1,-1,-1,-4]) 
    self.assertEqual(r1, -9)

if __name__ == '__main__':
  unittest.main()