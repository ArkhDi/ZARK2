import matplotlib.pyplot as plt
import sys

def plot_from_file(filename, title=None):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        x = []
        y = []

        for line in lines: 
            try:
                x_val, y_val = map(float, line.split())
                x.append(x_val)
                y.append(y_val)
            except ValueError:
                print(f"{line} неправильно")

        plt.plot(x, y)
        if title:
            plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"{filename} не найден.")
    except Exception as e:
        print(f"произошла неизвестная ошибка")

if len(sys.argv) < 2:
    print("Напиши в консоль python ЗАДАНИЕ_2.py data.txt [Заголовок графика]")
else:
    filename = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else None
    plot_from_file(filename, title)
