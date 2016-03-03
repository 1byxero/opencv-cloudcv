from django.shortcuts import render
from django.http import HttpResponse
from forms import DocumentForm

# Create your views here.

def index(request):
	if request.method=="POST":
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
	else:
		form = DocumentForm()
		return render(request,'polls/index.html',{"form":form})
