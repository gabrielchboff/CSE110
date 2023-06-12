import os
from dataclasses import dataclass


@dataclass(order=True)
class VanillaFileLib(object):

    @staticmethod
    def read_csv(fpath: str) -> list:
        fpath = ''.join(
            os.path.abspath(fpath)
        )
        with open(fpath, 'r') as f:
            lines = f.readlines()
            print(lines)
            rows = [line.split(',') for line in lines][1:]

        return rows


def get_average(lst: list) -> list:
    return sum(lst) / len(lst)

def plot_linear_graph(data):
    max_value = max(data)
    min_value = min(data)
    data_range = max_value - min_value

    width = 120  # Width of the terminal
    scale = width / data_range

    for y in range(max_value, min_value - 1, -1):
        line = ""
        for x in range(len(data)):
            if data[x] >= y:
                line += "•"
            else:
                line += " "
        print(line)



def main():
    rows = VanillaFileLib.read_csv('life-expectancy.csv')
    year = str(input('Enter the year of interest: '))

    global_value = [[float(row[3].strip()), row[0], row[2]] for row in rows]
    global_value_year = [[float(row[3].strip()), row[0]]
                         for row in rows if row[2] == year]

    just_values = [g[0] for g in global_value_year][:-110]

    max_value = max(global_value)
    min_value = min(global_value)
    max_value_year = max(global_value_year)
    min_value_year = min(global_value_year)
    average = get_average([float(row[3].strip())
                          for row in rows if row[2] == year])
    top_countries_year = sorted(global_value_year, reverse=True)[:3]

    print(f"""
    The overall max life expectancy is: {max_value[0]} from {max_value[1]} in {max_value[2]}
    The overall min life expectancy is: {min_value[0]} from {min_value[1]} in {min_value[2]}""")

    print(f"""
    For the year {year}:
    The average life expectancy across all countries was {average:.2f}
    The max life expectancy was in {max_value_year[1]} with {max_value_year[0]}
    The min life expectancy was in {min_value_year[1]} with {min_value_year[0]}
    """)

    print(f'Top 3 Countries with the best life expectancy in {year}:')
    for index, country in enumerate(top_countries_year):
        print(f'{index+1}. {country[1]}')

    print(f'\nA small graph of global life expectancy in {year}:\n')
    just_values = list(map(lambda x: int(x), just_values))
    plot_linear_graph(just_values)


if __name__ == '__main__':
    main()
