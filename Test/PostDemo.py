import requests
import json,hashlib

coverInfoStr = 'https://img.jinse.cn/7059424_watermarknone.png'

coverResp = requests.post("https://www.bonaxl.com/api/nftplatform/v1/oss/uploadFileUrlMetaInfo?pic="+coverInfoStr+"&suffix=png")

print(json.loads(coverResp.text)['data']['result'])

