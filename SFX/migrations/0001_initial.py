# Generated by Django 3.2.6 on 2021-09-20 11:20

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EHub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergySfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Energy/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers .Only .mp3 is accepted', null=True, upload_to='SFX/Energy/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentalSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Environment/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Environment/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='FightingSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Fighting/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers .Only .mp3 is  accepted', null=True, upload_to='SFX/Fighting/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='FireSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Fire/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Fire/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='LightiningSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Lightining/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Lightining/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MachinerySfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Machinery/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers. Only .mp3 is  accepted', null=True, upload_to='SFX/Machinery/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponsSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Set the price to 0 if the product type is free.', max_digits=6, max_length=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('paidproduct', models.FileField(blank=True, help_text='Provide a WatermarkProduct.This product is just a showcase to Customers.Only .mp3 is  accepted', null=True, upload_to='SFX/Weapons/free/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('freeproduct', models.FileField(blank=True, help_text='Provide a Watermark free Product to distribute to Customers .Only .mp3 is  accepted', null=True, upload_to='SFX/Weapons/paid/%y', validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('date_published', models.DateField(auto_now_add=True, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderWeaponsSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.weaponssfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMachinerySfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.machinerysfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLightiningSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.lightiningsfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFireSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.firesfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFightingSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.fightingsfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderEnvironmentalSfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.environmentalsfx')),
            ],
        ),
        migrations.CreateModel(
            name='OrderEnergySfx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('published_by', models.CharField(max_length=20, null=True)),
                ('addtoDpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.purchasedproducts')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EHub.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EHub.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SFX.energysfx')),
            ],
        ),
    ]