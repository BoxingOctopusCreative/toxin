# Toxin

Toxin is an LFI (Local File Inclusion) Exploitation Tool

## Installation

`$ python setup.py install`

## Usage

```bash
Usage: toxin [OPTIONS]

  Toxin: Local File Inclusion Exploitation Tool

Options:
  -t, --app_type TEXT   Application Type
  -u, --url TEXT        URL to query
  -p, --parameter TEXT  Parameter to inject into User-Agent header
  -c, --command TEXT    Command to Run
  -m, --mode TEXT       Mode (Inject or Exploit)
  -g, --paged           Paged Output
  --help                Show this message and exit.
```