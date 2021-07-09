n_list = ['popooqoq','bvdobvd','banana']
mirror_dict = {'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o',
'p':'q','q':'p','s':'z','z':'s','u':'u','v':'v','w':'w','x':'x'}

for word in n_list:
    tmp = list(word)
    print(tmp)
    mirror_word = ''
    for ch in tmp[::-1]:
        print(ch)
        if ch in mirror_dict:
            mirror_word += mirror_dict[ch]
            print(mirror_word)
        else:
            break