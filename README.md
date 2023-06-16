# UnluUyumuSorgula Sınıfı

Bu kod, Türkçe dilindeki ünlü uyumunu sorgulayan bir `UnluUyumuSorgula` sınıfını içerir. Sınıf, çeşitli ünlü uyumu kurallarını kontrol eder ve sonuçları ekrana yazdırır.

## Fonksiyonlar

- `__init__(self, kelime)`: Sınıfın başlatıcı metodu. İlk olarak, ünlü uyumu sorgulanabilirliğini kontrol eder ve sonrasında çeşitli ünlü uyumu kurallarını kontrol eden diğer fonksiyonları çağırır.

- `UyumIncelenimiSorgula(self, kelime)`: Verilen kelimenin ünlü uyumunun incelenip incelenemeyeceğini kontrol eder.

- `BuyukUnluUyumuKalinlikItibariyleKontrolu(self, kelime)`: Verilen kelimenin büyük ünlü uyumu kuralına kalınlık açısından uyup uymadığını kontrol eder.

- `BuyukUnluUyumuIncelikItibariyleKontrolu(self, kelime)`: Verilen kelimenin büyük ünlü uyumu kuralına incelik açısından uyup uymadığını kontrol eder.

- `BuyukUnluUyumuKontrolu(self, kelime)`: Verilen kelimenin büyük ünlü uyumu kuralına uyup uymadığını kontrol eder.

- `KucukUnluUyumuDuzlukItibariyleKontrolu(self, kelime)`: Verilen kelimenin küçük ünlü uyumu kuralına düzlük açısından uyup uymadığını kontrol eder.

- `KucukUnluUyumuYuvarlaklikItibariyleKontrolu1(self, kelime)`: Verilen kelimenin küçük ünlü uyumu kuralına yuvarlaklık açısından uyup uymadığını kontrol eder.

- `KucukUnluUyumuYuvarlaklikItibariyleKontrolu2(self, kelime)`: Verilen kelimenin küçük ünlü uyumu kuralına yuvarlaklık açısından uyup uymadığını kontrol eder.

## Kullanım

Aşağıdaki örnekte, `UnluUyumuSorgula` sınıfı bir örnekleme yapılıyor ve sınıfın çeşitli ünlü uyumu kurallarını kontrol eden fonksiyonları çağırılıyor:

```python
ornek = UnluUyumuSorgula("hakkı")
