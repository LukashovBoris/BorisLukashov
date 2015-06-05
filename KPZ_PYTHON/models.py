from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class MCU_TABLE(models.Model):
    NOTIFICE_NAME = models.CharField(max_length=200)
    STARTTIME =  models.IntegerField()
    OWNERNAME = models.CharField(max_length=200)


class MCU(models.Model):
    ADMIN = models.CharField(max_length=200)
    ID_TABLE = models.ForeignKey('MCU_TABLE',null=True)


class ADMINS(models.Model):
    NAME = models.CharField(max_length=200,unique= True)
    MCU_ID = models.ForeignKey('MCU',null=True)
    PA = models.CharField(max_length=200)
    ADDRESS = models.CharField(max_length=200)
    WORKTIME = models.IntegerField()
    STARTTIME = models.IntegerField()

class NOTIFICE(models.Model):
    NAME = models.CharField(max_length=200)
    STARTTIME = models.IntegerField()
    WORKTIME = models.IntegerField()
    PROCESS_CHECK  = models.ForeignKey('PROCESS',null=True)

class PROCESS(models.Model):
    def __uncicode__ (self):
        return u'%s'  % (self.NAME)

    NAME = models.CharField(max_length=200)
    STARTTIME = models.IntegerField()
    PA = models.CharField(max_length=200)


class INSPECTORS(models.Model):
    CHECKER = models.ForeignKey('NOTIFICE',null=True)
    NAME = models.CharField(max_length=200)
    STARTTIME = models.IntegerField()
    WORKTIME = models.IntegerField()
    PA = models.CharField(max_length=200)

class INSPECT(models.Model):
    MCUU_ID = models.ForeignKey('INSPECTORS',null=True)


def Add():
    try:
        ADMINS.objects.create(NAME = 'Alex',MCU_ID = MCU.objects.create(ADMIN = "Boris",ID_TABLE =
                                                                    MCU_TABLE.objects.create(NOTIFICE_NAME = "1",STARTTIME = '2',OWNERNAME = '3')),
                          PA ="235235TA",ADDRESS = "Lenina 17,12",WORKTIME = 8,STARTTIME = 6);
    except:pass
#Add()
def Del():
    try:
        ADMINS.objects.filter(NAME = 'Alex').delete()
    except:pass
def Upp ():
    try:
        ADMINS.objects.get(NAME = 'Alex').NAME = "Gollo"
    except:pass
Upp()
def GETSOMEVALUE():
    try:
        print(ADMINS.objects.all())
    except:pass
def ADDNOT():
    try:
        NOTIFICE.objects.create(NAME = 'OLEG',STARTTIME = 6, WORKTIME = 3,PROCESS_CHECK = PROCESS.objects.create(NAME = 'OLEG', STARTTIME = 3, PA = 'q2e31231'))
    except:pass
ADDNOT()
