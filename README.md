# 🌕 Ay-Otonom-Navigasyon: Elite Mission-Ready Ekosistemi

![Görev Bannerı](assets/banner.png)

## 🌟 Modern Ay Keşif Çerçevesi

**Ay-Otonom-Navigasyon**, güneş sistemimizin en zorlu ortamları için tasarlanmış, **Elite Mission-Ready** seviyesinde bir otonom navigasyon yığınıdır. TUA ve TEKNOFEST standartlarının ötesinde, gerçek bir Ay görevi için gerekli olan **Otonom Kurtarma Davranışları** ve **Gelişmiş Arazi Modelleme** özelliklerini içerir.

---

## 📐 Matematiksel Operasyon Teorisi & Ekler

### 1. Enerji ve Sürtünme Duyarlı Yol Planlama (A*)
Maliyet fonksiyonumuz, Ay yüzeyindeki sürtünme katsayısı ($\mu$) ve regolit direncini de kapsayacak şekilde genişletilmiştir:
$$ J(n) = \sum \frac{d(n, m) \cdot S(n) \cdot E(n)}{\mu(n)} $$
- $S(n)$: Eğim maliyeti.
- $E(n)$: Enerji maliyeti (Güneş ışığı tersi).
- $\mu(n)$: Arazi sürtünme katsayısı (Kaya > Regolit > Gevşek Toz).

### 2. Durum Tahmini (EKF) Matematiksel Modeli
Navigasyon yığını, rover'ın 9 serbestlik dereceli (DOF) hareketini şu non-lineer modelle takip eder:
$$ X_{k} = f(X_{k-1}, u_{k}) + w_{k} $$
$$ Y_{k} = h(X_{k}, v_{k}) $$
Jakoben Matrisi ($F$):
$ F = \frac{\partial f}{\partial X} \bigg|_{\hat{X}_{k-1}} $

---

## 🏗️ Elite Görev Mimarisi

```mermaid
graph TD
    subgraph "Dış Katman (Algılama)"
        LiDAR[Ouster OS1] --> SLAM[Graph SLAM]
        Cam[Stereo Cam] --> Terrain[Arazi Sınıflandırma]
    end

    subgraph "Karar & Strateji"
        Terrain --> Planner[Gelişmiş A*]
        Recovery[Otonom Kurtarma] --> MM[Görev Yöneticisi]
        MM --> Planner
    end

    subgraph "Fiziksel Eylem"
        Planner --> Controller[Hybrid DWA]
        Controller --> Actuators[Motor Sürücüleri]
    end
```

---

## 🛡️ Otonom Kurtarma ve Güvenlik (FDIR+)

Sistem, beklenmedik durumlarda rover'ın güvenliğini sağlayan ileri düzey protokoller içerir:
- **ShakeToClear:** Tekerlekler regolitte %30'dan fazla kayma (slip) yaparsa devreye giren titreşim manevrası.
- **ThermalSafeDrift:** Robot çekirdek sıcaklığı 70°C'yi aşarsa otonom olarak gölge bölgeye geçiş.
- **Graph SLAM Check:** SLAM belirsizliği kritik eşiği geçerse "Yerinde Dönme" (In-place Rotation) ile veri toplama.

---

## 🌑 Görev Yaşam Döngüsü (Mission Lifecycle)

```mermaid
stateDiagram-v2
    [*] --> Kontrol_Testi
    Kontrol_Testi --> Konumlandırma : Başarılı
    Konumlandırma --> Yol_Planlama : CBL Doğrulandı
    Yol_Planlama --> Hareket : Rota Onaylandı
    Hareket --> Engel_Kacınma : Engel Tespit
    Engel_Kacınma --> Hareket
    Hareket --> Kurtarma_Modu : Sıkışma/Hata
    Kurtarma_Modu --> Hareket : Kurtarıldı
    Hareket --> Hedef_Ulasıldı : Hedef 1m
    Hedef_Ulasıldı --> [*]
```

---

## 📦 Kurulum ve Profesyonel Yapılandırma

### Sistem Gereksinimleri
- **ROS2:** Humble (Ubuntu 22.04)
- **Kütüphaneler:** NumPy, SciPy, Matplotlib
- **Donanım:** NVIDIA Jetson Orin / Xavier

### Kurulum
```bash
git clone https://github.com/arch-yunus/Ay-Otonom-Navigasyon.git
colcon build --symlink-install
source install/setup.bash
```

---

## 📜 Katkıda Bulunma ve Yönetişim
Daha fazla detay için [CONTRIBUTING.md](CONTRIBUTING.md) ve [MISSION_OPERATIONS.md](docs/MISSION_OPERATIONS.md) dosyalarını inceleyebilirsiniz.

---

<p align="center">
  <b>Geleceğin Ay Altyapısını Bugün İnşa Ediyoruz</b><br>
  <i>Yunus-Arch Uzay Teknolojileri Ar-Ge Merkezi © 2026</i><br>
  <i>"Per Aspera Ad Astra"</i>
</p>
