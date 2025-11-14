import os
import sys
import time
import json
import requests
import webbrowser
import threading
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import track
from rich import print_json as js

console = Console()

# === আপনার চ্যানেল লিংক ===
TELEGRAM_CHANNEL = "https://t.me/infinityerror2"

# === চ্যানেল ওপেন করার ফাংশন (ব্যাকগ্রাউন্ডে) ===
def auto_open_channel():
    time.sleep(1)  # 1 সেকেন্ড পর ওপেন হবে
    webbrowser.open(TELEGRAM_CHANNEL)

# === লোগো ===
def show_logo():
    logo = """
[bold red]╔════════════════════════════════════════════════════╗
║                                                    ║
║  [bold cyan]██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗[/bold cyan]   ║
║  [bold cyan]██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝[/bold cyan]   ║
║  [bold cyan]██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║   [/bold cyan]   ║
║  [bold cyan]██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║   [/bold cyan]   ║
║  [bold cyan]██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║   [/bold cyan]   ║
║  [bold cyan]╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   [/bold cyan]   ║
║                                                    ║
║        [bold magenta]iNFiNiTY WSATSAPP REPORT[/bold magenta]           ║
║        [dim cyan]Powered by @infinityerror2 | v2.2[/dim cyan]        ║
╚════════════════════════════════════════════════════╝[/bold red]
    """
    console.print(Panel(logo, style="bold red", expand=False))
    print("[bold yellow]           ⚡ Unlimited WhatsApp Reporting ⚡[/]\n")

# === মেইন ফাংশন ===
def lmnx9():
    os.system("clear" if os.name == "posix" else "cls")
    show_logo()

    # === টুলস রান হওয়া মাত্রই চ্যানেল ওপেন (থ্রেডে) ===
    threading.Thread(target=auto_open_channel, daemon=True).start()

    number = console.input(" [bold green]TARGET NUMBER :: [/]").strip()
    if not number:
        print("[bold cyan][*] Opening @infinityerror2...[/]")
        webbrowser.open(TELEGRAM_CHANNEL)
        time.sleep(2)
        number = console.input(" [bold green]TARGET NUMBER :: [/]").strip()

    if not number.isdigit() or len(number) < 10:
        print("[bold red][!] Invalid number! Use 10+ digits.[/]")
        time.sleep(2)
        return lmnx9()

    while True:
        amt_input = console.input(" [bold green]REPORT AMOUNT :: [/]").strip()
        if not amt_input:
            print("[bold cyan][*] Opening @infinityerror2...[/]")
            webbrowser.open(TELEGRAM_CHANNEL)
            time.sleep(2)
            continue
        if amt_input.isdigit() and int(amt_input) > 0:
            amount = int(amt_input)
            break
        else:
            print("[bold red][!] Enter a valid number![/]")

    print(f"\n[bold cyan][*] Sending {amount} report(s) to [white]{number}[/]...[/]\n")
    time.sleep(1.5)

    success = 0
    failed = 0

    for _ in track(range(amount), description="[bold magenta]Reporting...[/]"):
        api = f"https://lmnx9.appletolha.com/wp/report.php?number={number}"
        try:
            response = requests.post(api, timeout=12)
            if response.status_code == 200:
                try:
                    data = response.json()
                    data.pop("developer", None)
                    data.pop("channel", None)
                    js(data=data)
                    success += 1
                except json.JSONDecodeError:
                    console.print(f"[dim]Response:[/] {response.text}")
                    success += 1
            else:
                console.print(f"[red][!] HTTP {response.status_code}[/]")
                failed += 1
        except requests.RequestException as e:
            console.print(f"[red][!] Network Error: {e}[/]")
            failed += 1
        time.sleep(0.8)

    # === ফাইনাল সামারি ===
    print("\n" + "═" * 56)
    console.print(
        Panel(
            f"[bold green]SUCCESS: {success}[/]  |  [bold red]FAILED: {failed}[/]\n"
            f"[bold white]TARGET:[/] {number}\n"
            f"[bold cyan]TOOL:[/] iNFiNiTY WSATSAPP REPORT v2.2\n"
            f"[bold yellow]Join Now: [link={TELEGRAM_CHANNEL}]@infinityerror2[/][/] ✨",
            title="REPORT SUMMARY",
            style="bold blue"
        )
    )
    print("[bold magenta]iNFiNiTY Mission Complete![/]\n")

    # === রিস্টার্ট ===
    restart = console.input("[bold yellow][?] Run again? (y/n): [/]").strip().lower()
    if restart == 'y':
        lmnx9()
    else:
        print("[bold cyan]Thanks for using iNFiNiTY![/]")
        print(f"[bold yellow]Join: @infinityerror2[/]")
        sys.exit(0)

# === রান ===
if __name__ == '__main__':
    try:
        lmnx9()
    except KeyboardInterrupt:
        print("\n\n[bold red][!] Stopped by user. Exiting...[/]")
        sys.exit(0)