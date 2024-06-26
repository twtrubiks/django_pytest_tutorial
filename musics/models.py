from django.db import models

class Sheet(models.Model):
    name = models.CharField(default="sheet name", max_length=16)

class Music(models.Model):
    song = models.TextField(default="song")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "music"
