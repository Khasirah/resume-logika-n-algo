# Metode divide and conquer

## metode D and C

### divide

1. mimilah data nilai elemen dari rankaian data menjadi dua bagian dan mengulangi pemilahan hingga satu elemen terdiri dari maksimal dua nilai

### conquer

1. mengurutkan masing-masing data nilai elemen

### prinsip dasar

1. membagi n input menjadi k subset input yang berbeda (1 < k <= n)
2. k subset input tersebut akan terdapat k subproblem
3. setiap subproblem mempunyai solusi menjadi k subsolusi
4. dari k subsolusi akan mendapatkan solusi yg optimal

### metode D and C

1. menggunakan rekursif dengan membagi masalah menjadi dua atau lebih submasalah
2. masalah umum seperti pengurutan dan perkalian
3. jenis metode:
    1. merge sorting
    2. quick sorting
    3. binary search
    4. teknik d and c

## merge sort

1. menggabungkan 2 array yang sudah terurut
2. membutuhkan fungsi rekursif untuk penyelesaian
3. prinsip kerja:
    1. kelompokkan deret bilangan kedalam 2 bagian, 4 bagian, 8 bagian, dst sampai tinggal sendiri
    2. lakukan pengurutan sesuai dengan kelompok sebelumnya
    3. lakukan pengurutan sejumlah pembagian

```python
def mergerSort(x):
    print(f"bilangan diurutkan: {x}")
    panjang_x = len(x)
    if panjang_x > 1:
        mid = panjang_x // 2
        sisi_kiri = x[:mid]
        sisi_kanan = x[mid:]
        mergerSort(sisi_kiri)
        mergerSort(sisi_kanan)
        i = j = k = 0
        while i < len(sisi_kiri) and j < len(sisi_kanan):
            if sisi_kiri[i] < sisi_kanan[j]:
                x[k] = sisi_kiri[i]
                i += 1
            else:
                x[k] = sisi_kanan[j]
                j += 1
            k += 1

        while i < len(sisi_kiri):
            x[k] = sisi_kiri[i]
            i += 1
            k += 1

        while j < len(sisi_kanan):
            x[k] = sisi_kanan[j]
            j += 1
            k += 1
            print(f"merge: {x}")

arr = [22,10,15,3,8,2]
mergerSort(arr)
print(arr)
```

## quick sorting

1. metode sort tercepat
2. diperkenalkan oleh **CAR Hoare** 
3. konsepnya membuat bagian2, sort dilakukan perbagian
4. pemilihan **pivot** merupakan hal yang menentukan apakah algoritma quicksort akan memberikan performa terbaik atau terburuk (Nugrehey)
5. printsip kerja:
    1. pilih sembarang elemen kita sebut X
    2. tempatkan X pada posisi J
    3. tambahkan elemen yg lebih kecil dari X ke J-1
    4. tambahkan elemen yg lebih besar dari X ke J+1
    5. sekarang kita memiliki kumpulan elemen yg lebih kecil dari X dan kumpulan yg lebih besar dari X
    6. lakukan langkah nomor satu kestiap kumpulan sampai tidak tersisa 1 elemen
    7. gabungkan kembali elemen2 yg sudah terurutkan tersebut

```python

```
