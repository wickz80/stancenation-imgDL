# Image downloader (stancenation.com) #

This is a simple python app used to fetch images from StanceNation articles.  It uses BeautifulSoup to extract article links.  Random headers and random timeouts are used to anonymize, and to not cause undue stress to servers.  

The script then processes each article, grabbing all images links and downloading them to a local directory using Requests.  

# Usage #

Command line -> Python stancenation

