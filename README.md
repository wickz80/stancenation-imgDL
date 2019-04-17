# Image downloader (stancenation.com) #

This is a simple python app used to fetch images from StanceNation articles.  It uses BeautifulSoup to extract article links.  Random headers and random timeouts are used to anonymize, and to not cause undue stress to servers.  

The script then processes each article, grabbing all images links and downloading them to a local directory using Requests.  

# Usage #

First, modify stancenation.py to reflect your destination directory and # pages to parse.

`pages_back = 25`
`base_url = 'http://www.stancenation.com/topics/car-features/page/'`
`url_list = []`
`downloadDirectory = "C:\\Images"`

In cmd (Windows):

`cd myDirectory\stancenation-imgDL`

`python stancenation.py`

Continue for as long as you'd like.

