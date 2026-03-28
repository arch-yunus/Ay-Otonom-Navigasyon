# Teknik Spesifikasyonlar: Ay-Otonom-Navigasyon

## 1. Yazılım Yığını
| Bileşen | Uygulama | Versiyon/Metrik |
| :--- | :--- | :--- |
| Çekirdek Dil | Python | 3.10+ |
| Ara Yazılım | ROS2 | Humble / Foxy |
| Matematik Motoru | NumPy / SciPy | Endüstriyel Sınıf |
| Yerel Planlayıcı | DWA | 10Hz Güncelleme Hızı |
| Küresel Planlayıcı | A* | Çok Kısıtlı (Enerji/Eğim) |

## 2. Donanım Uyumluluğu (Doğrulanmış)
- **Birincil LiDAR:** Ouster OS1-64 veya Velodyne VLP-16.
- **Stereo Vizyon:** Intel RealSense D435i (Radyasyon korumalı kasa önerilir).
- **IMU:** Bosch BNO055 veya yüksek hassasiyetli Honeywell HG1120.
- **Hesaplama:** NVIDIA Jetson Orin (Edge Computing) veya radyasyon korumalı Xilinx FPGA.

## 3. Fiziksel Kısıtlar
- **Yerçekimi:** $1.622 m/s^2$
- **Regolit Yapışkanlığı:** 0.1 - 1.0 kPa
- **Min Çalışma Sıcaklığı:** -230°C (Isıtıcılar ile)
- **Max Çalışma Sıcaklığı:** +120°C (Radyatör kanatçıkları ile)

## 4. Haberleşme Gecikmesi
| Bağlantı Tipi | Mesafe | Gecikme (Tipik) |
| :--- | :--- | :--- |
| Dünya-Ay (Uzak) | 384,400 km | 1.28 s (tek yön) |
| Yerel Mesh (Rover-Rover) | < 5 km | < 10 ms |
