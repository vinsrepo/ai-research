arrBad = ['dm','thằng chó','chết tiệt','đéo','địt mẹ','hãm','cặc','óc chó','cứt','hãm lol',"hãm chó","cu","chịch","hãm cứt"]


def profanityFilter(text):
    text = text.lower()
    brokenStr1 = text.split()
    badWordMask = '***********************'
    for i in range(len(brokenStr1)-1):
        two_word  = brokenStr1[i] + " " +brokenStr1[i + 1]
        if brokenStr1[i] in arrBad:
            print(brokenStr1[i] + '--> Bad word!')
            text = text.replace(brokenStr1[i],badWordMask[:len(brokenStr1[i])])
        elif two_word in arrBad:
            print(two_word + '--> bad word!')
            text = text.replace(two_word,badWordMask[:len(two_word)])
    return text

print(profanityFilter('thằng chó kia'))

