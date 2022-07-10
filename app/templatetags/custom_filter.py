from django import template
from app.models.Share import Share
register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def price_total(number1,number2):
    return number1 * number2

@register.filter(name='get_share')
def get_share(transaction_id,user_id):
    share=Share.get_Share_by_transaction_id_user(transaction_id,user_id)
    share=share.percent
    return str(share)+" %"