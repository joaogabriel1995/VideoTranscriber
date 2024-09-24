import whisper
import ffmpeg
import os
from modules.utils.create_file import createFile
class TranscriptionService:
    def __init__(self, model="small"):
        self.model = whisper.load_model(model)

    def transcription_audio(self, input_file:str):
        try:
            titleVideo = input_file[:input_file.rfind(".")]
            titleAudio = "{}.mp3".format(titleVideo)
            titleTranscription = "{}.txt".format(titleVideo)

            self.extractAudioFromVideo(input_file, titleAudio)
            result = self.model.transcribe(titleAudio)
        
            createFile(titleTranscription, result)
        
        except Exception as e:
            print(f"Erro ao baixar: {e}")
        pass
    def extractAudioFromVideo(self,input_file: str, output_file):
        print(input_file.rfind("."))
        titleVideo = input_file[:input_file.rfind(".")]
        titleAudio = "{}.mp3".format(titleVideo)
        ffmpeg.input(input_file).output(output_file, format='mp3').run()


