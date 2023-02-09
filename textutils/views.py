# I have created this file- Sree
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse("about Sree!")
#
# def random1(request):
#     return HttpResponse('''<a href = "https://www.youtube.com/watch?v=AepgWsROO4k"> Random1 Sree</a>''')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    purpose = ""
    # if removepunc == "on" and fullcaps == "on":
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     analyzed0 = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char
    #     analyzed1 = analyzed
    #     for char in analyzed1:
    #         char = char.upper()
    #         analyzed0 = analyzed0 + char
    #     params = {'purpose': 'Remove punctuations and Upper Case', 'analyzed_text': analyzed0}
    #     return render(request, 'analyze.html', params)

    if (removepunc == "on"):
        purpose = purpose + " Remove Punctuatuions|"
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text' : analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        purpose = purpose + " Changed to Upper Case|"
        analyzed = ""
        for char in djtext:

            analyzed = analyzed + char.upper()
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        purpose = purpose + " Removed NewLines|"
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == 'on'):
        purpose = purpose + " Remove Extra Space|"
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == 'on'):
        analyzed = ""
        purpose = purpose + " Number of characters|"
        count = 0
        for char in djtext:
            count = count + 1
        analyzed = djtext + "\n" + str(count)

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error!")

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != 'on'):
        return HttpResponse("Error! Please select any of the options to perform.")

    return render(request, 'analyze.html', params)