import os
from yt_dlp import YoutubeDL

class DownloadService:
    def __init__(self, ydl_opts=None):
        self.ydl_opts = ydl_opts or {
            'format': 'best',  # Seleciona a melhor qualidade de vídeo
            'outtmpl': './.tmp/%(title)s.%(ext)s',  # Define o nome do arquivo de saída
        }

    def download_video(self, video_url):
        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                # Extrai as informações do vídeo, sem baixar ainda
                info_dict = ydl.extract_info(video_url, download=False)
                
                # Obtém o nome do arquivo de saída com base no template de 'outtmpl'
                file_name = ydl.prepare_filename(info_dict)
                
                # Agora realiza o download
                download = ydl.download([video_url])
                print(download)
                # Verifica se o arquivo existe e retorna o caminho completo
                if os.path.exists(file_name):
                    print(f"Download completo para: {video_url}")
                    print(f"Arquivo salvo como: {file_name}")
                    return file_name  # Retorna o caminho completo do arquivo
                else:
                    print(f"Erro: O arquivo não foi salvo como esperado.")
                    return None
        
        except Exception as e:
            print(f"Erro ao baixar {video_url}: {e}")
            return None
