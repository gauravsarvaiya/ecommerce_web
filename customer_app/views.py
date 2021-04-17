from django.shortcuts import get_object_or_404, redirect, render
from shop_app.models import shop_items
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def demo(request):
    return HttpResponse("hello customer")

class product_list_show(LoginRequiredMixin,ListView):
    model = shop_items
    template_name = 'customer_app/shop_items_list_show.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data( **kwargs)
        context['object_list']=context['object_list'].all()
        return context

def add_to_cart(request, id):
    item = get_object_or_404(shop_items, id=id)
    order_item, created = OrderItem.objects.get_or_create(Product=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs .exists():
        order = order_qs[0] 
        if order.item.filter(Product_id=item.pk).exists():
            order_item.quntity += 1
            order_item.save()
            messages.info(request, "Item Quantity was updated.")
            return redirect('customer_app:product_list_show')
        else:
            messages.info(request, "Item was added to a cart.")
            order.item.add(order_item)
            return redirect('customer_app:product_list_show')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "Item was added to a cart.")
    return redirect('customer_app:product_list_show')

class cart_details(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'customer_app/cart_details.html', context=context)
        except ObjectDoesNotExist:
            return redirect('customer_app:product_list_show')
   


######################################################################################################

def remove_from_cart(request, id):
    item = get_object_or_404(shop_items, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(Product_id=item.pk).exists():
            order_item = OrderItem.objects.filter(Product=item, user=request.user, ordered=False)[0]
            order.item.model.delete(order_item)
            messages.info(request, "Item was removed from cart")
            return redirect("customer_app:product_list_show")
        else:
            messages.info(request, "Item was not in your cart")
            return redirect("customer_app:product_list_show")
    else:
        messages.info(request, "You do not have active order")
        return redirect("customer_app:product_list_show")

def remove_single_item_from_cart(request, id):
    item = get_object_or_404(shop_items, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(Product_id=item.pk).exists():
            order_item = OrderItem.objects.filter(Product=item, user=request.user, ordered=False)[0]
            if order_item.quntity > 1:
                order_item.quntity -= 1
                order_item.save()
                messages.info(request, "Item Quantity Updated")
                return redirect("customer_app:order_summery")
            else:
                order.item.model.delete(order_item)
            messages.info(request, "Item was removed from cart")
            return redirect("customer_app:product_list_show")
        else:
            messages.info(request, "Item was not in your cart")
            return redirect("customer_app:product_list_show")
    else:
        messages.info(request, "You do not have active order")
        return redirect("customer_app:product_list_show")


class OrderSummeryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'customer_app/order_summery.html', context=context)
        except ObjectDoesNotExist:
            return redirect('customer_app:product_list_show')

