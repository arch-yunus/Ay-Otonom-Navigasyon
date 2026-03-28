# Sistem Mimarisi: Ay-Otonom-Navigasyon

## 1. Konumlandırma ve Haritalama (SLAM)
Navigasyon yığını hibrit bir yaklaşım kullanır:
- **Birincil:** Yerel engel kaçınma için LiDAR tabanlı SLAM.
- **İkincil:** Küresel sürüklenme düzeltmesi için krater desenlerini kullanan Arazi Göreceli Navigasyon (TRN).

## 2. Yol Planlama Stratejisi
Algoritmalar şu kriterlerle kısıtlanmıştır:
- **Eğim Açıları:** Güvenlik için maksimum 20 derece.
- **Güç Tüketimi:** Yol uzunluğu ve arazi zorluğu analizi.
- **Tehlikeli Bölgeler:** Gölgeler (güneş enerjisi kaybı) ve dik kraterler.

## 3. Sensör Füzyonu (EKF)
Gelişmiş Kalman Filtresi (EKF) şunları entegre eder:
- Tekerlek Odometrisi (Düşük frekans)
- IMU (Yüksek frekans)
- Görsel Odometri (Stabilite)
- Ay Yıldız Takibi (Mutlak Yönelim)

## 4. Simülasyon Ortamı
`sim/` klasörü, **Shackleton Krateri** bölgesi için Gazebo konfigürasyonlarını sağlar:
- 1/6g Yerçekimi.
- Regolit toprak modellemesi.
- Düşük açılı ışıklandırma koşulları.
