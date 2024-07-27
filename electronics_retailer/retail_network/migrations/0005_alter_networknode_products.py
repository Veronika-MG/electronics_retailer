# Generated by Django 5.0.7 on 2024-07-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retail_network", "0004_alter_networknode_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networknode",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="network_nodes",
                to="retail_network.product",
            ),
        ),
    ]
