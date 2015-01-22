from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string


class ResponsiveContentType(models.Model):
    small = models.IntegerField(
        _('Small'),
        max_length=10,
        choices=[(i, 'small-%d' % i) for i in xrange(1, 13)],
        help_text=_('Number of columns on a small screen')
    )
    medium = models.IntegerField(
        _('Medium'),
        max_length=10,
        choices=[(i, 'medium-%d' % i) for i in xrange(1, 13)],
        help_text=_('Number of columns on a medium screen')
    )
    large = models.IntegerField(
        _('Large'),
        max_length=10,
        choices=[(i, 'large-%d' % i) for i in xrange(1, 13)],
        help_text=_('Number of columns on a large screen')
    )

    def render(self, **kwargs):
        """Render this model to a string for templating

        Keyword arguments:
        content -- the content
        request -- the django request
        """
        name = self.__class__.__name__.lower().split('_')[-1]
        return render_to_string(
            'content/%s.html' % name,
            {
                'content': self,
                'request': kwargs.get('request'),
            }
        )

    class Meta:
        abstract = True
