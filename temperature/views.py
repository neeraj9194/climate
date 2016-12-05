from django.shortcuts import render
from html.parser import HTMLParser
import urllib.request
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from . import models,forms 
from datetime import date
from chartit import DataPool, Chart
from django.db.models import Avg


def store_txt(url,country,table):
    #url='http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt'
    url_req=urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data_set = urllib.request.urlopen(url_req).readlines()[8:]
    obj,created=models.Country.objects.get_or_create(country=country)
    #print(obj,created)
    for row in data_set:
        #print(row.strip().split())
        data=[]
        count=0
        for col in row.strip().split():
            #print(col)
            try:
                data.append(float(col))
            except ValueError:
                data.append(None)
        count+=1
        data[0]=int(data[0])
        if data[0] != date.today().year: # Leaving current Year because of Inconsistent data.
            date_obj,date_created=models.Year.objects.get_or_create(year=data[0])
            obj2,created2=table.objects.update_or_create(cid=obj,year=date_obj,defaults={'jan':data[1],'feb':data[2],'mar':data[3],'apr':data[4],'may':data[4],'jun':data[6],'jul':data[7],'aug':data[8],'sep':data[9],'octu':data[10],'nov':data[11],'dec':data[12],'win':data[13],'spr':data[14],'sumr':data[15],'aut':data[16],'ann':data[17]})
                
        #print(obj,obj2,created2)
    
def get_data():
    url='http://www.metoffice.gov.uk/climate/uk/summaries/datasets'
    url_req=urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    yorder_html = urllib.request.urlopen(url_req).read()
    soup = BeautifulSoup(yorder_html, 'html.parser')
    table=soup.find_all('table')[1]
    row_count=0
    temp=[models.MaxTemp,models.MinTemp,models.MeanTemp,models.Sunshine,models.Rainfall]
    for row in table:
        #print(len(row))
        if row_count>4:
            break
        row_count+=1
        col_count=0
        url_txt=[]
        country=""
        cols=row.find_all('td')[:6]
        if cols==[]:
            continue
        for col in cols:
            #print(col)
            if col_count==0:
                country=col.text
                #print(country)
            else:
                url_txt.append(col.find('a').get('href'))
            col_count+=1
        #print(url_txt)
        for i in range(5):
            store_txt(url_txt[i],country,temp[i])
            
def index(request):        
    if request.method=='POST' and request.POST['flag']:
        get_data()
        form=forms.FilterForm()

    elif request.method=='POST':
        form=forms.FilterForm(request.POST)

    else:
        form=forms.FilterForm()

    year=models.Year.objects.all()
    country=models.Country.objects.all()
    return render(request,'temperature/index.html',{'year':year,'country':country,'form':form})

def display(request):
    obc=models.Country.objects.all()
    oby=models.Year.objects.all()
    if request.method=='POST' and request.POST['year'] and request.POST['country']:
        form=forms.FilterForm(request.POST)
        ob1=models.MinTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'],cid__cid=request.POST['country'])
        ob2=models.MaxTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'],cid__cid=request.POST['country'])
        ob3=models.MeanTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'],cid__cid=request.POST['country'])
    elif request.method=='POST' and request.POST['year'] and not request.POST['country']:
        form=forms.FilterForm(request.POST)
        ob1=models.MinTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'])
        ob2=models.MaxTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'])
        ob3=models.MeanTemp.objects.filter(year__year__in=oby.values('year'),year__yid=request.POST['year'])
    elif request.method=='POST' and not request.POST['year'] and request.POST['country']:
        form=forms.FilterForm(request.POST)
        ob1=models.MinTemp.objects.filter(year__year__in=oby.values('year'),cid__cid=request.POST['country'])
        ob2=models.MaxTemp.objects.filter(year__year__in=oby.values('year'),cid__cid=request.POST['country'])
        ob3=models.MeanTemp.objects.filter(year__year__in=oby.values('year'),cid__cid=request.POST['country'])
    else:
        form=forms.FilterForm()
        ob1=models.MinTemp.objects.filter(year__year__in=oby.values('year'))
        ob2=models.MaxTemp.objects.filter(year__year__in=oby.values('year'))
        ob3=models.MeanTemp.objects.filter(year__year__in=oby.values('year'))
    #print(ob1.values('year__year'))
    return render(request,'temperature/displaytable.html',{'form':form,'obj':list(zip(ob1,ob2,ob3))})

def chart(request,year=None,country=None):
    if year!=None:
        ch1=models.MinTemp.objects.filter(year__year=year,cid__country=country).values_list("jan",'feb','mar','apr','may','jun','jul','aug','sep','octu','sep','nov','dec')
        ch2=models.MaxTemp.objects.filter(year__year=year,cid__country=country).values_list("jan",'feb','mar','apr','may','jun','jul','aug','sep','octu','sep','nov','dec')
        ch3=models.MeanTemp.objects.filter(year__year=year,cid__country=country).values_list("jan",'feb','mar','apr','may','jun','jul','aug','sep','octu','sep','nov','dec')
        return render(request,'temperature/chart.html',{'data_min':list(float(i) for i in ch1[0]),'data_max':list(float(i) for i in ch2[0]),'data_mean':list(float(i) for i in ch3[0])})
    else:
        ch1=models.MinTemp.objects.filter(cid__country=country).all().aggregate(Avg("jan"),Avg('feb'))
        #print(ch1)
        return render(request,'temperature/chart.html',{'data_min':ch1})
