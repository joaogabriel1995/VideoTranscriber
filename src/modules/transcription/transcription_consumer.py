from .transcription_service import TranscriptionService
from infrastructure.rabbitmq.consumer import Consumer
import json

class TranscriptionConsumer(Consumer):
    def __init__(self, queue_name, channel):
        super().__init__()
        self.transcription_service = TranscriptionService()
        self.queue_name = queue_name
        self.channel = channel

    def on_request(self, ch, method, properties, body):
        print(body.decode())
        data = json.loads(body.decode())  # Decode the message body to get the URL
        print(f"Recebido Path: {data.get('input_file')}")
        self.transcription_service.transcription_audio(data.get('input_file'))
        ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge message

    def start_consuming(self, channel):
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_request)
        print(f"Aguardando mensagens na fila {self.queue_name}...")
        channel.start_consuming()
