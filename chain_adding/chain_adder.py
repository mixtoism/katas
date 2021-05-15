def adder(x):
    class temp_class:
        def __init__(self, value):
            self.value = value

        def __eq__(self, value):
            return self.value == value

        def __add__(self, value):
            return self(value)

        def __call__(self, value):
            adder_value = self.compute_sum(self, value)
            return self.create_new_instance(adder_value)

        @classmethod
        def compute_sum(cls, self, value):
            if isinstance(value, int):
                return self.value + value
            return self.value + value.value

        @classmethod
        def create_new_instance(cls, val):
            return cls(val)

    return temp_class(x)
