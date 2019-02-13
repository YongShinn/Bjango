from lxml import html
import requests

page = requests.get(
    'https://www.theeditorsmarket.com/product/ready-to-wear/tops/eviy-knotted-crop-top-bk')
tree = html.fromstring(page.content)
# This will create a list of buyers:
prod_name = tree.xpath('//*[@id="node-product-right-inner"]/h1/text()')
prod_price1 = tree.xpath(
    '//*[@id="node-product-price"]/div[1]/div[1]/span/text()')
prod_price2 = tree.xpath(
    '//*[@id="node-product-price"]/div[2]/div[1]/span/text()')
prod_price3 = tree.xpath(
    '//*[@id="node-product-price"]/div[3]/div[1]/span/text()')


print(prod_name)
print(prod_price1)
print(prod_price2)
print(prod_price3)


# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get(
#     'https://www.theeditorsmarket.com/product/ready-to-wear/tops/eviy-knotted-crop-top-bk').text

# soup = BeautifulSoup(source, 'lxml')
# prod_name = soup.find('div', class_='title')
# print(prod_name.prettify())

# csv_file = open('cms_scrape.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)

# try:
#     vid_src = article.find('iframe', class_='youtube-player')['src']

#     vid_id = vid_src.split('/')[4]
#     vid_id = vid_id.split('?')[0]

#     yt_link = f'https://youtube.com/watch?v={vid_id}'
# except Exception as e:
#     yt_link = None

# print(yt_link)

# print()

#     csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()
