# Generated by Django 5.0.7 on 2024-07-26 16:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("retail_network", "0009_alter_networknode_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="networknode",
            options={
                "verbose_name": "Торговый узел",
                "verbose_name_plural": "Торговые Узлы",
            },
        ),
    ]