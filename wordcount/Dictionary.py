# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 05:53:14 2018

@author: Kunal Bhandari
"""

from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    #return (HttpResponse("great"))
    return (HttpResponse("<h1> New </h1>")) # html code directly passes into response

def count(request): #httprequest object
    print(request)
    fulltext = request.GET['fulltext']
    wordcount=len(fulltext.split())
    print (fulltext)
    print (wordcount)
    return (render(request,'count.html',{'fulltext':fulltext,'count':wordcount}))#returns http response obejct

def about(request):
    return (render(request,"about.html"))    