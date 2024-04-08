# Generated by Django 3.2.12 on 2023-01-26 17:52

from django.db import migrations, models

from shared.django_apps.migration_utils import RiskyAddIndex


class Migration(migrations.Migration):
    """
    BEGIN;
    --
    -- Create index all_commits_on_pull on field(s) repository, pullid of model commit
    --
    CREATE INDEX "all_commits_on_pull" ON "commits" ("repoid", "pullid");
    COMMIT;
    """

    dependencies = [
        ("core", "0017_branch_branches_repoid_updatestamp"),
    ]

    operations = [
        RiskyAddIndex(
            model_name="commit",
            index=models.Index(
                fields=["repository", "pullid"], name="all_commits_on_pull"
            ),
        ),
    ]
