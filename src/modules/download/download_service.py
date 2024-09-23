
from yt_dlp import YoutubeDL

class DowloadService():
        
    def download_video(video_url):
        ydl_opts = {
            'format': 'best',  # Seleciona a melhor qualidade de vídeo
            'outtmpl': '%(title)s.%(ext)s',  # Define o nome do arquivo de saída
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    # Exemplo de uso

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
DowloadService.download_video(video_url)