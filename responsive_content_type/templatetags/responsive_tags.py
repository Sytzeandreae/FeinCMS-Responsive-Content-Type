from django import template
from django.template.loader import render_to_string

from feincms.templatetags.feincms_tags import _render_content


register = template.Library()


def _responsive_render_content(content, **kwargs):
    r = _render_content(content, **kwargs)
    return render_to_string('responsive/wrapper.html', {
        'r': r,
        'large': content.large,
        'medium': content.medium,
        'small': content.small
    })


@register.simple_tag(takes_context=True)
def render_responsive_region(context, feincms_object, region, request=None):
    i = [i.large if i.large else i.medium if i.medium else i.small for i in getattr(feincms_object.content, region)]
    n = []
    u = 1
    while len(i) > 0:
        if sum(i[:u]) > 12:
            n.append(i[:u-1]) if len(i[:u]) > 1 else i[:u]
            i = i[u-1:] if len(i[:u]) > 1 else i[u:]
            u = 0
        elif sum(i) <= 12:
            n.append(i)
            i = []
        u += 1

    content_items = getattr(feincms_object.content, region)
    occur = 0
    content = []
    for container in n:
        r = ''
        for l in container:
            r += _responsive_render_content(content_items[occur], request=request, context=context)
            occur += 1
        content.append(r)

    return render_to_string('responsive/row.html', {'content': content})