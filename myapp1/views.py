# Import necessary classes
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from .forms import OrderItemForm, InterestForm

# Create your views here.



def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


# def about(request):
#     # response = HttpResponse()
#     # heading1 = '<h>' + 'This is an Online Grocery Store ' + '</h>'
#     # response.write(heading1)
#     return render(request, 'myapp1/about0.html')

# def detail(request, type_no):
#     type_list = get_list_or_404(Item, type=type_no)
#     # response = HttpResponse()
#     # heading1 = '<p>' + 'The Type ' + str(type_no) +' : ' + '</p>'
#     # response.write(heading1)
#     # for type in type_list:
#     #     para = '<p>' + str(type) + '</p>'
#     #     response.write(para)
#     return render(request, 'myapp1/details0.html', locals())

def about(request):
    return render(request, 'myapp1/about0.html')

def get_items(request, type_no):
    response = HttpResponse()
    items = get_list_or_404(Item, type=type_no)
    for item in items:
        para = '<p>' + str(item.name) + '</p>'
        response.write(para)
    return response


def detail(request,type_no):
    tp = get_object_or_404(Type, id=type_no)
    items = get_list_or_404(Item, type=type_no)

    return render(request, 'myapp1/details0.html', locals())


def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})


def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_of_items <= order.item.stock:
                order.save()
                msg = 'Your order has been placed successfully.'
                newstock = order.item.stock - order.num_of_items
                Item.objects.filter(name=order.item.name).update(stock=newstock)
            else:
                msg = 'We do not have sufficient stock to fill your order.'
        return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
        return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})

def itemdetail(request, item_id):
    msg = ''
    item = get_object_or_404(Item, id=item_id)
    if request.method =='POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            inter = form.cleaned_data['interested']
            if inter == '1':
                newinterested = item.interested + 1
                Item.objects.filter(id=item_id).update(interested=newinterested)
                msg = 'Thanks for your submit'
        return render(request,'myapp1/order_response.html', {'msg': msg})
    else:
        form = InterestForm()
        return render(request, 'myapp1/itemdetail.html',locals())