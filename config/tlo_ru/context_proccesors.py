from .models import *



def products(request):
    return{
        'products':Product.objects.all()
    }