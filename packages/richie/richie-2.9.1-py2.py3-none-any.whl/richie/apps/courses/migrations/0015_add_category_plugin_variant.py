# Generated by Django 2.2.11 on 2020-03-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0014_auto_20200309_2343"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorypluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("glimpse", "Default"),
                    ("badge", "badge"),
                    ("tag", "Tag"),
                ],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
    ]
