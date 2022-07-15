from django.contrib import admin
from .models import Job, Memo, MemoWriter

admin.site.register(Job)
admin.site.register(Memo)
admin.site.register(MemoWriter)
