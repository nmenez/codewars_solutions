def validate_pin(PIN):
    print(len(PIN))
    if len(PIN) not in (4, 6):
        return False

    for let in PIN:
        if let not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return False
    else:
        return True

import unittest


class TestValidatePIN(unittest.TestCase):
    def test_1(self):
        self.assertTrue(validate_pin("1234"))
        self.assertFalse(validate_pin("12345"))
        self.assertFalse(validate_pin('a234'))

if __name__ == "__main__":
    unittest.main()
   # print(validate_pin("12345"))