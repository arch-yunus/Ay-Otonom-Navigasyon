# Görev Operasyonları Kılavuzu: Ay-Otonom-Navigasyon

## 1. Görev Öncesi Hazırlık (L-Minus)
- **Pil Kontrolü:** Minimum %90 doluluk.
- **Sistem Check:** `ros2 run ay_otonom_navigasyon fdir_node` komutuyla sağlık kontrolü.
- **Kalibrasyon:** IMU ve LiDAR kalibrasyon verilerinin doğrulanması.

## 2. Otonom Görev Başlatma
Görevi başlatmak için:
```bash
ros2 launch ay_otonom_navigasyon mission.launch.py goal_x:=10.5 goal_y:=25.0
```

## 3. Kurtarma Prosedürleri (Emergency)
Rover sıkıştığında sistem otomatik olarak `recovery_node` üzerinden kurtarma manevraları yapar. Manuel müdahale gerekiyorsa:
1. `teleop_node` kullanılarak manuel kontrol alınır.
2. `fdir_node` logları incelenerek hata kaynağı tespit edilir.

## 4. Veri Kaydı ve Analiz
Görev sonrasında telemetry verileri `log/` klasöründe saklanır. Bu veriler `analysis_tools/` scriptleri ile görselleştirilebilir.
