from django.shortcuts import render
from productapp.models import Product
from django.views.generic import ListView

# Create your views here.
class SearchProductView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q' , None)
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
        '''
        __icontains = field contains this
        __iextact = field is exactly this
        '''
