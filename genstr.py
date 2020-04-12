import string, random
billyDict=[
    'ass','we','can','herrington','billy','deep','dark','fantasy','like','embarrassing','me','huh','shinnippori','fu@k','faq','woo','musuko','mara','muscles','gachimuchi','shoulder','danny','target','down','biollante','lether','gym','horny','tongue','around','slaves','b1tch'
]
replaceChar={
    'C':'@','I':'l','O':'0','S':'5','X':'*','c':'@','l':'I','o':'0','s':'5','1':'I','5':'S','9':'g'
}

def genRandStr():
    length = random.randint(10,25)
    str_list = [random.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(length)]
    random_str = ''.join(str_list)
    return random_str

def genRandChar():
    return random.choice(string.digits)

def genStrFromDict():
    times = random.randint(2,4)
    str_list = random.sample(billyDict, times)
    for i in range(len(str_list)):
        if i == 0:
            str_list.insert(i+1, genRandChar())
        else:
            str_list.insert(i+i, genRandChar())
    random_str = ''.join(str_list)
    return random_str

def genChoice():
    return random.randint(0,1)

def randRepChar(src):
    target = src
    length = len(target)
    for i in range(length):
        choice = genChoice()
        if choice == 1:
            if target[i] in replaceChar:
                target = target[:i] + replaceChar[target[i]] + target[i+1:]
            else :
                pass
        else:
            sec_choice = genChoice()
            if sec_choice == 1:
                target = target[:i] + target[i].swapcase() + target[i+1:]
            else:
                pass
    return target

def outputTarget():
    len = random.randint(12,16)
    return randRepChar(genStrFromDict())[:len]
