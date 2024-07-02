"""This module tests the journal gist module."""

import unittest
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG,
                    filename="test_journal_gist_output.log")

sys.path.insert(0,
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

import journal_gist

class TestJournalGist(unittest.TestCase):
    """This class is used to define specific unit tests.

    Args:
        unittest (module): This module is used to enable unit testing.
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_openai_messaging_functions(self) -> None:
        """This method is used to test basic messaging functions."""
        messages = [
            {"role": "system", "content":"You are a helpful assistant."},
            {"role":"user", "content":"Hello!"}
        ]
        response = journal_gist.query_openai(messages)
        logging.info(response)

if __name__ == '__main__':
    unittest.main()
