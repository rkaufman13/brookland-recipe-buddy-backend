import datetime


def generate_and_encode_template(recipe, sender):
    today = datetime.date.today().strftime('%Y-%m-%d')
    short_title = "-".join(recipe.get('title').lower().split(" ")[:3])
    with open('recipe-template.markdown','r') as template:
        with open(f'{today}-{short_title}.md', 'r+') as output:
            buffer = template.readlines()




