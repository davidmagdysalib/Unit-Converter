import tkinter as tk
from gui import buildGui
from converter import ConvertUnits, ConvertTemperature


def handleConversion(value, category, fromUnit, toUnit, resultLabel):
    if not value.strip():
        resultLabel.configure(text="—")
        return

    try:
        value = float(value)

        if category == "Temperature":
            result = ConvertTemperature(value, fromUnit, toUnit)
        else:
            result = ConvertUnits(value, fromUnit, toUnit, category)

        if result is None:
            resultLabel.configure(text="Invalid conversion")
        else:
            resultLabel.configure(text=str(result))

    except ValueError:
        resultLabel.configure(text="Enter a valid number")
    except (KeyError, TypeError):
        resultLabel.configure(text="Invalid conversion")


root = tk.Tk()
buildGui(root, handleConversion)
root.mainloop()