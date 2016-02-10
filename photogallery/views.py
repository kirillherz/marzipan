from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import CakeModel
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
		
def listing_cakes(request):
	cakes_list = CakeModel.objects.all()
	if len(cakes_list) == 0:
		return render(request,'list_cakes.html')
	paginator = Paginator(cakes_list,1)
	page = request.GET.get('page')
	try:
		cakes = paginator.page(page);
	except PageNotAnInteger:
		cakes = paginator.page(1)
	except EmptyPage:
		cakes = paginator.page(paginator.num_pages)
	form = ReviewForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()	
		form = ReviewForm()
	form.set_cake_id(cakes.object_list[0].id)
	return render(request,'list_cakes.html',{'cakes':cakes, 'form' :form})
												 
def post_feedback(request):
	form = FeedbackForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return render(request, 'feedback_thanks.html',{})
	return render(request, 'post_feedback.html', {'form' : form})
