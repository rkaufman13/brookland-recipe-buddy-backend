import unittest
from parameterized import parameterized
from templatizer import generate_and_encode_template
import templatizer

templatizer.TEMPLATE_FILE="recipe-template-test.markdown"

class TestRecipeParsing(unittest.TestCase):
    def test_recipe_with_all_fields(self):
        #arrange
        recipe = generate_recipe()
        #act
        template,filename = generate_and_encode_template(recipe,"Me me me")
        #assert
        assert filename.endswith("a-fake-title.md")



def generate_recipe():
    return {
            "title": "a fake title",
            "instructions": ["do this","then do that"],
            "ingredients": ["this thing","that thing"],
            "description": "it tastes good",
            "site_name": "my site",
            "canonical_url": "google.com",
            "servings": 100,
        "cook_time": 5,
        "prep_time":10,
        "total_time":30
        }



if __name__ == '__main__':
    unittest.main()
