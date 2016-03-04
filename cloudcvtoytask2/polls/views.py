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
			greyscale = form.cleaned_data['greyscale']
			smoothen = form.cleaned_data['smoothen']
			binarythreshold = form.cleaned_data['binarythreshold']
			resize = form.cleaned_data['resize']
			histogram = form.cleaned_data['histogram']
			edgedetection = form.cleaned_data['edgedetection']			
			stufftodo=[]
			if(greyscale==True):
				stufftodo.append("greyscale")
			if(smoothen==True):
				stufftodo.append("smoothen")
			if(greyscale==True):
				stufftodo.append("greyscale")
			if(binarythreshold==True):
				stufftodo.append("binarythreshold")
			if(resize==True):
				stufftodo.append("resize")
			if(histogram==True):
				stufftodo.append("histogram")
			if(edgedetection==True):
				stufftodo.append("edgedetection")				
			ggwp = process(request,newdoc.docfile.name,stufftodo)			
			return ggwp
		else:
			return HttpResponse("Error brah")		
	else:
		form = DocumentForm()
		documents = Document.objects.all()				
		return render(request,'polls/index.html',{"form":form})


def process(request,name=None,stufftodo=[]):	
	if name==None or len(stufftodo)==0:
		return redirect(index)
	else:
		filepath = path.join(settings.MEDIA_ROOT,name)		
		if path.isfile(filepath):			
			sobelfilter(filepath)
			return HttpResponse("True")
		else:
			return HttpResponse("Some Error Error Occured")

