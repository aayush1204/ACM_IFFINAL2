from django.shortcuts import render
from .models import Companies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def if_home(request):

    
    return render(request, 'index.html', )

def job_list(request):

    company_list= Companies.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(company_list, 5)

    try:
        company_data = paginator.page(page)
    except PageNotAnInteger:
        comapny_data = paginator.page(1)
    except EmptyPage:
        company_data = paginator.page(paginator.num_pages)

    return render(request, 'job-listings.html', {'company_data': company_data}) 

def job_single(request,value):

    comp= Companies.objects.all()
    for i in comp:
        if i.Company_name == value:
            company_data=i

    perk= company_data.perks.split(';')
    mskill = company_data.mandatory_skills.split(';')    
    jreq = company_data.job_requirement.split(';')


    return render(request, 'job-single.html',{'company_data':company_data,'perk':perk,'mskill':mskill,'jreq':jreq })

