from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=400, null=True)),
                ('address', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Ads',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]