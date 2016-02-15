from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import CakeModel
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import ContextMixin

class ListingCakeView(MultipleObjectMixin,TemplateResponseMixin,ContextMixin, View):
    
    paginate_by = 1
    model = CakeModel
    context_object_name = 'cakes_list'
    template_name = 'list_cakes.html'
    
    def post(self,request, context, **kwargs):
       return render_to_response(request, context)
    
    def get_context_data(self, **kwargs):
        context = super(ListingCakeView, self).get_context_data(**kwargs)
        context['number'] = 231
        return context
        
    def get(self, request, *args, **kwargs):
       paginator, page, cakes, is_paginate = self.paginate_queryset(self.model.objects.all() ,1)
       context = {'cakes' : page }
       return self.render_to_response(self.get_context_data(**kwargs), **kwargs)
    
	
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
    form.id_cake = cakes.object_list[0].id
    return render(request,'list_cakes.html',{'cakes':cakes, 'form' :form})

def post_feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'feedback_thanks.html',{})
    return render(request, 'post_feedback.html', {'form' : form})
