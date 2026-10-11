import re

url = input("URL: ").strip()

# username = url.removeprefix("https://x.com/")
# print(f"Username: {username}") 

# re.sub(pattern, repl, string, count, flags=0)
# \. because . can be any character
# http or https == (http|https) == https?
# (www\.)? that the www. can be there or not 
# u can nest the ? in of another parenthesis
### username = re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
### print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?x\.com/([a-z0-9_]+)$", url, re.IGNORECASE): 
    print(f"Username:", matches.group(1))


# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)