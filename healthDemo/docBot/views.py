from django.shortcuts import render
from .models import File,FileForm

from docBot import nlp


# Create your views here.
def index(request):
    form = FileForm()
    return render(request,'docBot/index.html',{'form':form})

def result(request):
	if request.method == "POST":
		form = FileForm(request.POST)
		if form.is_valid():
			gender = form.cleaned_data["gender"]
			year = form.cleaned_data["yearOfBirth"]
			symptoms = form.cleaned_data["symptom"]
			result = nlp.run(symptoms,year,gender)
	else:
		result = FileForm()
	return render(request, 'docBot/result.html', {'result': result})

