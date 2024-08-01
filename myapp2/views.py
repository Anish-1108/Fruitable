from django.shortcuts import render,redirect
from .models import*
import razorpay
from django.conf import settings
from django.core.mail import send_mail
import pkg_resources

import random
# Create your views here.

def index (request):
    
    if "email" in request.session:
        
        uid =  user.objects.get(email=request.session["email"])
        pid =  Add_product.objects.all()
        lid =  Add_to_cart.objects.filter(user_id=uid).count()
        
        con={
            
            'uid' : uid,
            'pid' : pid,
            'lid' : lid
        }
   
        return render(request,'index.html',con)
    else:
        return render(request,'index.html')
       
def login(request):
    
    
    
        if request.POST:
        
            email = request.POST['email']
            password=request.POST['password']
            
            try:
                uid = user.objects.get(email = email)
                
                if uid.email == email:
                    
                    if uid.password == password:
                        request.session["email"] = uid.email
                        pid = Add_product.objects.all()                     
                        
                        con={
                            'pid' : pid
                        }
   
                        return render(request,'index.html',con)
    
                    
                    else:
                        con={
                            
                            'eid' : "Invalid Password..."
                            }
                        return render(request,"login.html",con)
                        
                else:
                    con={
                        'eid' : "Invalid Email..."
                    }
                    return render(request,"login.html",con)
                        
            except:
                con={
                        'eid' : "Invalid Email..."
                    }
                return render(request,"login.html",con)
        else:
            return render(request,"login.html")             
    
def logout(request):
    
    if "email" in request.session:
        
        del request.session["email"]
        
        return render(request,"login.html")
    
    else:
        
        return render (request,"login.html")
    
def forget_password(request):

    if request.POST:
        email = request.POST['email']
        otp = random.randint(1111,9999)
        
        try :
            uid = user.objects.get(email=email)
            
            uid.otp = otp
            uid.save()

            send_mail("Forget Password","Apke ke sath scam ho gaya hai please give this OTP : "+ str(uid.otp),"gohiljayb10@gmail.com",[email])
            
            con = {
                'uid' : uid,
                'email' : email
            }

            return render (request,"confirm_password.html",con)
        
        except:
            con = {
                'eid' : "Invalid Email..."
            }
            
            return render (request,"forget_password.html",con)
    else:
        return render (request,"forget_password.html")
    
def confirm_password(request):
    
    if request.POST:
        
        email = request.POST['email']
        otp = request.POST['otp']
        n_password = request.POST['n_password']
        c_password = request.POST['c_password']
        try:
            
            uid = user.objects.get(email=email)

            if str (uid.otp) == otp:
                
                if n_password == c_password:
                    uid.password = n_password
                    uid.save()

                    return render (request,"login.html") 
                else:
                    con = {
                        'email' : email,                    
                        'eid' : "Invalid Password...",
                }
                
                return render (request,"confirm_password.html",con) 
            else:
                con = {
                    'email' : email,    
                    'eid' : "Invalid OTP...",
                }
                
                return render (request,"confirm_password.html",con) 
            
        except:
            con = {
                'email' : email,
                'eid' : "Invalid Email...",      
            }
            return render (request,"confirm_password.html",con)
            
    else:
        return render (request,"confirm_password.html")
    
def categories(request,id):
    
    pid = Add_product.objects.filter(categories_id=id)
    cid = Categories.objects.all()
    lid =  Add_product.objects.all().count()
    
    con = {
        'pid' : pid,
        'cid' : cid,
        'lid' : lid
    }
    return render(request,"shop.html",con)

def shop (request):
    
    pid = Add_product.objects.all()
    cid = Categories.objects.all()
    lid =  Add_product.objects.all().count()
    
    low_to_high = request.GET.get('low_to_high')    
    high_to_low = request.GET.get('high_to_low')
    A_to_Z = request.GET.get('A_to_Z')
    Z_to_A = request.GET.get('Z_to_A')
    
    if low_to_high:
        pid = Add_product.objects.order_by('price') 
    elif high_to_low:
        pid = Add_product.objects.order_by('-price') 
    elif A_to_Z:
        pid = Add_product.objects.order_by('name') 
    elif Z_to_A:
        pid = Add_product.objects.order_by('-name') 
    else:
        pid = Add_product.objects.all()
        
    con = {
        
        'pid' : pid,
        'cid' : cid,
        'lid' : lid,
        'low_to_high' : low_to_high,
        'high_to_low' : high_to_low
    }
    return render(request,'shop.html',con)

