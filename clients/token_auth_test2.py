import requests
from pprint import pprint

# {'key': '8919ec10d58b72755883ace271e08638cc5c0a71'}

#! tokensız istek attığımızda sonuç :
#! status Code :  401
#! {'detail': 'Authentication credentials were not provided.'}

def client():
    token = 'Token 8919ec10d58b72755883ace271e08638cc5c0a71'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url="http://127.0.0.1:8000/api/kullanici-profilleri",
        headers = headers,
    )

    print('status Code : ', response.status_code)

    response_data = response.json()
    pprint(response_data)


#!Dosyayı terminalde import etmeden çağırırsak client() ı çalıştırmamak için :
if __name__ == '__main__':
    client()
