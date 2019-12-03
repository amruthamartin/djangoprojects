# Create your views here.
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def getDataPage(req):
    template = loader.get_template("data.html")
    res = template.render({}, req)
    return HttpResponse(res)


def getData (request):

    products= ["OPPO", "VIVO", "Samsung"]
    prices= [1000,20000,30000]
    data = {
        "products": products,
        "prices": prices
    }
    return JsonResponse(data)
