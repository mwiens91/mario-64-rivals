from django.db import migrations

CATEGORY_DICTIONARY = {
    "70 Star" : {
        "description": "70 star race! Start the timer when powering the game on; end the timer when Mario touches the big star at the end of the game (with at least 70 stars).",
        "preview_img": "default_category_images/70_star.png"
        },
    "120 Star" : {
        "description": "120 star race! Start the timer when powering the game on; end the timer when Mario touches the big star at the end of the game (with all 120 stars).",
        "preview_img": "default_category_images/120_star.png"
        },
}

def setup_categories(apps, schema_editor):
    Category = apps.get_model('leaderboards', 'Category')

    for category_name, category_dict in CATEGORY_DICTIONARY.items():
        Category.objects.create(
            name=category_name,
            description=category_dict["description"],
            preview_image=category_dict["preview_img"])


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0012_category_preview_image'),
    ]

    operations = [
        migrations.RunPython(setup_categories),
    ]
