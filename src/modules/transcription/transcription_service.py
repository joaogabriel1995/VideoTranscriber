import whisper
import ffmpeg

class TranscriptionService:
    def __init__(self, model="small"):
        self.model = whisper.load_model(model)

    def transcription_audio(self, input_file:str):
        try:
            self.extractAudioFromVideo(input_file)
            result = self.model.transcribe("output.mp3")
            print(result["text"])
        except Exception as e:
            print(f"Erro ao baixar: {e}")
        pass
    def extractAudioFromVideo(self,input_file: str):
        ffmpeg.input(input_file).output("output.mp3", format='mp3').run()


