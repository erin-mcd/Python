from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Components/Store'
# open connection and grab page
uClient = uReq(myurl)
pagehtml = uClient.read()

# close client
uClient.close()

pagesoup = soup(pagehtml, "html.parser")
# pagesoup.h1

# grabs each product
containers = pagesoup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "item, shipping, price was, price current\n"
f.write(headers)

# container = container[0]
# titlecontainer = container.a.img["title"]

for container in containers:
	item = container.a.img["title"]

	price_ship = container.findAll("li", {"class":"price-ship"})
	shipping = price_ship[0].text.strip()

	price_was = container.findAll("li", {"class":"price-was"})
	price_was = price_was[0].text.strip()
	
	price_was = price_was.replace("\n","")
	price_was = price_was.replace("\r","")

	sep = " "
	price_was = price_was.split(sep, 1)[0]
	
	price_current = container.findAll("li", {"class":"price-current"})
	price_current = price_current[0].strong.text.strip()
	#price_current = price_current[0].text.strip()
	#print("1:" + price_current)
	#price_current = price_current.replace("\xa0"," ")
	#print("2:" + price_current)	
	#price_current = price_current.split(sep, 1)[0]
	
	temp = container.findAll("li", {"class":"price-current"})
	price_currentdec = temp[0].sup.text.strip()
	price_current = "$" + price_current + price_currentdec

	print("item: " + item)
	print("shipping: " + shipping)
	print("price was: " + price_was)
	print("price current: " + price_current)

	f.write(item.replace(",","") + "," + shipping + "," + price_was + "," + price_current + "\n")

f.close()