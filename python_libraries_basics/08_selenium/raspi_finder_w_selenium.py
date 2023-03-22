#! /usr/bin/env python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://rpilocator.com/?country=DE&cat=PI4%2CPIZERO')