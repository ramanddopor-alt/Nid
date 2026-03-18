import tkinter as tk
from tkinter import ttk

class WeatherUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Weather Application')
        self.create_widgets()

    def create_widgets(self):
        # Current Conditions
        self.current_conditions_frame = ttk.LabelFrame(self.root, text='Current Conditions')
        self.current_conditions_frame.grid(column=0, row=0, padx=10, pady=10)

        self.temp_label = ttk.Label(self.current_conditions_frame, text='Temperature:')
        self.temp_label.grid(column=0, row=0, sticky='W')
        self.temp_value = ttk.Label(self.current_conditions_frame, text='-- °C')
        self.temp_value.grid(column=1, row=0, sticky='W')

        self.weather_label = ttk.Label(self.current_conditions_frame, text='Weather:')
        self.weather_label.grid(column=0, row=1, sticky='W')
        self.weather_value = ttk.Label(self.current_conditions_frame, text='--')
        self.weather_value.grid(column=1, row=1, sticky='W')

        # Forecast
        self.forecast_frame = ttk.LabelFrame(self.root, text='Forecast')
        self.forecast_frame.grid(column=0, row=1, padx=10, pady=10)

        self.forecast_label = ttk.Label(self.forecast_frame, text='Coming up:')
        self.forecast_label.grid(column=0, row=0, sticky='W')
        self.forecast_value = ttk.Label(self.forecast_frame, text='--')
        self.forecast_value.grid(column=1, row=0, sticky='W')

        # Charts
        self.chart_frame = ttk.LabelFrame(self.root, text='Temperature Chart')
        self.chart_frame.grid(column=0, row=2, padx=10, pady=10)

        self.chart_label = ttk.Label(self.chart_frame, text='Chart data will be displayed here.')
        self.chart_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = WeatherUI(root)
    root.mainloop()