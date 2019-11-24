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

### Loop
Pada python terdapat dua cara untuk melakukan perulangan atau loop, yaitu dengan `while` dan `for`
- While
  Contoh perulangan `while` :
  ```python
    # Membuat Tupel

    # Membuat List
    tupel_bahasa_pemrograman = ("Python", "Ruby", "PHP", "JAVA", "Javascript", "Golang", "C", "C++", "C#")
    # defenisikan variable i = 0
    i = 0
    # perulangan "loop" dengan while untuk menampilkan datanya
    while i < len(tupel_bahasa_pemrograman):
    print(tupel_bahasa_pemrograman[i])
    # menambahkan nilai satu pada variable i setiap kali perulangan
    i = i+1
  ```
- For
  Contoh Perulangan `for` :
  ```python
    list_bahasa_pemrograman = ("Python", "Ruby", "PHP", "JAVA", "Javascript", "Golang", "C", "C++", "C#")
    for bhs_pemrograman in list_bahasa_pemrograman:
        print(bhs_pemrograman)
  ```

### Function
- Cara mendefenisikan function
  pertama buat file bernama coba_func.py
    ```python
        # membuat fungsi tanpa parameter dan nilai kembalian (return)
        def nama_function_bebas():
            print("saya adalah function/fungsi")

        # membuat fungsi dengan parameter dan nilai kembalian
        def nama_function_bebas_dengan_param(a,b):
            return a + b
        
    ```
- Cara memanggil function di file yang sama
    ```python
        # jika memanggil fungsi di file yang sama cukup tuliskan nama fungsinya dan masukkan parameternya jika ada, jika tidak ada paramter kosongkan
        
        nama_function_bebasnama_function_bebas() # akan memprint : saya adalah function/fungsi
        hasil = nama_function_bebas_dengan_param(1,2) # 1 adalah nilai yang di berikan ke pada parameter a dan 2 adalah nilai untuk param b
        print(hasil) # akan mengeluarkan nilai dari return a + b yaitu 1 + 2
    ```
- Cara memanggil function di file yang berbeda
    ```python
        # import seperti yang pernah di bahas, digunakan untuk memanggil isi file python lain
        from coba_func import nama_function_bebas, nama_funciton_bebas_dengan_param

        # setelah di import maka kita tinggal memanggil fungsinya
        nama_function_bebasnama_function_bebas() # akan memprint : saya adalah function/fungsi
        hasil = nama_function_bebas_dengan_param(1,2) # 1 adalah nilai yang di berikan ke pada parameter a dan 2 adalah nilai untuk param b
        print(hasil) # akan mengeluarkan nilai dari return a + b yaitu 1 + 2
    
### Class

- Hal - hal yang perlu di perhatikan pada `class` untuk materi ini
  1. Object
  2. Constructor __init__
  3. Attribute
  4. Method
  5. Inheritance
  6. Property, Setter & Getter
1. Object dibuat dengan `constructor` pada sebuah class
2. Constructor 
   consturctor adalah method spesial pada class python, setiap kita mendeklarasikan/membuat class baru maka python otomatis akan membuat constructor method (default) tanpa perameter.
   untuk mendeklarasikan constructor secara explisit maka buat sebuah function dengan nama `__init__():`
   contoh :
   ```python
    class Human:
        def __init__():
            pass
   ```
3. Attribute
   Attribute adalah `variable` yang di defenisikan dalam sebuah `class` 
   pada python terdapat `access modifier` atau hak akses pada sebuah atribut, contoh pembuatan attribute beserta hak aksesnya.
   ```python
    class Motor:
        def __init__(self):
            print ("Di statar")
            self.nama = "Jirayya" # public sesuai nama, 
            self.__pembuat = "Kappa" # private, hanya dapat di akses lewat class itu sendiri
            self._keluaran = 2019 # protected, hanya bisa di akses lewat class itu sendiri dan turunannya.
    ```

4. Method
   Method adalah fungsi yang di defenisikan di dalam `body class`, kita telah membahas bahwa `__init__()` adalah spesial method pada `class` python, nah untuk mendefenisikan method di dalam sebuah class tidak lah sulit, pembuatannya sama saja dengan sebuah `function` biasa hanya saja dibuat di dalam `class`. contoh :
   ```python
    class Motor:
        def __init__(self):
            print ("Di statar")
            self.nama = "Jirayya"
            self.__pembuat = "Kappa"
            self._keluaran = 2019
        def nge_gas(self,type_kenalpot):
            if type_kenalpot == "bogar":
                print("brooombbbbbbbbooooomm.. brooombbbbbbbbooooomm.. brooombbbbbbbbooooomm." )
            else:
                print("ngeengggg... ngeenngg.. ngeenngg...")

        # panggil class
        motor_ari = Motor()

        print(motor_ari.nama)
        motor_ari.nge_gas("bogar")
        motor_ari._keluaran = "mm"
        print(motor_ari._keluaran) # protected atribute masih bisa di panggil atau di ubah.
        #print(motor_ari.__pembuat) # hilangkan komentar dan coba jalankan
    ```
5. Inheritance
   Inheritance atau pewarisan, sebuah `class` dapat mewariskan attribute dan method. caranya adalah dengan melalu pewarisan. di python cara untuk melakukan pewarisan adalah sebagai berikut: 
   ```python
   # class Vehicle adalah induk class
    class Vehicle:
        def vehicle_method(self):
            print("Halo saya induknya class")

    # Car adalah turunan (child) dari Vehicle
    class Car(Vehicle):
        def car_method(self):
            print("Saya turunannya class Vehicle, dipanggil dari method car_method pada class Car")

    # sama sepeerti car, Cycle juga turunan dari Vehicle
    class Cycle(Vehicle):
        def cycle_method(self):
            print("Saya turunannya class Vehicle, dipanggil dari method cycle_method pada class Cycle")

    cycle = Cycle()
    cycle.vehicle_method()
    cycle.cycle_method()
    ```
    ### Review Knowledge 

    1. Final project 1
    kita telah belajar tentang list, tupel, dan dict sebelumnya. dengan bekal materi itu buatlah sebuah data structur baru yang bernama linkedList. mengapa dan apa? pada list/array ada beberapa kekurangan salah satunya adalah ketika kita melakukan insert `sebuah_list.insert(1, 10)` maka yang terjadi di balik layar adalah python akan melakukan `loop` untuk menyusun ulang listnya. berbeda dengan list, linkedList mengetahui `siap dan apa` yang berada di sebelah kanannya, jadi ketika kita menginsertkan sebuah data maka akan lebih operasi yang terjadi adalah simpan nilai dari posisi index lama, masukkan nilai baru dan geser index lama ke sebelah kanan, begitu setursnya. Tugas anda adalah membuat sebuah class linkedList

    1. Final project 2
    Buat sebuah program yang akan menerima inputan a dan b, asumsikan adalah nilai pada `a` dan `b` adalah bilangan bulat 1-1000. program harus meng-genrate random data contoh `[38,90,34,75]` dengan nilai di dalam list tidak boleh kurang dari nilai `a` dan tidak boleh lebih besar dari nilai `b`. setalah mendapatkan nilai random urutkan nilai tersebut, program harus memprint nilai random dan nilai yang telah di urutkan!
    ```
    hint : 
     - random
     - perulangan
     - function/class/method
    ```