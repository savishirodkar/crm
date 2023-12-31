# Generated by Django 4.2.4 on 2023-08-28 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_admin_superadmin_remove_userprofile_isactive_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCare',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.userprofile')),
                ('is_customer_care', models.BooleanField(default=True, verbose_name='Customer Care')),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.userprofile',),
        ),
        migrations.AddField(
            model_name='agent',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
    ]
