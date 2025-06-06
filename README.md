🖥️ Linux System Info Collector

Bu Python scripti, SSH üzerinden uzak bir Linux sunucusuna bağlanarak temel sistem bilgilerini toplar ve system_info.txt dosyasına kaydeder.

---

🚀 Özellikler

- CPU bilgisi (lscpu)
- Bellek durumu (free -h)
- Disk kullanımı (df -h)
- Sistem çalışma süresi (uptime)
- İşletim sistemi bilgisi (cat /etc/os-release)

---

🔧 Kullanım

1. Repo'yu klonlayın veya dosyayı indirin:
   git clone https://github.com/ebubekirbastama/linux-system-info-collector.git
   cd linux-system-info-collector

2. collect_system_info.py dosyasını açın ve SSH bağlantı bilgilerinizi girin:
   host = "sunucu_ip_adresi"
   port = 22  # Veya sunucunuzun SSH portu
   user = "root"
   password = "şifreniz"

3. Gerekli Python kütüphanesini yükleyin:
   pip install paramiko

4. Scripti çalıştırın:
   python collect_system_info.py

5. Bilgiler system_info.txt dosyasına kaydedilecektir.

---

🛡️ Güvenlik Uyarısı

- SSH bilgilerinizi güvende tutun.
- Scripti sadece güvenilir ağlarda kullanın.
- Geliştirmeler ve iyileştirmeler için katkıda bulunabilirsiniz!

---

🤝 Katkıda Bulunma

Pull request'ler, issue'lar ve öneriler her zaman hoş karşılanır!

---

📜 Lisans

MIT License © 2025 Ebubekir Bastama

---

✨ İyi kodlamalar! ✨
