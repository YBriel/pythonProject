from bs4 import BeautifulSoup
import PostTem
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


for i in range(70, 80):
    print(i)
    html = requests.get(
        'https://cryptoslate.com/news/page/'+str(i)+'/',
        headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')
    # 查找<div class="list-post">下的<article>标签下的所有<a>标签
    #new_feed = soup.find('section', {'news-feed'})
    div_list_post2 = soup.find('div', {'class': 'list-feed slate'})
    div_list_post = div_list_post2.find_all('div', {'class': 'list-post'})
    for post in div_list_post:
       # print(post)
        #print(post.find('article')['id'], post.find('a')['href'])
        try:
            PostTem.postTem(post.find('article')['id'], post.find('a')['href'])
        except Exception as e:
            print("出现如下异常%s" % e)




