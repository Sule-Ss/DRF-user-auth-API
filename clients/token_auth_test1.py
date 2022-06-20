import requests
from pprint import pprint

# {'key': '8919ec10d58b72755883ace271e08638cc5c0a71'}

def client():
    credentials ={
        'username' :'yeniUser',
        'password' : 'test123..',
    }

    response = requests.post(
        url = "http://127.0.0.1:8000/api/dj-rest-auth/login/",
        data = credentials,       
    )

    print('status Code : ', response.status_code)

    response_data = response.json()
    pprint(response_data)

#!Dosyayı terminalde import etmeden çağırırsak client() ı çalıştırmamak için :
if __name__ == '__main__':
    client()