# Generated by Django 4.2.2 on 2023-06-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('datas', '0003_alter_data_field_2_alter_data_field_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='field_2',
            field=models.CharField(blank=True, default='', help_text='Enter a field name', max_length=30,
                                   verbose_name='2. Alan Degeri'),
        ),
        migrations.AlterField(
            model_name='data',
            name='field_3',
            field=models.CharField(blank=True, default='', help_text='Enter a field name', max_length=30,
                                   verbose_name='3. Alan Degeri'),
        ),
    ]
