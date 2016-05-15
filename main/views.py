from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
# Create your views here.


def music(request):
    context = {}
    if request.method == 'POST':
        key_word = request.POST.get('name')
        page = request.POST.get('page', '1')
        res = requests.get('https://auth-external.music.qq.com/open/fcgi-bin/fcg_weixin_music_search.fcg?remoteplace=txt.weixin.officialaccount&w=' + key_word + '&platform=weixin&jsonCallback=MusicJsonCallback&perpage=10&curpage=' + page)
        r = res.content[19:-2]
        json_r = json.loads(r)
        """
        {"perpage": 10,
         "retcode": 0,
         "keyword": "gaga",
         "curnum": 10,
         "list": [{
                      "f": "3822013|Gaga|107007|Afro Sol|324527|Afro Sol|2397384|278|7|1|0|0|4450645|192000|0|0|0|0|0|0|002PNu0K4UKpEO|002911G93IAtsn|004aH0Pe3qqyOn",
                      "singername": "Afro Sol - Afro Sol",
                      "albumname": "Afro Sol",
                      "downUrl": "http://stream7.qqmusic.qq.com/33822013.mp3",
                      "t": 1, "ring": 0,
                      "m4a": "http://ws.stream.qqmusic.qq.com/3822013.m4a?fromtag=46",
                      "id": 3822013, "songname": "Gaga"}],
         "curpage": 1,
         "totalnum": 391}

        """
        context = json_r
    return render(request, 'music.html', context)

def live(request):
    return render(request, 'live.html', {})