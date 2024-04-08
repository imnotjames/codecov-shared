# Generated by Django 4.2.2 on 2023-08-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0032_auto_20230731_1641"),
    ]

    # BEGIN;
    # --
    # -- Alter field flare on pull
    # --
    # -- (no-op)
    # --
    # -- Rename field flare on pull to _flare
    # --
    # -- (no-op)
    # --
    # -- Add field _flare_storage_path to pull
    # --
    # ALTER TABLE "pulls" ADD COLUMN "flare_storage_path" varchar(200) NULL;
    # COMMIT;

    operations = [
        migrations.AlterField(
            model_name="pull",
            name="flare",
            field=models.JSONField(db_column="flare", null=True),
        ),
        migrations.RenameField(
            model_name="pull",
            old_name="flare",
            new_name="_flare",
        ),
        migrations.AddField(
            model_name="pull",
            name="_flare_storage_path",
            field=models.URLField(db_column="flare_storage_path", null=True),
        ),
    ]
