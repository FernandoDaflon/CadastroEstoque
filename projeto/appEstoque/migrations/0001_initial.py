# Generated by Django 3.0 on 2019-12-03 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appEstoque.Categoria')),
            ],
        ),
    ]
