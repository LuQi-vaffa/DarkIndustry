import requests
import os

def download_resources(path):
    path = path
    try:
        if not os.path.exists(d):
            os.mkdir(d)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("资源保存成功")
        else:
            print("资源已存在")
    except:
        print("资源获取失败")


url="http://img1.doubanio.com/f/sns/ff18c28bb4d2a80510aa6599f1726ddf758faa55/css/sns/dist/anonymous_home/index.css"
d='D:\\B\\'
path=d+url.split('/')[-1]
download_resources(path)