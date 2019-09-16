import requests
import os
import sys
from autokeras_pretrained.object_detector import ObjectDetector

FILE = 'image.jpg'
dFILE = os.path.join('data', FILE)

def download_image(url):
    img_data = requests.get(url).content
    with open(dFILE, 'wb') as handler:
        handler.write(img_data)

def image_stats():
    return os.stat(FILE).st_size

def run_model():

    execution_path = os.getcwd()
    detector = ObjectDetector()
    source = os.path.join(execution_path, 'data' , FILE)
    dest = output_file_path=output_image_path=os.path.join(execution_path ,'data')
    results = detector.predict(source, output_file_path=dest)

    for eachObject in results:
        print(eachObject)
        #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    #person = 0
    #for i in detections:
    #    if i['name'] == 'person':
    #        person = person + 1
    #print(('Persons detected in the image = %s') % (person))

def run():
    if len(sys.argv) > 1:
        download_image(sys.argv[1])
        run_model()
    else:
        print('You need to pass at least one parameter to docker')

if '__main__' in __name__:
    run()

