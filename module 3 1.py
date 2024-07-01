calls=0

def count_call():
    global calls
    calls = calls  + 1

def string_info(string):
    stringinfo = (len(string), string.upper(), string.lower())
    print(stringinfo)
    count_call()

def is_contains(list,list_to_search):
    f = False
    print(list, list_to_search)
    for i in range(len(list_to_search)):
            if list.upper() == list_to_search[i].upper():
                f = True
                break
    print(f)
    count_call()

string_info('PiramIda')
string_info('Я люблю свою работу')
is_contains('Я люблю',['я люблю свою работу','я приду сюда в субботу','и конечно в воскресенье'])
is_contains('Anton',['Denis','anTon','Dasha'])
is_contains('Dasha',['Olga','Sveta','Danil'])
is_contains('1',['2','4','6','9','1'])
print('Количество вызываемых функций:',calls)