import tkinter as tk

BG = "#181825"
SIDEBAR = "#202033"
CARD = "#28283D"
ACCENT = "#89B4FA"
WHITE = "#CDD6F4"
MUTED = "#A6ADC8"

unitData = {
    "Mass": [("Ton (t)", "t"), ("Kilogram (kg)", "kg"), ("Gram (g)", "g"), ("Milligram (mg)", "mg"), ("Pound (lb)", "lb"), ("Ounce (oz)", "oz")],
    "Length": [("Kilometer (km)", "km"), ("Meter (m)", "m"), ("Decimeter (dm)", "dm"), ("Centimeter (cm)", "cm"), ("Millimeter (mm)", "mm"), ("Mile (mi)", "mi"), ("Yard (yd)", "yd"), ("Foot (ft)", "ft"), ("Inch (in)", "in")],
    "Temperature": [("Celsius (°C)", "C"), ("Fahrenheit (°F)", "F"), ("Kelvin (K)", "K")],
    "Time": [("Second (s)", "s"), ("Minute (min)", "min"), ("Hour (h)", "h"), ("Day (d)", "d")],
    "Volume": [("Cubic Meter (m³)", "m³"), ("Liter (L)", "L"), ("Milliliter (mL)", "mL"), ("Gallon (gal)", "gal"), ("Quart (qt)", "qt"), ("Pint (pt)", "pt")],
    "Data Storage": [("Bit (b)", "b"), ("Byte (B)", "B"), ("Kilobyte (KiB)", "KiB"), ("Megabyte (MiB)", "MiB"), ("Gigabyte (GiB)", "GiB"), ("Terabyte (TiB)", "TiB")]
}


def buildGui(root, onConvert):

    root.title("UnitFlow")
    root.geometry("1100x700")
    root.minsize(900, 600)
    root.configure(bg=BG)

    selectedCategory = {"value": None}
    selectedFromUnit = tk.StringVar()
    selectedToUnit = tk.StringVar()

    # Sidebar
    sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    tk.Label(sidebar, text="UNITFLOW", font=("Arial", 22, "bold"), bg=SIDEBAR, fg=ACCENT).pack(pady=(35, 45))
    tk.Label(sidebar, text="CATEGORIES", font=("Arial", 10, "bold"), bg=SIDEBAR, fg=MUTED).pack(anchor="w", padx=20, pady=10)

    # Main Area
    main = tk.Frame(root, bg=BG)
    main.pack(side="right", fill="both", expand=True, padx=35, pady=30)

    tk.Label(main, text="Unit Converter", font=("Arial", 28, "bold"), bg=BG, fg=WHITE).pack(anchor="w")
    tk.Label(main, text="Convert measurements instantly.", font=("Arial", 12), bg=BG, fg=MUTED).pack(anchor="w", pady=(5, 30))

    # Conversion Panels
    conversionArea = tk.Frame(main, bg=BG)
    conversionArea.pack(fill="both", expand=True)

    fromCard = tk.Frame(conversionArea, bg=CARD, padx=20, pady=20)
    fromCard.pack(side="left", fill="both", expand=True, padx=(0, 10))

    toCard = tk.Frame(conversionArea, bg=CARD, padx=20, pady=20)
    toCard.pack(side="right", fill="both", expand=True, padx=(10, 0))

    tk.Label(fromCard, text="FROM", font=("Arial", 11, "bold"), bg=CARD, fg=MUTED).pack(anchor="w")

    valueEntry = tk.Entry(fromCard, font=("Arial", 22), bg="#34344D", fg=WHITE, insertbackground=WHITE, relief="flat")
    valueEntry.pack(fill="x", pady=15, ipady=10)

    tk.Label(fromCard, text="SELECT UNIT", font=("Arial", 10, "bold"), bg=CARD, fg=MUTED).pack(anchor="w")

    tk.Label(toCard, text="TO", font=("Arial", 11, "bold"), bg=CARD, fg=MUTED).pack(anchor="w")

    resultLabel = tk.Label(toCard, text="—", font=("Arial", 22, "bold"), bg=CARD, fg=ACCENT)
    resultLabel.pack(fill="x", pady=15)

    tk.Label(toCard, text="SELECT UNIT", font=("Arial", 10, "bold"), bg=CARD, fg=MUTED).pack(anchor="w")

    fromList = tk.Frame(fromCard, bg=CARD)
    fromList.pack(fill="both", expand=True, pady=10)

    toList = tk.Frame(toCard, bg=CARD)
    toList.pack(fill="both", expand=True, pady=10)

    # Automatic Conversion
    def updateResult(*args):
        if not selectedCategory["value"] or not selectedFromUnit.get() or not selectedToUnit.get():
            resultLabel.configure(text="—")
            return

        onConvert(valueEntry.get(), selectedCategory["value"], selectedFromUnit.get(), selectedToUnit.get(), resultLabel)

    valueEntry.bind("<KeyRelease>", updateResult)

    # Unit Selection
    def createUnitButtons(parent, units, variable):
        for widget in parent.winfo_children():
            widget.destroy()

        unitButtons = {}

        def selectUnit(code):
            variable.set(code)

            for unitCode, button in unitButtons.items():
                button.configure(bg="white" if unitCode == code else CARD, fg=BG if unitCode == code else WHITE)

            updateResult()

        for label, code in units:
            button = tk.Button(parent, text=label, font=("Arial", 10), bg=CARD, fg=WHITE, relief="flat", anchor="w", padx=10, pady=7, cursor="hand2", command=lambda c=code: selectUnit(c))
            button.pack(fill="x", pady=2)
            unitButtons[code] = button

    # Category Selection
    categoryButtons = {}

    def selectCategory(category):
        selectedCategory["value"] = category
        selectedFromUnit.set("")
        selectedToUnit.set("")
        resultLabel.configure(text="—")

        for name, button in categoryButtons.items():
            button.configure(bg="white" if name == category else CARD, fg=BG if name == category else WHITE)

        createUnitButtons(fromList, unitData[category], selectedFromUnit)
        createUnitButtons(toList, unitData[category], selectedToUnit)

    for category in unitData:
        button = tk.Button(sidebar, text=category, font=("Arial", 12), bg=CARD, fg=WHITE, relief="flat", anchor="w", padx=15, pady=12, cursor="hand2", command=lambda c=category: selectCategory(c))
        button.pack(fill="x", padx=15, pady=5)
        categoryButtons[category] = button

    # Result Information
    resultInfo = tk.Label(main, text="Select a category and units to begin.", font=("Arial", 11), bg=BG, fg=MUTED)
    resultInfo.pack(pady=15)