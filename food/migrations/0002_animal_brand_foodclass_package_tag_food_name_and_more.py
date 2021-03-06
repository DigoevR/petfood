# Generated by Django 4.0 on 2021-12-26 11:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='FoodClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mass', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='name',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.CreateModel(
            name='FoodPackage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.package')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.animal'),
        ),
        migrations.AddField(
            model_name='food',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.brand'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.foodclass', verbose_name='class of food'),
        ),
        migrations.AddField(
            model_name='food',
            name='packages',
            field=models.ManyToManyField(through='food.FoodPackage', to='food.Package', verbose_name='available packages'),
        ),
        migrations.AddField(
            model_name='food',
            name='tags',
            field=models.ManyToManyField(null=True, to='food.Tag'),
        ),
    ]
