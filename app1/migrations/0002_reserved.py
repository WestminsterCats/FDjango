# Generated by Django 4.2.3 on 2024-04-30 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(null=True)),
                ('audit', models.DateField(null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('itemlocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.itemlocation')),
                ('itemstatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.itemstatus')),
                ('itemtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.itemtype')),
            ],
        ),
    ]