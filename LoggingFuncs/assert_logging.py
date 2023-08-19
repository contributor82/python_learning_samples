"""Module for Assert logging """
# Assert facilitates logging.
import logging
import unittest

class AssertLogging(unittest.TestCase):
    """Assert logging class """

    def test_assert_logging(self) -> None:
        """test assert logging method """
        with self.assertLogs('Logging', level='INFO') as assert_log:
            logging.getLogger('Logging').info('First message')
            logging.getLogger('Logging.bar').error('Second message')
        self.assertEqual(assert_log.output,['INFO:Logging:First message',
                                            'ERROR:Logging.bar:Second message'])

if __name__ == '__main__':
    unittest.main()
# al_instance = AssertLogging("assert_logging')
# al_instance.assert_logging()
