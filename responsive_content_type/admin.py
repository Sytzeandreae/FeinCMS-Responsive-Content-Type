from django.conf import settings
from django.contrib import admin

from feincms.module.page.models import Page
from feincms.module.page.modeladmins import PageAdmin


class ResponsivePageAdmin(PageAdmin):
    class Media:
        js = [
            'responsive_content_type/js/jquery-1.10.2.min.js',
            'responsive_content_type/js/responsive_editor.js',
        ]
        static_url = getattr(settings, 'STATIC_URL', '/static')
        css = {
            'all': (
                static_url + 'responsive_content_type/css/foundation.css',
            )
        }

# Clear all page extensions
Page._extensions = []
admin.site.unregister(Page)

# Add the extensions again
admin.site.register(Page, ResponsivePageAdmin)


# We want the same kind of responsive administration interface
# for the elephantblog admin, so if it is installed, create a new admin for it
if 'elephantblog' in settings.INSTALLED_APPS:
    from elephantblog.models import Entry
    from elephantblog.admin import EntryAdmin

    class ResponsiveEntryAdmin(EntryAdmin):
        class Media:
            js = [
                'responsive_content_type/js/jquery-1.10.2.min.js',
                'responsive_content_type/js/responsive_editor.js',
            ]
            static_url = getattr(settings, 'STATIC_URL', '/static')
            css = {
                'all': (
                    static_url +
                    'responsive_content_type/css/foundation.min.css',
                )
            }

    Entry._extensions = []
    admin.site.unregister(Entry)
    admin.site.register(Entry, ResponsiveEntryAdmin)
