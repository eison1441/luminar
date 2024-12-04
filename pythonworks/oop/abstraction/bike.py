from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):
    def start(self):
        print("bike start method")

    def accelerate(self):
        print("bike accelerate method")

    def stop(self):
        print("bike stop method")

Hunter_instance=Hunter()
Hunter_instance.start()
Hunter_instance.accelerate()
Hunter_instance.stop()