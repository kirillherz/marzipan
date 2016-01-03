from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import CakeModel
from django.shortcuts import render

def listing_cakes(request):
	cakes_list = CakeModel.objects.all()
	paginator = Paginator(cakes_list,1)
	page = request.GET.get('page')
	try:
		cakes = paginator.page(page);
	except PageNotAnInteger:
		cakes = paginator.page(1)
	except EmptyPage:
		cakes = paginator.page(paginator.num_pages)
	return render(request,'list_cakes.html',{'cakes':cakes})
