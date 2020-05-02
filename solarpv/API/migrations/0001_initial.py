# Generated by Django 3.0.4 on 2020-05-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateNumber', models.CharField(max_length=120)),
                ('certID', models.CharField(max_length=120)),
                ('userID', models.CharField(max_length=120)),
                ('reportNumber', models.CharField(max_length=120)),
                ('issueDate', models.CharField(max_length=120)),
                ('standardID', models.CharField(max_length=120)),
                ('locationID', models.CharField(max_length=120)),
                ('modelNumber', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientID', models.CharField(max_length=120)),
                ('clientName', models.CharField(max_length=120)),
                ('clientType', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationID', models.CharField(max_length=120)),
                ('address1', models.CharField(max_length=120)),
                ('address2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('postalCode', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('phoneNumber', models.CharField(max_length=120)),
                ('faxNumber', models.CharField(max_length=120)),
                ('clientID', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelNumber', models.CharField(max_length=120)),
                ('sequenceID', models.CharField(max_length=120)),
                ('maxSystemVoltage', models.CharField(max_length=120)),
                ('voc', models.CharField(max_length=120)),
                ('isc', models.CharField(max_length=120)),
                ('vmp', models.CharField(max_length=120)),
                ('imp', models.CharField(max_length=120)),
                ('pmp', models.CharField(max_length=120)),
                ('ff', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelNumber', models.CharField(max_length=120)),
                ('productName', models.CharField(max_length=120)),
                ('cellTechnology', models.CharField(max_length=120)),
                ('cellManufacturer', models.CharField(max_length=120)),
                ('numberOfCells', models.CharField(max_length=120)),
                ('numberOfCellsInSeries', models.CharField(max_length=120)),
                ('numberOfSeriesStrings', models.CharField(max_length=120)),
                ('numberOfDiodes', models.CharField(max_length=120)),
                ('productLength', models.CharField(max_length=120)),
                ('productWidth', models.CharField(max_length=120)),
                ('productWeight', models.CharField(max_length=120)),
                ('superstateType', models.CharField(max_length=120)),
                ('superstateManufacturer', models.CharField(max_length=120)),
                ('substrateType', models.CharField(max_length=120)),
                ('substrateManufacturer', models.CharField(max_length=120)),
                ('frameType', models.CharField(max_length=120)),
                ('frameAdhesive', models.CharField(max_length=120)),
                ('encapsulateType', models.CharField(max_length=120)),
                ('encapsulantManufacturer', models.CharField(max_length=120)),
                ('junctionBoxType', models.CharField(max_length=120)),
                ('junctionBoxManufacturer', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceID', models.CharField(max_length=120)),
                ('serviceName', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('isFIRequired', models.CharField(max_length=120)),
                ('FIfrequency', models.CharField(max_length=120)),
                ('standardID', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequenceID', models.CharField(max_length=120)),
                ('sequenceName', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standardID', models.CharField(max_length=120)),
                ('standardName', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('publishedDate', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=120)),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('middleName', models.CharField(max_length=120)),
                ('jobTitle', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('officePhone', models.CharField(max_length=120)),
                ('cellPhone', models.CharField(max_length=120)),
                ('prefix', models.CharField(max_length=120)),
                ('clientID', models.CharField(max_length=120)),
            ],
        ),
    ]
