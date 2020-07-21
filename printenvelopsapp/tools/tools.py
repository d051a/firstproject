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
    cost = []
    for envelop in elems:
        envelop_cost = envelop.cost
        if envelop_cost == None:
            envelop_cost = 0
        cost.append(envelop_cost)
    return sum(cost)


def change_neuter_gender_text(string):
    neuter_gender_text = string
    if 'один' in neuter_gender_text:
        outer_string = neuter_gender_text.replace('один', 'одно')
        return outer_string
    return neuter_gender_text


def without_commas(string):
    outer_nums = string
    outer_nums = outer_nums.replace(',', '')
    outer_nums = outer_nums.replace(';', '')
    return outer_nums
