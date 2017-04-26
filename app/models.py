import os
import datetime
from mongoengine import connect, Document, StringField, DateTimeField

# get the mlab URI from environment variables
uri = os.getenv('MLAB_URI')
# connect to our database at MLAB
connect(host=uri)

class Notebook(Document):
    '''
    This collection defines how our notes document will look
    '''
    title = StringField(max_length=100, required=True) # Title of the note
    notes = StringField(max_length=100, required=True) # Details of the note
    date_modified = DateTimeField(default=datetime.datetime.now) # Time note was created
