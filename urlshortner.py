import random
import string
import webbrowser

url_mapping = {}

def shorten_url(url):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    url_mapping[short_url] = url
    return short_url

def expand_url(short_url):
    return url_mapping.get(short_url, "Short URL not found.")

def open_short_url(short_url):
    long_url = expand_url(short_url)
    if long_url != "Short URL not found.":
        webbrowser.open(long_url)
    else:
        print("Short URL not found.")

while True:
    print("\n1. Shorten URL")
    print("2. Expand URL")
    print("3. Open Short URL")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        long_url = input("Enter the long URL: ")
        short_url = shorten_url(long_url)
        print("Shortened URL:", short_url)
    elif choice == '2':
        short_url = input("Enter the short URL: ")
        long_url = expand_url(short_url)
        print("Expanded URL:", long_url)
    elif choice == '3':
        short_url = input("Enter the short URL to open: ")
        open_short_url(short_url)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
