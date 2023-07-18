from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

print("开始请求")
html = requests.get(
    'https://cryptoslate.com/elizabeth-warren-asks-sec-to-investigate-elon-musks-dual-roles-at-twitter-and-tesla/',
    headers=headers).text

#print("html内容为{}", html)

soup = BeautifulSoup(html, 'html.parser')
# 查找<div class="list-post">下的<article>标签下的所有<a>标签
title = soup.find('h1', {'class': 'post-title'})
print("文章标题:", title.text)

# 文章封面
cover = soup.find('div', {'class': 'post-header article clearfix'})
coverInfo = cover.find('img', {'class': 'nolazy'})
print('文章封面', coverInfo['srcset'])
# print(coverInfo['src']) #图片地址

# 文章内图片
pics = soup.find_all('figure', {'class': 'wp-caption aligncenter'})

for pic in pics:
    contentPic = pic.find('img')
    print('文章图片', contentPic['src'])
# 文章内容

# articles = soup.find_all('article')
# print(articles)
# articleRes = articles.find_all('p')
# for ar in articleRes:
#     print(ar)
#文章内容
# articleSoup = soup.find("div", {'class': 'post-box clearfix'})
# paragraphs = articleSoup.find_all('p')
# print("内", paragraphs)
# content = '\n'.join([p.text.strip() for p in paragraphs])
# print('文章内容：\n', content)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the <article> tag within the parent <div> element with class "post-box clearfix"
article_p = soup.select_one('div.post-box.clearfix article')

# Find all the direct child <p> tags within the <article> tag
first_level_p_tags = article_p.find_all('p', recursive=False)

# Extract and print the text content of each direct child <p> tag
content = '\n'.join([p.text.strip() for p in first_level_p_tags])
#print(content)
#for p_tag in first_level_p_tags:
#   print(p_tag.get_text().strip())

article_tag = soup.select_one('div.posted-in').find_all('a')
for a_tag in article_tag:
    print(a_tag.get_text().strip())