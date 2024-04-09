class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

if __name__ == '__main__':

    in_miles = Distance(42.0, "Miles")
    print(in_miles)
    print(in_miles.unit)
    print(dir(in_miles))
