# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404
from django.shortcuts import render


# Create your views here.



def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def about(request):
    # response = HttpResponse()
    # heading1 = '<h>' + 'This is an Online Grocery Store ' + '</h>'
    # response.write(heading1)
    return render(request, 'myapp1/about0.html')

def detail(request, type_no):
    type_list = get_list_or_404(Item, type=type_no)
    # response = HttpResponse()
    # heading1 = '<p>' + 'The Type ' + str(type_no) +' : ' + '</p>'
    # response.write(heading1)
    # for type in type_list:
    #     para = '<p>' + str(type) + '</p>'
    #     response.write(para)
    return render(request, 'myapp1/detail0.html', locals())