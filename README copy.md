# Projek Juli DATA ENGINEER - Kalbe Nutritionals

### 1. 	Membuat script melalui shell/bash untuk melakukan pengecekan direktori apakah ada didalam path yang sudah ditentukan 

```bash
path="D:\PROJEK\RAKAMIN\DE - Kalbe\pindah" #Menentukan variabel path 
name_of_directory="pindah" #Memberikan nama pada direktori
dir="$path/$name_of_directory" #Memmbuat variabel berupa path direktori 
```

#### Pengecekan apakah direktori sudah ada

```bash
if [ -d "$dir" ]; then
    echo "Ada direktori $name_of_directory!" #Mengirimkan pesan bahwa ada direktori tersebut
else
    echo "Direktori $name_of_directory Tidak Ada!" #Mengirimkan pesan bahwa direktori tidak ada
    exit 1
fi
```

#### Dilakukan setup penjadwalan setiap jam 7 pagi

```bash
Dengan menggunakan crontab -e pada bash WSL, kemudian ditambahkan
00 07 * * * root rakamin1.sh
```

Artinya pada setiap jam 7 pagi akan menjalankan script rakamin1.sh dengan hak root

### 2.	Masih menggunakan script shell/bash pada nomor 1, menambahkan kondisi lain jika direktori ada didalam path seperti ;

```bash
# Variabel
path="D:\PROJEK\RAKAMIN\DE - Kalbe\pindah" #Menentukan variabel path 
name_of_directory="pindah" #Memberikan nama pada direktori
dir="$path/$name_of_directory" #Memmbuat variabel berupa path direktori 
filename_csv="KalbeSales.csv" #File target
source_dir="d:/PROJEK/RAKAMIN/DE - Kalbe" #Source file target

# Cek apakah direktori sudah ada
if [ -d "$dir" ]; then
    echo "Ada direktori $name_of_directory!"
    cp "$source_dir/$filename_csv" "$dir" #Jika ada maka dilakukan duplikasi data ke variabel dir
    echo "File Pindah Berhasil" 
else
    echo "Direktori $name_of_directory Tidak Ada!"
    mkdir "$dir" #Jika tidak ada maka membuat direktori baru, dari variabel yang sudah ditentukan
    exit 1
fi
```

### 3.	Melengkapi syntax(yang ditandai) untuk memasukkan data dari Python ke Mysql

```python
# Melakukan import mysql connector
import mysql.connector

#Melakukan percobaan percobaan koneksi
conn = mysql.connector.connect(
    user='username',
    password='password',
    host='localhost',
    database='database_name'
)

#Membuat object cursor sebagai penanda
cursor = conn.cursor()

#Deklarasi SQL Query untuk memasukkan record ke DB (KARYAWAN)
insert_sql = (
    'INSERT INTO KARYAWAN (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)'
    'VALUES (?, ?, ?, ?, ?)'
)

values = ("John", "Doe", 24, "Male", 5000)

try:
    # Eksekusi SQL Command
    cursor.execute(insert_sql, values)

    # Melakukan perubahan (commit) pada DB
    conn.commit()
    print("Data berhasil dimasukkan!")
except Exception as e:
    # Rollback apabila ada issue
    conn.rollback()
    print("Error:", e)

# Menutup koneksi
conn.close()
```

### 4.	Konversi intruksi ini untuk Bahasa SQL

```sql
CREATE DATABASE KALBE; #Membuat database dengan nama ‘KALBE’
USE KALBE; #Menggunakan database KALBE
#Proses Membuat Tabel Inventory
CREATE TABLE Inventory( 
    Item_code INT PRIMARY KEY,
    Item_name VARCHAR(100),
    Item_price DECIMAL(10,2),
    Item_total INT
);

INSERT INTO Inventory (Item_code, Item_name, Item_price, Item_total) 
VALUES 
    (2341, 'Promag Tablet', 3000, 100),
    (2342, 'Hydro Coco 250ML', 7000, 20),
    (2343, 'Nutrive Benecol 100ML', 20000, 30),
    (2344, 'Blackmores Vit C 500Mg', 95000, 45),
    (2345, 'Entrasol Gold 370G', 90000, 120);

#Menampilkan Item_name dengan Item_total tertinggi

SELECT Item_name FROM Inventory 
    WHERE Item_total = (
        SELECT MAX(Item_total) FROM Inventory
    );

#Mengupdate Item_price dengan Item_total tertinggi

UPDATE Inventory
    SET Item_price = 77500
    WHERE Item_total = (
        SELECT MAX(Item_total) FROM Inventory
    );

#Menghapus Item_name yang memiliki Item_total paling sedikit

DELETE Invetory
    WHERE Item_total = (
        SELECT MIN(Item_total) FROM Inventory
    );

```

#### Apa yang terjadi jika dimasukkan Item_name lain pada Item_code 2343 di table Inventory ?

Terjadi error, karena melakukan insert data dengan Item_code = 2343, yang dimana Item_code bersifat PRIMARY KEY, tidak memiliki duplikat atau nilai unik, kecuali dilakukan update data dengan Item_name baru, maka akan terupdate.

### 5.	Membuat Query SQL dengan menampilkan semua pesanan customer dimana purchase_amount kurang dari 100 atau diluar pesanan melebihi tanggal 25 Agustus 2022 dan customer_id diatas 2001

```sql
SELECT *
    FROM customer_table
    WHERE purchase_amount < 100 OR 
        (DATE(order_date) < '2022-08-22' AND INT(customer_id) > 2001);

```

### 6.	Jelaskan kelasahan gambar dan berikan solusi terbaik pada case ini.

![](img\soal6.png)

ddPlant (nvarchar(max), null) artinya kolom ddPlant memiliki tipe data “varchar” dan dapat NULL, namun sepertinya kesalahannya pada General Information pilihan Plant memilih nilai “Belawan”, namun outputnya pada kolom ddPlant, nilai “Surabaya” masuk dalam pilihan tersebut. Solusi terbaik adalah dicek Kembali pada options plant, asumsi saya option plant berjenis centang/klik namun pada tampilan menampilkan abjad teratas sehingga Surabaya masuk dalam list output.

### 7.	Membuat sebuah star schema pada database KALBE dengan memiliki 1 fact table dan 5 dimension table menggunakan Physical Data Model Theory

![](img\fact_table.png)


