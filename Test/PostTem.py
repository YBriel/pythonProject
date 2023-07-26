from bs4 import BeautifulSoup
from urllib.parse import urlencode
import requests
import json


def postTem(postId, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text

    params = {'mediaType': 2}
    params['postId'] = postId
    soup = BeautifulSoup(html, 'html.parser')
    # 查找<div class="list-post">下的<article>标签下的所有<a>标签
    title = soup.find('h1', {'class': 'post-title'})
    #print("文章标题:", title.text)
    params["title"] = title.text
    cover = soup.find('div', {'class': 'post-header article clearfix'})
    coverInfo = cover.find('img', {'class': 'nolazy'})
    coverTem= coverInfo['srcset']
   # coverTem=coverTem[coverTem.rfind(','):].replace(" 2x", '')
    print('文章封面',  coverTem.rsplit(',')[-1].replace('2x', '').strip())

    # 文章内图片
    pics = soup.find_all('figure', {'class': 'wp-caption aligncenter'})

    cover_url = coverTem.rsplit(',')[-1].replace('2x', '').strip()

    headers0 = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    # cover_resp = requests.post(
    #     "https://www.bonaxl.com/api/nftplatform/v1/oss/uploadFileUrlMetaInfo?pic=" + urlencode(cover_url) + "&suffix=jpg")
    cover_param = {'pic': cover_url, 'suffix':'jpg'}

    cover_body = json.dumps(cover_param)
    # print(body)
    cover_resp = requests.post('https://www.bonaxl.com/api/nftplatform/v1/oss/uploadFileUrlMetaInfoBody',headers=headers0,
                              data=cover_body)
    params['cover'] = json.loads(cover_resp.text)['data']['result']
    postMediaInfos = []
    postMediaInfos.append(json.loads(cover_resp.text)['data']['result'])

    contentPics = []
    for pic in pics:
        contentPic = pic.find('img')
        contentPics.append(contentPic['src'])
        coverResp = requests.post(
            "https://www.bonaxl.com/api/nftplatform/v1/oss/uploadFileUrlMetaInfo?pic=" + contentPic['src'] + "&suffix=jpg")
        postMediaInfos.append(json.loads(coverResp.text)['data']['result'])
        print('文章图片', contentPic['src'])

    params['postMediaInfos'] = postMediaInfos
    # 文章内容

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the <article> tag within the parent <div> element with class "post-box clearfix"
    article_p = soup.select_one('div.post-box.clearfix article')

    # Find all the direct child <p> tags within the <article> tag
    first_level_p_tags = article_p.find_all('p', recursive=False)

    # Extract and print the text content of each direct child <p> tag
    content = '  \n'.join(["  " + p.text.strip() for p in first_level_p_tags])

    params["content"] = content
   # params["content"] = article_p.text
    postSponsorInfo = {
        "sponsorId": "e4e5b89332ec47049160ae9a487c8092",
        "userId": "e4e5b89332ec47049160ae9a487c8092",
        "postType": 1,
        "userAvatar": "168241357387742.jpg",
        "userName": "在家干嘛",
        "userCustomerName": "nxjdsjjs",
        "projectMemberNums": 1100
    }
    params['postSponsorInfo'] = postSponsorInfo

    # print(content)
    # for p_tag in first_level_p_tags:
    #   print(p_tag.get_text().strip())
    hash_tags_list = []
    params['hashTags'] = hash_tags_list
    soup_post_tag = soup.select_one('div.posted-in')
    if soup_post_tag is not None:
        article_tag = soup_post_tag.find_all('a')
        for a_tag in article_tag:
            # print(a_tag.get_text().strip())
            hash_tags_list.append(a_tag.get_text().strip())

        params['hashTags'] = hash_tags_list

    # 获取封面meta信息

    #print(params)
    params['mentionedUsers'] = []
    params['mentionedCommunities'] = []
    params['mentionedPostClubInfos'] = []
    params['mentionedBounties'] = []
    params['mentionedBounties'] = []
    params['mentionedWatchList'] = []
    params['mentionedDApps'] = []
    params['source'] = 3
    headers2 = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiZmJmNzk0NDgyNDE1NDJmOGEwMjc3YTYzODk2ZDg3MTAiLCJmcm9tLXNvdXJjZSI6MSwiZXhwIjoxNjkxMjA5MDIwfQ.Chb1oa-Wg4DdmiQyRfG0awUvCxotlpFn7D-9edZM9xncNBU1TEwCDSgoZHHZDq-f5Hrq8Fmbm8oFmHbzMM2_Mw'
    }
    body = json.dumps(params)
    #print(body)
    response2 = requests.post('https://www.bonaxl.com/api/nftplatform/v2/rpc/post/addMongoPostTem', headers=headers2,
                              data=body)
    print('添加post返回', postId, json.loads(response2.text))

if __name__ == '__main__':
    postTem("12","https://cryptoslate.com/caroline-ellisons-private-writings-in-months-before-alameda-ftx-collapse-uncovered-in-discovery-process/")
