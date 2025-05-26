# test_agent.py
# This file contains unit tests for the agent.py script.

import unittest
from agent import run_ai_agent # Assuming agent.py is in the same directory or PYTHONPATH

class TestAgent(unittest.TestCase):
    """
    Test suite for the run_ai_agent function in agent.py.
    """

    def test_run_ai_agent_success(self):
        """
        Tests the run_ai_agent function with a valid API key and prompt.
        """
        api_key = "testkey123"
        prompt = "test prompt"
        expected_response = "AI (using key 'test...123'): Processed 'test prompt'"
        self.assertEqual(run_ai_agent(api_key, prompt), expected_response)

    def test_run_ai_agent_success_short_key(self):
        """
        Tests the run_ai_agent function with a short API key (less than 8 chars).
        """
        api_key = "key123"
        prompt = "short key test"
        # As per agent.py logic, if key is too short, it's displayed as is.
        expected_response = f"AI (using key '{api_key}'): Processed '{prompt}'"
        self.assertEqual(run_ai_agent(api_key, prompt), expected_response)

    def test_run_ai_agent_no_apikey(self):
        """
        Tests the run_ai_agent function when None is provided as the API key.
        """
        prompt = "test prompt with no key"
        expected_response = "Error: API key not provided."
        self.assertEqual(run_ai_agent(None, prompt), expected_response)

    def test_run_ai_agent_empty_apikey(self):
        """
        Tests the run_ai_agent function when an empty string is provided as the API key.
        """
        prompt = "test prompt with empty key"
        expected_response = "Error: API key not provided."
        self.assertEqual(run_ai_agent("", prompt), expected_response)

if __name__ == '__main__':
    unittest.main()