def add_to_cart(request,id):
    if "email" in request.session:
        
        uid =  user.objects.get(email=request.session["email"])
        pid = Add_product.objects.get(id=id)
        
        Add_to_cart.objects.create(user_id = uid,
                                   product_id = pid,
                                   name = pid.name,
                                   price = pid.price,
                                   qyt = pid.qyt,
                                   total_price = pid.qyt * pid.price,
                                   pic = pid.pic
                                   )
        return redirect('cart')
    else:
        return render(request,"login.html")


def contact (request):
    
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        
        uid =  Contact_US.objects.create(name = name , email = email , message = message)
        
        return render(request,"contact.html")
    else:
        return render(request,"contact.html")
    

def shopdetail (request):

    return render(request,'shop-detail.html')


def search(request):
    
    name = request.GET['name']
    
    if name:
        
        pid = Add_product.objects.filter(name__contains=name)
        
        con = {
            
            'pid' : pid
        }
        return render(request,"shop.html",con)
    else:
        return render(request,"index.html")


def Add_address (request):
       
    uid =  user.objects.get(email=request.session["email"])
    vid = Address.objects.get(user_id=uid)
    aid = Address.objects.filter(user_id=uid).exists()
    
    if aid:
        pro_all = Add_to_cart.objects.all()
        l1 = []
        
        for i in pro_all:
            l1.append(f" name = {i.name}, price = {i.price} , qty = {i.qyt}, total price = {i.total_price}")
        
        vid.list = l1
        vid.save()
        return redirect('chackout')
    
    else:
        if request.POST:
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            address = request.POST['address']
            city = request.POST['city']
            country = request.POST['country']
            pincode = request.POST['pincode']
            mobile = request.POST['mobile']
            email = request.POST['email']
            
            aid = Address.objects.create(user_id=uid,
                                        f_name=f_name,
                                        l_name=l_name,
                                        address=address,
                                        city = city,
                                        country = country,
                                        pincode = pincode,
                                        mobile = mobile,
                                        email = email)
            
            
            vid = Address.objects.get(user_id=uid)
            pro_all = Add_to_cart.objects.all()
            l1 = []
            
            for i in pro_all:
                l1.append(f" name = {i.name}, price = {i.price} , qty = {i.qyt}, total price = {i.total_price}")
            
            vid.list = l1
            vid.save()
            
            return render(request,'Add_address.html')
        else:
            return render(request,'Add_address.html')
        
 

def change_address(request):
    uid =  user.objects.get(email=request.session["email"])
    try:    
        did = Address.objects.filter(user_id=uid).delete()
        
        return render(request,"Add_address.html")
    
    except:
        return render(request,"Add_address.html")


def cart (request):
    uid =  user.objects.get(email=request.session["email"])
    cid = Add_to_cart.objects.filter(user_id=uid)
    lid =  Add_product.objects.all().count()
    
    con = {
        'cid' : cid,
        'lid' : lid
    }

    return render(request,'cart.html',con)

def plus(request,id):
    
    pid = Add_to_cart.objects.get(id=id)
    
    if pid:
        pid.qyt = pid.qyt + 1
        pid.total_price = pid.price * pid.qyt
        pid.save()
        
        return redirect('cart')
    else:
        return render(request,"cart.html")


 
def minus(request,id):
    
    mid = Add_to_cart.objects.get(id=id)
    
    if mid.qyt == 1:
        mid = Add_to_cart.objects.get(id=id).delete()
        return redirect('cart')
        

    else:
        if mid:
            mid.qyt = mid.qyt - 1
            mid.total_price = mid.price * mid.qyt
            mid.save()
            
            return redirect('cart')
        else:
            return render(request,"cart.html")

def deletes_cart(request,id):
    
    did = Add_to_cart.objects.get(id=id).delete()
    
    return redirect('cart')



def chackout (request):
    
    uid =  user.objects.get(email=request.session["email"])
   
    lid =  Add_to_cart.objects.filter(user_id=uid).count()
    try:
        
        pid = Add_to_cart.objects.filter(user_id=uid)
        l1 = []
        
        for i in pid:
            l1.append(i.total_price)
            
        total = sum(l1)
        sub_total = total + 50
        
        amount = total*100 
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({
                                    'amount':amount,
                                    'currency':'INR',
                                    'payment_capture':1
        })
        
        con = {
            
            'lid' : lid,
            'pid' : pid,
            'total' : total,
            'sub_total' : sub_total,
            'response' : response
        }
        
        return render(request,'chackout.html',con)
    except:
        return render(request,'chackout.html')

  
def register(request):
    
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        uid = user.objects.create(username = username , email = email , password = password)
        
        return render(request,"login.html")
    else:
        return render(request,"register.html")
    
    
    
def testimonial (request):

    return render(request,'testimonial.html')

def hhh (request):

    return render(request,'404.html')