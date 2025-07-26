from recipe_scrapers import scrape_me

def parse_recipe(url):
    try:
        scraper = scrape_me(url)
        return {
            "title": scraper.title(),
            "instructions": scraper.instructions_list(),
            "ingredients": scraper.ingredients(),
            "cook_time": scraper.cook_time(),
            "prep_time": scraper.prep_time(),
            "total_time": scraper.total_time(),
            "description": scraper.description(),
            "site_name": scraper.site_name(),
            "canonical_url": scraper.canonical_url(),
            "servings": scraper.yields()
        }

    except Exception as ex:
        print(f"No recipe found at {url}")
        print(ex)
        return None

if __name__ == '__main__':
    parse_recipe("https://www.noracooks.com/best-vegan-lasagna/")