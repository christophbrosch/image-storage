from django import template

register = template.Library()

@register.inclusion_tag('images/_image.html', takes_context=False)
def render_image(image):
    return {
        'image': image
    }