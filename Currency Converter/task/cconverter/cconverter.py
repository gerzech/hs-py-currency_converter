import requests

def cconverter(currency):
    currency = currency.lower()
    cur_cache = {}
    url = f"http://www.floatrates.com/daily/{currency}.json"
    response = requests.get(url).json()
    if currency != "usd":
        cur_cache["usd"] = response["usd"]["rate"]
    if currency != "eur":
        cur_cache["eur"] = response["eur"]["rate"]
    while True:
        ex_cur = input().lower()
        if ex_cur == "": break
        money = float(input())
        print("Checking the cache...")
        if ex_cur in cur_cache:
            print("Oh! It is in the cache!")
            print(f"You received {round(cur_cache[ex_cur] * money, 2)} {ex_cur.upper()}.")
        else:
            cur_cache[ex_cur] = response[ex_cur]["rate"]
            print("Sorry, but it is not in the cache!")
            print(f"You received {round(cur_cache[ex_cur] * money, 2)} {ex_cur.upper()}.")




cconverter(input())