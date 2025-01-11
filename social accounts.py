import requests
import time

# Define your Bearer Token (Twitter API v2 credential)


# 获取单个用户名的粉丝数
def fetch_follower_count(username):
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=public_metrics"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        followers_count = user_data['data']['public_metrics']['followers_count']
        return username, followers_count
    elif response.status_code == 429:
        reset_time = int(response.headers.get("X-Rate-Limit-Reset", time.time() + 60))
        wait_time = max(0, reset_time - time.time())
        print(f"Rate limit exceeded, waiting for {wait_time} seconds...")
        time.sleep(wait_time)
        return fetch_follower_count(username)
    else:
        print(f"Error fetching data for {username}: {response.status_code} - {response.text}")
        return username, None

# 批量处理用户名，减少批次大小并增加延迟
def get_followers_in_batches(usernames, batch_size=5, delay_between_requests=10):
    for i in range(0, len(usernames), batch_size):
        batch = usernames[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1}: {batch}")
        for username in batch:
            username, followers_count = fetch_follower_count(username)
            if followers_count is not None:
                print(f"{username} has {followers_count} followers.")
            else:
                print(f"Failed to fetch followers count for {username}.")
            time.sleep(delay_between_requests)
# Twitter usernames list
usernames = ['UNSriLanka', 'UNThailand', 'UNTimorLeste', 'uninvietnam', 'UN_Albania', 'UNArmenia', 
             'UNinAzerbaijan', 'UNBelarus', 'UN_BiH', 'ungeorgia', 'uninkazakhstan', 'UN_Kosovo', 
             'un_kyrgyzstan', 'UNMoldova', 'UN_Montenegro', '1UN_MK', 'UNSerbia', 'UNinTajikistan', 
             'UN_Turkiye', 'UN_Turkmenistan', 'UN_Ukraine', 'un_uzbekistan', 'ONUArgentina', 
             'UNBdosandOECS', 'unitednationsbz', 'ONUBolivia', 'ONUBrasil', 'ONUChile', 'onucolombia', 
             'UNCOSTARICA', 'ONU_Cuba', 'ONU_RD', 'ONUecuador', 'ONUElSalvador', 'ONUGuatemala', 
             'UNGuyana', 'UNHaiti', 'ONUHonduras', 'UNJamaica', 'ONUMX', 'ONUPanama', 'ONUParaguay', 
             'ONUPeru', 'UNSuriname', 'UN_TandT', 'ONUUruguay', 'onuvenezuela', 'CaribbeanUN', 
             'UN_Caribbean', 'UNinMicronesia', 'UNALGERIA', 'UNBenin', 'UN_Botswana', 'onubf', 
             'UN_Burundi', 'UNCaboVerde', 'UN_Cameroon', 'RcaUnct', 'OnuTchad', 'ONU_Comores', 
             'UN_Congo', 'UNDjibouti', 'UNEgypt', 'UNinEritrea', 'UNERITREA', 'UNEswatini', 
             'UNEthiopia', 'OnuGabon', 'UNinGhana', 'OnuGuinee', 'UNGuinea_Bissau', 'unkenya', 
             'UNLesotho', 'UN_Liberia', 'UNinLibya', 'UNMadagascar', 'UNMalawi', 'OnuMauritanie', 
             'UN_Mauritius', 'ONUMaroc', 'ONUMocambique', 'UNNamibia', 'SNU_Niger', 'UN_Nigeria', 
             'UNRwanda', 'NacoesS', 'ONU_STP', 'OnuSenegal', 'UN_Seychelles', 'UNinSeychelles', 
             'UNSierraLeone', 'UNinSomalia', 'UNinSouthAfrica', 'UN_SouthSudan', 'UN_Sudan', 
             'UNGambia', 'UN_Togo', 'NuTunisie', 'UNinUganda', 'UnitedNationsTZ', 'UNZambia', 
             'UNZimbabwe', 'UN_Bahrain', 'UNIraq', 'UnitedNationsJO', 'UNinKuwait', 'UN_Lebanon', 
             'UNinPalestine', 'UN_SaudiArabia', 'UNinSyria', 'UN_UAE']



# 按批次处理用户名'unbhutan', 'UNinIndia','UNinIndonesia','UN_Iran','UNinLaoPDR','UNinLaoPDR','UNinMalaysia',
            # 批量处理用户名，减少批次大小并增加延迟
def get_followers_in_batches(usernames, batch_size=5, delay_between_requests=10):
    for i in range(0, len(usernames), batch_size):
        batch = usernames[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1}: {batch}")
        for username in batch:
            username, followers_count = fetch_follower_count(username)
            if followers_count is not None:
                print(f"{username} has {followers_count} followers.")
            else:
                print(f"Failed to fetch followers count for {username}.")
            time.sleep(delay_between_requests)
get_followers_in_batches(usernames)
