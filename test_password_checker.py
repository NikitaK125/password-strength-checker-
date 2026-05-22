import unittest
from password_checker import (
    check_length, check_uppercase, check_lowercase,
    check_digits, check_special_chars, check_common_passwords,
    evaluate_password
)

class TestPasswordChecker(unittest.TestCase):

    # Length tests
    def test_short_password(self):
        score, msg = check_length("abc")
        self.assertEqual(score, 0)

    def test_minimum_length(self):
        score, msg = check_length("abcdefgh")
        self.assertEqual(score, 1)

    def test_great_length(self):
        score, msg = check_length("abcdefghijklmnop")
        self.assertEqual(score, 3)

    # Uppercase tests
    def test_has_uppercase(self):
        score, _ = check_uppercase("Hello")
        self.assertEqual(score, 1)

    def test_no_uppercase(self):
        score, _ = check_uppercase("hello")
        self.assertEqual(score, 0)

    # Lowercase tests
    def test_has_lowercase(self):
        score, _ = check_lowercase("Hello")
        self.assertEqual(score, 1)

    def test_no_lowercase(self):
        score, _ = check_lowercase("HELLO")
        self.assertEqual(score, 0)

    # Digit tests
    def test_multiple_digits(self):
        score, _ = check_digits("abc123")
        self.assertEqual(score, 2)

    def test_one_digit(self):
        score, _ = check_digits("abc1")
        self.assertEqual(score, 1)

    def test_no_digits(self):
        score, _ = check_digits("abcdef")
        self.assertEqual(score, 0)

    # Special character tests
    def test_special_chars(self):
        score, _ = check_special_chars("abc@#")
        self.assertEqual(score, 2)

    # Common password test
    def test_common_password(self):
        score, msg = check_common_passwords("password")
        self.assertEqual(score, -3)

    def test_not_common_password(self):
        score, _ = check_common_passwords("Tr0ub4dor&3")
        self.assertEqual(score, 0)

    # Full evaluation tests
    def test_very_weak_password(self):
        result = evaluate_password("abc")
        self.assertIn(result["strength"], ["VERY WEAK", "WEAK"])

    def test_strong_password(self):
        result = evaluate_password("MyP@ssw0rd#2024!")
        self.assertIn(result["strength"], ["STRONG", "VERY STRONG"])

    def test_result_has_required_keys(self):
        result = evaluate_password("TestPass1!")
        self.assertIn("score", result)
        self.assertIn("strength", result)
        self.assertIn("feedback", result)
        self.assertIn("bar", result)


if __name__ == "__main__":
    unittest.main()
