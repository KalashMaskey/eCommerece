from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product
from carts.models import Cart
# Create your views here.


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/featured-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug=self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug,active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except:
            raise Http404("Strange")
        return instance

class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/featured-detail.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


# Same Working Mechanism but in Function Based View
# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list' : queryset
#     }
#     return render(request, 'products/list.html', context)

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk=self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('No Product Found')
        pk = self.kwargs.get('pk')
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

# Same Working Mechanism but in Function Based View

# def product_detail_view(request, pk=None, *args, **kwargs):
#     # instance = get.get_object_or_404(Product, pk=pk)
#     # try:
#     #     instance = Product.objects.get(id=pk)
#     # except Product.DoesNotExist:
#     #     print('No Product Found')
#     # except:
#     #     print('?')
#
#     instance = Product.objects.get_by_id(pk)
#     if instance is None:
#         raise Http404('Product doesnot exist')
#     # qs = Product.objects.filter(id=pk)
#     #
#     # if qs.exists() and qs.count() ==1: #len(qs)
#     #     instance = qs.first()
#     # else:
#     #     raise Http404('No Product Found')
#
#     context = {
#         'object': instance
#     }
#     return render(request, 'products/detail.html', context)
