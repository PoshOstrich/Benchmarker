import tkinter as tk
import platform
import timeit
import cpuinfo
import requests





def get_cpu_prices(cpu_name):
    url = f"https://pcpartpicker.com/product/api/search/?q={cpu_name}"
    try:
        response = requests.get(url)
        data = response.json()
        prices = data['products'][0]['price']
    except requests.exceptions.RequestException as e:
        print(f"Request Exception:  {e}")
        prices = "N/A"
    except (KeyError, IndexError, ValueError, TypeError, requests.exceptions.JSONDecodeError) as e:
        print(f"error processing response: {e}")
        prices = "N/A"

    return prices


def perform_light_test():
    start = timeit.default_timer()

    for _ in range(100000000):
        pass
    end = timeit.default_timer()
    time_taken = end - start

    timer_label.config(text=f"Benchmark completed in {time_taken: .2f} seconds")


def perform_medium_test():
    start = timeit.default_timer()

    for _ in range(1000000000):
        pass
    end = timeit.default_timer()
    time_taken = end - start

    timer_label.config(text=f"Benchmark completed in {time_taken: .2f} seconds")


def perform_heavy_test():
    start = timeit.default_timer()

    for _ in range(1500000000):
        pass
    end = timeit.default_timer()
    time_taken = end - start

    timer_label.config(text=f"Benchmark completed in {time_taken: .2f} seconds")


window = tk.Tk()
window.geometry("1920x1080")

banner_label = tk.Label(window, text="Windows Benchmarker", font=("Arial", 25, "bold"))
banner_label.pack(pady=50, padx=50, anchor='w')

info = f"System: {platform.system()}\nProcessor: {cpuinfo.get_cpu_info()['brand_raw']}"
details = tk.Label(window, text=info, font=("Helvetica", 14))
details.pack(pady=100, padx=100)

cpu_name = cpuinfo.get_cpu_info()['brand_raw']
price_label = tk.Label(window, text="Price: ", font=("Helvetica", 14))
price_label.pack()

timer_label = tk.Label(window, text="Execution time: ", font=("Helvetica", 14))
timer_label.pack()


def update_price():
    price = get_cpu_prices(cpu_name)
    price_label.config(text=f"Price: {price}")


update_price()

low = tk.Button(window, text='Start light test', bd=5, command=perform_light_test)
low.pack(side='left')
low.config(width=50, height=15)
low.place(x=50, y=200)

medium = tk.Button(window, text='Start medium test', bd=5, command=perform_medium_test)
medium.pack(side='left')
medium.config(width=50, height=15)
medium.place(x=50, y=450)

high = tk.Button(window, text='Start heavy test', bd=5, command=perform_heavy_test)
high.pack(side='left')
high.config(width=50, height=15)
high.place(x=50, y=700)

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
canvas.place(x=1200, y=300)

canvas.create_rectangle(350, 60, 700, 700, fill="gray")

canvas.create_oval(350, 70, 500, 200, fill="black")
canvas.create_oval(350, 220, 500, 350, fill="black")
canvas.create_oval(350, 370, 500, 500, fill="black")

window.mainloop()
