# Generated by Django 3.2.4 on 2021-07-07 12:21

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('language', models.CharField(choices=[('eng', 'English'), ('esp', 'Spanish'), ('fra', 'French'), ('ger', 'German'), ('hin', 'Hindi')], default='eng', max_length=100)),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('scf', 'Sci-fi'), ('rom', 'Romance'), ('hor', 'Horror'), ('fic', 'Fiction'), ('bio', 'Biography'), ('adv', 'Adventure')], max_length=23)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
