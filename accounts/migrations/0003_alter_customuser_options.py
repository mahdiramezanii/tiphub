# Generated by Django 4.1 on 2022-08-22 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_teacher_about_alter_teacher_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name": "کاربر", "verbose_name_plural": "کاربران"},
        ),
    ]
