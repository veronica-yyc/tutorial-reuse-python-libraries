import numpy as np

from my_package.plotmoody import plot_moodychart
from my_package.frictionfactor import calculate_frictionfactor

def main() -> None:
    print("Hello from my-package, aka. Moody Chart maker!")

    range = input("Enter min and max value of Relative Roughness values (separated by a comma)\nto be ploted:\n")
    range = range.replace(" ", "")
    a,b = range.split(",")
    a,b = float(a),float(b)
    a = np.log10(a)
    b = np.log10(b)

    num = input("Enter number of Relative Roughness values you wish to plot (int):\n")
    num = int(num)
    
    plot_moodychart(min(a,b), max(a,b), num)

