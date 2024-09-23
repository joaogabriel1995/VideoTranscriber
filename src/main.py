from infrastructure.rabbitmq.rabbitmq_config import RabbitMQConfig 


def run():
    rabbitmq = RabbitMQConfig()
    rabbitmq.connect()
    
    # Declarar filas e trocas conforme necessário
    rabbitmq.declare_queue('download_queue')


run()