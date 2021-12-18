# Generated by Django 4.0 on 2021-12-18 08:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('is_answered', models.BooleanField()),
                ('lower', models.IntegerField()),
                ('upper', models.IntegerField()),
                ('next_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_ques', to='survey.question')),
            ],
            managers=[
                ('available', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_question', to='survey.question')),
            ],
        ),
    ]
