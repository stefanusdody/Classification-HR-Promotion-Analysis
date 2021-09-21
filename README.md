## Human Resource Promotion Analysis

![promotion](https://user-images.githubusercontent.com/36668856/134099790-38d3eaea-8e9d-439a-8be9-c419531921ed.png)

## Project ini dapat diakses melalui 

Dashboard model klasifikasi dengan algorithma Logistic Regression untuk memprediksi apakah klien akan berlangganan deposito berjangka atau tidak dapat diakses melalui link website berikut:

https://h8-milestone2-stepanusdody.herokuapp.com/

## Introduction

#### Case = Classification

#### Dataset

dataset adalah kumpulan data SDM. Dalam dataset terdiri dari 50000 baris dan 14 kolom.

#### Sumber Dataset

data asli berasal dari kaggle dengan link data : https://www.kaggle.com/shivan118/hranalysis?select=train.csv

#### Objective

Setiap tahunnya, ada sekitar 5% karyawannya melakukan promosi di perusahaan. untuk itu, kita akan membuat model klasifikasi untuk melihat apakah karyawan dipromosikan atau tidak?

## library
- pandas 
- numpy 
- matplotlib
- seaborn 

####  Feature Selection
- SelectFromModel

#### Pre - Processing
- train_test_split

#### Handle imbalaced dataset
- SMOTE

#### model classification
- LogisticRegression
- KNeighborsClassifier 
- RandomForestClassifier

#### Model Evaluation
- recall_score
- accuracy_score
- precision_score
- f1_score

## Exploratory Data Analysis

![missing_values](https://user-images.githubusercontent.com/36668856/134102574-43677590-2b99-4fab-99f0-12c4ac1afd96.png)
![promoted](https://user-images.githubusercontent.com/36668856/134102582-21c1e64b-f4a1-4df4-b26d-89fe06739dbf.png)
![age](https://user-images.githubusercontent.com/36668856/134102589-a31f2cc0-59fe-420a-adbc-7f10b33305d0.png)
![training](https://user-images.githubusercontent.com/36668856/134102621-e6a1b7fb-08f5-4503-8b1d-919f64b723be.png)
![penghargaan](https://user-images.githubusercontent.com/36668856/134102628-d04b2dea-5f17-409f-9010-02b3af516306.png)
![masa_kerja](https://user-images.githubusercontent.com/36668856/134102642-34182a3b-5b9f-4663-a518-17bdea562a09.png)
![KPI](https://user-images.githubusercontent.com/36668856/134102654-71399923-d638-42e4-8052-735e37dfa1b5.png)
![pernahpenghargaan](https://user-images.githubusercontent.com/36668856/134102662-c1bba22d-28bd-47e2-95de-ebcf74a575be.png)
![nilai_training](https://user-images.githubusercontent.com/36668856/134102675-5c78d81f-cb5d-43d7-93af-deeefbf90e9f.png)
![departemen](https://user-images.githubusercontent.com/36668856/134102688-09bcba46-7037-42fc-ad92-f0574edff1de.png)
![region](https://user-images.githubusercontent.com/36668856/134102699-3fbf9492-a0a7-4140-bb22-982b3bc5b637.png)
![bachelor](https://user-images.githubusercontent.com/36668856/134102708-0911700e-2ffc-49f0-80ba-a86dfc24edf0.png)
![gender](https://user-images.githubusercontent.com/36668856/134102722-f65db517-2f86-4ac0-b32f-f0c3ac38fab7.png)
![channel](https://user-images.githubusercontent.com/36668856/134102727-e44ef322-bc1a-4e33-91a7-e3e91f4208cf.png)

## Training and Fit Model
![training fit_model](https://user-images.githubusercontent.com/36668856/134102831-665d711b-bef4-4414-bf87-e66256015b97.png)

## Evaluation Model
![evaluation](https://user-images.githubusercontent.com/36668856/134102868-7dfea1ab-d212-465f-a2ca-58bcee44233f.png)
![ROC](https://user-images.githubusercontent.com/36668856/134102873-d1bbc235-2fcf-4778-8bd1-7dfb527a154a.png)

## Model Inference
menggunakan data baru untuk melakukan prediksi
![model_inference](https://user-images.githubusercontent.com/36668856/134102925-8c99f997-0774-4ea0-8ea9-24ba5a6e6cd2.png)




