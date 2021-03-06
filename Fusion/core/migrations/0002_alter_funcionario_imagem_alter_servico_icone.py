# Generated by Django 4.0.1 on 2022-01-20 19:18

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-cog', 'Engenagem'), ('lni-mobile', 'Mobile'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuário'), ('lni-layers', 'Design')], max_length=12, verbose_name='Icone'),
        ),
    ]
