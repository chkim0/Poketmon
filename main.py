import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from PIL import Image

class FeatureExtractor:
    
    def __init__(self):
        base_model = VGG16(weights='imagenet')
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)

def load():
    df = pd.read_csv('./data/pokemon.csv')
    df_name = df['Name']
    fe = FeatureExtractor()
    features = []
    img_paths = []  # 변경: 이미지 경로를 저장할 빈 리스트 생성
    for i in df_name:
        try:
            img_path = f"./data/images/{i}.png"  # 변경: img_paths 대신 img_path 사용
            if not os.path.exists(img_path):
                img_path = f"./data/images/{i}.jpg"
            img = Image.open(img_path)
            feature = fe.extract(img)
            img_paths.append(img_path)  # 변경: 이미지 경로를 리스트에 추가
            features.append(feature)
        except Exception as e:
            print('예외가 발생했습니다.', e)
    return features, img_paths  # 변경: features와 img_paths를 반환

def start():
    features, img_paths = load()  # load 함수를 호출하여 데이터 로드
    fe = FeatureExtractor()
    img = Image.open("./data/images/araquanid.jpg")
    query = fe.extract(img)
    dists = np.linalg.norm(features - query, axis=1)
    ids = np.argsort(dists)[:30]
    scores = [(dists[id], img_paths[id], id) for id in ids]
    axes = []
    fig = plt.figure(figsize=(8, 8))
    for a in range(5 * 6):
        score = scores[a]
        axes.append(fig.add_subplot(5, 6, a + 1))
        subplot_title = str(round(score[0], 2)) + "/num" + str(score[2] + 1)
        axes[-1].set_title(subplot_title)
        plt.axis('off')
        plt.imshow(Image.open(score[1]))
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    start()


