# Laporan Proyek Machine Learning - Muhammad Zaki Fuadi
## _Submission Pertama_

Proyek ini bertujuan untuk menentukan churn dari nasabah bank, churn adalah tingkatan seorang konsumen menghentikan kegiatan berlangganan dari sebuah produk di perusahaan tersebut, subjek pada proyek ini adalah seorang nasabah bank. 

## Domain Proyek

> Churn adalah istilah yang digunakan untuk menggambarkan keadaan dimana pelanggan tidak lagi menggunakan layanan atau produk dari suatu perusahaan. Dalam konteks perbankan, churn terjadi ketika pelanggan menutup rekening atau beralih ke bank lain, mengurangi tingkat churn menjadi krusial dalam industri perbankan karena kehilangan pelanggan dapat berdampak signifikan terhadap pendapatan bank. Selain itu, biaya untuk menarik pelanggan baru lebih mahal daripada mempertahankan pelanggan yang sudah ada[1].
> Kehilangan pelanggan dapat berdampak negatif pada pendapatan bank. Biaya untuk menarik pelanggan baru lebih tinggi daripada mempertahankan pelanggan yang sudah ada. Oleh karena itu, mengurangi tingkat churn sangat penting untuk menjaga kesehatan finansial bank. Hal ini disampaikan oleh Kevin Tynan, seorang analis perbankan senior di Bloomberg Intelligence, dalam sebuah artikel di Forbes[2].

## Business Understanding
### - Problem Statement
- Bagaimana cara memprediksi tingkat churn nasabah pada bank ?
- Apa strategi yang efektif untuk mempertahankan nasabah bank ?

### - Goals
- Membangun model prediksi churn yang akurat, dengan memiliki model prediksi yang akurat, bank dapat mengambil tindakan proaktif untuk mempertahankan pelanggan dan mencegah kehilangan mereka ke bank lain
- Menentukan strategi yang efektif untuk mempertahankan nasabah, dengan mengetahui faktor-faktor yang memengaruhi churn pelanggan, bank dapat memilih strategi yang tepat untuk mempertahankan pelanggan dan meningkatkan kepuasan mereka.

### - Solution Statement
- Menggunakan algoritma RandomForest dengan hyperparameter tuning untuk meningkatkan akurasi prediksi data.

## Data Understanding

Dataset didapat pada [kaggle]  (https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction/download?datasetVersionNumber=1)

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

| Informasi | Penjelasan |
| ------ | ------ |
| Jumlah Baris | 10000 |
| Jumlah Kolom | 14 |
| Missing Value | 0 |

Keterangan kolom data :

| Nama | Keterangan |
| ------ | ------ |
| Row Number | Urutan Baris |
| CustomerId | Id Nasabah |
| Surname | Nama Nasabah |
| CreditScore | Skor Kredit Nasabah |
| Geography | Lokasi Nasabah |
| Gender | Jenis Kelamin Nasabah |
| Age | Umur Nasabah |
| Tenure | Lama Nasabah Menabung di Bank |
| Balance | Tabungan Nasabah |
| NumOfProducts | Jumlah Produk yang Digunakan Nasabah di Bank |
| HasCrCard | Apakah Memiliki Kartu (Biner) |
| IsActiveMember | Apakah Aktif Member (Biner) |
| EstimatedSalary | Rata-rata Pendapatan Nasabah |
| Churn | Apakah Churn (Biner) |

