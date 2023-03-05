# discogs-collector
Uses Discogs-API to collect information from your collection on Discogs.

## Installation

```sh
pip install -r packages.txt
```

```sh
python main.py
```

## Usage

Input: Discogs Token

Output: csv of all your tracks from your whole collection with following data

- Id
- Title
- Artist
- Comment ("Vinyl")
- Duration (millisec)
- Genre
- Track
- Year
- Album
- Label

Need to check / to do: 
- Date downloaded/created
- Date added
- Language
- Century
- Subgenre
- Discnumber
- Catalog
- Labelcode
- Date
- Media