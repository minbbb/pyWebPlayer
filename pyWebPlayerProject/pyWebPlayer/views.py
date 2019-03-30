from django.shortcuts import render
from django.http import HttpResponse
from pyWebPlayer.models import music
from pyWebPlayer.models import dir
import os
from django.templatetags.static import static
from django.conf import settings
import pyWebPlayer.settings
from pathlib import Path

def index(request):
    return render(request, 'pyWebPlayer/index.html')

def getFiles(request):
    send = ''
    if Path(request.GET["path"]).as_posix() != settings.STATIC_URL + "pyWebPlayer/muslink":
        send += "<ul data-dirUrl='" + Path(request.GET["path"]).parents[0].as_posix() + "'>DIR <span>..</span></ul>"
    for elem in dir.objects.filter(dirPath = request.GET["path"]):
        send += "<ul data-dirUrl='" + elem.getUrl() + "'>DIR <span>" + elem.getDirName() + "</span></ul>"
    for elem in music.objects.filter(dirPath = request.GET["path"]):
        send += "<ul data-musicUrl='" + elem.getUrl() + "'>MUS <span>" + elem.getFileName() + "</span></ul>"
    return HttpResponse(send)

def updateDBRequest(request):
    pathToLink = Path(os.path.abspath(os.path.dirname(__file__)) + settings.STATIC_URL + "pyWebPlayer/muslink")
    music.objects.all().delete()
    dir.objects.all().delete()
    if os.path.exists(pathToLink):
        os.remove(pathToLink)
    os.symlink(pyWebPlayer.settings.MUSIC_LINK, pathToLink)
    updateDB(pyWebPlayer.settings.MUSIC_LINK)
    return HttpResponse("success")

def updateDB(dirName):
    names = os.listdir(dirName)
    for name in names:
        fullname = os.path.join(dirName, name)
        full = Path(settings.STATIC_URL + "pyWebPlayer/muslink" + fullname[len(str(pyWebPlayer.settings.MUSIC_LINK)):])
        if os.path.isdir(fullname):
            dir(fullUrl = full.as_posix(), dirName = full.name, dirPath = full.parents[0].as_posix()).save()
            updateDB(fullname)
        if os.path.isfile(fullname):
            music(fullUrl = full.as_posix(), fileName = full.name, dirPath = full.parents[0].as_posix()).save()
