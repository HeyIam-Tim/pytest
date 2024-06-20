import requests
from typing import  Union


class SomeWebClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def __user_get_status(self, user_id: str) -> dict[str, Union[str, dict]]:
        url = f'{self.url}/web/user/get-status/{user_id}'
        res = requests.get(url=url)
        json_data = res.json()
        return json_data

    def get_user_last_action_time(self, user_id: str) -> str:
        json_data = self.__user_get_status(user_id=user_id)
        message = json_data['result']['message']
        link = json_data['result']['link']
        return f'{message}+{link}'

#
# some_web_client = SomeWebClient(url='https://www.avito.ru')
# print(some_web_client.get_user_last_action_time(user_id=177068588))
