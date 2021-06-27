from django import template

register = template.Library()


@register.simple_tag
def bizz_fuzz(num):
    output = ""
    if num % 3 == 0:
        output += 'Bizz'
    if num % 5 == 0:
        output += 'Fuzz'
    if output == "":
        output += str(num)

    return output


@register.simple_tag
def check_age(age):
    if age > 13:
        return 'allowed'
    else:
        return 'blocked'


@register.simple_tag
def format_date(date):
    return date.strftime("%d/%m/%Y")
