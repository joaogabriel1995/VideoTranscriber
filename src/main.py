import threading
from infrastructure.rabbitmq.rabbitmq_config import RabbitMQConfig 
from modules.download.dowload_consumer import DownloadConsumer
from modules.transcription.transcription_consumer import TranscriptionConsumer


def run_consumer(consumer, channel):
    consumer.start_consuming(channel)

def run():
    # Configuração do RabbitMQ
    rabbitmq = RabbitMQConfig()
    rabbitmq.connect()

    rabbitmq1 = RabbitMQConfig()
    rabbitmq1.connect()

    download_channel = rabbitmq.create_channel()
    transcription_channel = rabbitmq1.create_channel()

    # Declaração das filas
    rabbitmq.declare_queue('download_queue', download_channel)
    rabbitmq1.declare_queue('transcription_queue', transcription_channel)

    # Inicialização dos consumidores
    download_consumer = DownloadConsumer("download_queue", download_channel)
    transcription_consumer = TranscriptionConsumer("transcription_queue", transcription_channel)

    # Criando threads para consumir as filas simultaneamente
    download_thread = threading.Thread(target=run_consumer, args=(download_consumer, download_channel))
    transcription_thread = threading.Thread(target=run_consumer, args=(transcription_consumer, transcription_channel))

    # Iniciando as threads
    download_thread.start()
    transcription_thread.start()

    # Aguardando as threads terminarem (opcional, caso queira que o programa aguarde o fim das threads)
    # download_thread.join()
    # transcription_thread.join()

run()
