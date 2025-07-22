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
    ingredients_as_bullets = " - " + "\n - ".join(recipe.get("ingredients"))
    with (open('recipe-template.markdown','r') as template):
        buffer = template.read()
        buffer = buffer.replace(RECIPE_TITLE,recipe.get("title")).replace(RECIPE_SOURCE,recipe.get("site_name")).replace(RECIPE_URL,recipe.get("canonical_url")).replace(COOK_TIME,str(recipe.get("cook_time"))).replace(PREP_TIME,str(recipe.get("prep_time"))).replace(TOTAL_TIME,str(recipe.get("total_time"))).replace(RECIPE_SUBMITTER,sender).replace(RECIPE_SERVINGS,str(recipe.get("servings"))).replace(RECIPE_DESCRIPTION,recipe.get("description")).replace(INSTRUCTIONS,recipe.get("instructions")).replace(INGREDIENTS,ingredients_as_bullets)

        return buffer, filename
