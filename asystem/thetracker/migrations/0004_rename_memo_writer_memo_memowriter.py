# Generated by Django 4.0.5 on 2022-07-15 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thetracker', '0003_memowriter_memo_memo_writer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='memo_writer',
            new_name='memowriter',
        ),
    ]