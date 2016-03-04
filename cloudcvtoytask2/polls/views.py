from django.http import HttpResponse
from django.shortcuts import render,redirect
from forms import DocumentForm
from models import Document
from os import path
from django.conf import settings
from opencvstuff import *
#foregroundextraction,imagegradient,smoothing





# Create your views here.

def index(request):
	if request.method=="POST":
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()			
			ggwp = process(request,newdoc.docfile.name)			
			return ggwp
		else:
			return HttpResponse("Error brah")		
	else:
		form = DocumentForm()
		documents = Document.objects.all()				
		return render(request,'polls/index.html',{"form":form})


def process(request,name=None):
	if name==None:
		return redirect(index)
	else:
		filepath = path.join(settings.MEDIA_ROOT,name)		
		if path.isfile(filepath):
			smoothing(filepath)
			return HttpResponse("True")
		else:
			return HttpResponse("Some Error Error Occured")

