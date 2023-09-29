import unittest
from data_capture import DataCapture


class DataCaptureTest(unittest.TestCase):

    def setUp(self):
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)
        self.stats = self.data_capture.build_stats()


    def test_add(self):
        data_capture = DataCapture()
        self.assertEqual(data_capture._counts[1], 0)
        data_capture.add(1)
        self.assertEqual(data_capture._counts[1], 1)
    
    def test_less(self):
        self.assertEqual(self.stats.less(4), 2)
    
    def test_between(self):
        self.assertEqual(self.stats.between(3, 6), 4)
        self.assertEqual(self.stats.between(6, 9), 2)
        self.assertEqual(self.stats.between(4, 9), 3)

    def test_greater(self):
        self.assertEqual(self.stats.greater(4), 2)


if __name__ == "__main__":
    unittest.main()