import cloudscraper
import time
import signal
import sys
from colorama import Fore, Style

# Fungsi untuk menangani sinyal interupsi
def signal_handler(sig, frame):
    print(f"\n{Fore.RED}Program dihentikan! Terima kasih telah menggunakan SEED Auto Claim.")
    sys.exit(0)

# Menghubungkan sinyal dengan handler
signal.signal(signal.SIGINT, signal_handler)

# Fungsi untuk klaim seed
def claim_seed(init_data):
    url = "https://elb.seeddao.org/api/v1/seed/claim"  # URL baru
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Telegram-Data": init_data
    }

    try:
        print(f"{Fore.YELLOW}Mengirim permintaan untuk klaim seed...")
        response = scraper.post(url, headers=headers)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")  # Cetak konten respons API
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}Klaim seed berhasil!")
        elif response.status_code == 403:
            print(f"{Fore.RED}Klaim seed sudah dilakukan sebelumnya atau akses ditolak.")
        else:
            print(f"{Fore.RED}Gagal klaim seed. Status code: {response.status_code}")
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan saat klaim seed: {e}")

# Fungsi untuk menghitung mundur
def countdown(t):
    while t:
        hours, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        timer = f"{hours:02}:{mins:02}:{secs:02}"
        print(f"\r{Fore.CYAN}Countdown: {timer} ", end="")
        time.sleep(1)
        t -= 1
    print(f"\r{Fore.GREEN}Waktu habis! Saatnya klaim.")

# Fungsi untuk menjalankan program
def main():
    global scraper
    scraper = cloudscraper.create_scraper()  # Inisialisasi cloudscraper
    
    print("============================")
    print(f"{Fore.CYAN}        SEED Auto Claim")
    print(f"{Fore.CYAN}   Channel : t.me/ugdairdrop")
    print("============================")

    # Membaca init_data dari file
    with open('init_data.txt', 'r') as file:
        init_data = file.read().strip()

    # Input waktu countdown sekali saja
    countdown_hours = float(input("Masukkan waktu countdown (dalam jam): "))
    countdown_seconds = int(countdown_hours * 3600)

    while True:
        try:
            # Klaim seed
            claim_seed(init_data)
            print(f"{Fore.CYAN}Menunggu {countdown_hours} jam sebelum klaim seed berikutnya...")
            countdown(countdown_seconds)  # Tunggu waktu yang ditentukan
        except Exception as e:
            print(f"{Fore.RED}Program terhenti secara tidak terduga: {e}")
            break

if __name__ == "__main__":
    main()
