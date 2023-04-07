from django.shortcuts import render,redirect
from .models import Email,Moblie


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        print(phone,"ttttttttttttttttttttttttt")

        # Save email to database
        email_obj = Email.objects.create(email=email)
        print(email_obj,"email")
        print(phone,"dsjndslkndslkndslkndslksnd")
        list=[]
        phn=phone.split(',')
        for i in phn:
            print(i)
            list.append(i)
            print(list)
        # Save mobile to database linked to email
            mobile_obj = Moblie.objects.create(email_id=email_obj,  moblie=i)
        print(mobile_obj,"mobile")
        
        
        # emails = Email.objects.all().order_by('-id')
        emails = Email.objects.all().order_by('-id').prefetch_related('moblie_set')
        print(emails,"uuuuuuuuuuuuuuuuu")
        
        context = {'emails': emails}
        print(context,"ttttttttttttttttttt")
        # context={'list':list,'email_obj':email_obj,'email1':emails,'mobile1':mobiles}
        return render(request, 'home.html',context)
    else:
        return render(request, 'home.html')

