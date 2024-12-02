from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('status', models.CharField(max_length=10, choices=[('created', 'Created'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='created')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
