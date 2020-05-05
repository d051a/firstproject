import pymorphy2



def change_word_maturity(string, maturity):
    morph = pymorphy2.MorphAnalyzer()
    out_string = ''
    for word in string.split(' '):
        if word.find('(') != -1:
            tmp_str = '(' + morph.parse(word[1:])[0].inflect({'sing', maturity}).word
        elif word.find(')') != -1:
            tmp_str = morph.parse(word[:-1])[0].inflect({'sing', maturity}).word + ')'
        else:
            tmp_str = morph.parse(word)[0].inflect({'sing', maturity}).word
        out_string += tmp_str + ' '
    return out_string.strip()