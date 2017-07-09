import os
import urllib.request
from . import settings

class ManhuaPipeline(object):
    def __init__(self):
        self.cnt = 1
        dir_path = './pic2/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def process_item(self, item, spider):
        for pic_url in item['img_urls']:
            print(pic_url)
            pic_name = str(self.cnt) + '.jpg'
            pic = urllib.request.urlopen(pic_url).read()
            with open('./pic2/' + pic_name, 'wb') as f:
                f.write(pic)
            self.cnt += 1

        return item

