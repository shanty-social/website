# Generated by Django 3.2.11 on 2022-02-07 18:12

import api.models
import authlib.oauth2.rfc6749.models
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SSHKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('key', models.TextField(max_length=2000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OAuth2Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=36)),
                ('token_type', models.CharField(max_length=40)),
                ('access_token', models.CharField(max_length=255, unique=True)),
                ('refresh_token', models.CharField(db_index=True, max_length=255)),
                ('scope', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), null=True, size=None)),
                ('revoked', models.BooleanField(default=False)),
                ('issued_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_in', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.TokenMixin),
        ),
        migrations.CreateModel(
            name='OAuth2Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=36)),
                ('code', models.CharField(max_length=120, unique=True)),
                ('redirect_uri', models.TextField(null=True)),
                ('response_type', models.TextField(null=True)),
                ('scope', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), null=True, size=None)),
                ('auth_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.AuthorizationCodeMixin),
        ),
        migrations.CreateModel(
            name='OAuth2Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('client_secret', models.CharField(default=uuid.uuid4, max_length=36)),
                ('client_name', models.CharField(max_length=120)),
                ('website_uri', models.URLField(max_length=256, null=True)),
                ('description', models.TextField(null=True)),
                ('redirect_uris', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('default_redirect_uri', models.CharField(max_length=256, null=True)),
                ('scope', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), null=True, size=None)),
                ('response_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), null=True, size=None)),
                ('grant_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), default=api.models.grant_types_default, size=None)),
                ('token_endpoint_auth_method', models.CharField(choices=[('client_secret_post', 'client_secret_post'), ('client_secret_basic', 'client_secret_basic')], default='client_secret_post', max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.ClientMixin),
        ),
    ]
