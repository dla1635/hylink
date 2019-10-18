from django.contrib import admin
from .models import Link
from .models import Label
from .models import Tag
from .models import LinkLabelJoin
from .models import LinkTagJoin


# Register your models here.
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(Label)
admin.site.register(LinkLabelJoin)
admin.site.register(LinkTagJoin)