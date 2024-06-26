# Generated by Django 5.0.2 on 2024-03-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_requirementlevel_framework_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complianceassessment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("planned", "Planned"),
                    ("in_progress", "In progress"),
                    ("in_review", "In review"),
                    ("done", "Done"),
                    ("deprecated", "Deprecated"),
                ],
                default="planned",
                max_length=100,
                null=True,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="riskassessment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("planned", "Planned"),
                    ("in_progress", "In progress"),
                    ("in_review", "In review"),
                    ("done", "Done"),
                    ("deprecated", "Deprecated"),
                ],
                default="planned",
                max_length=100,
                null=True,
                verbose_name="Status",
            ),
        ),
    ]
