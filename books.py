#! /opt/homebrew/bin/python3

import csv

file = "/Users/hunteradder626/Library/Containers/com.amazon.Kindle/Data/Library/Application Support/Kindle/Cache/KindleSyncMetadataCache.xml"

with open (file, 'r') as f:
    contents = f.read()

contents = contents.strip().split('<')

books = []
book = {}

def getBookTitle(eachLine):
    title = eachLine.split('>')[1]
    if title != '---------------':
        book['Title'] = title
        newList['Title'] = title

def getAuthor(eachLine):
    author = eachLine.split('>')[1]
    if author != '----':
        if 'author' not in book:
            book['Author'] = author
        else:
            book['Author'] = book['Author'] + ', ' + author

def getPubDetails(eachLine):
    publishDate = eachLine.split('>')[1]
    publishDate = publishDate.split('T')[0].split('-')[0]
    if publishDate != '':
        book['Year Published'] = publishDate

def getPublisher(eachLine):
    publisher = eachLine.split('>')[1]
    if publisher != '':
        book['Publisher'] = publisher

for eachLine in contents:
    if 'title pronunciation' in eachLine:
        if book != {}:
            book['Bookshelves'] = 'Kindle'
            book['Binding'] = 'Kindle Edition'
            books.append(book)
            book = {}
        getBookTitle(eachLine)
    elif 'author pronunciation' in eachLine:
        getAuthor(eachLine)
    if 'publication_date' in eachLine:
        getPubDetails(eachLine)
    elif 'publisher' in eachLine:
        getPublisher(eachLine)

bookHeader = ['Title','Author','ISBN','My Rating','Average Rating','Publisher','Binding','Year Published','Original Publication Year','Date Read','Date Added','Shelves','Bookshelves','My Review']

with open ('Kindle_books.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = bookHeader)
    writer.writeheader()
    writer.writerows(books)

headers = ['Title', 'ASIN Number']
