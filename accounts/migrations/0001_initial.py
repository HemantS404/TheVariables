# Generated by Django 4.1.7 on 2023-03-09 17:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('First_name', models.CharField(help_text='Enter your First name', max_length=20)),
                ('Last_name', models.CharField(help_text='Enter your Last name', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter your Date of Birth', null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Enter your Phone Number', max_length=128, null=True, region=None)),
                ('email', models.EmailField(help_text='Enter your Email', max_length=255, unique=True, verbose_name='email address')),
                ('profile_pic', models.ImageField(blank=True, help_text='Upload your Profile Photo', null=True, upload_to='Profile-Pic/', verbose_name='Profile Photo')),
                ('email_token', models.CharField(blank=True, max_length=250, null=True)),
                ('password_reset_token', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]