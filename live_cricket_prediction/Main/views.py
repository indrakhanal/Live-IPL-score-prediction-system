from django.shortcuts import render
from django.http import request, HttpResponse
import numpy as np
# from joblib import load
import pickle

def home(request):
    return render(request, 'home.html')

def frontend_data(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        bat_team = request.POST.get('bat')
        bowl_team = request.POST.get('bowl')
        try:
            current_run =int(request.POST.get('run'))
            current_wkt = int(request.POST.get('wkt'))
            current_over = float(request.POST.get('over'))
            last_five_run = int(request.POST.get('l_five'))
            last_five_wkt = int(request.POST.get('l_wkt'))
        except:
            message = 'All Value Should fill up'
            return render(request, 'home.html', context={'message': message})
        csk = "csk"
        dd = "dd"
        kxip = "kxip"
        kkr = "kkr"
        mi = "mi"
        rcb = "rcb"
        rr = "rr"
        shr = "shr"
        dict_item = {'csk' :0, 'dd':0, 'kxip':0, 'kkr':0, 'mi':0, 'rcb':0, 'rr':0, 'shr':0}
        value = list(dict_item.values())
        key = dict_item.keys()
        if bat_team != bowl_team:
            if bat_team == csk:
                value[0]= 1
            elif bat_team==dd:
                value[1]=1
            elif bat_team == kxip:
                value[2]=1
            elif bat_team==kkr:
                value[3]=1
            elif bat_team == mi:
                value[4]=1
            elif bat_team == rcb:
                value[5]=1
            elif bat_team == rr:
                value[6]=1
            elif bat_team == shr:
                value[7]=1
            # for bowling team

            dict_item_bowl = {'csk': 0, 'dd': 0, 'kxip': 0, 'kkr': 0, 'mi': 0, 'rcb': 0, 'rr': 0, 'shr': 0}
            value_bowl = list(dict_item_bowl.values())
            if bowl_team == csk:
                value_bowl[0]= 1
            elif bowl_team==dd:
                value_bowl[1]=1
            elif bowl_team == kxip:
                value_bowl[2]=1
            elif bowl_team==kkr:
                value_bowl[3]=1
            elif bowl_team == mi:
                value_bowl[4]=1
            elif bowl_team == rcb:
                value_bowl[5]=1
            elif bowl_team == rr:
                value_bowl[6]=1
            elif bowl_team == shr:
                value_bowl[7]=1
            print(type(value), type(value_bowl))
            list_data_team = value+value_bowl
            print(list_data_team, 'all team data')

            list_remaining_data = [current_run, current_wkt, current_over, last_five_run, last_five_wkt]
            print(list_remaining_data, 'other data ')

            final_data =[list_data_team + list_remaining_data]
            print(final_data)
            with open('Main/final_modal.pkl', 'rb') as f:
                model = pickle.load(f)
                final_pridect = model.predict(final_data)
                output = int(final_pridect)
                context = {
                    'final':f'First Batting Team Will Set {output} Target',
                }
        else:
            message = 'error!!' \
                      ' same team cannot bat and bowl at same time'
            return render(request, 'home.html', context={'msg':message})

    return render(request, 'home.html', context)