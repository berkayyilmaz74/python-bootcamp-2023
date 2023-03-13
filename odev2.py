# Ödev 2: Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

print("**********************************************")

# Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
ogrenciList=["Berkay Yılmaz","Tuncay Kalkmaz","Hüsnü Çoban","Mesut Oduncu","Hayriye Tutmaz","Naciye Pekmez"]
print("**1**")
print(ogrenciList)

    
# Aldığı isim soy isim ile eklenen öğrenci
ogrenciList.append("Nurullah Aslan")
print("**2**")
print(ogrenciList)

# Aldığı isim soy isim ile listeden kaldıran
print("**3**")
ogrenciList.remove("Nurullah Aslan")
print(ogrenciList)

# Listeye birden fazla öğrenci ekleme
ogrenciList.extend(["Nurullah Aslan","Sultan Coşar"])
print("**4**")
print(ogrenciList)

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
print("**5**")
for sinifim in ogrenciList:
    print(sinifim)

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
print("**6**")
i=0
while i <len(ogrenciList):
    print( str(i) + " No'lu Ogrenci "+ ogrenciList[i])
    i+=1

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
print("**7**")

for i in range(len(ogrenciList)-1, -1, -1):
    print(str(i) + " No'lu Ogrenci " + ogrenciList[i] + " listeden silindi.")
    del ogrenciList[i]
print("**8**")
print(ogrenciList)