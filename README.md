# ouiSearch
Search vendor info by using the complete or OUI part of mac addresses.

## Usage
- Search: python ouiSearch.py MAC_ADDRESS | MAC_OUI
- Update or download the OUI file: python ouiSearch.py --update
### Examples
    python ouiSearch.py --update // Download or update the oui file 
    python ouiSearch.py 1111:2222:3333
    python ouiSearch.py 11:22:22:33:33
    python ouiSearch.py 1111-2222-3333
    python ouiSearch.py 11-11-22-22-33-33
    python ouiSearch.py 111122223333
    python ouiSearch.py 111122