# Generated by Django 5.0.1 on 2024-04-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SurveyQuestions', '0004_delete_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('radio', 'multiple choice'), ('checkbox', 'All That Apply')], default='text', max_length=8),
        ),
    ]
