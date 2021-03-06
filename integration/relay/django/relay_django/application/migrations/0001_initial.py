# Generated by Django 2.2.13 on 2020-11-15 11:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='名前は半角英数字、アンスコ4文字〜20文字です。', regex='^[A-Za-z0-9_]{4,20}$')], verbose_name='名前')),
                ('url', models.URLField(help_text='https://tabocom.backlog.com', verbose_name='URL')),
                ('api_key', models.CharField(max_length=100, verbose_name='API_KEY')),
                ('project_id', models.CharField(max_length=10, verbose_name='プロジェクトID')),
                ('issuetype_id', models.CharField(max_length=10, verbose_name='種別ID')),
                ('priority_id', models.CharField(max_length=1, verbose_name='優先度ID')),
            ],
            options={
                'verbose_name': 'Backlog設定',
                'verbose_name_plural': 'Backlog設定一覧',
            },
        ),
        migrations.CreateModel(
            name='Gitlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='名前は半角英数字、アンスコ4文字〜20文字です。', regex='^[A-Za-z0-9_]{4,20}$')], verbose_name='名前')),
                ('url', models.URLField(help_text='http://gitlab.gitlab:8085', verbose_name='URL')),
                ('owner_access_token', models.CharField(blank=True, help_text='For bulk process', max_length=50, null=True, verbose_name="Owner's Access Token")),
                ('report_username', models.CharField(help_text='For report user(Project Maintainer is required)', max_length=50, verbose_name='Username')),
                ('access_token', models.CharField(help_text='For report user', max_length=50, verbose_name='Access Token')),
                ('project_id', models.CharField(help_text="It's a number, not a name.", max_length=5, verbose_name='Project ID')),
                ('vul_labels', models.CharField(help_text='Comma-separated list of label names', max_length=50, verbose_name='Labels(Vul)')),
                ('lib_labels', models.CharField(help_text='Comma-separated list of label names', max_length=50, verbose_name='Labels(Lib)')),
            ],
            options={
                'verbose_name': 'Gitlab設定',
                'verbose_name_plural': 'Gitlab設定一覧',
            },
        ),
        migrations.CreateModel(
            name='GoogleChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='名前は半角英数字、アンスコ4文字〜20文字です。', regex='^[A-Za-z0-9_]{4,20}$')], verbose_name='名前')),
                ('webhook', models.URLField(help_text='https://chat.googleapis.com/v1/spaces/XXXXX/messages?key=YYYYY&token=ZZZZZ', verbose_name='Webhook')),
            ],
            options={
                'verbose_name': 'GoogleChat設定',
                'verbose_name_plural': 'GoogleChat設定一覧',
            },
        ),
        migrations.CreateModel(
            name='GitlabVul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrast_org_id', models.CharField(max_length=36, verbose_name='組織ID')),
                ('contrast_app_id', models.CharField(max_length=36, verbose_name='アプリID')),
                ('contrast_vul_id', models.CharField(blank=True, max_length=19, null=True, verbose_name='脆弱性ID')),
                ('gitlab_issue_id', models.PositiveSmallIntegerField(verbose_name='Issue ID')),
                ('gitlab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vuls', related_query_name='vul', to='application.Gitlab', verbose_name='Gitlab')),
            ],
            options={
                'verbose_name': 'Gitlab脆弱性',
                'verbose_name_plural': 'Gitlab脆弱性一覧',
            },
        ),
        migrations.CreateModel(
            name='GitlabNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='コメント')),
                ('creator', models.CharField(max_length=200, verbose_name='投稿者')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='投稿日時')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('contrast_note_id', models.CharField(max_length=36, unique=True, verbose_name='ContrastNoteID')),
                ('gitlab_note_id', models.PositiveSmallIntegerField(verbose_name='GitlabNoteID')),
                ('vul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', related_query_name='note', to='application.GitlabVul', verbose_name='Gitlab脆弱性')),
            ],
            options={
                'verbose_name': 'Gitlab脆弱性コメント',
                'verbose_name_plural': 'Gitlab脆弱性コメント一覧',
            },
        ),
        migrations.CreateModel(
            name='GitlabLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrast_org_id', models.CharField(max_length=36, verbose_name='組織ID')),
                ('contrast_app_id', models.CharField(max_length=36, verbose_name='アプリID')),
                ('contrast_lib_lg', models.CharField(blank=True, max_length=20, null=True, verbose_name='ライブラリ言語')),
                ('contrast_lib_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='ライブラリID')),
                ('gitlab_issue_id', models.PositiveSmallIntegerField(verbose_name='Issue ID')),
                ('gitlab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='libs', related_query_name='lib', to='application.Gitlab', verbose_name='Gitlab')),
            ],
            options={
                'verbose_name': 'Gitlabライブラリ',
                'verbose_name_plural': 'Gitlabライブラリ一覧',
            },
        ),
    ]
