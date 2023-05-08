
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
# Create your views here.
# def home(request):
#     return HttpResponse("hi welcome home")

# def home(request):
#     return HttpResponse("<h1>hi welcome home</h1>")


# def home(request):
#     return render(request,'home.html',{"name":"Afitha","id":1})


# def home(request):
#     datasample=loader.get_template('home.html')
#     data={"name":"Ansar",
#           "id":2
#           }
#     response=datasample.render(data,request)
#     return HttpResponse(response)


# def homepage(request):
#     return render(request,'index.html')

# def calcvalues(request):
#     numberone=int(request.GET['numone'])
#     numbertwo=int(request.GET['numtwo'])
#     result=numberone+numbertwo
#     return render(request,'result.html',{"res":result})

# def calcvalues(request):
#     numberone=int(request.POST['numone'])
#     numbertwo=int(request.POST['numtwo'])
#     result=numberone+numbertwo
#     return render(request,'result.html',{"res":result})
####################################################################

def homeone(request):
    datasample=loader.get_template('home.html')
    data={"catagory":"Appliances",
           "products":[{
            "Id":1,
            "subcatagory":"Television",
            "Brand":"LG",
            "Features":["45 inch LED"],
           },
           {
            "Id":2,
            "subcatagory":"Washing machine",
            "Brand":"Samsung",
            "Features":["automatic","top load","7L"],
           }
           ]
           }
        
    response=datasample.render(data,request)
    return HttpResponse(response)

# ####################################################################

from .models import items as its
def dbitemdisp(request):
    datasample=loader.get_template('dbitemdisp.html')
    db=its.objects.all()
    data={'pros':db}  
    response=datasample.render(data,request)
    return HttpResponse(response)


def prod(request,pi):
    datasample=loader.get_template('productdet.html')
    pro=its.objects.get(id=pi)
    data={'pros':pro}  
    response=datasample.render(data,request)
    return HttpResponse(response)


# def addtocart(req):
#     print(req)
#     print(req.GET['qty'])
#     print(req.GET['proid'])


# def addtocart(req):
#     response= HttpResponse("item added to cart")
#     data=req.COOKIES.get('pid')
#     if data!=None:
#         data=data+','+req.GET['qty'] + ':' + req.GET['proid']
#     else:
#         data=req.GET['proid'] + ':' + req.GET['qty']
#     response.set_cookie('pid',data)
#     return response    


# def viewcart(request):
#     datasample=loader.get_template('shoppingcart.html')
#     data=request.COOKIES.get('pid')
#     items=data.split(',')
#     print(items)
#     value=[]
#     for i in items:
#         cart=i.split(':')
#         proid=cart[0]
#         qty=cart[1]
#         value.append({proid:qty})
#     print(value)
#     datas={"mycart":value}
#     response=datasample.render(datas,request)
#     return HttpResponse(response)


def addtocart(req):
    print(req)
    qty=int(req.GET["qty"])
    proid=int(req.GET["proid"])
    cartitems={}
    response= HttpResponse("item  added")
    if req.session.__contains__("cartdata"):
        cartitems=req.session["cartdata"]
    cartitems[proid]=qty
    req.session["cartdata"]=cartitems
    print(type(req.session["cartdata"]))
    return response

# def viewcart(req):
#     page=loader.get_template("shoppingcart.html")
#     if req.session.__contains__("cartdata"):
#         for key in req.session.keys():
#             itemss = req.session[key]
#             val = list(itemss.items())
#             print(val)
#             for i in range(len(val)):
#                 proid=val[i][0]
#                 qty=val[i][1]
#                 print("proid:-",proid)
#                 print("qty:-",qty)
#     response=page.render({},req)
#     return HttpResponse(response)



def viewcart(req):
    page=loader.get_template("shoppingcart.html")
    if req.session.__contains__("cartdata"):
        for key in req.session.keys():
            itemss = req.session[key]
            val = list(itemss.items())
            itemdb=[]
            for i in range(len(val)):
                proid=val[i][0]
                qty=val[i][1]
                db=its.objects.get(id=proid)
                itemdb.append({
                    "id":proid,
                    "qty":qty,
                    "name":db.name,
                    "price":db.price,
                    "total":qty*int(db.price),
                })
                fullam=0
            for i in itemdb:
                for key,value in i.items():
                    if key=="total":
                        fullam+=value
            data={"product":itemdb,'fullamt':fullam}
            response=page.render(data,req)
            return HttpResponse(response)
    else:
        return HttpResponse("No item added in cart!!")



def  getjsondata(requset):
    data=[]
    for i in its.objects.all():
        data.append({
            "id":i.id,
            "name":i.name,
            "price":i.price,
            "Des":i.desc,
            "fea":i.Fea
        }
        )
    newdata={'new':data}
    return JsonResponse(newdata)


def search(request):
    datasample=loader.get_template('prodser.html')
    data={}  
    response=datasample.render(data,request)
    return HttpResponse(response)

def getproduct(request,keyw):
    da=[]
    for i in its.objects.filter(name__contains=keyw):
        da.append({
            "id":i.id,
            "name":i.name,
            "price":i.price, 
        })
    datas={'produ':da}
    return JsonResponse(datas)
        