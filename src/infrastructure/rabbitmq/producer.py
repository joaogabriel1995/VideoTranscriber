from abc  import ABC, abstractmethod

class Producer(ABC):
    
    @abstractmethod
    def publish():
        pass

