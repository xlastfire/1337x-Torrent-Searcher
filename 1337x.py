import requests as req
from bs4 import BeautifulSoup as Soup
import pyperclip
import sys
import os
from termcolor import colored

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_torrents(query):
    """Fetch torrent search results from 1337x."""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    url = f'https://1337x.to/search/{query.replace(" ", "+")}/1/'
    r = req.get(url, headers=headers)
    soup = Soup(r.content, 'html5lib')
    
    torrents_container = soup.find('table', class_='table-list table table-responsive table-striped')
    if not torrents_container:
        print(colored("No torrents found.", "red"))
        return []
    
    torrents = []
    for t in torrents_container.find_all('tr')[1:]:
        try:
            link = 'https://1337x.to' + t.find_all('a')[1]['href']
            title = t.find_all('a')[1].text.strip()
            seeds = t.find('td', class_='coll-2 seeds').text.strip()
            leeches = t.find('td', class_='coll-3 leeches').text.strip()
            
            size_tag = t.find('td', class_='coll-4 size mob-vip') or t.find('td', class_='coll-4 size mob-uploader')
            size = size_tag.text.replace(seeds, '').strip() if size_tag else "Unknown"
            
            torrents.append({
                'title': title,
                'seeds': seeds,
                'leeches': leeches,
                'size': size,
                'link': link
            })
        except Exception:
            continue
    
    return torrents

def display_torrents(torrents):
    """Display the list of torrents in a formatted output."""
    for i, torrent in enumerate(torrents, start=1):
        print(colored(f"[{i}] {torrent['title']}", "cyan"))
        print(colored(f"\tSize: {torrent['size']}", "yellow"))
        print(colored(f"\tSeeds: {torrent['seeds']}", "green"))
        print(colored(f"\tLeeches: {torrent['leeches']}", "red"))
        print()

def get_magnet_link(torrent):
    """Fetch and return the magnet link for the selected torrent."""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    r = req.get(torrent['link'], headers=headers)
    soup = Soup(r.content, 'html5lib')
    for link in soup.find_all('a'):
        if 'magnet:' in link['href']:
            return link['href']
    return None

def main():
    while True:
        clear_console()
        query = input(colored("Enter search query (or type 'exit' to quit): ", "blue")).strip()
        if query.lower() == "exit":
            print(colored("Exiting program...", "red"))
            break
        if not query:
            continue
        
        torrents = fetch_torrents(query)
        if not torrents:
            continue
        
        display_torrents(torrents)
        
        try:
            choice = input(colored("Enter the number of the torrent you want: ", "blue")).strip()
            if choice.lower() == "exit":
                print(colored("Exiting program...", "red"))
                break
            choice = int(choice) - 1
            selected_torrent = torrents[choice]
        except (ValueError, IndexError):
            print(colored("Invalid selection.", "red"))
            continue
        
        magnet_link = get_magnet_link(selected_torrent)
        if magnet_link:
            print(colored("\nMagnet Link:", "green"), magnet_link)
            pyperclip.copy(magnet_link)
            print(colored("Magnet link copied to clipboard!", "yellow"))
        else:
            print(colored("Magnet link not found.", "red"))
        
        input(colored("\nPress Enter to search again or type 'exit' to quit...", "blue"))

if __name__ == "__main__":
    main()
