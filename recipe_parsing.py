from recipe_scrapers import scrape_me

def parse_recipe(url):
    try:
        scraper = scrape_me(url)
        return {
            "title": scraper.title(),
            "instructions": scraper.instructions(),
            "ingredients": scraper.ingredients(),
            "cook_time": scraper.cook_time(),
            "prep_time": scraper.prep_time(),
            "total_time": scraper.total_time(),
            "description": scraper.description(),
            "site_name": scraper.site_name(),
            "canonical_url": scraper.canonical_url()
        }

    except: #YOU'RE a too broad exception clause
        print(f"No recipe found at {url}")
        return None

if __name__ == '__main__':
    parse_recipe("https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")