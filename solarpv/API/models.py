from django.db import models

class User(models.Model):
    userID  = models.CharField(unique=True, max_length=120)
    firstName = models.CharField( max_length=120)
    lastName = models.CharField( max_length=120)
    middleName = models.CharField( max_length=120)
    jobTitle = models.CharField( max_length=120)
    email = models.CharField( max_length=120)
    officePhone  = models.CharField( max_length=120)
    cellPhone  = models.CharField( max_length=120)
    prefix  = models.CharField( max_length=120)
    clientID  = models.CharField( max_length=120)

    def __str__(self):
        return self.firstName
class Location(models.Model):
    LocationID  = models.CharField( max_length=120)
    address1 = models.CharField( max_length=120)
    address2 = models.CharField( max_length=120)
    city = models.CharField( max_length=120)
    state = models.CharField( max_length=120)
    postalCode = models.CharField( max_length=120)
    country = models.CharField( max_length=120)
    phoneNumber = models.CharField( max_length=120)
    faxNumber = models.CharField( max_length=120)
    clientID = models.CharField( max_length=120)
    def __str__(self):
        return "Location"
class Client(models.Model):
    clientID = models.CharField( max_length=120)
    clientName = models.CharField( max_length=120)
    clientType = models.CharField( max_length=120)
    def __str__(self):
        return "Client"
class Certificate(models.Model):
    certificateNumber = models.CharField( max_length=120)
    certID = models.CharField( max_length=120)
    userID = models.CharField( max_length=120)
    reportNumber = models.CharField( max_length=120)
    issueDate = models.CharField( max_length=120)
    standardID = models.CharField( max_length=120)
    locationID = models.CharField( max_length=120)
    modelNumber = models.CharField( max_length=120)
    def __str__(self):
        return "Certificate"
class Product(models.Model):
    modelNumber = models.CharField( max_length=120)
    productName = models.CharField( max_length=120)
    cellTechnology = models.CharField( max_length=120)
    cellManufacturer = models.CharField( max_length=120)
    numberOfCells = models.CharField( max_length=120)
    numberOfCellsInSeries = models.CharField( max_length=120)
    numberOfSeriesStrings = models.CharField( max_length=120)
    numberOfDiodes = models.CharField( max_length=120)
    productLength = models.CharField( max_length=120)
    productWidth = models.CharField( max_length=120)
    productWeight = models.CharField( max_length=120)
    superstateType = models.CharField( max_length=120)
    superstateManufacturer = models.CharField( max_length=120)
    substrateType = models.CharField( max_length=120)
    substrateManufacturer = models.CharField( max_length=120)
    frameType = models.CharField( max_length=120)
    frameAdhesive = models.CharField( max_length=120)
    encapsulateType = models.CharField( max_length=120)
    encapsulantManufacturer = models.CharField( max_length=120)
    junctionBoxType = models.CharField( max_length=120)
    junctionBoxManufacturer = models.CharField( max_length=120)
    def __str__(self):
        return "Product"
class TestStandard(models.Model):
    standardID = models.CharField( max_length=120)
    standardName = models.CharField( max_length=120)
    description = models.CharField( max_length=120)
    publishedDate = models.CharField( max_length=120)
    def __str__(self):
        return "TestStandard"
class PerformanceData(models.Model):
    modelNumber = models.CharField( max_length=120)
    sequenceID = models.CharField( max_length=120)
    maxSystemVoltage = models.CharField( max_length=120)
    voc = models.CharField( max_length=120)
    isc = models.CharField( max_length=120)
    vmp = models.CharField( max_length=120)
    imp = models.CharField( max_length=120)
    pmp = models.CharField( max_length=120)
    ff = models.CharField( max_length=120)
    def __str__(self):
        return "PerformanceData"
class Service(models.Model):
    serviceID = models.CharField( max_length=120)
    serviceName = models.CharField( max_length=120)
    description = models.CharField( max_length=120)
    isFIRequired = models.CharField( max_length=120)
    FIfrequency = models.CharField( max_length=120)
    standardID = models.CharField( max_length=120)
    def __str__(self):
        return "Service"
class TestSequence(models.Model):
    sequenceID = models.CharField( max_length=120)
    sequenceName = models.CharField( max_length=120)
    def __str__(self):
        return "TestSequence"
