# Generated by Django 4.2.5 on 2023-09-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_productprice_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productcategory",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
