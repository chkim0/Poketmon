# Poketmon
230914_ 이미지유사도분석

![스크린샷 2023-11-20 193459](https://github.com/chkim0/Poketmon/assets/113896147/784e63c9-5939-4fe1-8a85-bdd759b72b44)



FeatureExtractor 클래스를 정의
![image](https://github.com/chkim0/Poketmon/assets/113896147/52711bb8-cd51-47a9-ac52-153672c952b1)


 VGG16 모델을 사용하여 이미지의 특징을 추출 초기화 메서드(__init__)에서는 VGG16 모델을 불러오고 'fc1' 레이어의 출력을 얻어 self.model에 저장 
 extract 메서드에서는 주어진 이미지를 VGG16 모델에 맞게 전처리하고, 'fc1' 레이어의 출력을 추출한 뒤 이를 정규화하여 반환



 ![image](https://github.com/chkim0/Poketmon/assets/113896147/bd55fefa-618f-4556-9fda-7a83f583922d)

features = []: features라는 빈 리스트를 초기화 추출된 특징을 이 리스트에 저장.

img_paths = []: img_paths라는 빈 리스트를 초기화. 이 리스트에는 처리된 이미지의 경로를 저장.

DataFrame df_name을 순환하며 각 반복에서:

DataFrame에서 가져온 i를 사용하여 이미지 경로를 생성. 이미지는 PNG 또는 JPG 형식.

path.exists()를 사용하여 생성된 이미지 경로가 있는지 확인. 그렇지 않다면 경로에 ".jpg"를 추가하고 다시 확인.

이미지를 PIL 또는 Pillow과 같은 이미지 처리 라이브러리의 Image.open 메서드를 사용하여 엽니다.


이미지 검색 및 시각화

![image](https://github.com/chkim0/Poketmon/assets/113896147/3fa42ec7-534d-4b9c-9106-80b685cf6464)


주어진 이미지 파일("araquanid.jpg")을 열어서 해당 이미지의 특징을 추출

이미지 검색을 위해 변수에서 추출한 이미지 특징과 데이터프레임에서 추출한 다른 이미지들의 특징 간의 유클리드 거리를 계산

계산된 거리를 기준으로 상위 30개의 이미지에 해당하는 인덱스를 선택

선택된 이미지들의 정보(거리, 파일 경로, 인덱스)를 scores 리스트에 저장

시각화를 위해 빈 그림과 서브플롯을 생성하고, 상위 30개 이미지를 시각화 후 각 이미지의 제목은 해당 이미지와 query 이미지 간의 거리를 나타냄.


결과 
![image](https://github.com/chkim0/Poketmon/assets/113896147/f3362005-5e76-488a-9040-f2b5af23bc4f)

이미지와 유사도 확인 

![image](https://github.com/chkim0/Poketmon/assets/113896147/6325ea11-b2a3-428b-9f4f-aaeee986cd8f)


