# Torrent Search Script

A Python script to search for torrents on 1337x, display results with seed/leech count, and fetch magnet links.

## Features
- Search for torrents on 1337x
- Display results in a formatted list with colors
- Fetch and copy magnet links to clipboard
- User-friendly interface with interactive selection

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pyperclip`
  - `termcolor`

Install dependencies using:
```sh
pip install requests beautifulsoup4 pyperclip termcolor
```

## Usage
Run the script:
```sh
python torrent_search.py
```
Enter a search query and select a torrent by number to get its magnet link.

## Example Output
```
Enter search query (or type 'exit' to quit): Deadpool

[1] Deadpool.and.Wolverine.2024.1080p.AMZN.WEBRip.1400MB.DD5.1.x264-GalaxyRG
        Size: 1.4 GB
        Seeds: 5784
        Leeches: 3356

[2] Deadpool 2 (2018) English HDTS- 720p - x264 - AC3 - 2.4GB-TamilRockers
        Size: 2.4 GB
        Seeds: 5780
        Leeches: 1804

Enter the number of the torrent you want: 1

Magnet Link: magnet:?xt=urn:btih:...
Magnet link copied to clipboard!
```

## License
This project is licensed under the MIT License.

