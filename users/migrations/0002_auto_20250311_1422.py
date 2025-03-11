from django.db import migrations
from ..models import User


def create_default_user(apps, schema_editor):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            name='Gamma Gemini',
            password='adminpassword'
        )


def remove_default_user(apps, schema_editor):
    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_user, remove_default_user),
    ]
