import requests

from django.http import HttpResponse


def index(request):
    usd = requests.get("https://api.coinmarketcap.com/v2/ticker/1/?convert=EUR").json()['data']['quotes']['USD']['price']
    return HttpResponse("1 BTC = %.2f USD" % usd)
