# Assert facilitates logging. 
import logging
import unittest

class AssertLogging(unittest.TestCase): 

    def test_assert_logging(self) -> None: 
        with self.assertLogs("Logging", level="INFO") as al: 
            logging.getLogger("Logging").info("First message")
            logging.getLogger("Logging.bar").error("Second message")
        self.assertEqual(al.output,['INFO:Logging:First message', 'ERROR:Logging.bar:Second message'])


if __name__ == '__main__': 
    unittest.main()

# al_instance = AssertLogging("assert_logging")
# al_instance.assert_logging()