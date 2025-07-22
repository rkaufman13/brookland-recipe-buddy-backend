import datetime
RECIPE_TITLE = "{{title}}"
RECIPE_SOURCE = "{{source_site}}"
RECIPE_URL = "{{canonical_url}}"
PREP_TIME = "{{prep_time}}"
COOK_TIME = "{{cook_time}}"
TOTAL_TIME = "{{total_time}}"
RECIPE_SUBMITTER = "{{submitter_name}}"
RECIPE_SERVINGS = "{{servings}}"
RECIPE_DESCRIPTION = "{{description}}"
INGREDIENTS = "{{ingredients}}"
INSTRUCTIONS = "{{instructions}}"

def generate_and_encode_template(recipe, sender):
    today = datetime.date.today().strftime('%Y-%m-%d')
    short_title = "-".join(recipe.get('title').lower().split(" ")[:3])
    filename = f'{today}-{short_title}.md'
    with (open('recipe-template.markdown','r') as template):
        buffer = template.read()
        buffer = buffer.replace(RECIPE_TITLE,recipe.get("title")).replace(RECIPE_SOURCE,recipe.get("site_name")).replace(RECIPE_URL,recipe.get("canonical_url")).replace(COOK_TIME,recipe.get("cook_time")).replace(PREP_TIME,recipe.get("prep_time")).replace(TOTAL_TIME,recipe.get("total_time")).replace(RECIPE_SUBMITTER,sender).replace(RECIPE_SERVINGS,recipe.get("servings")).replace(RECIPE_DESCRIPTION,recipe.get("description")).replace(INSTRUCTIONS,recipe.get("instructions")).replace(INGREDIENTS,recipe.get("ingredients"))

        return buffer, filename
