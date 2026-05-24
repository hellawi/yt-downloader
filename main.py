import yt_dlp

def download_video(url: str, output_dir: str = "."):
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "format": "best",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    while True:
        url = input("Введите ссылку на YouTube: ")
        download_video(url)

        answer = input("\nХотите скачать ещё? (y/n): ").strip().lower()
        if answer != "y":
            print("Программа остановлена.")
            break