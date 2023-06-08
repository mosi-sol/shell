import tkinter as tk

class GDP:
    def __init__(self, gdp_per_capita_year_a, gdp_per_capita_year_b, burn_rate):
        self.gdp_per_capita_year_a = gdp_per_capita_year_a
        self.gdp_per_capita_year_b = gdp_per_capita_year_b
        self.burn_rate = burn_rate

    def calculate_growth_rate(self):
        growth_rate = (((self.gdp_per_capita_year_b - self.gdp_per_capita_year_a) / self.gdp_per_capita_year_a) - (self.burn_rate / 100)) * 100
        return round(growth_rate, 1)

    def calculate_tax_owed(self, tax_rate):
        tax_owed = self.gdp_per_capita_year_b * (tax_rate / 100)
        return round(tax_owed, 2)

def calculate_gdp():
    try:
        gdp_per_capita_year_a = int(gdp_per_capita_year_a_entry.get())
        gdp_per_capita_year_b = int(gdp_per_capita_year_b_entry.get())
        burn_rate = float(burn_rate_entry.get())
        tax_percent = float(tax_percent_entry.get())

        gdp = GDP(gdp_per_capita_year_a, gdp_per_capita_year_b, burn_rate)
        growth_rate = gdp.calculate_growth_rate()
        tax_owed = gdp.calculate_tax_owed(tax_percent)

        result_label.config(text=f"GDP per capita growth rate after accounting for burn rate: {growth_rate}%\nTax owed: ${tax_owed}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create the main window
window = tk.Tk()
window.title("GDP Calculator")

# Create the input fields
gdp_per_capita_year_a_label = tk.Label(window, text="GDP per capita for year A")
gdp_per_capita_year_a_label.pack()
gdp_per_capita_year_a_entry = tk.Entry(window)
gdp_per_capita_year_a_entry.pack()

gdp_per_capita_year_b_label = tk.Label(window, text="GDP per capita for year B")
gdp_per_capita_year_b_label.pack()
gdp_per_capita_year_b_entry = tk.Entry(window)
gdp_per_capita_year_b_entry.pack()

burn_rate_label = tk.Label(window, text="Burn rate (as a decimal)")
burn_rate_label.pack()
burn_rate_entry = tk.Entry(window)
burn_rate_entry.pack()

tax_percent_label = tk.Label(window, text="Tax percent (as a decimal)")
tax_percent_label.pack()
tax_percent_entry = tk.Entry(window)
tax_percent_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate GDP", command=calculate_gdp)
calculate_button.pack()

# Create the result label
result_label = tk.Label(window)
result_label.pack()

# Start the main event loop
window.mainloop()