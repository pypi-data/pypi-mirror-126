# Generated by Django 2.2.12 on 2020-05-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nesteditem", "0002_auto_20200417_1237"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nesteditem",
            name="variant",
            field=models.CharField(
                choices=[("list", "List"), ("accordion", "Accordion")],
                default="list",
                help_text="Form factor variant",
                max_length=50,
                verbose_name="Variant",
            ),
        ),
    ]
