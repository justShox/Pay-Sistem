from fastapi import APIRouter
import requests

currency_router = APIRouter(prefix='/currency', tags=['Для работы с курсом валют'])


# Запрос на получения нужны курсов валют
@currency_router.post("/get-rates")
async def get_currency_rates():
    nbu_url = 'https://nbu.uz/uz/exchange-rates/json/'
    usd = requests.get(nbu_url).json()[-1]['nbu_buy_price']
    rub = requests.get(nbu_url).json()[-6]['nbu_buy_price']
    eur = requests.get(nbu_url).json()[7]['nbu_buy_price']
    return {'USD': usd, 'RUB': rub, 'EUR': eur}
