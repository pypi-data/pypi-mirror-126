# TLE Download

A small utility to download TLEs from Space Track.

## Installation

```
pipx install tle-download

# or

pip install tle-download
```

## Command Line Usage

```
export SPACE_TRACK_USERNAME=user@example.com
export SPACE_TRACK_PASSWORD=your-password

# Search by Catalog ID:

tledl catid 40075 36797

# Search by TLE line 0 text

tledl line0 AISSAT LEMUR
```

## All Command Line Options

```
Usage: tledl [OPTIONS] SEARCH_TYPE:{line0|catid} SEARCHES...

Arguments:
  SEARCH_TYPE:{line0|catid}  [required]
  SEARCHES...                [required]

Options:
  --username TEXT       [env var: SPACE_TRACK_USERNAME]
  --password TEXT       [env var: SPACE_TRACK_PASSWORD]
  --outpath FILE        [default: tles.txt]
  --sleep INTEGER       sleep between requests so you don't break API limits
                        [default: 3]
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

## Python Usage

```python
from tle_download import get_tles

tles = get_tles(username, password, 'line0', ['AISSAT', 'LEMUR'])
```
