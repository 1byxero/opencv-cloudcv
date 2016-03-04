from __future__ import unicode_literals

from django.db import models


class Document(models.Model):	
    docfile = models.FileField(upload_to='documents')

    def __unicode__(self):
		return str(self.docfile)

# Create your models here.
