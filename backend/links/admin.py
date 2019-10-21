from django.contrib import admin
from .models import Link
from .models import Label
from .models import Tag
from .models import LinkLabel
from .models import LinkTag


# Register your models here.
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(Label)
admin.site.register(LinkLabel)
admin.site.register(LinkTag)