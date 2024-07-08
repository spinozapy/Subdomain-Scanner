# Subdomain Scanner

A powerful Python tool to discover subdomains of a specified domain using common subdomains and random subdomain generation.

## Requirements
- Python 3.x
- `dnspython` library (Install using `pip install dnspython`)
- `colorama` library (Install using `pip install colorama`)

## Installation

1. Clone the repository.
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tool:
    ```bash
    python main.py
    ```

## Usage
1. Choose an option:
    - Type `1` to run the subdomain scanner and enter the domain to discover subdomains.
    - Type `2` to view the list of common subdomains.
    - Type `3` to add new subdomains to the list.

2. Follow the prompts to enter the domain, view results, or add new subdomains. For adding subdomains, type each new subdomain and press Enter. Type `exit` to finish adding.

## Features
- Scans for common subdomains.
- Generates and tests random subdomains.
- Allows users to add custom subdomains.
- Displays found subdomains.

## Example

```bash
Subdomain Scanner
=================

Choose an option (type 'exit' to quit):

1  = Run Subdomain Scanner
2  = List of Common Subdomains
3  = Add Subdomains

root@scanner:~$ 1
[Subdomain Scanner]: Enter the domain: example.com

[Subdomain Scanner]: Subdomain Scan Results
Found Subdomains:
  www.example.com
  mail.example.com
  ftp.example.com
  blog.example.com
  ...

root@scanner:~$ 2

[Subdomain Scanner]: Common Subdomains
Common Subdomains:
  www
  mail
  ftp
  blog
  ...

root@scanner:~$ 3
[Subdomain Scanner]: Enter subdomains to add (type 'exit' to finish adding):
Add Subdomain: newsub1

[Subdomain Scanner]: Added subdomain: newsub1

Add Subdomain: newsub2

[Subdomain Scanner]: Added subdomain: newsub2

Add Subdomain: exit

[Subdomain Scanner]: Subdomain addition finished.

```

## Usage Caution
- For educational or testing purposes only.
- Do not use for malicious activities.
- Follow ethical standards while using this tool.
