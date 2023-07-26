# Generated by Django 4.2.3 on 2023-07-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "date_of_death",
                    models.DateField(blank=True, null=True, verbose_name="Died"),
                ),
            ],
            options={
                "ordering": ["first_name", "last_name"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter a book genre (e.g. Science Fiction)",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter the language the book is written in (e.g. Farsi, English, Swahili)",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "summary",
                    models.CharField(
                        help_text="Enter a brief description of the book",
                        max_length=500,
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                        max_length=13,
                        unique=True,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="catalog.author",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        help_text="Select a genre for this book", to="catalog.genre"
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.language",
                    ),
                ),
            ],
        ),
    ]
