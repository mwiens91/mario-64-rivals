from django.db import migrations

COURSE_DICTIONARY = {
    1: "Bob-omb Battlefield",
    2: "Whomp's Fortress",
    3: "Jolly Roger Bay",
    4: "Cool, Cool Mountain",
    5: "Big Boo's Haunt",
    6: "Hazy Maze Cave",
    7: "Lethal Lava Land",
    8: "Shifting Sand Land",
    9: "Dire, Dire Docks",
    10: "Snowman's Land",
    11: "Wet-Dry World",
    12: "Tall, Tall Mountain",
    13: "Tiny, Huge Island",
    14: "Tick Tock Clock",
    15: "Rainbow Ride",
    # 16: "Bowser in the Dark World",
    # 17: "Bowser in the Fire Sea",
    # 18: "Bowser in the Sky",
}

def setup_courses(apps, schema_editor):
    Course = apps.get_model('leaderboards', 'Course')

    for course_number, course_name in COURSE_DICTIONARY.items():
        Course.objects.create(
            name=course_name,
            course_number= course_number)


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(setup_courses),
    ]
