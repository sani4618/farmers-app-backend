from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse 

@csrf_exempt
def addfarmers(request):
    if request.method=="POST":
        reiceived_json_data=json.loads(request.body)
        getfarmerid=reiceived_json_data["farmerid"]
        getbloodgroup=reiceived_json_data["BldGrp"]
        getpincode=reiceived_json_data["pinCode"]
        getdob=reiceived_json_data["dob"]
        getemail=reiceived_json_data["phNum"]
        getAddress=reiceived_json_data["address"]
        getfarmername=reiceived_json_data["farmerName"]
        data={"farmerid":getfarmerid,"BldGrp":getbloodgroup,"pinCode":getpincode,"dob":getdob,"phNum":getemail,"address":getAddress,"farmerName":getfarmername}
        print(data)
        
    