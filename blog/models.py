from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='blog_images/')
    #uporabljen za spremembo imena objekta v pythonu:
    def __str__(self):
        return self.title
    #okrajšan body ze preview(100 znakov):
    def summary(self):
        return self.body[:100]#vrne prvih 100 znakov
    #popravljena oblika časa za prikaz:
    def pub_date_modded(self):
        return self.pub_date.strftime(' %e. %b  %Y')
