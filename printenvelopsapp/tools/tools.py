from printenvelopsapp.models import SentEnvelop


def get_clear_address(address):
    clear_address = address.split(',')
    return str(clear_address[0])


def add_num_before_text(text):
    text_with_num = '№ {}'.format(text)
    return text_with_num


def set_sent_cost(weight_cost, sent):
    try:
        price = weight_cost * sent.weight
        sent.cost = price
    except:
        sent.cost = 0
    sent.save()


def sum_envelops_cost(elems):
    cost = [envelop.cost for envelop in elems]
    return sum(cost)


