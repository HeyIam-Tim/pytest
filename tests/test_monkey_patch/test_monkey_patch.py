from my_funcs.some_web_client import SomeWebClient


def test_worker(monkeypatch):
    def mock_get_user_last_action_time(*args, **kwargs) -> str:
        return 'Доступ с вашего IP-адреса временно ограничен+ru.avito://1/firewall/captcha/show'

    monkeypatch.setattr('my_funcs.some_web_client.SomeWebClient.get_user_last_action_time', mock_get_user_last_action_time)

    valid_data = {'result': {'message': 'Доступ с вашего IP-адреса временно ограничен', 'link': 'ru.avito://1/firewall/captcha/show'}}
    # responses.add(
    #     method=responses.GET,
    #     url='https://www.avito.ru/web/user/get-status/177068588',
    #     json=valid_data,
    #     status=200,
    # )
    some_web_client = SomeWebClient(url='https://www.avito.ru')
    res = some_web_client.get_user_last_action_time(user_id='177068588')
    c = 1

    assert res == f"{valid_data['result']['message']}+{valid_data['result']['link']}"

