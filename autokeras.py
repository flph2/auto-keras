import sys
import os
import requests


FILE = '/opt/autokeras/image.jpg'

def download_image(url):
    img_data = requests.get(url).content
    with open(FILE, 'wb') as handler:
        handler.write(img_data)

def image_stats():
    return os.stat(FILE).st_size
    
def run():
    if len(sys.argv) > 1:
        download_image(sys.argv[1])
        print(('tamanho da imagem em mb: %s') % (int(image_stats()) / 1024))
        print(('autokeras test %s') % (sys.argv[1]))
    else:
        print('You need to pass at least one parameter to docker')



if '__main__' in __name__:
    run()
