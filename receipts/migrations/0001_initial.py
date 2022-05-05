# Generated by Django 4.0.3 on 2022-05-05 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=200)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=3, max_digits=10)),
                ('date', models.DateField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='receipts.accounts')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='receipts.categories')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
