"""
Title     : Detect Floating Point Numbers
Subdomain : Regex and Parsing
Domain    : Python
"""

from re import compile, match

pattern = compile("^[-+]?\d*\.\d+$")
for _ in range(int(input())):
    print(bool(pattern.match(input())))
