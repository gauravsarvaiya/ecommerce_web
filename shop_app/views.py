from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404,HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import shop_items
from ecom_app.models import UserProfile


@login_required
def demo(request):
    return HttpResponse("hello shop_owner")


class shop_info(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = shop_items
    fields = ['product_name','product_price','product_brand','product_image']

    success_url = reverse_lazy('shop_app:product_list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(shop_info,self).form_valid(form)
    
    def test_func(self):
        x = self.request.user
        if x.is_shop:
            return True
        else:
            raise
        Http404('you are not allowed here')

class product_list(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = shop_items
    
    def get_context_data(self,  **kwargs):
        context=super().get_context_data( **kwargs)
        context['object_list']=context['object_list'].filter(user = self.request.user)
        return context
    
    def test_func(self):
        x = self.request.user
        if x.is_shop:
            return True
        else:
            raise
        Http404('you are not allowed here')

class product_update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = shop_items
    fields = ['product_name','product_price','product_brand','product_image']
    success_url = reverse_lazy('shop_app:product_list')

    def test_func(self):
        x = self.request.user
        if x.is_shop:
            return True
        else:
            raise
        Http404('you are not allowed here')



class product_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = shop_items
    context_object_name = 'task'
    success_url = reverse_lazy('shop_app:product_list')

    def test_func(self):
        x = self.request.user
        if x.is_shop:
            return True
        else:
            raise
        Http404('you are not allowed here')

class product_details(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = shop_items
    context_object_name = 'top'

    def test_func(self):
        x = self.request.user
        if x.is_shop:
            return True
        else:
            raise
        Http404('you are not allowed here')

###############################################################







    


