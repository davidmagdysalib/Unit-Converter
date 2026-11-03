"""
This File contains the main function that runs the unit converter program.
It Converts Units Of mass, length, temperature, time, volume, data storage. 

1- Mass Units :
    - Ton (t) : 1,000,000 g
    - Kilogram (kg) : 1,000 g
    - Gram (g) : 1 g
    - Milligram (mg) : 0.001 g

    - Pound (lb) : 453.59237 g
    - Ounce (oz) : 28.349523125 g

2- Length Units :
    - Kilometer (km) : 1,000 m
    - Meter (m) : 1 m
    - Decimeter (dm) : 0.1 m
    - Centimeter (cm) : 0.01 m
    - Millimeter (mm) : 0.001 m

    - Mile (mi) : 1,609.344 m
    - Yard (yd) : 0.9144 m
    - Foot (ft) : 0.3048 m
    - Inch (in) : 0.0254 m

3- Temperature Units :
    - Celsius (°C) : 1 °C
    - Fahrenheit (°F) : (C * 9/5) + 32
    - Kelvin (K) : C + 273.15

4- Time Units :
    - Second (s) : 1 s
    - Minute (min) : 60 s
    - Hour (h) : 3600 s
    - Day (d) : 86400 s

5- Volume Units :
    - Cubic Meter (m³) : 1000 L
    - Liter (L) : 1 L
    - Milliliter (mL) : 0.001 L

    - Gallon (gal) : 3.785411784 L
    - Quart (qt) : 0.946352946 L
    - Pint (pt) : 0.473176473 L

6- Data Storage Units :
    - Bit (b) : 1 bit
    - Byte (B) : 8 bits
    - Kilobyte (KiB) : 8,192 bits
    - Megabyte (MiB) : 8,388,608 bits
    - Gigabyte (GiB) : 8,589,934,592 bits
    - Terabyte (TiB) : 8,796,093,022,208 bits

"""

# Dictionary For Mass Units Conversion Factors:
MassUnits = {  # Based on Gram (g).

    "t" : 1000000,  # 1 Ton = 1,000,000 g
    "kg" : 1000,  # 1 Kilogram = 1,000 g
    "g" : 1,  # 1 Gram = 1 g
    "mg" : 0.001,  # 1 Milligram = 0.001 g

    "lb" : 453.59237,  # 1 Pound = 453.592 g
    "oz" : 28.349523125   # 1 Ounce = 28.3495 g

}

# Dictionary For Length Units Conversion Factors:
LengthUnits = {  # Based on Meter (m).

    "km" : 1000,  # 1 Kilometer = 1,000 m
    "m" : 1,  # 1 Meter = 1 m
    "dm" : 0.1,  # 1 Decimeter = 0.1 m
    "cm" : 0.01,  # 1 Centimeter = 0.01 m
    "mm" : 0.001,  # 1 Millimeter = 0.001 m

    "mi" : 1609.344,  # 1 Mile = 1,609.34 m
    "yd" : 0.9144,  # 1 Yard = 0.9144 m
    "ft" : 0.3048,  # 1 Foot = 0.3048 m
    "in" : 0.0254   # 1 Inch = 0.0254 m

}

# Dictionary For Time Units Conversion Factors:
TimeUnits = {  # Based on Second (s).

    "s" : 1,  # 1 Second = 1 s
    "min" : 60,  # 1 Minute = 60 s
    "h" : 3600,  # 1 Hour = 3,600 s
    "d" : 86400   # 1 Day = 86,400 s

}

# Dictionary For Volume Units Conversion Factors:
VolumeUnits = {  # Based on Liter (L).

    "m³" : 1000,  # 1 Cubic Meter = 1,000 L
    "L" : 1,  # 1 Liter = 1 L
    "mL" : 0.001,  # 1 Milliliter = 0.001 L

    "gal" : 3.785411784,  # 1 Gallon = 3.78541 L
    "qt" : 0.946352946,  # 1 Quart = 0.946353 L
    "pt" : 0.473176473,  # 1 Pint = 0.473176 L

} 

# Dictionary For Data Storage Units Conversion Factors:
DataStorageUnits = {  # Based on Bit (b).

    "b" : 1,  # 1 Bit = 1 b
    "B" : 8,  # 1 Byte = 8 b
    "KiB" : 8192,  # 1 Kilobyte = 8,192 b
    "MiB" : 8388608,  # 1 Megabyte = 8,388,608 b
    "GiB" : 8589934592,  # 1 Gigabyte = 8,589,934,592 b
    "TiB" : 8796093022208   # 1 Terabyte = 8,796,093,022,208 b

}

# Convert Units Function: (Without Temperature Units)
def ConvertUnits(Value : float, FromUnit : str, ToUnit : str, UnitType : str):
    """
    Convert Units Functions : It Converts Units From and To Using The Correct Value.

    Args:
        Value (float): _description_
        FromUnit (str): _description_
        ToUnit (str): _description_
        UnitType (str): _description_
    """

    if UnitType == "Mass":
        return round(Value * MassUnits[FromUnit] / MassUnits[ToUnit], 5)

    elif UnitType == "Length":
        return round(Value * LengthUnits[FromUnit] / LengthUnits[ToUnit], 5)

    elif UnitType == "Time":
        return round(Value * TimeUnits[FromUnit] / TimeUnits[ToUnit], 5)

    elif UnitType == "Volume":
        return round(Value * VolumeUnits[FromUnit] / VolumeUnits[ToUnit], 5)

    elif UnitType == "Data Storage":
        return round(Value * DataStorageUnits[FromUnit] / DataStorageUnits[ToUnit], 5)

def ConvertTemperature(Value : float, FromUnit : str, ToUnit : str):
    """
    Convert Temperature Function : It Converts Temperature Units From and To Using The Correct Value.

    Args:
        Value (float): _description_
        FromUnit (str): _description_
        ToUnit (str): _description_
    """

    if FromUnit == "C" and ToUnit == "F":
        return round((Value * 9/5) + 32, 5)

    elif FromUnit == "C" and ToUnit == "K":
        return round(Value + 273.15, 5)

    elif FromUnit == "F" and ToUnit == "C":
        return round((Value - 32) * 5/9, 5)

    elif FromUnit == "F" and ToUnit == "K":
        return round((Value - 32) * 5/9 + 273.15, 5)

    elif FromUnit == "K" and ToUnit == "C":
        return round(Value - 273.15, 5)

    elif FromUnit == "K" and ToUnit == "F":
        return round((Value - 273.15) * 9/5 + 32, 5)

    else:
        return Value
