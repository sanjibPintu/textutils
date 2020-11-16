# I have created this file-sanjib
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analize(request):
    #get the text
    djtext=request.POST.get('text','default')
    # check the check box value
    removepunc=request.POST.get('removepunc','off')
    fullcapps=request.POST.get('fullcapps','off')
    fulllow=request.POST.get('fulllow','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')

    # check which check box is on
    if removepunc=="on":
        panctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized=""
        for char in djtext:
            if char not in panctuation:
                analized=analized+char
        params={'purpose':'Remove Pnction','analyzed_text':analized}
        djtext=analized

    if(fullcapps=="on"):
        #capitalize the text
        analized=""
        for char in djtext:
            analized=analized + char.upper()
        params={'purpose':'Convert into Upper Case','analyzed_text':analized}
        djtext = analized

    if (fulllow == "on"):
        # capitalize the text
        analized = ""
        for char in djtext:
            analized = analized + char.lower()
        params = {'purpose': 'Convert into Upper Case', 'analyzed_text': analized}
        djtext = analized

    if(newlineremover=='on'):
        # New line Remover
        analized = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analized = analized + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analized}
        djtext = analized
        # return render(request, 'analize.html', params)

    if(spaceremover=='on'):
        # Extra Space remover
        analized = ""
        for index ,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analized = analized + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analized}
        djtext = analized
        # return render(request, 'analize.html', params)

    if(charcount=='on'):
        # Count The Charector
        analized = len(djtext)
        params = {'purpose': 'The Number of Charector', 'analyzed_text': analized}

    if (removepunc!="on" and fullcapps!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on" and fulllow != "on") :
        return HttpResponse("Please check any of the button!!")


    return render(request,'analize.html',params)
