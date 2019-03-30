from django.db import models

class music(models.Model):
    fullUrl = models.TextField(default="")
    fileName = models.TextField(default="")
    dirPath = models.TextField(default="")

    def __str__(self):
        return self.fileName

    def getFileName(self):
        return self.fileName

    def getUrl(self):
        return self.fullUrl

    def getDirPath(self):
        return self.dirPath

class dir(models.Model):
    fullUrl = models.TextField(default="")
    dirName = models.TextField(default="")
    dirPath = models.TextField(default="")

    def __str__(self):
        return self.fullUrl

    def getUrl(self):
        return self.fullUrl

    def getDirName(self):
        return self.dirName

    def getDirPath(self):
        return self.dirPath
