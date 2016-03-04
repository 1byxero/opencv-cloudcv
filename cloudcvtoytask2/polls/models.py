from __future__ import unicode_literals

from django.db import models


class Document(models.Model):		
    docfile = models.FileField(upload_to='documents')
    greyscale = models.BooleanField(default=False)
    smoothen = models.BooleanField(default=False)
    binarythreshold = models.BooleanField(default=False)
    resize = models.BooleanField(default=False)
    histogram = models.BooleanField(default=False)
    edgedetection = models.BooleanField(default=False)	
    sobelfilter = models.BooleanField(default=False)	
    foregroundextract = models.BooleanField(default=False)	
    def __unicode__(self):
		return str(self.docfile)

# Create your models here.
