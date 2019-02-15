# Generated by Django 2.1.5 on 2019-02-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_pessoas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoas',
            name='Produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto'),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='nome',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
