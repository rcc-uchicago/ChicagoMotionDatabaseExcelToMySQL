import datetime
from peewee import MySQLDatabase, Model, CharField, FloatField, IntegerField, DateTimeField, BooleanField

from test_multiple_files import parse_videoclips

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('db_CMD', user='root', password='')


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = mysql_db


class VideoClips(BaseModel):
    name = CharField(max_length=25, unique=True)
    folder = CharField(max_length=25)
    frameRate = IntegerField(default=0)
    nFrames = IntegerField(default=0)
    timeStamp = BooleanField(default=False)
    nErrors = IntegerField(default=0)
    aperture = CharField(max_length=25, null=True)
    binning = CharField(max_length=15)
    color = BooleanField(default=False)
    distance = FloatField(null=True)
    exposure = CharField(max_length=25, null=True)
    date = DateTimeField(null=True)
    description = CharField(max_length=1000)


VideoClips.create_table()

videoclips_rows = parse_videoclips()

for videoclip_row in videoclips_rows:
    videoclip = VideoClips(name=videoclip_row[0],
                           folder=videoclip_row[1],
                           frameRate=videoclip_row[2],
                           nFrames=videoclip_row[3],
                           timeStamp=videoclip_row[4],
                           nErrors=videoclip_row[5],
                           aperture=videoclip_row[6],
                           binning=videoclip_row[7],
                           color=videoclip_row[8],
                           distance=videoclip_row[9],
                           exposure=videoclip_row[10],
                           date=videoclip_row[11],
                           description=videoclip_row[12])
    videoclip.save()

for videoclip in VideoClips.filter(name="bees5-1"):
    print(videoclip.name)
