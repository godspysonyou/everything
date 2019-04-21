def test():
    print('test running')

choice_dic = {
    '1': test
}

while True:
    choice = input('>>: ').strip()
    if not choice or choice not in choice_dic:continue
    choice_dic[choice]()