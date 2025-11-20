import unittest
from ai_agent import UniversalCreditAgent

class TestUniversalCreditAgent(unittest.TestCase):
    def test_initialization(self):
        agent = UniversalCreditAgent()
        self.assertIsInstance(agent, UniversalCreditAgent)

if __name__ == '__main__':
    unittest.main()
