from django.shortcuts import render

from .models import USER, DATA


# Create your views here.

def Index(request):
    return render(request, 'login.html')


def loginview(request):
    if request.POST['role'] == 'customer':
        email = request.POST['email']
        password = request.POST['password']
        logger = USER.objects.get(email=email)
        if logger:
            if logger.password == password and logger.role == 'customer':
                return render(request, 'profile.html')
        else:
            message = 'Password does not match...'
            return render(request, 'login.html', {'msg': message})
    else:
        if request.POST['role'] == 'admin':
            email = request.POST['email']
            password = request.POST['password']
            logger = USER.objects.get(email=email)
            if logger:
                if logger.password == password and logger.role == 'admin':
                    customer1=DATA.objects.get(id=1)
                    customer2=DATA.objects.get(id=2)
                    quantity1 = customer1.quantity
                    quantity2 = customer2.quantity
                    weight1 = customer1.weight
                    weight2 = customer2.weight
                    box1 = customer1.box_count
                    box2 = customer2.box_count
                    total_qty = quantity1 + quantity2
                    total_weight = weight1 + weight2
                    total_box = box1 + box2
                    return render(request, 'admin.html', {'qty1':quantity1, 'wght1':weight1, 'qty2':quantity2, 'wght2':weight2,
                                                          'box1':box1, 'box2':box2, 'total_qty':total_qty, 'total_weight':total_weight, 'total_box':total_box})
            else:
                message = 'Password does not match...'
                return render(request, 'login.html')


def ProfileData(request):
    details = DATA(order_date=request.POST.get('order_date'),
                   company=request.POST.get('company'),
                   owner=request.POST.get('owner'),
                   item=request.POST.get('item'),
                   quantity=request.POST.get('quantity'),
                   weight=request.POST.get('weight'),
                   request_for_shipment=request.POST.get('request_for_shipment'),
                   tracking_id=request.POST.get('tracking_id'),
                   shipment_size=request.POST.get('shipment_size'),
                   box_count=request.POST.get('box_count'),
                   specification=request.POST.get('specification'),
                   checklist_quantity=request.POST.get('checklist_quantity')
                   )
    details.save()
    message='Your data is recorded successfully..'
    return render(request, 'thanks.html', {'msg':message})