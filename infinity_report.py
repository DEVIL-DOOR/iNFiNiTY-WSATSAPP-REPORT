import os,sys,time,json,rich,requests
from rich import print
from rich import print_json as js

def lmnx9():
    os.system("clear")
    print("[bold][green]\n ->> WP REPORT - MR.SHUVO")
    number = input(" ->> ENTER NUMBER :: ").strip()
    try:
        amount = input(" ->> ENTER AMOUNT :: ").strip()
    except ValueError:
        lmnx9()
    if number:
        for x in range(int(amount)):
            api = f"https://lmnx9.appletolha.com/wp/report.php?number={number}"
            try:
                lmn = requests.post(api).json()
                js(data=lmn)
            except:pass
        print(45*"-")
        print(f"[bold][violet] ->> MR.SHUVO WP REPORT DONE {amount}")
    else:
        return false

if __name__ in '__main__':
    lmnx9()