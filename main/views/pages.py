import random

import json

from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('user')
    return render(request, 'main/home.html')


def user(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.user.talantuser.cs_result.result and request.user.talantuser.dota_result.result:
        return render(request, 'main/user.html',
                      {'user': request.user, 'score': request.user.talantuser.cs_result.result_num,
                       'kd': json.loads(request.user.talantuser.cs_result.result_json)['kd'],
                       'avg_cs': json.loads(request.user.talantuser.cs_result.result_json)['avg_cs'],
                       'avg_plant_defuse': json.loads(request.user.talantuser.cs_result.result_json)[
                           'avg_plant_defuse'],
                       'avg_give_weapon': json.loads(request.user.talantuser.cs_result.result_json)['avg_give_weapon'],
                       'avg_mvp': json.loads(request.user.talantuser.cs_result.result_json)['avg_mvp'],
                       'role': json.loads(request.user.talantuser.dota_result.result_json)['role'],
                       'comparing_skill': json.loads(request.user.talantuser.dota_result.result_json)[
                           'comparing_skill'],
                       'benefit': json.loads(request.user.talantuser.dota_result.result_json)['benefit'],
                       'frequency_fight': json.loads(request.user.talantuser.dota_result.result_json)[
                           'frequency_fight'],
                       })
    elif request.user.talantuser.cs_result.result:
        return render(request, 'main/user.html', {'user': request.user, 'score':request.user.talantuser.cs_result.result_num,
                                              'role': json.loads(request.user.talantuser.dota_result.result_json)['role'],
                                              'comparing_skill': json.loads(request.user.talantuser.dota_result.result_json)['comparing_skill'],
                                              'benefit': json.loads(request.user.talantuser.dota_result.result_json)['benefit'],
                                              'frequency_fight': json.loads(request.user.talantuser.dota_result.result_json)['frequency_fight'],
                                              })
    elif request.user.talantuser.dota_result.result:
        return render(request, 'main/user.html',
                      {'user': request.user, 'score': request.user.talantuser.dota_result.result_num,
                       'role': json.loads(request.user.talantuser.dota_result.result_json)['role'],
                       'comparing_skill': json.loads(request.user.talantuser.dota_result.result_json)[
                           'comparing_skill'],
                       'benefit': json.loads(request.user.talantuser.dota_result.result_json)['benefit'],
                       'frequency_fight': json.loads(request.user.talantuser.dota_result.result_json)[
                           'frequency_fight'],
                       })
    else:
        return render(request, 'main/user.html', {'user': request.user, 'score': random.randint(0, 100)})


def page_not_found(request, exception):
    return render(request, 'main/error.html')
