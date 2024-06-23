Bu dosya, ÖSYM'nin sitesine her 15 saniyede bir istek yollar ve bir sonraki açıklanacak olan ÖSYM sınavının sonucunun sisteme yüklenip yüklenmediğini kontrol eder. 

Eğer script; sisteme yeni bir sonuç yüklendiğini tespit ederse, doğrudan sonuç sayfasını html olarak dışarı aktarır.

Sonuç dosyası olarak scriptin çalıştığı klasörün içerisine "Result.html" ismiyle aktarılır.

Gereken dependencyler yüklendikten sonra tek yapılması gereken main.py içerisindeki belirtilen yerlere TC Kimlik Numarası ve ÖSYM Ais Şifresinin yazılması.

Girdiğiniz şifre, ÖSYM AİS sisteminin kendi şifresi olmalı. EDevlet şifresiyle karıştırılmamalı. Scriptte EDevlet desteği yok.

Dependencies:
-> Selenium (https://pypi.org/project/selenium/)

Şu versiyonlarda test edildi:
Python -> 3.11.8
Selenium -> 4.22.0
Windows 11
