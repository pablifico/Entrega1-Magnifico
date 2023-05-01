# Generated by Django 4.2 on 2023-04-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('descripcion', RichTextField()), 
                ('fecha_nacimiento', models.DateField()),
                ('posicion', models.CharField(max_length=20)),
                ('foto_de_identificacion', models.ImageField(upload_to='avatares', null=True, blank=True)),
            ],
        ),

    ]
