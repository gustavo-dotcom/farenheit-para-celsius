class Conversor:
    def __init__(self):
        self.farenheit = int(input("Digite uma temperatura em farenheit:\n"))

    def conversorParaCelsius(self):
        celsius = (5 * (self.farenheit - 32) / 9)
        print(f"Esta temperatura em celsius seria: {celsius:.1f}")