![Cek-Outlier](https://user-images.githubusercontent.com/70827786/234861700-ce96af52-d50b-4069-83df-f717f0b27d22.png)
Gambar 1. Distribusi EstimatedSalary
![Cek-Outlier1](https://user-images.githubusercontent.com/70827786/234862076-5c857c04-a49e-43a7-b4d3-949439825c88.png)
Gambar 2. Distribusi Age
![Cek-Outlier2](https://user-images.githubusercontent.com/70827786/234862098-b0d2663c-4ad4-4e65-91fc-667e376a7003.png)
Gambar 3. Distribusi Balance

Pada gambar 2. variabel "Age" terdapat banyak outlier sehingga akan dilakukan metode IQR (Interquartile Range) untuk mengidentifikasi dan menghapus outlier.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. 

- Menerapkan dan menyebutkan teknik data preparation yang dilakukan. (Data Imbalancing, data normalization)
- Data Imbalancing mengatasi masalah ini dengan menyeimbangkan distribusi kelas sehingga model atau algoritma lebih akurat dalam memprediksi kedua kelas.
- Data Normalization meningkatkan akurasi dan kecepatan dalam pemrosesan data serta meningkatkan interpretasi hasil analisis.
- Dengan melakukan data preparation, hasil analisis dan model yang dihasilkan akan lebih akurat dan efektif.
- Pembagian dataset training dan dataset testing yaitu 80% banding 20% untuk mempercepat proses mesin belajar dan evaluasi model.

![Heatmap](https://user-images.githubusercontent.com/70827786/234901719-07621fc2-4620-41cf-937b-968aeb5781fe.png)
Gambar 4. Heatmap dataset churn

> Dilihat "age" dengan "exited" memiliki korelasi positif lemah, berarti semakin tua usia nasabah, semakin tinggi kemungkinannya untuk keluar dari bank.
> Dilihat "NumOfProducts" dengan "Balance", memiliki korelasi negatif paling besar, berarti semakin banyak produk yang dimiliki oleh nasabah, semakin rendah jumlah saldo yang dimilikinya.

## Data Modelling

Model menggunakan RandomForest, karena dilakukan hyperparameter tuning, akurasi terbaik yaitu menggunakan algoritma XGBoostClassifier. 

> Saat dilakukan hyperparameter tuning, dibandingkan beberapa algorithma yaitu : LogisticRegression, DecisionTree, RandomForest, KNeighbors, XGBoostClassifier, SCV.
> XGBoostClassifier mengatur beberapa parameter, yaitu dataset (dalam hal ini XGBdata), parameter XGBoost (params), jumlah fold yang digunakan (nfold=5), metrics yang ingin digunakan untuk evaluasi (metrics="auc"), jumlah iterasi boosting (num_boost_round=200), serta jumlah iterasi yang diperbolehkan tanpa peningkatan performa (early_stopping_rounds=20).
> Setelah melakukan cross validation, hasil rata-rata dari skor yang dihasilkan oleh model pada tiap fold-nya dicetak pada output. Skor pada cross validation ini digunakan untuk mengukur performa model dalam memprediksi target kelas pada data yang belum dilihat sebelumnya. Semakin besar skor, semakin baik performa model dalam memprediksi kelas target. Model memiliki kemampuan untuk memprediksi dengan akurasi sekitar 84%.

Akurasi model sebesar 84% dengan nilai MSE 0,16 dan MAE 0,16. Kemudian menggunakan plot importance dengan algoritma RandomForest untuk mengetahui variabel yang paling berpengaruh terjadinya churn rate ini.

## Evaluation

Pada hasil evaluasi memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:

![Hyperparameter Tuning](https://user-images.githubusercontent.com/70827786/235040464-43044f55-1b7b-4029-a2c8-254869fbdd23.png)

Gambar 5.  Hyperparameter Tuning

Pada Gambar 5. Pada hyperparameter digunakan beberapa algoritma klasifikasi untuk menentukan model terbaik, dicoba pada LogisticRegression, DecisionTree, RandomForest, KNeighbors, XGB dan SVC. 

- LogisticRegression : memprediksi probabilitas kejadian sebuah peristiwa (dalam hal ini, kemungkinan sebuah pelanggan akan beralih), pelanggan mana yang paling mungkin untuk beralih berdasarkan variabel yang telah ditentukan.
- DecisionTree :  membuat keputusan berdasarkan serangkaian aturan dan pertanyaan (tree) yang digunakan untuk memprediksi target variabel, memprediksi tentang pelanggan yang akan beralih dengan menguji aturan berdasarkan fitur-fitur yang diberikan.
- RandomForest : mirip dengan Decision Tree, namun beroperasi dengan menggabungkan beberapa decision tree, mirip dengan Decision Tree, namun beroperasi dengan menggabungkan beberapa decision tree.
- KNeighbors : Melakukan klasifikasi dengan mencari tetangga terdekat dari suatu data point, memprediksi apakah pelanggan akan beralih dengan membandingkan fitur-fitur yang diberikan dengan data pelanggan yang sudah beralih sebelumnya.
- XGB : Algoritma ensemble learning yang menggunakan banyak model kecil (boosting) untuk membuat model yang lebih besar dan lebih akurat, ensemble learning yang menggunakan banyak model kecil (boosting) untuk membuat model yang lebih besar dan lebih akurat.
- SVC : Algoritma ini cocok digunakan untuk kasus dimana terdapat pemisah antara dua kelas data yang jelas. Dalam hal ini, SVC dapat digunakan untuk memprediksi apakah pelanggan akan beralih atau tidak berdasarkan variabel yang telah ditentukan.

Pada Gambar 5. Model Random Forest dan XGB memiliki nilai mean F1 Score yang cukup tinggi yaitu 0.795503 dan 0.794184 secara berturut-turut. Namun, jika diperhatikan juga nilai standard deviation (std), model XGB memiliki nilai std yang lebih rendah yaitu 0.009113 dibandingkan dengan model Random Forest yang memiliki nilai std 0.011238. Nilai std yang lebih rendah menunjukkan bahwa model XGB memiliki stabilitas performa yang lebih baik ketika diuji dengan data yang berbeda-beda, sehingga dapat dipertimbangkan sebagai model terbaik. Sehingga pada model algoritma yang digunakan pada permasalahan churn rate ini menggunakan XGBoost.

![CM](https://user-images.githubusercontent.com/70827786/235040222-b79c5bae-3304-485c-95a5-a02eb5e7b9c8.png)

Gambar 6. Correlation Matrix

Pada Gambar 6. dapat dilihat :

- 1497 merupakan True Positive, yaitu jumlah data positif yang berhasil diprediksi dengan benar oleh model.
- 96 merupakan False Positive, yaitu jumlah data negatif yang salah diprediksi sebagai positif oleh model.
- 354 merupakan False Negative, yaitu jumlah data positif yang salah diprediksi sebagai negatif oleh model.
- 840 merupakan True Negative, yaitu jumlah data negatif yang berhasil diprediksi dengan benar oleh model

dilihat bahwa model memiliki performa yang cukup baik, dengan nilai precision, recall, dan f1-score yang relatif tinggi untuk kedua kelas. Precision yang tinggi dapat membantu bank untuk mengidentifikasi nasabah yang berpotensi meninggalkan bank dengan lebih akurat, sehingga bank dapat mengambil tindakan preventif atau merancang program loyalty yang lebih efektif. Precision yang tinggi dapat membantu bank untuk mengidentifikasi nasabah yang berpotensi meninggalkan bank dengan lebih akurat, sehingga bank dapat mengambil tindakan preventif atau merancang program loyalty yang lebih efektif. Namun, recall untuk kelas 1 terlihat lebih rendah dibandingkan dengan kelas 0, sehingga perlu diperhatikan lebih lanjut.

![PlotImportance](https://user-images.githubusercontent.com/70827786/235040197-e2ecf578-de38-48e4-afcf-68723b50594f.png)
Gambar 7. Plot Importance XGBoost Algorithm

Pada Gambar 7. Plot importance menggunakan variabel estimated salary, surname dan creditscore merupakan 3 urutan paling tinggi, sehingga menjadi faktor penting dalam memprediksi apakah seorang nasabah akan keluar (churn) dari bank atau tidak.
Hal ini mungkin berarti bahwa faktor-faktor terkait gaji dan nama keluarga (surname) dapat menjadi faktor penting dalam memprediksi apakah seorang nasabah akan keluar (churn) dari bank atau tidak. Misalnya, nasabah dengan gaji yang lebih tinggi mungkin cenderung memiliki kecenderungan yang lebih rendah untuk keluar dari bank, atau mungkin nasabah dengan beberapa jenis nama keluarga tertentu cenderung lebih stabil dalam menjaga akun mereka di bank. Namun, perlu dicatat bahwa hal ini hanya spekulasi dan harus dilihat dengan hati-hati dalam konteks tertentu dan diuji dalam analisis yang lebih dalam.

## REFERENCES
[1] Wen Z, Yan J, Zhou L, Liu Y, Zhu K, Guo Z, Li Y, Zhang F (2018) Peringatan churn pelanggan dengan pembelajaran mesin Dalam The Euro-China Conference on Intelligent Data Analysis and Applications, hlm 343–350 Springer.
[2] Tynan, K. (2018, March 5). Why Reducing Customer Churn Is Crucial For Banks. Forbes. 
