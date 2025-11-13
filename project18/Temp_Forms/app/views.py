from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic, Webpage,AccessRecord

def insert_topic(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        TTO = Topic.objects.get_or_create(Topic_name=tn)

        if TTO[1]:
            topics = Topic.objects.all()
            webpages = Webpage.objects.all()
            accessrecord= AccessRecord.objects.all()
            return render(request, 'display.html', {
                'topics': topics,
                'webpages': webpages,
                'accessrecord':accessrecord,
            })
        else:
            return HttpResponse('Topic_name is already present')

    return render(request, 'insert_topic.html')


def insert_webpage(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        TO = Topic.objects.get(Topic_name=tn)
        TE = request.POST['TE']
        TU = request.POST['TU']

        WTO = Webpage.objects.get_or_create(
            Topic_name=TO,
            name=TE,
            Url=TU
        )

        if WTO[1]:
            topics = Topic.objects.all()
            webpages = Webpage.objects.all()
            accessrecord= AccessRecord.objects.all()
            return render(request, 'display.html', {
                'topics': topics,
                'webpages': webpages,
                'accessrecord':accessrecord,
            })
        else:
            return HttpResponse('Webpage is already present')

    topics = Topic.objects.all()
    return render(request, 'insert_webpage.html', {'topics': topics})

def insert_accessrecord(request):
    if request.method == 'POST':
        WN = request.POST['WN']     
        AU = request.POST['AU']
        DT = request.POST['DT']

        # Get Webpage Object
        WO = Webpage.objects.get(name=WN)

        # Create AccessRecord
        ATO = AccessRecord.objects.get_or_create(
            name=WO,
            Author=AU,
            Date=DT
        )

        if ATO[1]:
            topics = Topic.objects.all()
            webpages = Webpage.objects.all()
            accessrecord = AccessRecord.objects.all()

            return render(request, 'display.html', {
                'topics': topics,
                'webpages': webpages,
                'accessrecord': accessrecord
            })
        else:
            return HttpResponse('AccessRecord is already present')

    webpages = Webpage.objects.all()
    return render(request, 'insert_accessrecord.html', {'webpages': webpages})

def display(request):
    topics = Topic.objects.all()
    webpages = Webpage.objects.all()
    accessrecord = AccessRecord.objects.all()

    return render(request, 'display.html', {
        'topics': topics,
        'webpages': webpages,
        'accessrecord': accessrecord
    })

# Showing select_multiple_topics display in browser
# def select_multiple_topics(request):
#     QLTO = Topic.objects.all()
#     d = {'QLTO': QLTO}

#     if request.method == 'POST':
#         STL = request.POST.getlist('tn')  # Getting multiple topic names from the form
#         print(STL)

#         EWQS = Webpage.objects.none()  # Empty queryset to combine results
#         for TO in STL:
#             EWQ = Webpage.objects.filter(Topic_name=TO)
#             EWQS = EWQS | EWQ  # Combine querysets using OR operator

#         d1 = {'EWQS': EWQS}
#         return render(request, 'display.html', d1)

#     return render(request, 'select_multiple_topics.html', d)

def select_multiple_topics(request):
    QLTO = Topic.objects.all()

    if request.method == 'POST':
        STL = request.POST.getlist('tn')      # Getting selected values

        EWQS = Webpage.objects.none()
        for TO in STL:
            # IMPORTANT CHANGE
            EWQ = Webpage.objects.filter(Topic_name__Topic_name=TO)
            EWQS = EWQS | EWQ

        # IMPORTANT CHANGE: send 'webpages'
        d1 = {
            'topics': Topic.objects.all(),
            'webpages': EWQS,
            'accessrecord': AccessRecord.objects.all(),
        }

        return render(request, 'display.html', d1)

    return render(request, 'select_multiple_topics.html', {'QLTO': QLTO})


def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)
















 