import unittest
import random

from main import Organizer


class TestCases(unittest.TestCase):
    """
    Description:
        test suite of test cases
    """
    def setUp(self):
        """
        Description:
            creating setup for all the test case
        """
        self.case1_file_path = "sample1.csv"
        self.case2_file_path = "sample2.csv"
        self.case3_file_path = "sample3.csv"
        self.load_testing_file_path = "sampleload_test.csv"
        
    def test_case1(self):
        """
        Description:
            running test cases for multiple booked hours
            and sample1.csv
        """
        # Running 3 test cases with random number of booked
        # hrs for case1_file_path
        
        for e in range(0, 3):
            booked_hrs = random.randint(1, 10)
            print "############## Calculating both cases for %s ###########" % booked_hrs
            o = Organizer(self.case1_file_path, booked_hrs)
            o.calculate()

    def test_case2(self):
        """
        Description:
            running test cases for multiple booked hours
            and sample2.csv
        """
        # Running 3 test cases with random number of booked
        # hrs for case2_file_path
        
        for e in range(0, 3):
            booked_hrs = random.randint(1, 10)
            print "############## Calculating both cases for %s ###########" % booked_hrs
            o = Organizer(self.case2_file_path, booked_hrs)
            o.calculate()

    def test_case3(self):
        """
        Description:
            running test cases for multiple booked hours
            and sample3.csv
        """
        # Running 3 test cases with random number of booked
        # hrs for case3_file_path
        
        for e in range(0, 3):
            booked_hrs = random.randint(1, 10)
            print "############## Calculating both cases for %s ###########" % booked_hrs
            o = Organizer(self.case3_file_path, booked_hrs)
            o.calculate()

    def test_load(self):
        """
        Description:
            running test cases for multiple booked hours
            and sample_load.csv
        """
        # Running 3 test cases with random number of booked
        # hrs for load_testing_file_path
        
        for e in range(0, 3):
            booked_hrs = random.randint(1, 10)
            print "############## Calculating both cases for %s ###########" % booked_hrs
            o = Organizer(self.load_testing_file_path, booked_hrs)
            o.calculate()


if __name__ == "__main__":
    unittest.main()
