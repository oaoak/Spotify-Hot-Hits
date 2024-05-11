import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



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
    def visualize(self, data, master, attribute1, attribute2):
        """Visualize the graph based on the given data, master window, and attribute."""
        pass


class HistogramPlot(GraphStrategy):
    """Class for plotting histogram graphs."""

    def visualize(self, data, master, attribute, a2=None):
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

    def visualize(self, data, master, attribute, a2=None):
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


class LinePlot(GraphStrategy):
    """Class for plotting line plot graphs."""

    def visualize(self, data, master, x_attribute, y_attribute):
        """Visualize a line plot graph based on the given data, master window, x attribute, and y attribute."""
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 1]})
        ax1.plot(data[x_attribute], data[y_attribute], color='blue')
        ax1.set_xlabel(x_attribute.capitalize())
        ax1.set_ylabel(y_attribute.capitalize())
        ax1.set_title(f'Line Plot of {y_attribute.capitalize()} vs. {x_attribute.capitalize()}')
        ax1.ticklabel_format(useOffset=False, axis='both', style='plain')
        summary_stats = data[[x_attribute, y_attribute]].describe().T
        summary_table = ax2.table(cellText=summary_stats.values, colLabels=summary_stats.columns,
                                  cellLoc='center', loc='center')
        summary_table.auto_set_font_size(False)
        summary_table.set_fontsize(10)
        summary_table.scale(1.2, 1.2)
        ax2.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


class BarPlot(GraphStrategy):
    """Class for plotting bar plot graphs."""

    def visualize(self, data, master, x_attribute, y_attribute):
        """Visualize a bar plot graph based on the given data, master window, x attribute, and y attribute."""
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 1]})
        sns.barplot(x=x_attribute, y=y_attribute, data=data, ax=ax1)
        ax1.set_xlabel(x_attribute.capitalize())
        ax1.set_ylabel(y_attribute.capitalize())
        ax1.set_title(f'Bar Plot of {y_attribute.capitalize()} by {x_attribute.capitalize()}')
        summary_stats = data[y_attribute].describe().to_frame().T
        summary_table = ax2.table(cellText=summary_stats.values, colLabels=summary_stats.columns,
                                  cellLoc='center', loc='center')
        summary_table.auto_set_font_size(False)
        summary_table.set_fontsize(10)
        summary_table.scale(1.2, 1.2)
        ax2.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


class ScatterPlot(GraphStrategy):
    """Class for plotting scatter plot graphs."""

    def visualize(self, data, master, x_attribute, y_attribute):
        """Visualize a scatter plot graph based on the given data, master window, x attribute, and y attribute."""
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 10), gridspec_kw={'height_ratios': [3, 1]})
        ax1.scatter(data[x_attribute], data[y_attribute], color='blue')
        ax1.set_xlabel(x_attribute.capitalize())
        ax1.set_ylabel(y_attribute.capitalize())
        ax1.set_title(f'Scatter Plot of {y_attribute.capitalize()} vs. {x_attribute.capitalize()}')
        summary_stats = data[[x_attribute, y_attribute]].describe().T
        summary_table = ax2.table(cellText=summary_stats.values, colLabels=summary_stats.columns,
                                  cellLoc='center', loc='center')
        summary_table.auto_set_font_size(False)
        summary_table.set_fontsize(10)
        summary_table.scale(1.2, 1.2)
        ax2.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


class BoxplotPlot(GraphStrategy):
    """Boxplot visualization strategy."""

    def visualize(self, data, master, attribute, a2=None):
        """Generate boxplot visualization."""
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        sns.boxplot(x=attribute, data=data, ax=ax)
        ax.set_title(f'Boxplot of {attribute.capitalize()}')
        ax.set_xlabel(attribute.capitalize())
        ax.set_ylabel('Value')

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
