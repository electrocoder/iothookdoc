# Generated by Django 4.2.2 on 2023-06-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('devices', '0006_device_field_4_device_field_5_device_field_6_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='field_2',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='2. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_3',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='3. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_4',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='4. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_5',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='5. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_6',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='6. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_7',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='7. Alan Adı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='field_8',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='8. Alan Adı'),
        ),
    ]
