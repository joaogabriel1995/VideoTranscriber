from yt_dlp import YoutubeDL

class DownloadService:
    def __init__(self, ydl_opts=None):
        self.ydl_opts = ydl_opts or {
            'format': 'best',  # Seleciona a melhor qualidade de vídeo
            'outtmpl': '%(title)s.%(ext)s',  # Define o nome do arquivo de saída
        }

    def download_video(self, video_url):
        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([video_url])
            print(f"Download completo para: {video_url}")
        except Exception as e:
            print(f"Erro ao baixar {video_url}: {e}")
