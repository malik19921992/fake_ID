#!/usr/bin/env python3

import requests
import random


def f_name():
    url  = "https://www.cs.cmu.edu/Groups/AI/areas/nlp/corpora/names/male.txt"
    data = requests.get(url)
    line_num = 1
    f_names = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip()
            f_names.append(line)
        line_num += 1
    f_name = random.choices(f_names)
    for fn in f_name: return fn

def l_name():
    url = "https://raw.githubusercontent.com/colinangusmackay/Xander.PasswordValidator/master/src/Xander.PasswordValidator/Resources/Surnames.txt"
    data = requests.get(url)
    line_num = 1
    l_names = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip() # remove spaces between lines
            l_names.append(line)
        line_num += 1
    l_name = random.choices(l_names)
    for ln in l_name: return ln



def street():
    url  = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/security-question-answers/street-names.txt"
    data = requests.get(url)
    line_num = 1
    streets = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip()
            streets.append(line)
        line_num += 1
    street = random.choices(streets)
    for st in street: return st



def city():
    url  = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/security-question-answers/cities.txt"
    data = requests.get(url)
    line_num = 1
    cities = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip()
            cities.append(line)
        line_num += 1
    city = random.choices(cities)
    for ct in city: return ct


def country():
    url = "https://gist.githubusercontent.com/kalinchernev/486393efcca01623b18d/raw/daa24c9fea66afb7d68f8d69f0c4b8eeb9406e83/countries"
    data = requests.get(url)
    line_num = 1
    countries = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip()
            countries.append(line)
        line_num += 1
    country = random.choices(countries)
    for cu in country: return cu


def phone():
    url = "https://gist.githubusercontent.com/codelingoblog/13d6fc68b70e29e4307655cd64bf3213/raw/ab5e6771ebd45278aff4990291a42526952db084/phone_numbers.txt"
    data = requests.get(url)
    line_num = 1
    phones = []
    for line in data.text.splitlines(True):
        line = line.strip()
        phones.append(line)
        line_num += 1
    phone = random.choices(phones)
    for ph in phone: return ph


def email():
    url = "https://raw.githubusercontent.com/papyrussolution/OpenPapyrus/master/Src/PPTEST/DATA/email-list.txt"
    data = requests.get(url)
    line_num = 1
    emails = []
    for line in data.text.splitlines(True):
        if line_num in range(8,22):
            line = line.strip()
            emails.append(line)
        line_num += 1
    email = random.choices(emails)
    for em in email: return em




print("name    : {} {}".format(f_name(),l_name()))
print("phone   : {}".format(phone()))
print("street  : {}".format(street()))
print("city    : {}".format(city()))
print("country : {}".format(country()))
print("email   : {}".format(email()))


 
