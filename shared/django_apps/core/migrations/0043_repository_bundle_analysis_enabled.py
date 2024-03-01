# Generated by Django 4.2.7 on 2024-01-09 21:10

from django.db import migrations, models

from shared.django_apps.migration_utils import RiskyAddField


class Migration(migrations.Migration):
    """
    BEGIN;
    --
    -- Add field bundle_analysis_enabled to repository
    --
    ALTER TABLE "repos" ADD COLUMN "bundle_analysis_enabled" boolean DEFAULT false NOT NULL;
    ALTER TABLE "repos" ALTER COLUMN "bundle_analysis_enabled" DROP DEFAULT;
    COMMIT;
    """

    dependencies = [
        ("core", "0042_repository_languages"),
    ]

    operations = [
        RiskyAddField(
            model_name="repository",
            name="bundle_analysis_enabled",
            field=models.BooleanField(default=False),
        ),
    ]
