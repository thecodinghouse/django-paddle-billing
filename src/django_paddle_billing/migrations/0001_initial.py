# Generated by Django 5.1.2 on 2024-10-29 13:25

import django.db.models.deletion
import django_paddle_billing.encoders
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived')], max_length=10)),
                ('quotas', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('description', models.TextField(blank=True)),
                ('default', models.BooleanField(db_index=True, default=False)),
                ('available', models.BooleanField(db_index=True, default=False)),
                ('visible', models.BooleanField(db_index=True, default=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='django_paddle_billing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('country_code', models.CharField(max_length=2)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='django_paddle_billing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='django_paddle_billing.product')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('next_billed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled'), ('past_due', 'Past Due'), ('paused', 'Paused'), ('trialing', 'Trialing')], max_length=10)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='billing.account')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='django_paddle_billing.address')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='django_paddle_billing.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='django_paddle_billing.customer')),
                ('products', models.ManyToManyField(related_name='subscriptions', to='django_paddle_billing.product')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occurred_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='django_paddle_billing.customer')),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='django_paddle_billing.subscription')),
            ],
        ),
    ]
