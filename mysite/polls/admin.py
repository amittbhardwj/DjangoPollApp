from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_display = ('question', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)
