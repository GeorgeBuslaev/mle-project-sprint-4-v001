import requests

#Задаем параметры для доступа к сервису
recommendation_service_url = "http://127.0.0.1:8000"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

#Рекомендации для холодныйх пользователей без онлайн активности
params = {"user_id": 1234567890, 'k': 10}
print('***********************************************')
print(f"Cold user {params['user_id']} recommendation:")
print(f"requests code: {params}")
resp = requests.post(recommendation_service_url + "/recommendations_offline", headers=headers, params=params)
if resp.status_code == 200:
    recs = resp.json()
else:
    recs = []
    print(f"status code: {resp.status_code}")
print(f"recommendation: {recs['recs']}")

#Рекомендации для холодныйх пользователей, по последнему выбранному товару
params = {"item_id": 59206785}
print('***********************************************')
print(f"Cold user with item {params['item_id']} recommendation:")
print(f"requests code: {params}")
resp = requests.post(recommendation_service_url +"/similar_items", headers=headers, params=params)
if resp.status_code == 200:
    similar_items = resp.json()
else:
    similar_items = None
    print(f"status code: {resp.status_code}")
print(f"recommendation: {similar_items['item_id_2']}")

#Рекомендации для пользователя с персональными рекомендациями, но без онлайн-истории
params = {"user_id": 1374571, 'k': 10}
print('***********************************************')
print(f"User {params['user_id']} personal recommendation:")
print(f"requests code: {params}")
resp = requests.post(recommendation_service_url + "/recommendations_offline", headers=headers, params=params)
if resp.status_code == 200:
    recs = resp.json()
else:
    recs = []
    print(f"status code: {resp.status_code}")
print(f"recommendation: {recs['recs']}")

#Рекомендации для пользователя с персональными рекомендациями и онлайн-историей
#Передаем данные о последней активности пользователя - формируем онлайн-историю
print('***********************************************')
print(f"User {params['user_id']} with online activity personal recommendation:")
user_id = 1374571
event_item_ids = [59206785, 56822013, 40813255, 482397, 71542594, 1444979, 19178160, 17368498, 1132410, 444542]

for event_item_id in event_item_ids:
    resp = requests.post(recommendation_service_url + "/put", 
                         headers=headers, 
                         params={"user_id": user_id, "item_id": event_item_id})
                         
params = {"user_id": user_id, 'k': 10}
print(f"requests code: {params}")

resp = requests.post(recommendation_service_url + "/recommendations", headers=headers, params=params)
if resp.status_code == 200:
    recs = resp.json()
else:
    recs = []
    print(f"status code: {resp.status_code}")
    
print(f"Blended recommendation: {recs['recs']}")



