# Laporan Proyek Machine Learning - Muhammad Zaki Fuadi
## _Submission Pertama_

Proyek ini bertujuan untuk menentukan churn dari nasabah bank, churn adalah tingkatan seorang konsumen menghentikan kegiatan berlangganan dari sebuah produk di perusahaan tersebut, subjek pada proyek ini adalah seorang nasabah bank. 

## Domain Proyek

> Churn adalah istilah yang digunakan untuk menggambarkan keadaan dimana pelanggan tidak lagi menggunakan layanan atau produk dari suatu perusahaan. Dalam konteks perbankan, churn terjadi ketika pelanggan menutup rekening atau beralih ke bank lain, mengurangi tingkat churn menjadi krusial dalam industri perbankan karena kehilangan pelanggan dapat berdampak signifikan terhadap pendapatan bank. Selain itu, biaya untuk menarik pelanggan baru lebih mahal daripada mempertahankan pelanggan yang sudah ada.
> Kehilangan pelanggan dapat berdampak negatif pada pendapatan bank. Biaya untuk menarik pelanggan baru lebih tinggi daripada mempertahankan pelanggan yang sudah ada. Oleh karena itu, mengurangi tingkat churn sangat penting untuk menjaga kesehatan finansial bank. Hal ini disampaikan oleh Kevin Tynan, seorang analis perbankan senior di Bloomberg Intelligence, dalam sebuah artikel di Forbes.

## Business Understanding
### - Problem Statement
- Bagaimana cara memprediksi tingkat churn nasabah pada bank
- Apa strategi yang efektif untuk mempertahankan nasabah bank

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

{Gambar keadaan data}

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. 

- Menerapkan dan menyebutkan teknik data preparation yang dilakukan. (Data Imbalancing, data normalization)
- Data Imbalancing mengatasi masalah ini dengan menyeimbangkan distribusi kelas sehingga model atau algoritma lebih akurat dalam memprediksi kedua kelas.
- Data Normalization meningkatkan akurasi dan kecepatan dalam pemrosesan data serta meningkatkan interpretasi hasil analisis.
- Dengan melakukan data preparation, hasil analisis dan model yang dihasilkan akan lebih akurat dan efektif.

![Cek-Outlier.png]( {Cek Outlier.png} )

![Heatmap.png]( {Heatmap.png} )


## Data Modelling

Model menggunakan RandomForest, karena dilakukan hyperparameter tuning, akurasi terbaik yaitu menggunakan algoritma RandomForest. Akurasi model sebesar 84% dengan nilai MSE 0,16 dan MAE 0,16. Kemudian menggunakan plot importance dengan algoritma RandomForest untuk mengetahui variabel yang paling berpengaruh terjadinya churn rate ini.

## Evaluation

Pada hasil evaluasi memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:

![CM.png]( {CM.png} )

dilihat bahwa model memiliki performa yang cukup baik, dengan nilai precision, recall, dan f1-score yang relatif tinggi untuk kedua kelas. Precision yang tinggi dapat membantu bank untuk mengidentifikasi nasabah yang berpotensi meninggalkan bank dengan lebih akurat, sehingga bank dapat mengambil tindakan preventif atau merancang program loyalty yang lebih efektif. Precision yang tinggi dapat membantu bank untuk mengidentifikasi nasabah yang berpotensi meninggalkan bank dengan lebih akurat, sehingga bank dapat mengambil tindakan preventif atau merancang program loyalty yang lebih efektif. Namun, recall untuk kelas 1 terlihat lebih rendah dibandingkan dengan kelas 0, sehingga perlu diperhatikan lebih lanjut.

![PlotImportance.png]( {PlotImportance.png} )

Pada plot importance menggunakan variabel estimated salary, surname dan creditscore merupakan 3 urutan paling tinggi, sehingga menjadi faktor penting dalam memprediksi apakah seorang nasabah akan keluar (churn) dari bank atau tidak.
Hal ini mungkin berarti bahwa faktor-faktor terkait gaji dan nama keluarga (surname) dapat menjadi faktor penting dalam memprediksi apakah seorang nasabah akan keluar (churn) dari bank atau tidak. Misalnya, nasabah dengan gaji yang lebih tinggi mungkin cenderung memiliki kecenderungan yang lebih rendah untuk keluar dari bank, atau mungkin nasabah dengan beberapa jenis nama keluarga tertentu cenderung lebih stabil dalam menjaga akun mereka di bank. Namun, perlu dicatat bahwa hal ini hanya spekulasi dan harus dilihat dengan hati-hati dalam konteks tertentu dan diuji dalam analisis yang lebih dalam.

