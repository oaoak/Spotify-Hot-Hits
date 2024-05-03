from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns


def summary(data, attribute, ax):
    """Summary statistic of the data."""
    summary_stats = data[attribute].describe().to_frame().T
    summary_table = ax.table(cellText=summary_stats.values, colLabels=summary_stats.columns,
                             cellLoc='center', loc='center')
    summary_table.auto_set_font_size(False)
    summary_table.set_fontsize(10)
    summary_table.scale(1.2, 1.2)


class GraphStrategy(ABC):
    """Abstract class for different types of graph strategies."""

    @abstractmethod
    def visualize(self, data, master, attribute):
        """Visualize the graph based on the given data, master window, and attribute."""
        pass


class HistogramPlot(GraphStrategy):
    """Class for plotting histogram graphs."""

    def visualize(self, data, master, attribute):
        """Visualize a histogram graph based on the given data, master window, and attribute."""
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 1]})
        ax1.hist(data[attribute], bins=10, color='blue', edgecolor='black')
        ax1.set_xlabel(attribute.capitalize())
        ax1.set_ylabel('Frequency')
        ax1.set_title(f'Histogram of {attribute.capitalize()}')
        ax1.ticklabel_format(useOffset=False, axis='x', style='plain')
        summary(data, attribute, ax2)
        ax2.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


class DensityPlot(GraphStrategy):
    """Class for plotting density plot graphs."""

    def visualize(self, data, master, attribute):
        """Visualize a density plot graph based on the given data, master window, and attribute."""
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 1]})
        sns.kdeplot(data[attribute], color="blue", shade=True, ax=ax1)
        ax1.set_title(f'Density Plot of {attribute.capitalize()}')
        ax1.set_xlabel(attribute.capitalize())
        ax1.set_ylabel('Density')
        ax1.ticklabel_format(useOffset=False, axis='x', style='plain')
        ax1.set_ylim(bottom=0)
        summary(data, attribute, ax2)
        ax2.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
