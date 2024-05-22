from django.shortcuts import render,get_object_or_404
from vendor.models import Vendor
from menu.models import Category,FoodItem
from django.http import HttpResponse,JsonResponse

from django.db.models import Prefetch
from .models import Cart
from django.db.models import Q

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D   
from django.contrib.gis.db.models.functions import Distance


# in the above import statement D is for distance
# Create your views here.
def marketplace(request):
    vendors=Vendor.objects.filter(is_approved=True)
    vendor_count=vendors.count()
    context={
        'vendors':vendors,
        'vendor_count':vendor_count,
    }
    return render(request,'marketplace/listing.html',context)

def vendor_detail(request,vendor_slug):
    vendor=get_object_or_404(Vendor,vendor_slug=vendor_slug)
    categories=Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
        )
    )
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user=request.user)
    else:
        cart_items=None   
    context={
        'vendor':vendor,
        'categories':categories,
        'cart_items':cart_items,
        
    }
    return render(request,'marketplace/vendor_detail.html',context)


def add_to_cart(request,food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            try:
                fooditem=FoodItem.objects.get(id=food_id)
                #check if the user has already added that food to the cart
                try:
                    chkCart=Cart.objects.get(user=request.user,fooditem=fooditem)
                    # increase the cart quantity
                    chkCart.quantity+=1
                    chkCart.save()
                    return JsonResponse({'status':'Success','message':'Increased the cart quantity'})
                
                except:
                    chkCart=Cart.objects.create(user=request.user,fooditem=fooditem,quantity=1)
                    return JsonResponse({'status':'Success','message':'Increased the cart quantity'})
                
                    
            except:
                return JsonResponse({'status':'Failed','message':'This food does not exist'})
            
    
                
        
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    else:
        return JsonResponse({'status':'Failed','message':'Please login to continue'})
    
    
def search(request):
    if not 'address' in request.GET:
        return redirect('marketplace')
    else:
        address=request.GET['address']
        latitude=request.GET['lat']
        longitude=request.GET['lng']
        radius=request.GET['radius']
        keyword=request.GET['keyword']
        
        # print(address,latitude,longitude,radius)
        fetch_vendors_by_fooditems=FoodItem.objects.filter(food_title__icontains=keyword,is_available=True).values_list('vendor',flat=True)
        vendors=Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword,is_approved=True,user__is_active=True))
        
        print(vendors)
        if latitude and longitude and radius:
            pnt=GEOSGeometry('POINT(%s %s)' % (longitude,latitude))
            vendors=Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditem) | Q(vendor_name__icontains=keyword,is_approved=True,user__is_active=True),
            user_profile__location__distance_lte=(pnt,D(km=radius))
            ).annotate(distance=Distance("user_profile__location",pnt)).order_by("distance")
            
            for v in vendors:
                v.kms=v.distance.km
        vendor_count=vendors.count()
        context={
            'vendors':vendors,
            'vendor_count':vendor_count,
            'source_location':address,
        }
        
        return render(request,'marketplace/listing.html',context)