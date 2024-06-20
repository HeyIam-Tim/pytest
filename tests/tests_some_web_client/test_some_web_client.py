import pytest

from my_funcs.some_web_client import SomeWebClient
import responses


@responses.activate
def test_some_web_client():
    valid_data = {'result': {'message': 'Доступ с вашего IP-адреса временно ограничен', 'link': 'ru.avito://1/firewall/captcha/show'}}
    responses.add(
        method=responses.GET,
        url='https://www.avito.ru/web/user/get-status/177068588',
        json=valid_data,
        status=200,
    )
    some_web_client = SomeWebClient(url='https://www.avito.ru')
    res = some_web_client.get_user_last_action_time(user_id='177068588')
    c = 1

    assert res == f"{valid_data['result']['message']}+{valid_data['result']['link']}"


@responses.activate
def test_some_web_client_with_error():
    valid_data = {'result1': 'Not Found'}
    responses.add(
        method=responses.GET,
        url='https://www.avito.ru/web/user/get-status/177068588-',
        json=valid_data,
        status=404,
    )
    with pytest.raises(KeyError):
        some_web_client = SomeWebClient(url='https://www.avito.ru')
        res = some_web_client.get_user_last_action_time(user_id='177068588-')
    c = 1

    # assert res == f"{valid_data['result']['message']}+{valid_data['result']['link']}"
