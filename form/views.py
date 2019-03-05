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
    template = loader.get_template('form/accueil.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    try:
        appareil = request.POST['appareil']
        print(appareil)
        if appareil == 'laptop':
            conso_appareil = Laptop
        elif appareil == 'smartphone':
            conso_appareil = Smartphone
        print(conso_appareil)

        connection = request.POST['connection']
        print(connection)
        if connection == 'filaire':
            conso_network = Wired
        elif connection == 'wifi':
            conso_network = Wifi
        elif connection == 'mobile':
            conso_network == Mobile
        print(conso_network)

        if request.POST['heure'] != '':
            heure = request.POST['heure']
        else:
            heure = 0
        
        if request.POST['minute'] != '':
            minute = request.POST['minute']
        else:
            minute = 0
        print(heure)
        print(minute)

        energie = (conso_appareil + Youtube * (Datacenter + conso_network))*(int(heure) * 60 + int(minute))
        print(energie)

        energie_alt = (conso_appareil + Spotify * (Datacenter + conso_network))*(int(heure) * 60 + int(minute)) 
        print(energie_alt)
        
        economie = (energie - energie_alt) * 100 / energie

        print(connection, heure, minute)
        template = loader.get_template('form/result_1.html')
        context = {'energie': round(energie,3), 'energie_alt': round(energie_alt,3), 'economie': round(economie,2)}
    except:
        print('no connection')
    
        template = loader.get_template('form/yt_vs_sd.html')
        context = {}
    
    return HttpResponse(template.render(context, request))