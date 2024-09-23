from abc  import ABC, abstractmethod

class Consumer(ABC):
    
    @abstractmethod
    def on_request():
        pass

