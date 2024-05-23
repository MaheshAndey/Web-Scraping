from bs4 import BeautifulSoup
import lxml

with open('website.html',  encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)

anchor = soup.find_all(name='a')

for tag in anchor:
    print(tag.getText())

a = soup.find(id="name")
print(a)

b = soup.select_one(selector='p a')
print(b)
