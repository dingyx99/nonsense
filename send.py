import requests, string, random, uuid
from gen import outputTarget

post_url = APP_URL
header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080"}
proxies = {
    'HTTPS': '*.*.*.*:*',
    'HTTP': '*.*.*.*:*'
}

def getSessionID():
    s = requests.session()
    s.get(headers=header, url=LOGIN_URL, proxies=proxies)
    return s

def generate_random_user():
    user_length = random.randint(6,9)
    str_list = [random.choice(string.digits) for i in range(user_length)]
    str_list.insert(0,random.choice("123456789"))
    random_str = ''.join(str_list)
    return random_str

def generate_guid():
    return uuid.uuid4()

if __name__ == "__main__":
    while True:
        username = generate_random_user()
        print("Current Fake Username:",username)
        password = outputTarget()
        print("Current Fake Password:",password)
        params={"u": username, "p": password}
        session = getSessionID()
        session.post(post_url, params, headers=header, proxies=proxies)
        session.close()
