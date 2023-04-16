import tkinter as tk # import the Tkinter module for GUI development
import requests # import the requests module for HTTP requests

# A class to handle currency conversion using OpenExchangeRates API
class CurrencyConverter:
    API_URL = "https://openexchangerates.org/api/latest.json?app_id=fbdb8bf4bc5743c69e298f358be4a5aa"

    def __init__(self):
        self.app_id = "fbdb8bf4bc5743c69e298f358be4a5aa"
        self.currencies = []  # list of currencies available
        self.rates = {}  # dictionary to store exchange rates

        self.load_currencies()  # load currencies and exchange rates from API

    # Fetch currencies and exchange rates from API
    def load_currencies(self):
        response = requests.get(self.API_URL)
        data = response.json()
        self.currencies = sorted(list(data["rates"].keys()))
        self.currencies.insert(0, data["base"])  # add base currency to the list
        self.rates = data["rates"]

    # Convert amount from one currency to another
    def convert(self, from_currency, to_currency, amount):
        if from_currency == to_currency:
            return amount

        if from_currency != "USD":
            # convert amount to USD first if not already in USD
            amount = amount / self.rates[from_currency]

        # convert amount from USD to target currency
        amount = round(amount * self.rates[to_currency], 2)

        return amount

# A class to create a GUI for the currency converter application
class CurrencyConverterApp:
    def __init__(self, master):
        self.converter = CurrencyConverter()  # create a currency converter instance

        # Initialize Tkinter variables for dropdown menus, amount entry, result display
        self.from_currency_var = tk.StringVar(master)
        self.from_currency_var.set(self.converter.currencies[0])
        self.to_currency_var = tk.StringVar(master)
        self.to_currency_var.set(self.converter.currencies[1])
        self.amount_var = tk.StringVar(master)
        self.result_var = tk.StringVar(master)

        # Create dropdown menus for selecting currencies
        from_currency_dropdown = tk.OptionMenu(master, self.from_currency_var, *self.converter.currencies)
        from_currency_dropdown.pack()

        to_currency_dropdown = tk.OptionMenu(master, self.to_currency_var, *self.converter.currencies)
        to_currency_dropdown.pack()

        # Create an entry field for amount input
        amount_entry = tk.Entry(master, textvariable=self.amount_var)
        amount_entry.pack()

        # Create a button to perform currency conversion
        convert_button = tk.Button(master, text="Convert", command=self.convert)
        convert_button.pack()

        # Create a label to display the conversion result
        result_label = tk.Label(master, textvariable=self.result_var)
        result_label.pack()

        # Create a button to reset the form
        reset_button = tk.Button(master, text="Reset", command=self.reset)
        reset_button.pack()

    # Perform currency conversion and display the result
    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_var.get())

        converted_amount = self.converter.convert(from_currency, to_currency, amount)

        self.result_var.set(f"{converted_amount} {to_currency}")

    # Reset the form to its initial state
    def reset(self):
        self.from_currency_var.set(self.converter.currencies[0])
        self.to_currency_var.set(self.converter.currencies[1])
        self.amount_var.set("")
        self.result_var.set("")

# Main function to run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()  # create a Tkinter root window
    root.title("Currency Converter")
    app = CurrencyConverterApp(root)
    root.mainloop()