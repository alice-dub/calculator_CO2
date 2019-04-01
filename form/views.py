from django.http import HttpResponse
from django.template import loader

#from .models import Question

#Unité : bytes, kW
Spotify = 58 * 10**6 / 60 #bytes / min 
Youtube = 170000000 / 10 #bytes / min
Datacenter = 7.2 * 10 **-11 #kWh / bytes
Wired = 4.29 * 10 ** -10 #kWh / bytes 
Wifi = 1.52 * 10 ** -10 #kWh / bytes
Mobile = 8.84 * 10 ** -10 #kWh / bytes
Smartphone = 1.1 * 10 ** -4 #kWh / min
Laptop = 3.2 * 10 ** -4 #kWh / min


def accueil(request):
    template = loader.get_template('accueil.html')
    context = {}
    return HttpResponse(template.render(context, request))

def video(request):
    try:
        appareil = request.POST['appareil']
        print(appareil)
        if appareil == 'laptop':
            conso_appareil = Laptop
        elif appareil == 'smartphone':
            conso_appareil = Smartphone
        print(conso_appareil)

        connection = request.POST['connection']
        if connection == 'filaire':
            conso_network = Wired
        elif connection == 'wifi':
            conso_network = Wifi
        elif connection == 'mobile':
            conso_network == Mobile

        if request.POST['heure'] != '':
            heure = request.POST['heure']
        else:
            heure = 0
        
        if request.POST['minute'] != '':
            minute = request.POST['minute']
        else:
            minute = 0

        energie = (conso_appareil + Youtube * (Datacenter + conso_network))*(int(heure) * 60 + int(minute))

        energie_alt = (conso_appareil + Spotify * (Datacenter + conso_network))*(int(heure) * 60 + int(minute)) 
        
        economie = (energie - energie_alt) * 100 / energie

        template = loader.get_template('result.html')
        context = {'energie': round(energie,3), 'energie_alt': round(energie_alt,3), 'economie': round(economie,2)}
    except:
    
        template = loader.get_template('form/video.html')
        context = {}
    
    return HttpResponse(template.render(context, request))

def augm_vie(request):
    template = loader.get_template('accueil.html')
    context = {}
    return HttpResponse(template.render(context, request))

def box(request):
    template = loader.get_template('accueil.html')
    context = {}
    return HttpResponse(template.render(context, request))