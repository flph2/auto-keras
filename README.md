# Auto Keras (Auto ML)
O Codigo em questão roda o autokeras contido no arquivo autokeras.py

# Uso do Auto Keras
 * Build da imagem ```docker build -t autokeras```
 * Run -> ```docker run autokeras --name autokeras $URL_IMAGEM ```

Exemplo:

 ``` docker run autokeras --name autokeras 'https://www.eneagrama.com.br/wp-content/uploads/2018/02/as-pessoas-sao-diferentes-umas-das-outras-800x419.jpg ```



if you need to see the image result with all detected objects, run docker mounting /opt/imageai/data/ as a volume
```
mkdir data
docker run -v "$(pwd)"/data:/opt/imageai/data autokeras "$IMAGE_URL"
``` 

