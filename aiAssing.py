import matplotlib.pyplot as plt
from tensorflow.keras import datasets
from tensorflow.keras import Sequential, optimizers
from tensorflow.keras.layers import Flatten, Dense
# mnist 데이터세트 가져오기
(train_imgs, train_labels), (test_imgs, test_labels)\
 = datasets.mnist.load_data()
# 픽셀 값을 0~1 사이로 정규화
train_imgs, test_imgs = \
 train_imgs / 255.0, test_imgs / 255.0
# 처음 25장의 학습 이미지 출력
plt.figure(figsize=(10, 10))
for i in range(25):
 plt.subplot(5, 5, i+1)
 plt.xticks([])
 plt.yticks([])s
 plt.grid(False)
 plt.imshow(train_imgs[i], cmap=plt.cm.gray_r)
 plt.xlabel(train_labels[i])
plt.show()
# 모델 구성 후 요약 정보 출력
model = Sequential([
 Flatten(input_shape=(28, 28)),
 Dense(128, activation='sigmoid'),
 Dense(10, activation='softmax'),
])
model.summary()
# 모델 컴파일
model.compile(optimizer=optimizers.SGD(0.1, momentum=0.9),
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])
# 학습
model.fit(train_imgs, train_labels, epochs=5)
# 테스트 집합을 대상으로 평가
test_loss, test_acc =\
 model.evaluate(test_imgs, test_labels, verbose=2)
print('인식률 = ', test_acc)