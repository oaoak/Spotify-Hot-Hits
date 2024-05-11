import tkinter as tk
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
from tkinter import ttk
from graph import HistogramPlot, DensityPlot, BarPlot, ScatterPlot, LinePlot, BoxplotPlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AppUI(tk.Tk):
    """UI for graphical analysis."""

    def __init__(self):
        """UI constructor."""
        super().__init__()
        self.data = pd.read_csv("spotify-data.csv")
        self.welcome_page()
        self.numerical_values = ["artistcount", "releasedyear", "releasedmonth"
            , "releasedday", "inspotifyplaylists", "inspotifycharts"
            , "streams", "inappleplaylists", "inapplecharts"
            , "indeezercharts", "bpm", "danceability"
            , "valence", "energy", "acousticness"
            , "instrumentalness", "liveness", "speechiness"]
        self.visual_option_one = None
        self.visual_option_two = None
        self.visual_option_three = None
        self.visual_option_four = None
        self.visual_option_five = None

    def welcome_page(self):
        """Homepage for the UI."""
        self.destroy_widgets()
        self.title("Spotify Hot Hits")
        self.frame = tk.Frame(self, width=1000, height=1000)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(background="black")
        for row in range(2):
            self.frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.frame.columnconfigure(column, weight=1)
        self.canvas = tk.Canvas(self.frame, width=1000, height=200, bg="black", highlightbackground="black")
        self.canvas.grid(row=0, column=0)
        self.logo = tk.PhotoImage(file="images/Hot_Hits.png")
        self.repo_logo = tk.PhotoImage(file="images/repo_logo.png").subsample(2)
        self.visual_logo = tk.PhotoImage(file="images/data_viz.png").subsample(2)
        self.exit_logo = tk.PhotoImage(file="images/exit_logo.png").subsample(2)
        self.statistic_logo = tk.PhotoImage(file="images/statistic_logo.png").subsample(2)
        self.storytelling_logo = tk.PhotoImage(file="images/storytelling_logo.png").subsample(2)
        self.canvas.update_idletasks()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.logo_width = self.logo.width()
        self.logo_height = self.logo.height()
        self.logo_x = (self.canvas_width - self.logo_width) // 2
        self.logo_y = (self.canvas_height - self.logo_height) // 2
        self.canvas.create_image(self.logo_x, self.logo_y, image=self.logo, anchor="nw")
        self.visualization_option = tk.Canvas(self.frame, width=450, height=100, bg='blue',
                                              highlightbackground="black")
        self.visualization_option.grid(row=1, column=0, padx=5, pady=15)
        self.visualization_option.create_image(100, -45, image=self.visual_logo, anchor="nw")
        self.visualization_option.bind("<Button-1>", self.visualization_option_page)
        self.visualization_option.bind("<Enter>", self.on_enter)
        self.visualization_option.bind("<Leave>", self.on_leave)
        self.redirect_repo_option = tk.Canvas(self.frame, width=450, height=100, bg='blue',
                                              highlightbackground="black")
        self.redirect_repo_option.grid(row=3, column=0, padx=5, pady=15)
        self.redirect_repo_option.create_image(100, -55, image=self.repo_logo, anchor="nw")
        self.redirect_repo_option.bind("<Button-1>", self.open_repository)
        self.redirect_repo_option.bind("<Enter>", self.on_enter)
        self.redirect_repo_option.bind("<Leave>", self.on_leave)
        self.storytelling = tk.Canvas(self.frame, width=450, height=100, bg='blue', highlightbackground="black")
        self.storytelling.grid(row=2, column=0, padx=5, pady=15)
        self.storytelling.create_image(100, -45, image=self.storytelling_logo, anchor="nw")
        self.storytelling.bind("<Button-1>", self.storytelling_page)
        self.storytelling.bind("<Enter>", self.on_enter)
        self.storytelling.bind("<Leave>", self.on_leave)
        self.exit_option = tk.Canvas(self.frame, width=450, height=100, bg='#D30000', highlightbackground="black")
        self.exit_option.grid(row=4, column=0, padx=5, pady=15)
        self.exit_option.create_image(100, -55, image=self.exit_logo, anchor="nw")
        self.exit_option.bind("<Button-1>", self.on_destroy_window)
        self.exit_option.bind("<Enter>", self.on_enter)
        self.exit_option.bind("<Leave>", self.on_leave)

    def open_repository(self, event):
        """Redirect to project repository."""
        webbrowser.open("https://github.com/oaoak/Spotify-Hot-Hits")

    def storytelling_page(self, event):
        """Storytelling page."""
        self.destroy_widgets()
        self.navigation_buttons(self.welcome_page)
        self.title("Data Storytelling")
        self.storytelling_frame = tk.Frame(self)
        self.storytelling_frame.pack(fill="both", expand=True)
        self.storytelling_frame.configure(background="black")
        for row in range(3):
            self.storytelling_frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.storytelling_frame.columnconfigure(column, weight=1)
        self.storytelling_canvas = tk.Canvas(self.storytelling_frame, width=1000, height=500, bg="black",
                                             highlightbackground="black")
        self.storytelling_canvas.grid(row=0, column=0, columnspan=2)
        self.story1_label = tk.Label(self.storytelling_canvas, text="How can released year, beat per minute, valence, "+"\n"+"and energy of the song have effect on user streaming?"
                                     , bg="black", font=("Chalkduster", 24))
        self.story1_label.pack()
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        axs = axs.flatten()

        variables = ['releasedyear', 'bpm', 'valence', 'energy']

        for i, variable in enumerate(variables):
            axs[i].scatter(self.data[variable], self.data['streams'], alpha=0.5)
            axs[i].set_xlabel(variable.capitalize())
            axs[i].set_ylabel('Streams')
            axs[i].set_title('Streams vs ' + variable.capitalize())

        canvas_scatter = FigureCanvasTkAgg(fig, master=self.storytelling_frame)
        canvas_scatter.draw()
        canvas_scatter.get_tk_widget().grid(row=1, column=0, columnspan=2)

    def visualization_option_page(self, event):
        """Option page for distribution visualization."""
        self.destroy_widgets()
        self.title("Visualization Option")
        self.navigation_buttons(self.welcome_page)
        self.visualization_option_frame = tk.Frame(self, width=1500, height=1000)
        self.visualization_option_frame.pack(fill="both", expand=True)
        self.visualization_option_frame.configure(background="black")
        for row in range(3):
            self.visualization_option_frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.visualization_option_frame.columnconfigure(column, weight=1)
        self.return_logo = tk.PhotoImage(file="images/return.png").subsample(2)
        self.histogram_logo = tk.PhotoImage(file="images/histogram_logo.png").subsample(2)
        self.density_logo = tk.PhotoImage(file="images/density_logo.png").subsample(2)
        self.scatter_logo = tk.PhotoImage(file="images/scatter_logo.png").subsample(2)
        self.bar_logo = tk.PhotoImage(file="images/bar_logo.png").subsample(2)
        self.box_logo = tk.PhotoImage(file="images/box_logo.png").subsample(2)
        self.visual_option_one = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#FF3C00',
                                           highlightbackground="black")
        self.visual_option_one.grid(row=0, column=0, padx=5, pady=5)
        self.visual_option_one.create_image(100, -55, image=self.box_logo, anchor="nw")
        self.visual_option_one.bind("<Button-1>", self.boxplot_page)
        self.visual_option_one.bind("<Enter>", self.on_enter)
        self.visual_option_one.bind("<Leave>", self.on_leave)
        self.visual_option_two = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#FF3C00',
                                           highlightbackground="black")
        self.visual_option_two.grid(row=1, column=0, padx=5, pady=5)
        self.visual_option_two.create_image(100, -45, image=self.density_logo, anchor="nw")
        self.visual_option_two.bind("<Button-1>", self.density_plot_page)
        self.visual_option_two.bind("<Enter>", self.on_enter)
        self.visual_option_two.bind("<Leave>", self.on_leave)
        self.visual_option_three = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#FF3C00',
                                           highlightbackground="black")
        self.visual_option_three.grid(row=2, column=0, padx=5, pady=5)
        self.visual_option_three.create_image(100, -45, image=self.scatter_logo, anchor="nw")
        self.visual_option_three.bind("<Button-1>", self.scatter_plot_page)
        self.visual_option_three.bind("<Enter>", self.on_enter)
        self.visual_option_three.bind("<Leave>", self.on_leave)
        self.visual_option_four = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#9800FF',
                                             highlightbackground="black")
        self.visual_option_four.grid(row=0, column=1, padx=5, pady=5)
        self.visual_option_four.create_image(100, -55, image=self.histogram_logo, anchor="nw")
        self.visual_option_four.bind("<Button-1>", self.histogram_page)
        self.visual_option_four.bind("<Enter>", self.on_enter)
        self.visual_option_four.bind("<Leave>", self.on_leave)
        self.visual_option_five = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#9800FF',
                                            highlightbackground="black")
        self.visual_option_five.grid(row=1, column=1, padx=5, pady=5)
        self.visual_option_five.create_image(100, -45, image=self.bar_logo, anchor="nw")
        self.visual_option_five.bind("<Button-1>", self.bar_chart_page)
        self.visual_option_five.bind("<Enter>", self.on_enter)
        self.visual_option_five.bind("<Leave>", self.on_leave)



    def histogram_page(self, event):
        """Histogram visualization page."""
        self.destroy_widgets()
        self.title("Histogram Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_hist = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_hist.pack(fill="both", expand=True)
        self.attribute_label = tk.Label(self.visualization_hist, text="Select Attribute:", font="Chalkduster")
        self.attribute_label.pack(pady=10)
        self.attribute_combobox = ttk.Combobox(self.visualization_hist, values=self.numerical_values, state="readonly")
        self.attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_hist, text="Plot", font="Chalkduster", command=self.plot_histogram)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_hist, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.attribute_combobox.set(""))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_hist, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_histogram(self):
        """Histogram plot command."""
        self.destroy_plot_frame()
        selected_attribute = self.attribute_combobox.get()
        if selected_attribute:
            histogram_strategy = HistogramPlot()
            self.hist_plot_frame = tk.Frame(self.visualization_hist, bg="white")
            self.hist_plot_frame.pack(fill="both", expand=True)
            histogram_strategy.visualize(self.data, self.hist_plot_frame, selected_attribute)

    def density_plot_page(self, event):
        """Density plot visualization."""
        self.destroy_widgets()
        self.title("Density Plot Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_density = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_density.pack(fill="both", expand=True)
        self.attribute_label = tk.Label(self.visualization_density, text="Select Attribute:", font="Chalkduster")
        self.attribute_label.pack(pady=10)
        self.attribute_combobox = ttk.Combobox(self.visualization_density, values=self.numerical_values,
                                               state="readonly")
        self.attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_density, text="Plot", font="Chalkduster",
                                command=self.plot_density_plot)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_density, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.attribute_combobox.set(""))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_density, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_density_plot(self):
        """Density plot command."""
        self.destroy_plot_frame()
        selected_attribute = self.attribute_combobox.get()
        if selected_attribute:
            density_plot_strategy = DensityPlot()
            self.density_plot_frame = tk.Frame(self.visualization_density, bg="white")
            self.density_plot_frame.pack(fill="both", expand=True)
            density_plot_strategy.visualize(self.data, self.density_plot_frame, selected_attribute)

    def bar_chart_page(self, event):
        """Bar chart visualization page."""
        self.destroy_widgets()
        self.title("Bar Chart Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_bar = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_bar.pack(fill="both", expand=True)
        self.attribute_label = tk.Label(self.visualization_bar, text="Select Attribute:", font="Chalkduster")
        self.attribute_label.pack(pady=10)
        self.x_attribute_combobox = ttk.Combobox(self.visualization_bar, values=self.numerical_values,
                                                 state="readonly")
        self.x_attribute_combobox.pack(pady=5)
        self.y_attribute_combobox = ttk.Combobox(self.visualization_bar, values=self.numerical_values,
                                                 state="readonly")
        self.y_attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_bar, text="Plot", font="Chalkduster",
                                command=self.plot_bar_chart)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_bar, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.clear_attribute_comboboxes(self.x_attribute_combobox,
                                                                              self.y_attribute_combobox))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_bar, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_bar_chart(self):
        """Bar chart plot command."""
        self.destroy_plot_frame()
        x_selected_attribute = self.x_attribute_combobox.get()
        y_selected_attribute = self.y_attribute_combobox.get()
        if x_selected_attribute and y_selected_attribute:
            bar_plot_strategy = BarPlot()
            self.bar_frame = tk.Frame(self.visualization_bar, bg="white")
            self.bar_frame.pack(fill="both", expand=True)
            bar_plot_strategy.visualize(self.data, self.bar_frame, x_selected_attribute, y_selected_attribute)

    def scatter_plot_page(self, event):
        """Scatter plot visualization page."""
        self.destroy_widgets()
        self.title("Scatter Plot Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_scatter_plot = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_scatter_plot.pack(fill="both", expand=True)
        self.x_attribute_label = tk.Label(self.visualization_scatter_plot, text="Select X Attribute:",
                                          font="Chalkduster")
        self.x_attribute_label.pack(pady=10)
        self.x_attribute_combobox = ttk.Combobox(self.visualization_scatter_plot, values=self.numerical_values,
                                                 state="readonly")
        self.x_attribute_combobox.pack(pady=5)
        self.y_attribute_label = tk.Label(self.visualization_scatter_plot, text="Select Y Attribute:",
                                          font="Chalkduster")
        self.y_attribute_label.pack(pady=10)
        self.y_attribute_combobox = ttk.Combobox(self.visualization_scatter_plot, values=self.numerical_values,
                                                 state="readonly")
        self.y_attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_scatter_plot, text="Plot", font="Chalkduster",
                                command=self.plot_scatter_plot)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_scatter_plot, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.clear_attribute_comboboxes(self.x_attribute_combobox,
                                                                                  self.y_attribute_combobox))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_scatter_plot, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_scatter_plot(self):
        """Scatter plot command."""
        self.destroy_plot_frame()
        x_selected_attribute = self.x_attribute_combobox.get()
        y_selected_attribute = self.y_attribute_combobox.get()
        if x_selected_attribute and y_selected_attribute:
            scatter_plot_strategy = ScatterPlot()
            self.scatter_plot_frame = tk.Frame(self.visualization_scatter_plot, bg="white")
            self.scatter_plot_frame.pack(fill="both", expand=True)
            scatter_plot_strategy.visualize(self.data, self.scatter_plot_frame, x_selected_attribute,
                                            y_selected_attribute)

    def line_plot_page(self, event):
        """Line plot visualization page."""
        self.destroy_widgets()
        self.title("Line Plot Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_line_plot = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_line_plot.pack(fill="both", expand=True)
        self.x_attribute_label = tk.Label(self.visualization_line_plot, text="Select X Attribute:",
                                          font="Chalkduster")
        self.x_attribute_label.pack(pady=10)
        self.x_attribute_combobox = ttk.Combobox(self.visualization_line_plot, values=self.numerical_values,
                                                 state="readonly")
        self.x_attribute_combobox.pack(pady=5)
        self.y_attribute_label = tk.Label(self.visualization_line_plot, text="Select Y Attribute:",
                                          font="Chalkduster")
        self.y_attribute_label.pack(pady=10)
        self.y_attribute_combobox = ttk.Combobox(self.visualization_line_plot, values=self.numerical_values,
                                                 state="readonly")
        self.y_attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_line_plot, text="Plot", font="Chalkduster",
                                command=self.plot_line_plot)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_line_plot, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.clear_attribute_comboboxes(self.x_attribute_combobox,
                                                                                  self.y_attribute_combobox))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_line_plot, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_line_plot(self):
        """Line plot command."""
        self.destroy_plot_frame()
        x_selected_attribute = self.x_attribute_combobox.get()
        y_selected_attribute = self.y_attribute_combobox.get()
        if x_selected_attribute and y_selected_attribute:
            line_plot_strategy = LinePlot()
            self.line_plot_frame = tk.Frame(self.visualization_line_plot, bg="white")
            self.line_plot_frame.pack(fill="both", expand=True)
            line_plot_strategy.visualize(self.data, self.line_plot_frame, x_selected_attribute,
                                         y_selected_attribute)

    def boxplot_page(self, event):
        """Boxplot visualization page."""
        self.destroy_widgets()
        self.title("Boxplot Visualization")
        self.navigation_buttons(lambda: self.visualization_option_page(None))
        self.visualization_box = tk.Frame(self, bg="blue", width=1500, height=1000)
        self.visualization_box.pack(fill="both", expand=True)
        self.attribute_label = tk.Label(self.visualization_box, text="Select Attribute:", font="Chalkduster")
        self.attribute_label.pack(pady=10)
        self.attribute_combobox = ttk.Combobox(self.visualization_box, values=self.numerical_values, state="readonly")
        self.attribute_combobox.pack(pady=5)
        plot_button = tk.Button(self.visualization_box, text="Plot", font="Chalkduster", command=self.plot_boxplot)
        plot_button.pack(pady=5)
        clear_button = tk.Button(self.visualization_box, text="Clear Selection", font="Chalkduster",
                                 command=lambda: self.attribute_combobox.set(""))
        clear_button.pack(pady=5)
        delete_button = tk.Button(self.visualization_box, text="Delete Plot", font="Chalkduster",
                                  command=self.destroy_plot_frame)
        delete_button.pack(pady=5)

    def plot_boxplot(self):
        """Boxplot plot command."""
        self.destroy_plot_frame()
        selected_attribute = self.attribute_combobox.get()
        if selected_attribute:
            boxplot_strategy = BoxplotPlot()
            self.boxplot_frame = tk.Frame(self.visualization_box, bg="white")
            self.boxplot_frame.pack(fill="both", expand=True)
            boxplot_strategy.visualize(self.data, self.boxplot_frame, selected_attribute)


    def navigation_buttons(self, return_location):
        """Navigation bar for re-directing."""

        def return_button_clicked(event):
            return_location()

        button_frame = tk.Frame(self, bg="black", width=1500, height=200)
        button_frame.pack(side="top", fill="x")
        return_button_canvas = tk.Canvas(button_frame, width=100, height=50, bg="#FCD12A", highlightbackground="black")
        return_button_canvas.pack(side="left", padx=10, pady=10)
        return_button_text = return_button_canvas.create_text(50, 25, text="Return", fill="black",
                                                              font=("Chalkduster", 12))
        return_button_canvas.bind("<Button-1>", return_button_clicked)
        return_button_canvas.bind("<Enter>", lambda event: return_button_canvas.config(bg="#FFFF00"))
        return_button_canvas.bind("<Leave>", lambda event: return_button_canvas.config(bg="#FCD12A"))
        home_button_canvas = tk.Canvas(button_frame, width=100, height=50, bg="#FCD12A", highlightbackground="black")
        home_button_canvas.pack(side="left", padx=10, pady=10)
        home_button_text = home_button_canvas.create_text(50, 25, text="Home", fill="black", font=("Chalkduster", 12))
        home_button_canvas.bind("<Button-1>", lambda event: self.welcome_page())
        home_button_canvas.bind("<Enter>", lambda event: home_button_canvas.config(bg="#FFFF00"))
        home_button_canvas.bind("<Leave>", lambda event: home_button_canvas.config(bg="#FCD12A"))

    def on_enter(self, event):
        """Cursor hover on the area."""
        if event.widget == self.visualization_option:
            self.visualization_option.config(bg="cyan", relief="solid")
        if event.widget == self.redirect_repo_option:
            self.redirect_repo_option.config(bg="cyan", relief="solid")
        if event.widget == self.storytelling:
            self.storytelling.config(bg="cyan", relief="solid")
        if event.widget == self.exit_option:
            self.exit_option.config(bg="#FF0000", relief="solid")
        if event.widget == self.visual_option_one:
            self.visual_option_one.config(bg="#FF7600", relief="solid")
        if event.widget == self.visual_option_two:
            self.visual_option_two.config(bg="#FF7600", relief="solid")
        if event.widget == self.visual_option_three:
            self.visual_option_three.config(bg="#FF7600", relief="solid")
        if event.widget == self.visual_option_four:
            self.visual_option_four.config(bg="#D400FF", relief="solid")
        if event.widget == self.visual_option_five:
            self.visual_option_five.config(bg="#D400FF", relief="solid")

    def on_leave(self, event):
        """Cursor go off the area."""
        if event.widget == self.visualization_option:
            self.visualization_option.config(bg="blue", relief="flat")
        if event.widget == self.redirect_repo_option:
            self.redirect_repo_option.config(bg="blue", relief="flat")
        if event.widget == self.storytelling:
            self.storytelling.config(bg="blue", relief="flat")
        if event.widget == self.exit_option:
            self.exit_option.config(bg="#D30000", relief="flat")
        if event.widget == self.visual_option_one:
            self.visual_option_one.config(bg="#FF3C00", relief="flat")
        if event.widget == self.visual_option_two:
            self.visual_option_two.config(bg="#FF3C00", relief="flat")
        if event.widget == self.visual_option_three:
            self.visual_option_three.config(bg="#FF3C00", relief="flat")
        if event.widget == self.visual_option_four:
            self.visual_option_four.config(bg="#9800FF", relief="flat")
        if event.widget == self.visual_option_five:
            self.visual_option_five.config(bg="#9800FF", relief="flat")

    def destroy_widgets(self):
        """Clear entire widgets."""
        for widget in self.winfo_children():
            widget.destroy()

    def destroy_plot_frame(self):
        """Clear frame."""
        if hasattr(self, 'hist_plot_frame'):
            self.hist_plot_frame.destroy()
        if hasattr(self, 'density_plot_frame'):
            self.density_plot_frame.destroy()
        if hasattr(self, 'scatter_plot_frame'):
            self.scatter_plot_frame.destroy()
        if hasattr(self, 'bar_frame'):
            self.bar_frame.destroy()
        if hasattr(self, 'boxplot_frame'):
            self.boxplot_frame.destroy()

    def clear_attribute_comboboxes(self, *comboboxes):
        """Clear selection in multiple comboboxes."""
        for combobox in comboboxes:
            combobox.set("")

    def on_destroy_window(self, event):
        """Exit."""
        self.destroy()

    def run(self):
        """Run the application."""
        self.mainloop()
