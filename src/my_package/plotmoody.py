import numpy as np
import matplotlib.pyplot as plt

from .frictionfactor import calculate_frictionfactorcurve

def plot_moodychart(a = -6, b = -2, num = 5) -> None:
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    for e_over_d in np.logspace(a,b, num=num):
    
        [x,y] = calculate_frictionfactorcurve(e_over_d)

        ax1.loglog(x, y)
        ax1.text(x[-1], y[-1], f"      {e_over_d:.1e}")

    ax1.set_xlabel("Reynold's Number [-], (log scale)")
    ax1.set_ylabel("Friction Factor [-], (log scale)")
    ax2.set_ylabel("Surface Roughness Over Pipe Diameter [-]", labelpad=55)
    ax2.set_yticklabels([])
    ax2.set_yticks([])
    ax1.set_title("My Moody Chart")

    plt.tight_layout()

    ax1.grid(True, which="both", ls="-") 
    plt.savefig("MyMoodyChart.png")