import re

url = 'twitter.com/sevannradhak'

name = re.search(r'^(?:(?:(?:https|http)://(?:www\.)?)?twitter.com/)?(\w+)(?:/|/?)', url)
# name = re.search(r'^https?://(?:www\.)?twitter\.com/(.+)$', url, re.IGNORECASE)
# print(username.group(5))
if name:
    print(f'Username: ', name.group(1))
# elif username == username.group(2):
#     print(f'Username: {username}')
# elif username == username.group(3):
#     print(f'Username: {username}')
# elif username == username.group(4):
#     print(f'Username: {username}')
# elif username == username.group(5):
#     print(username.group(5))

# username = url.removeprefix('https://twitter.com/')

# print(f'Username: {username}')