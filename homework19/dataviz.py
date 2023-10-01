import seaborn as sns
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def plot_data(data, plot_type):
    if plot_type == "histogram":
        sns.histplot(data=data, x="total_bill", kde=True)
        plt.title("Гістограма з KDE")
        print("Тип графіку: Гістограма з KDE")
        print("Використання: Візуалізація розподілу"
              "числового даних (total_bill)")
        print(data["total_bill"].describe())
    elif plot_type == "boxplot":
        sns.boxplot(data=data, x="day", y="total_bill")
        plt.title("Скрижальковий графік")
        print("Тип графіку: Скрижальковий графік")
        print("Використання: Візуалізація розподілу числових даних"
              "(total_bill) за категоріями (дні)")
        print(data.groupby("day")["total_bill"].describe())
    elif plot_type == "scatterplot":
        sns.scatterplot(data=data, x="total_bill", y="tip")
        plt.title("Точковий графік")
        print("Тип графіку: Точковий графік")
        print("Використання: Візуалізація залежності між"
              "двома числовими даними (total_bill і tip)")
        print(data[["total_bill", "tip"]].head())
    elif plot_type == "barplot":
        sns.barplot(data=data, x="day", y="total_bill", ci=None)
        plt.title("Графік смуги")
        print("Тип графіку: Графік смуги")
        print("Використання: Візуалізація середніх значень"
              " числових даних (total_bill) за категоріями (дні)")
        print(data.groupby("day")["total_bill"].mean())
    else:
        print("Допустимі значення:"
              "'histogram', 'boxplot', 'scatterplot', 'barplot'")
        return

    plt.xlabel("X-вісь")
    plt.ylabel("Y-вісь")
    plt.show()


tips = sns.load_dataset("tips")
plot_type = input("Введіть тип графіку"
                  "('histogram', 'boxplot', 'scatterplot', 'barplot'): ")
plot_data(tips, plot_type)
