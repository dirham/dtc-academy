# Intro Programming With Python


### Variable

Adalah lokasi penyimpanan dan terkait nama simbolis yang berisi beberapa kuantitas yang diketahui atau tidak diketahui atau informasi, nilai. (wikipedia). Dengan kata lain variable adalah sebuah wadah yang di gunakan untuk menampung sebuah nilai (tipe data). Contoh pendeklarasian variable di pyhton :

```nama_variable = tipe data```

pada bagian seblah kiri kita menentukan nama variable, kemudian `=` adalah operator assigment, yang artinya pemberian nilai, nilai yang dimaksudkan adalah `tipe data`. lebih jelasnya mari kita membuat variable dengan memberikan nilai `string`, `int`, `float` kedalamnya.

```python
nama = "baco" 
umur = 20 
tinggi = 167.5 
```
Pada baris pertama kita membuat variable `nama` yang bertipe data `str` dan nilai `baco`. baris kedua dan ketiga kita membuat variable dengan tipe data `int` dan `float` dengan nilai `20` dan `167.5`.

### Comment atau Komenter
Komentar pada bahasa pemrograman digunakan sebagai dokumentasi kode yang kita tulis, setiap baris komentar yang kita tulis akan di abaikan oleh *python interpreter* menjadikan baris komentar tidak akan di eksekusi (dijalankan).
contoh komentar :
> `#` dengan menggunakan hastag (#) maka baris kode ini tidak akan di jalankan
> jika kita membutuhkan komentar yang lebih panjang dan lebih dari satu baris maka kita bisa menggunakan single quote (**'**) sebanyak 3 kali (**'''**), baris komentar di masukkan di antara (**'''**) dan (**'''**). perhatikan bahwa anda harus menutup kembail dengan **'''** ketika membuat komentar multi line.

### Bermain dengan string

kita telah mengetahui bagai mana membuat sebuah variable dengan tipe data string `nama = "baco"`. pada bagian ini kita akan coba bermain - main dengan `string`.
silahkan buka VSCode dan buat file baru bernama **coba_string.py** ketikan kode berikut :
```python
nama = "Baco"
umur = 40

#buat variable baru untuk menampung panjang karakter yang ada pada variable nama
hitung_karakter_nama = len(nama)
#menggunakan perintah print() untuk menampilkan data ke layar
print(hitung_karakter_nama)
#variable baru untuk merubah umur menjadi str
umur_to_str = str(umur)
#tampilkan tipe data umur sebelum di rubah.
print(type(umur))
#tampilkan tipe data setelah di rubah
print(type(umur_to_str))
#membuat variable `nama` menjadi huruf kecil
print(nama.lower())
#membuat variable `nama` menjadi huruf besar
print(nama.upper())

```

### Flow Control

Kadang kala kita ingin melakukan kontrol pada aplikasi kita berdasarkan data yang telah atau akan di terima. Hal ini memungkinkan kita untuk mengatur bagaimana aplikasi yang kita buat merespon setiap masukan data yang berbeda - beda.

Pada python kita dapat mengontrol bagaimana aplikasi kita meresponse dengan menggunakan perintah `if`, `else` dan `elif`.

mari kita lihat bagaimana cara penggunaannya, buat file baru bernama **if_else.py** :
```python
umur = 20

if umur <= 17:
    print("anda masih di bawah umur!")
else:
    print("Yey, Anda sudah Dewasa, selamat menikmati kehidupan nyata!")
```
pada kode program diatas kita mendeklarasikan `block` code dengan menggunakan sintaks `if` dan `else`. perhatikan bahwa ada spasi diantara baris `if` dan `print`. jarak yang di buat pada baris tersebut menandakan bahwa perintah `print` yang ada di bawah `if` adalah bagian dari pada `code block if`. dalam python hal ini disebut **`indent`**.

Berikutnya kita akan mencoba menggunakan `elif`, buka kembali **if_else.py** dan rubah kode yang ada di dalamnya menjadi seperti berikut :

```python
umur = 20

if umur_int <= 17:
    print("di bawah umur")
elif umur_int >= 20 and umur_int <=30:
    print("Jomblo masih di toleransi!")
elif umur_int > 35 and umur_int <= 37:
    print("lampu kuning")
else:
    print("perbanyak berdoa dan sedekah")
```

silahkan jalankan dan lihat hasil yang di keluarkan.

##### penjelasan :
pada kode sebelumnya kita telah membahas tentang `if, else dan indent`, nah pada kode diatas kita melihat ada beberapa hal baru diantaranya (`<, >, <=, and, elif`).
pada python ada beberapa operator (operan) yang di gunakan untuk membandingkan sebuah nilai.
`<` : lebih kecil dari
`>` : lebih besar dari
`<=` : lebih kecil atau sama dengan
`>=` : lebih besar atau sama dengan
`==` : identik sama dengan
`!=` : tidak sama dengan
selain operator pembanding ada pula boolean operator
`and` : jika dua kondisi (operan)terpenuahi maka `True` jika salah satu salah maka `False`. contoh penggunaan : `umur < 20 and umur > 25`
`or` : jika salah satu dari kondisi (operan) terpenuhi maka `True` jika keduanya salah maka `False`. contoh penggunaan : `umur < 20 or umur > 17`
`not` : jika bukan. contoh : `print(umur is not 30)`

pada kode diatas juga terdapat keyword `elif`, keyword ini digunakan jika kita ingin melakukan pengecekan kondisi lebih dari satu kali.

##### Try this one :
```python
umur = input("masukkan umur : ")

umur_int = int(umur)
if umur_int <= 17:
    print("di bawah umur")
elif umur_int >= 20 and umur_int <=30:
    print("Jomblo masih di toleransi!")
elif umur_int > 35 and umur_int <= 37:
    print("lampu kuning")
else:
    print("perbanyak berdoa dan sedekah")
```

##### try at home :
```python
if 1 < 2:
    if 2 < 3:
        print("ntaps! pinter")
    else:
        print("lah, belajar matematika dimana?")
else:
    print("tidak mungkin ini terprint")
```

### List, Tupel dan Dictionary
- list 
    Python secara default tidak mengenal `array` seperti pada bahasa pemrograman lainnya tetapi menganal tipe data `list`.
    list merupakan sekumpunlan dataa atau tipe data. untuk lebih jelasnya bisa di litah pada baris kode berikut :
    `mylist = ['Baco', 20, 160.7]`. Dengan list kita dapat menampung banyak data dangan berbagai jenis tipe data sekaligus. Untuk lebih lanjut tentang `list` silahkan buka editor dan buat file baru bernama **list_python.py** :
    ```python
    mylist = ['baco', 20, 160.6]
    # tampilkan isi mylist
    print(mylist)
    # mengambil isi dari mylist
    print(mylist[0])
    ```
    **index** untuk mengakses data dalam sebuah list kita bisa menggunakan index. index pada sebuah list selalu diawali dengan 0. jadi untuk mengakses string `baco` pada mylist cukup menuliskan mylist[0]. perlu di perhatikan bahwa setiap data dalam `list` selalu di pisakhan dengan comma (`,`).

- tupel
    seperti pada `list` tupel juga merupakan data struktur pada python yang dapat menyimpan berbagai macam data dan tipe data. contoh penggunaannya adalah sebagai berikut : `mytupel = ("susi", "sisu", "usis")`. lalu apa perbedaan tupel dan list? pertama dari cara pembuatannya. jika pada list kita menggunakan `[]` maka pada tupel kita menggunakan `()`. selain dari cara pembuatannya. yang membuat tupel dan list menjadi sangat berbeda adalah. pada list kita bisa merubah nilai dari isinya, sedangkan pada tupel tidak bisa.
    selain dari pada perbedaan diatas tupel dan list memiliki persamaan yang sangat banyak mulai dari mengakses data yang sama-sama menggunakan index dari 0.
- dictionary
    Sayangnya pada tupel dan list kita kita hanya bisa mengakses data menggunakan index mulai dar `0 - len()-1`. Pertanyaannya, lalu bagaimana jika saya ingin membuat data yang dapat diakses sesuai nama/index yang saya tentutkan? jawabannya adalah dengan dictionary.
    berikut contoh penggunaannya : `mydic = {"nama": "Baco", "umur": 20, "tinggi": 167.7}`

### Function