import unittest
import Experiment

class MyTestCase(unittest.TestCase):

  def test_t7(self):
    self.assertRaises(ValueError, Experiment.largest, [])

if __name__ == '__main__':
  unittest.main()