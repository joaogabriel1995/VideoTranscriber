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
        self.channel = self.connection.channel()


    def declare_queue(self, queue_name):
        """Declara uma fila."""
        self.channel.queue_declare(queue=queue_name, durable=True)
        print(f"Fila '{queue_name}' declarada.")

    def close(self):
        """Fecha a conexão e o canal."""
        if self.channel:
            self.channel.close()
        if self.connection:
            self.connection.close()
        print("Conexão fechada com RabbitMQ.")


if __name__ == "__main__":
    rabbitmq = RabbitMQConfig()
    rabbitmq.connect()
    
    # Declarar filas e trocas conforme necessário
    rabbitmq.declare_queue('download_queue')
    
    # Depois de terminar, feche a conexão
    rabbitmq.close()


