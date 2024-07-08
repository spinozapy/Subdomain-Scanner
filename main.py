import dns.resolver
import os
import colorama
import random
import string
from datetime import datetime

colorama.init()
clear_command = "cls" if os.name == "nt" else "clear"

def clear_screen():
    os.system(clear_command)

def print_info(title, info):
    print(colorama.Fore.GREEN + f"[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"{title}")
    print("")
    for key, value in info.items():
        if isinstance(value, list):
            print(colorama.Fore.YELLOW + f"{key}:")
            for item in value:
                print(colorama.Fore.LIGHTWHITE_EX + f"  {item}")
        else:
            print(colorama.Fore.YELLOW + f"{key}: " + colorama.Fore.LIGHTWHITE_EX + f"{value}")
    print("")

subdomains = [
    "www", "mail", "ftp", "blog", "shop", "dev", "api", "admin", "test", "webmail", 
    "support", "login", "secure", "portal", "docs", "news", "app", "store", "forum", 
    "manager", "server", "smtp", "backup", "vpn", "inbox", "m", "mta", "ns", "status", 
    "billing", "chat", "contact", "my", "products", "prod", "help", "downloads", "updates", 
    "tickets", "calendar", "api", "cloud", "push", "mailserver", "wiki", "staging", "dev", 
    "test", "research", "archive", "docs", "home", "beta", "support", "static", "media", 
    "web", "user", "employee", "partner", "developer", "integration", "portal", "platform", 
    "app", "connect", "members", "private", "public", "sys", "status", "log", "admin", 
    "my", "sandbox", "support", "search", "contact", "event", "newsletter", "team", 
    "notifications", "internal", "external", "mail", "blog", "news", "community", 
    "resources", "files", "store", "account", "sign", "auth", "admin", "profile", 
    "main", "secure", "api", "user", "docs", "management", "identity", "accounts", 
    "platform", "service", "support", "client", "feedback", "app", "sandbox"
]

def generate_random_subdomains(domain, count=10):
    random_subdomains = []
    for _ in range(count):
        random_sub = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        subdomain = f'{random_sub}.{domain}'
        random_subdomains.append(subdomain)
    return random_subdomains

def subdomain_scanner(domain, subdomains):
    found_subdomains = []
    for sub in subdomains:
        subdomain = f'{sub}.{domain}'
        try:
            dns.resolver.resolve(subdomain, 'A')
            found_subdomains.append(subdomain)
        except:
            pass
    
    random_subdomains = generate_random_subdomains(domain)
    for subdomain in random_subdomains:
        try:
            dns.resolver.resolve(subdomain, 'A')
            found_subdomains.append(subdomain)
        except:
            pass

    return {"Found Subdomains": list(set(found_subdomains))}

def add_subdomains():
    global subdomains
    print(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter subdomains to add (type 'exit' to finish adding):")
    while True:
        new_subdomain = input(colorama.Fore.MAGENTA + "Add Subdomain: " + colorama.Fore.WHITE).strip()
        if new_subdomain.lower() == 'exit':
            break
        elif new_subdomain:
            subdomains.append(new_subdomain)
            print(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"Added subdomain:" + colorama.Fore.WHITE + f" {new_subdomain}")
        else:
            print(colorama.Fore.RED + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "No subdomain entered. Please try again.")
    print(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Subdomain addition finished.")

def main():
    while True:
        clear_screen()
        print(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Choose an option (type 'exit' to quit):")
        print("")
        print(colorama.Fore.YELLOW + "1 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Run Subdomain Scanner")
        print(colorama.Fore.YELLOW + "2 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "List of Common Subdomains")
        print(colorama.Fore.YELLOW + "3 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Add Subdomains")
        print("")

        choice = input(colorama.Fore.MAGENTA + "root@you~$ " + colorama.Fore.WHITE).strip()

        if choice == '1':
            domain = input(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the domain: " + colorama.Fore.WHITE).strip()
            info = subdomain_scanner(domain, subdomains)
            print_info("Subdomain Scan Results", info)
        elif choice == '2':
            print_info("Common Subdomains", {"Common Subdomains": subdomains})
        elif choice == '3':
            add_subdomains()
        elif choice.lower() == 'exit':
            break
        else:
            print(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.RED + "Invalid choice, please try again.")
        
        input(colorama.Fore.GREEN + "[Subdomain Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")

if __name__ == "__main__":
    main()
