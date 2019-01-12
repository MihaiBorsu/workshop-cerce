from django.contrib import admin

# Register your models here.
from vote.models import Vote, VoteTopic

admin.site.register(Vote)
admin.site.register(VoteTopic)