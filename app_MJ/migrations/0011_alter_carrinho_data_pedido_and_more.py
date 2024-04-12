# Generated by Django 4.2.11 on 2024-04-12 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app_MJ", "0010_total_pagamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrinho",
            name="data_pedido",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="carrinhoproduto",
            name="data_pedido",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="data_cadastro",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="produto",
            name="data_produto",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
