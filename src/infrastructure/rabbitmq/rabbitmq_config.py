import pika



class RabbitMQConfig:
    def __init__(self, host='localhost', port=5672, user='guest', password='guest' ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
        self.channel = None

    
    def connect(self):
        credentials = pika.PlainCredentials(self.user, self.password)  
        parameters = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters)


    def declare_queue(self, queue_name, channel):
        """Declara uma fila."""
        print(f"Fila '{queue_name}' declarada.")
        channel.queue_declare(queue=queue_name, durable=True)

    # def close(self):
    #     """Fecha a conexão e o canal."""
    #     if self.channel:
    #         self.channel.close()
    #     if self.connection:
    #         self.connection.close()
    #     print("Conexão fechada com RabbitMQ.")

    def create_channel(self):
        return self.connection.channel()


if __name__ == "__main__":
    rabbitmq = RabbitMQConfig()
    rabbitmq.connect()
    
    # Declarar filas e trocas conforme necessário
    rabbitmq.declare_queue('download_queue')
    
    # Depois de terminar, feche a conexão
    rabbitmq.close()


