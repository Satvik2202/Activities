class MedPlus:
    def _init_(self, name: str, batch: int, price: float):
        self.name = name
        self.batch = batch
        self.price = price
        try:
            if type(name) != str:
                raise TypeError("Name should be a string")
            if type(batch) != int:
                raise TypeError("Batch number should be an integer")
            if type(price) != float:
                raise TypeError("Price should be a float")
        except TypeError as e:
            print(f"Error: {e}")
            return

    def get_name(self):
        return self.name
    
    def get_batch(self):
        return self.batch
    
    def get_price(self):
        return self.price
k= MedPlus("Satvik",3,6.9)
print(k.get_name())
