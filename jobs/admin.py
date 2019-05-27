from django.contrib import admin

from .models import Job#.models=pika spredaj samo pomeni da gre za isti
# direktorijo v kateri se nahajamo znotraj te datoteke(admin.py).Job je naš
# objekt v models.py(definiran v importu brez končnice)

# funkcija, ki registrira naš model v admin interface
admin.site.register(Job)
