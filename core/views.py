from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import newspaper
# Create your views here.

@login_required
def home(request):
	cnn_paper = newspaper.build('http://cnn.com')
	sina_paper = newspaper.build('http://www.lemonde.fr/', language='fr')
	size = cnn_paper.size()
	context = {
		'cnn': cnn_paper,
		'sina': sina_paper,
		'size': size,
	}
	
	return render(request, 'home.html', context)

# def away(request):
# 	return HttpResponse('HAI')
