from Item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones=0):
        # Call to super function to have access to all attributes/ methods
        super().__init__(name, price, quantity)

        # Run validations to receive arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones
