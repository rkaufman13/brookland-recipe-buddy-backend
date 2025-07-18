import unittest
from parameterized import parameterized
from validators import contains_url

class TestUrlMatching(unittest.TestCase):
    @parameterized.expand([('https://www.google.com','https://www.google.com'),('Here is the recipe I used. https://paleogrubs.com/sausage-and-cauliflower-casserole-recipe. I hope you like it','https://paleogrubs.com/sausage-and-cauliflower-casserole-recipe')])
    def test_valid_urls_extracted(self, string, expected):
        result = contains_url(string)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
