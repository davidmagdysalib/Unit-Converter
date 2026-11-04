# UnitFlow – Python Unit Converter

**UnitFlow** is a modern desktop unit converter built using Python and Tkinter. It provides a clean graphical interface that allows users to convert between different measurement units across six categories: Mass, Length, Temperature, Time, Volume, and Data Storage.

The application features interactive unit selection, automatic conversion, and a dark-themed graphical interface.

## Features

- Modern dark-themed graphical user interface.
- Six supported conversion categories.
- Interactive category selection through a sidebar.
- Clickable unit selection panels.
- Automatic conversion when the input value or selected units change.
- Separate conversion logic and GUI architecture.
- Accurate conversion factors for supported units.
- Input validation and error handling.

## Supported Categories and Units

### 1. Mass

All mass conversion factors are based on grams (g).

| Unit | Symbol | Conversion to grams |
|---|---|---:|
| Metric Tonne | t | 1,000,000 g |
| Kilogram | kg | 1,000 g |
| Gram | g | 1 g |
| Milligram | mg | 0.001 g |
| Pound | lb | 453.59237 g |
| Ounce | oz | 28.349523125 g |

### 2. Length

All length conversion factors are based on meters (m).

| Unit | Symbol | Conversion to meters |
|---|---|---:|
| Kilometer | km | 1,000 m |
| Meter | m | 1 m |
| Decimeter | dm | 0.1 m |
| Centimeter | cm | 0.01 m |
| Millimeter | mm | 0.001 m |
| Mile | mi | 1,609.344 m |
| Yard | yd | 0.9144 m |
| Foot | ft | 0.3048 m |
| Inch | in | 0.0254 m |

### 3. Temperature

Temperature uses separate mathematical formulas because its scales have different zero points.

| Unit | Symbol |
|---|---|
| Celsius | °C |
| Fahrenheit | °F |
| Kelvin | K |

Supported conversions include:
- Celsius to Fahrenheit and Kelvin.
- Fahrenheit to Celsius and Kelvin.
- Kelvin to Celsius and Fahrenheit.

### 4. Time

All time conversion factors are based on seconds (s).

| Unit | Symbol | Conversion to seconds |
|---|---|---:|
| Second | s | 1 s |
| Minute | min | 60 s |
| Hour | h | 3,600 s |
| Day | d | 86,400 s |

### 5. Volume

All volume conversion factors are based on liters (L).

| Unit | Symbol | Conversion to liters |
|---|---|---:|
| Cubic Meter | m³ | 1,000 L |
| Liter | L | 1 L |
| Milliliter | mL | 0.001 L |
| US Gallon | gal | 3.785411784 L |
| US Quart | qt | 0.946352946 L |
| US Pint | pt | 0.473176473 L |

### 6. Data Storage

All data storage conversion factors are based on bits (b).

| Unit | Symbol | Conversion to bits |
|---|---|---:|
| Bit | b | 1 bit |
| Byte | B | 8 bits |
| Kibibyte | KiB | 8,192 bits |
| Mebibyte | MiB | 8,388,608 bits |
| Gibibyte | GiB | 8,589,934,592 bits |
| Tebibyte | TiB | 8,796,093,022,208 bits |

**Note:** Binary storage units use multiples of 1,024. Their technically correct symbols are KiB, MiB, GiB, and TiB.

## How It Was Created

The project was developed using Python and Tkinter.

Development was divided into three main parts:

### 1. GUI – `gui.py`

The graphical interface was created using Tkinter.

It contains:
- A sidebar for selecting conversion categories.
- A main conversion area.
- Separate panels for source and destination units.
- Interactive buttons for selecting units.
- An input field and result display.

The interface uses Tkinter Frames to organize the layout and Buttons to provide interactive unit selection.

### 2. Conversion Logic – `converter.py`

The conversion engine uses dictionaries containing conversion factors relative to a common base unit.

For example, the mass dictionary uses grams as its base unit:

```python
MassUnits = {
    "t": 1000000,
    "kg": 1000,
    "g": 1,
    "mg": 0.001,
    "lb": 453.59237,
    "oz": 28.349523125
}
```

Each dictionary value represents how many base units are contained in one unit.

### 3. Application Controller – `main.py`

The main file connects the graphical interface to the conversion engine.

It receives the user's input, identifies the selected category and units, calls the appropriate conversion function, and displays the result.

This separation makes the application easier to maintain and expand.

## Mathematical Logic

For mass, length, time, volume, and data storage, the application uses a common conversion formula:

**Result = Value × (Source Factor / Destination Factor)**

For example:

Convert 5 kilograms into grams:

- Source factor = 1,000
- Destination factor = 1
- Input value = 5

Result:

```python
5 * 1000 / 1 = 5000
```

Therefore, 5 kg = 5,000 g.

Temperature requires separate formulas because its scales have different offsets.

For example:

```python
Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15
```

## Project Structure

```text
UnitFlow/
│
├── main.py
├── gui.py
├── converter.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Technologies Used

- **Python:** Main programming language.
- **Tkinter:** Desktop graphical user interface.
- **Git:** Version control.
- **GitHub:** Project hosting and source code management.
- **PyInstaller:** Packaging the application into a Windows executable.

## Running the Project

Make sure Python is installed, then run:

```bash
python main.py
```

To create a Windows executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be generated inside the `dist` directory.

## Future Improvements

- Add more measurement units.
- Improve interface animations and interactions.
- Add a unit-swap feature.
- Add conversion history.
- Support additional measurement categories.

---

**UnitFlow** is a project created to practice Python programming, GUI development, mathematical logic, dictionaries, functions, and modular software architecture.
