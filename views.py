from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import RiskManagerForm, SMSForm
from .models import RiskManagerDetail, BroadcastResponse, ApplicantDetails, BroadcastDetails
import urllib.request
import urllib.parse
import json 
import datetime
from django.views import View
from django.core.paginator import Paginator

def homepage(request):
    context = RiskManagerDetail.objects.all()
    return render(request,'collection/home.html',{'context':context})


def add_rm(request):
    form = RiskManagerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(homepage)
    return render(request, "collection/create_rm.html", {'form':form})


def edit_details(request, pk):
    context = RiskManagerDetail.objects.get(pk=pk)
    form = RiskManagerForm(request.POST or None, instance=context)
    if form.is_valid():
        form.save()
        return redirect(homepage)
    return render(request, "collection/edit.html", {'context':context, 'form':form})

# def customer_list(request, risk_manager__firstname):
#     context = ApplicantDetails.objects.filter(risk_manager__firstname=risk_manager__firstname)
#     return render(request,'collection/customer_details.html',{'context':context})



 
def SMS_view(message, to):
    data =  urllib.parse.urlencode({'api_key':'A53467dcf64df72a81c113b618e355cfb',
        'message':message, 'sender':'MYSTRO', 'to':to, 'method':'sms'})
    data = data.encode('utf-8')
    my_request = urllib.request.Request("https://api-alerts.kaleyra.com/v4/?")
    output = urllib.request.urlopen(my_request, data)
    conclusion = output.read()
    return (conclusion)


def send_SMS(request):
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_type = cd.get("message_type")
            sr_no = cd.get("sr_no")
            name = cd.get("name")
            loan_product = cd.get("loan_product")
            recepient_contact_no = cd.get("recepient_contact_no")
            recepient_name = cd.get("recepient_name")
            message_template = cd.get("message_template")
            message = cd.get("message")

            if message_type and recepient_contact_no:
                send = json.loads(SMS_view(message=message, to=recepient_contact_no))
                status = send['status']
                message1 = send['message']
                for i in send['data']:
                    id1 = i['id']
                    customid = i['customid']
                    customid1 = i['customid1']
                    customid2 = i['customid2']
                    mobile = i['mobile']
                    status1 = i['status']
                    context =  BroadcastResponse.objects.create(api_status=status , sms_id=id1, 
                    customid=customid, customid1=customid1, customid2=customid2, mobile=mobile,
                    status=status1, message=message1, type='SMS', created_date=datetime.date.today())
                    context.save()
                data = BroadcastDetails.objects.create(message_type=message_type, sr_no=sr_no, name=name,
                        loan_product=loan_product, recepient_contact_no=recepient_contact_no, 
                        recepient_name=recepient_name, message_template=message_template, 
                        message=message, created_date=datetime.date.today())
                data.save()
                return HttpResponse("sms sent")
            else:
                return HttpResponse("Missing Fields")
    else:
        form = SMSForm()
    return render(request, "collection/send_SMS.html", {'form':form})



    
def get_list(request):
    context = ApplicantDetails.objects.all()
    paginator = Paginator(context, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "collection/get-list.html", {'page_obj':page_obj})

