from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter(name="placeholder")
def placeholder(value, token):
    """ Add placeholder attribute, esp. for form inputs and textareas """
    value.field.widget.attrs["placeholder"] = token
    return value