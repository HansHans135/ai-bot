#匯入需要的套件
import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt

#使用Tensorflow提供的模型
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

#匯入需要的套件，將提示詞填入" "當中, batch_size是產生圖片的數量。圖片越多需要時間越長。以下將產生3張圖片
images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=3)

#畫出結果
def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")


plot_images(images)