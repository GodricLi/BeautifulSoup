# _*_ coding=utf-8 _*_


from bs4 import BeautifulSoup

html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Beautiful Suop</title>
</head>
<body>
<p class="title" name="dromouse"><b>The story</b></p>
<p class="story" >once upon a time there were three title sisters;and their name were
<a href="http://example.com/elsie" class="sister" id="link1">Elise</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
