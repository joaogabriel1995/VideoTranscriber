from .download_service import DownloadService
from infrastructure.rabbitmq.consumer import Consumer
import json

class DownloadConsumer(Consumer):
    def __init__(self, queue_name, channel):
        super().__init__()
        self.download_service = DownloadService()
        self.queue_name = queue_name
        self.channel = channel

    def on_request(self, ch, method, properties, body):
        print(body.decode())
        video_url = json.loads(body.decode())  # Decode the message body to get the URL
        print(f"Recebido URL: {video_url.get('url')}")
        directory = self.download_service.download_video(video_url.get('url'))
        ch.basic_ack(delivery_tag=method.delivery_tag) 
        message = {
            "input_file": directory,
        }
        self.channel.basic_publish(exchange='',
            routing_key='transcription_queue',
            body=json.dumps(message))
        

    def start_consuming(self, channel):
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_request)
        print(f"Aguardando mensagens na fila {self.queue_name}...")
        channel.start_consuming()
