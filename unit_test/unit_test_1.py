def clean_name(name):
    """ Cleans a customer name by stripping spaces and capitalizing words"""
    return " ".join(name.strip().title().split())

import unittest

class TestDataCleaning(unittest.TestCase):
    def test_clean_name(self):
        self.assertEqual(clean_name(" john do      "),"John Do")
        self.assertEqual(clean_name("HoAng LonG    "),"Hoang Long")
        self.assertEqual(clean_name("   aLiSsan dra     "),"Alissan Dra")

if __name__ == "__main__":
    unittest.main()