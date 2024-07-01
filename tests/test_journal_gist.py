"""This module tests the journal gist module."""

import unittest
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG, 
                    filename="test_journal_gist_output.log")

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

class TestJournalGist(unittest.TestCase):
    """This class is used to define specific unit tests.

    Args:
        unittest (module): This module is used to enable unit testing.
    """

    def setUp():
        pass

    def tearDown():
        pass



if __name__ == '__main__':
    unittest.main()
