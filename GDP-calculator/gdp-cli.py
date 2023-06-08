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

# Example usage
gdp_per_capita_year_a = int(input("Enter GDP per capita for year A: "))
gdp_per_capita_year_b = int(input("Enter GDP per capita for year B: "))
burn_rate = float(input("Enter burn rate as a decimal: "))
tax_percent = float(input("Enter tax percent as a decimal: "))

gdp = GDP(gdp_per_capita_year_a, gdp_per_capita_year_b, burn_rate)
growth_rate = gdp.calculate_growth_rate()
tax_owed = gdp.calculate_tax_owed(tax_percent)

print(f"Year A GDP per capita: {gdp_per_capita_year_a}")
print(f"Year B GDP per capita: {gdp_per_capita_year_b}")
print(f"GDP per capita growth rate after accounting for burn rate: {growth_rate}%")
print(f"Burn rate: {burn_rate}%")
print(f"Tax percent: {tax_percent}%")
print(f"Tax owed: ${tax_owed}")