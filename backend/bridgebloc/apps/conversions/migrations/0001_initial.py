# Generated by Django 4.2.4 on 2023-08-31 08:17

import bridgebloc.common.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tokens', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenConversion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'source_chain',
                    bridgebloc.common.fields.EVMChainIDField(
                        choices=[
                            (1, 'Ethereum'),
                            (42161, 'Arbitrum One'),
                            (43114, 'Avalanche'),
                            (137, 'Polygon Pos'),
                            (1101, 'Polygon Zkevm'),
                            (5, 'Ethereum Testnet'),
                            (421613, 'Arbitrum One Testnet'),
                            (43113, 'Avalanche Testnet'),
                            (80001, 'Polygon Pos Testnet'),
                            (1442, 'Polygon Zkevm Testnet'),
                        ],
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name='source chain',
                    ),
                ),
                (
                    'destination_chain',
                    bridgebloc.common.fields.EVMChainIDField(
                        choices=[
                            (1, 'Ethereum'),
                            (42161, 'Arbitrum One'),
                            (43114, 'Avalanche'),
                            (137, 'Polygon Pos'),
                            (1101, 'Polygon Zkevm'),
                            (5, 'Ethereum Testnet'),
                            (421613, 'Arbitrum One Testnet'),
                            (43113, 'Avalanche Testnet'),
                            (80001, 'Polygon Pos Testnet'),
                            (1442, 'Polygon Zkevm Testnet'),
                        ],
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name='destination chain',
                    ),
                ),
                (
                    'conversion_type',
                    models.CharField(
                        choices=[('cctp', 'Cctp'), ('lxly', 'Lxly'), ('circle_api', 'Circle Api')],
                        max_length=150,
                        verbose_name='conversion type',
                    ),
                ),
                (
                    'destination_address',
                    bridgebloc.common.fields.EVMAddressField(max_length=42, verbose_name='destination address'),
                ),
                ('amount', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='amount')),
                (
                    'creator',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='conversions',
                        to='accounts.account',
                        verbose_name='creator',
                    ),
                ),
                (
                    'destination_token',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='destination_circle_api_conversions',
                        to='tokens.token',
                        verbose_name='destination token',
                    ),
                ),
                (
                    'source_token',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='source_circle_api_conversions',
                        to='tokens.token',
                        verbose_name='source token',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenConversionStep',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'step_type',
                    models.CharField(
                        choices=[
                            ('confirm deposit', 'Confirm Deposit'),
                            ('send to recipient', 'Send To Recipient'),
                            ('create deposit address', 'Create Deposit Address'),
                            ('attestation service confirmation', 'Attestation Service Confirmation'),
                            ('send to recipient', 'Send To Recipient'),
                        ],
                        max_length=150,
                        verbose_name='step type',
                    ),
                ),
                ('metadata', models.JSONField(verbose_name='metadata')),
                (
                    'status',
                    models.CharField(
                        choices=[('failed', 'Failed'), ('pending', 'Pending'), ('successful', 'Successful')],
                        max_length=10,
                        verbose_name='status',
                    ),
                ),
                (
                    'conversion',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='conversion_steps',
                        to='conversions.tokenconversion',
                        verbose_name='conversion',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]