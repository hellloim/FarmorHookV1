import os
import sys
import requests
import time
import random
from colorama import init, Fore, Back, Style
from threading import Thread

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(Fore.RED + Style.BRIGHT + Back.BLACK + """
""" + Style.RESET_ALL)

def print_info():
    print(Fore.MAGENTA + Style.BRIGHT + "YouTube: " + Fore.CYAN + Style.BRIGHT + "https://www.youtube.com/@farmor." + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "Discord: " + Fore.CYAN + Style.BRIGHT + "farmoronlyfans" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "GitHub: " + Fore.CYAN + Style.BRIGHT + "https://github.com/hellloim" + Style.RESET_ALL)

def print_credits():
    print(Fore.YELLOW + Style.BRIGHT + "Credits to Infamous Koala for the idea of the tool." + Style.RESET_ALL)

def register_webhook(webhook):
    print(Fore.GREEN + Style.BRIGHT + f"Registered the webhook: {webhook}" + Style.RESET_ALL)

def send_message(webhook, message):
    try:
        payload = {'content': message}
        response = requests.post(webhook, json=payload)
        response.raise_for_status()
        print(Fore.GREEN + Style.BRIGHT + "Message sent successfully!" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Error sending message: {e}" + Style.RESET_ALL)

def spam_webhook(webhook, message, count, threads):
    def spam_thread():
        for _ in range(count // threads):
            send_message(webhook, message)

    try:
        thread_list = []
        for _ in range(threads):
            thread = Thread(target=spam_thread)
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()

        print(Fore.GREEN + Style.BRIGHT + "Spam complete!" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.YELLOW + Style.BRIGHT + "\nSpam interrupted." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Error during spam: {e}" + Style.RESET_ALL)

def spam_random_numbers(webhook, count, threads):
    def spam_thread():
        for _ in range(count // threads):
            random_number = random.randint(1, 1000)
            send_message(webhook, str(random_number))

    try:
        thread_list = []
        for _ in range(threads):
            thread = Thread(target=spam_thread)
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()

        print(Fore.GREEN + Style.BRIGHT + "Random number spam complete!" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.YELLOW + Style.BRIGHT + "\nRandom number spam interrupted." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Error during random number spam: {e}" + Style.RESET_ALL)

def get_webhook_info(webhook):
    try:
        response = requests.get(webhook)
        response.raise_for_status()
        print(Fore.CYAN + Style.BRIGHT + "Webhook Info:" + Style.RESET_ALL)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Error getting webhook info: {e}" + Style.RESET_ALL)

def delete_webhook(webhook):
    try:
        response = requests.delete(webhook)
        response.raise_for_status()
        print(Fore.GREEN + Style.BRIGHT + "Webhook deleted." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Error deleting webhook: {e}" + Style.RESET_ALL)

def relaunch():
    python_executable = sys.executable
    script_path = os.path.abspath(__file__)
    os.execl(python_executable, python_executable, script_path)

def main():
    clear_screen()
    print_title()

    print(Fore.YELLOW + Style.BRIGHT + "FarmorHook V1.0 - Hello, Welcome to FarmorHook Version 1.0" + Style.RESET_ALL)
    print_info()
    print_credits()

    webhook = input(Fore.CYAN + Style.BRIGHT + "\n[farmorHOOK] > Enter the Discord webhook URL: " + Style.RESET_ALL)
    register_webhook(webhook)

    while True:
        clear_screen()
        print_title()
        print(Fore.YELLOW + Style.BRIGHT + """
1. Send message to webhook
2. Spam webhook
3. Spam random numbers
4. Get webhook info
5. Delete webhook
6. Relaunch
7. Exit
""" + Style.RESET_ALL)

        webhook_action = input(Fore.CYAN + Style.BRIGHT + "\n[farmorHOOK] > Choose an option: " + Style.RESET_ALL)

        if webhook_action == '1':
            message = input("Enter the message to send: ")
            send_message(webhook, message)
            input("Press Enter to continue...")
        elif webhook_action == '2':
            message = input("Enter the message to spam: ")
            count = int(input("Enter the number of times to spam: "))
            threads = int(input("Enter the number of threads: "))
            spam_webhook(webhook, message, count, threads)
            input("Press Enter to continue...")
        elif webhook_action == '3':
            count = int(input("Enter the number of random numbers to spam: "))
            threads = int(input("Enter the number of threads: "))
            spam_random_numbers(webhook, count, threads)
            input("Press Enter to continue...")
        elif webhook_action == '4':
            get_webhook_info(webhook)
            input("Press Enter to continue...")
        elif webhook_action == '5':
            delete_webhook(webhook)
            time.sleep(2)
            break
        elif webhook_action == '6':
            print(Fore.YELLOW + Style.BRIGHT + "\n[farmorHOOK] > Relaunching..." + Style.RESET_ALL)
            time.sleep(2)
            relaunch()
        elif webhook_action == '7':
            print(Fore.YELLOW + Style.BRIGHT + "\n[farmorHOOK] > Exiting..." + Style.RESET_ALL)
            sys.exit(0)

if __name__ == "__main__":
    main()
