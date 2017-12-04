from django.contrib import admin

from .models import G1File, G1FileField, G1PostingType, G1FileUploadErrorMessage

class G1FileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': ['filename']}
        ),
    ]
    list_display = ('filename', )
    search_fields = ['filename']
 
admin.site.register(G1File, G1FileAdmin);


class G1FileFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': ['filename', 'ftype', 'index', 'desc', 'vdf', 'struct', 'pos', 'comments']}
        ),
    ]
    list_display = ('filename', 'ftype', 'index', 'desc', 'vdf', 'struct', 'pos', 'comments')
    search_fields = ['filename__filename']

    def get_ordering(self, request):
        return ['ftype', 'index']

 
admin.site.register(G1FileField, G1FileFieldAdmin);


class G1PostingTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,					{'fields': ['posting_type', 'bl', 'description']}),
    ]
    list_display = ('posting_type', 'bl', 'description')
    search_fields = ['posting type', 'bl', 'description']

admin.site.register(G1PostingType, G1PostingTypeAdmin);


class G1FileUploadErrorMessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,					{'fields': ['filename', 'code', 'posted', 'description']}),
    ]
    list_display = ('filename', 'code', 'posted', 'description')
    search_fields = ['filename__filename', 'code', 'posted', 'description']

admin.site.register(G1FileUploadErrorMessage, G1FileUploadErrorMessageAdmin);
