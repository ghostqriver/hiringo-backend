# Generated by Django 3.2.8 on 2021-11-06 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseBasic',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userstudentprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userteacherprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserBasic',
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
        migrations.DeleteModel(
            name='UserPermission',
        ),
        migrations.DeleteModel(
            name='UserStudentProfile',
        ),
        migrations.DeleteModel(
            name='UserTeacherProfile',
        ),
    ]
