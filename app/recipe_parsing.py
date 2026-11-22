from recipe_scrapers import scrape_me
from recipe_scrapers._exceptions import SchemaOrgException


def parse_recipe(url):
    try:
        scraper = scrape_me(url)
        recipe = {
            "title": scraper.title(),
            "instructions": scraper.instructions(),
            "ingredients": scraper.ingredients(),
            "description": scraper.description(),
            "site_name": scraper.site_name(),
            "canonical_url": scraper.canonical_url(),
            "servings": scraper.yields()
        }
        try:
            recipe['cook_time']=scraper.cook_time()
        except SchemaOrgException:
            pass
        try:
            recipe['prep_time']=scraper.prep_time()
        except SchemaOrgException:
            pass
        try:
            recipe['total_time']=scraper.total_time()
        except SchemaOrgException:
            pass
        return recipe

    except Exception as ex:
        print(f"No recipe found at {url}")
        print(ex)
        return None

if __name__ == '__main__':
    parse_recipe("https://cooking.nytimes.com/recipes/1020453-crisp-gnocchi-with-brussels-sprouts-and-brown-butter")