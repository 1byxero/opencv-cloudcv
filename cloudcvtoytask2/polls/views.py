from django.http import HttpResponse
from django.shortcuts import render,redirect
from forms import DocumentForm
from models import Document




# Create your views here.

def index(request):
	if request.method=="POST":
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			return redirect('/', name="index")			
		else:
			return HttpResponse("Error brah")		
	else:
		form = DocumentForm()
		documents = Document.objects.all()				
		return render(request,'polls/index.html',{"form":form,"documents":documents})
