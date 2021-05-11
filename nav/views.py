from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {"name":"sunil", "from":"ambah"}
    return render(request, 'index.html',params)
def home(request):
    return  HttpResponse("<h1> Home</h1> <a href='http://127.0.0.1:8000/'>Return to home</a>")
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lineremover = request.GET.get('lineremover', 'off')
    Charcount = request.GET.get('Charcount', 'off')
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>.?/@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuation:
                analyzed = analyzed+i


        params = {'purpose':"remove punctuation", 'Analyzed_text':analyzed}

        return render(request, "analyze.html", params)
    elif fullcaps=='on':
        analyzed = ''

        for i in djtext:
            analyzed = analyzed+i.upper()
        params = {'purpose': "capitalization", 'Analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif lineremover == 'on':
        analyzed = ''
        for index, i in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed+i
        params = {'purpose':'Extraspaceremover','Analyzed_text':analyzed}
        return  render(request, 'analyze.html', params)
    elif Charcount=='on':
        analyzed =0
        for i in djtext:
            if i!=' ':
                analyzed +=1
        params = {'purpose':'Charcount','Analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    else:
        return  HttpResponse("error 404")
# def captalization(request):
#     return  HttpResponse("captalization  <a href='http://127.0.0.1:8000/'>Return to home</a>")
# def lineromover(request):
#     return  HttpResponse("lineromover <a href='/'>Back</a>")
# def spaceremover(request):
#     return  HttpResponse("spaceremover <a href='http://127.0.0.1:8000/'>Return to home</a>")
def ex1(request):
    s = ["<a href= 'www.google.com'>Google<a/>,<br>, <a href= 'www.Youtube.com'>Youtube<a/>"]
    return HttpResponse(s)

