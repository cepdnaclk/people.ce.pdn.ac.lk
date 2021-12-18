# get all users from FEeLS
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import requests
from urllib.parse import urlparse

fileOpened = open("output.txt", "w")
s = requests.Session()
url = 'https://feels.pdn.ac.lk/user/profile.php?id=1'
s.headers.update({
    'Origin': urlparse(url).netloc,
    'Referer': url
})
r = s.get(url)
# add your cookie here
s.cookies['MoodleSessionfeels'] = '######Login and copy your cookie here########'
for x in range(3000, 5000):
    url = f'https://feels.pdn.ac.lk/user/profile.php?id={x}'
    r = s.get(url, headers={'X-Requested-With': 'XMLHttpRequest'})
    text = r.text

    if text.find("The details of this user are not available to you") != -1:
        continue
    else:
        link = r.text[text.find('''<div class="page-context-header"><div class="page-header-image"><img src="''') +
                      74:text.find('''class=''', text.find('''<div class="page-context-header"><div class="page-header-image"><img src="''') +
                      74)-2]
        name = text[text.find("<title>")+7:text.find("</title>")-14]
        print(name, link)
        fileOpened.write(name + link + "\n")
fileOpened.close()
