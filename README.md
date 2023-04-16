Currency Converter
This Python code provides a GUI application for currency conversion using OpenExchangeRates API. It uses Tkinter for the GUI development and requests module for HTTP requests.

Requirements
•	Python 3.x
•	requests module
•	tkinter module (included in Python standard library)

Installation
•	Install Python 3.x from the official website.
•	Install requests module using pip:


pip install requests 
•	No installation required for tkinter module as it is included in the standard library.



Usage
To run the application, navigate to the directory where the code is saved and execute the following command:

python currency_converter.py 

The application window will appear, allowing you to select the source and target currencies, enter the amount, and convert the currency.You can reset the form to its initial state using the Reset button.

Limitations
•	This code uses the free OpenExchangeRates API which has a limit of 1,000 requests per month. If the limit is exceeded, the API may stop responding until the next month.
•	The exchange rates are updated hourly by the API. Therefore, the conversion may not be up-to-date.

