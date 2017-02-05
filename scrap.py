#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests
import sys

BASE = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.jpg"
GIST = sys.argv[1]

def getWalls(url):
  r = requests.get(url)

  soup = BeautifulSoup(r.text, 'html.parser')
  tags = soup.find(id="thumbs").find_all('figure')

  for tag in tags:
    yield tag.get('data-wallpaper-id')

getWalls(GIST)

for wall in getWalls(GIST):
  print(BASE.format(wall))
