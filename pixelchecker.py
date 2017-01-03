'''
Author: Ryan Kwon
Using BeautifulSoup to scrape and Tweepy to utilize Twitter's API, this Python program scrapes
Google's Pixel website and sees what the current inventory status is on all models of the Pixel
XL model phones(not regular Pixels but that can easily be added by following the included functions)
and posts the status of all phones to a Twitter account(I've made @pixelxlstock to demonstrate). If
a phone is in stock, it will send a direct message to a specified user(in this example code, it will
send a direct message to my personal twitter account @itsryankwon when a 128GB Silver model, 128GB Black
model, or Blue model is in stock).
'''

from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import tweepy
import time

def get_api():
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  return tweepy.API(auth)


def vSil1(sp):
  msg = ""
  d = sp.find_all(attrs={"data-backend-docid": "_pixel_xl_phone_silver_32gb"})
  dStr = str(d)
  if ss in dStr:
    msg = msg + "Google Pixel XL 32GB(Very Silver) is available for preorder https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  elif oos in dStr:
    msg = msg + "Google Pixel XL 32GB(Very Silver) is out of stock https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  else:
    msg = msg + "Google Pixel XL 32GB(Very Silver) IS IN STOCK! https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)

def vSil2(sp):
  msg = ""
  d = sp.find_all(attrs={"data-backend-docid": "_pixel_xl_phone_silver_128gb"})
  dStr = str(d)
  if ss in dStr:
    msg = msg + "Google Pixel XL 128GB(Very Silver) is available for preorder https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  elif oos in dStr:
    msg = msg + "Google Pixel XL 128GB(Very Silver) is out of stock https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  else:
    msg = msg + "Google Pixel XL 128GB(Very Silver) IS IN STOCK! https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
    api.send_direct_message("itsryankwon", text=msg)

def qBlack1(sp):
  msg = ""
  d = sp.find_all(attrs={"data-backend-docid": "_pixel_xl_phone_black_32gb"})
  dStr = str(d)
  if ss in dStr:
    msg = msg + "Google Pixel XL 32GB(Quite Black) is available for preorder https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  elif oos in dStr:
    msg = msg + "Google Pixel XL 32GB(Quite Black) is out of stock https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  else:
    msg = msg + "Google Pixel XL 32GB(Quite Black) IS IN STOCK! https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)

def qBlack2(sp):
  msg = ""
  d = sp.find_all(attrs={"data-backend-docid": "_pixel_xl_phone_black_128gb"})
  dStr = str(d)
  if ss in dStr:
    msg = msg + "Google Pixel XL 128GB(Quite Black) is available for preorder https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  elif oos in dStr:
    msg = msg + "Google Pixel XL 128GB(Quite Black) is out of stock https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  else:
    msg = msg + "Google Pixel XL 128GB(Quite Black) IS IN STOCK! https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
    api.send_direct_message("itsryankwon", text=msg)

def rBlue1(sp):
  msg = ""
  d = sp.find_all(attrs={"data-backend-docid": "_pixel_xl_phone_blue_32gb"})
  dStr = str(d)
  if ss in dStr:
    msg = msg + "Google Pixel XL 32GB(Really Blue) is available for preorder https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  elif oos in dStr:
    msg = msg + "Google Pixel XL 32GB(Really Blue) is out of stock https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
  else:
    msg = msg + "Google Pixel XL 32GB(Really Blue) IS IN STOCK! https://store.google.com/config/pixel_phone" + " - " + str(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')) + " #pixelxl"
    print(msg)
    api.update_status(status=msg)
    api.send_direct_message("itsryankwon", text=msg)

oos = "Out of stock"
ss = "Ships soon."
api = get_api()

status = False

while status == False: 
  r = urllib.request.urlopen('https://store.google.com/config/pixel_phone').read()
  soup = BeautifulSoup(r, "html.parser")

  vSil1(soup)
  vSil2(soup)
  qBlack1(soup)
  qBlack2(soup)
  rBlue1(soup)
  
  #time.sleep(n) optional if you want the program to check every n seconds
