import tkinter as tk
import pandas as pd
from tkinter import ttk
from graph import HistogramPlot, DensityPlot


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

    def welcome_page(self):
        """Homepage for the UI."""
        self.destroy_widgets()
        self.title("Spotify Hot Hits")
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(background="black")
        for row in range(2):
            self.frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.frame.columnconfigure(column, weight=1)
        self.canvas = tk.Canvas(self.frame, width=1000, height=200, bg="black", highlightbackground="black")
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.logo = tk.PhotoImage(file="images/Hot_Hits.png")
        self.visual_logo = tk.PhotoImage(file="images/distribution_logo.png").subsample(2)
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
        self.distribution_visualization_option = tk.Canvas(self.frame, width=450, height=100, bg='blue',
                                                           highlightbackground="black")
        self.distribution_visualization_option.grid(row=1, column=0, padx=5, pady=15)
        self.distribution_visualization_option.create_image(100, -45, image=self.visual_logo, anchor="nw")
        self.distribution_visualization_option.bind("<Button-1>", self.distribution_visualization_option_page)
        self.distribution_visualization_option.bind("<Enter>", self.on_enter)
        self.distribution_visualization_option.bind("<Leave>", self.on_leave)
        self.statistic_visualization_option = tk.Canvas(self.frame, width=450, height=100, bg='blue',
                                                        highlightbackground="black")
        self.statistic_visualization_option.grid(row=1, column=1, padx=5, pady=15)
        self.statistic_visualization_option.create_image(100, -45, image=self.statistic_logo, anchor="nw")
        self.statistic_visualization_option.bind("<Button-1>", self.statistic_correlation_option_page)
        self.statistic_visualization_option.bind("<Enter>", self.on_enter)
        self.statistic_visualization_option.bind("<Leave>", self.on_leave)
        self.storytelling = tk.Canvas(self.frame, width=450, height=100, bg='#03AC13', highlightbackground="black")
        self.storytelling.grid(row=2, column=0, padx=5, pady=15)
        self.storytelling.create_image(100, -45, image=self.storytelling_logo, anchor="nw")
        self.storytelling.bind("<Button-1>", self.storytelling_page)
        self.storytelling.bind("<Enter>", self.on_enter)
        self.storytelling.bind("<Leave>", self.on_leave)
        self.exit_option = tk.Canvas(self.frame, width=450, height=100, bg='#D30000', highlightbackground="black")
        self.exit_option.grid(row=2, column=1, padx=5, pady=15)
        self.exit_option.create_image(100, -55, image=self.exit_logo, anchor="nw")
        self.exit_option.bind("<Button-1>", self.on_destroy_window)
        self.exit_option.bind("<Enter>", self.on_enter)
        self.exit_option.bind("<Leave>", self.on_leave)

    def storytelling_page(self, event):
        """Storytelling page. (Under maintenance)"""
        self.destroy_widgets()
        self.navigation_buttons(self.welcome_page)
        self.title("Data Storytelling")
        self.storytelling_frame = tk.Frame(self)
        self.storytelling_frame.pack(fill="both", expand=True)
        self.storytelling_frame.configure(background="black")
        for row in range(2):
            self.storytelling_frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.storytelling_frame.columnconfigure(column, weight=1)
        self.storytelling_canvas = tk.Canvas(self.storytelling_frame, width=1000, height=500, bg="black",
                                             highlightbackground="black")
        self.storytelling_canvas.grid(row=0, column=0, columnspan=2)
        self.maintenance_logo = tk.PhotoImage(file="images/maintenance.png")
        self.storytelling_canvas.create_image(350, 100, image=self.maintenance_logo, anchor="nw")

    def statistic_correlation_option_page(self, event):
        """Statistic options page. (Under maintenance)"""
        self.destroy_widgets()
        self.navigation_buttons(self.welcome_page)
        self.title("Statistic Visualization")
        self.statistic_frame = tk.Frame(self)
        self.statistic_frame.pack(fill="both", expand=True)
        self.statistic_frame.configure(background="black")
        for row in range(2):
            self.statistic_frame.rowconfigure(row, weight=1)
        for column in range(2):
            self.statistic_frame.columnconfigure(column, weight=1)
        self.statistic_canvas = tk.Canvas(self.statistic_frame, width=1000, height=500, bg="black",
                                          highlightbackground="black")
        self.statistic_canvas.grid(row=0, column=0, columnspan=2)
        self.maintenance_logo = tk.PhotoImage(file="images/maintenance.png")
        self.statistic_canvas.create_image(350, 100, image=self.maintenance_logo, anchor="nw")

    def distribution_visualization_option_page(self, event):
        """Option page for distribution visualization."""
        self.destroy_widgets()
        self.title("Distribution Visualization")
        self.navigation_buttons(self.welcome_page)
        self.visualization_option_frame = tk.Frame(self, width=1500, height=1000)
        self.visualization_option_frame.pack(fill="both", expand=True)
        self.visualization_option_frame.configure(background="black")
        for row in range(3):
            self.visualization_option_frame.rowconfigure(row, weight=1)
        for column in range(1):
            self.visualization_option_frame.columnconfigure(column, weight=1)
        self.return_logo = tk.PhotoImage(file="images/return.png").subsample(2)
        self.histogram_logo = tk.PhotoImage(file="images/histogram_logo.png").subsample(2)
        self.density_logo = tk.PhotoImage(file="images/density_logo.png").subsample(2)
        self.visual_option_one = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#FF3C00',
                                           highlightbackground="black")
        self.visual_option_one.grid(row=0, column=0, padx=5, pady=5)
        self.visual_option_one.create_image(100, -55, image=self.histogram_logo, anchor="nw")
        self.visual_option_one.bind("<Button-1>", self.histogram_page)
        self.visual_option_one.bind("<Enter>", self.on_enter)
        self.visual_option_one.bind("<Leave>", self.on_leave)
        self.visual_option_two = tk.Canvas(self.visualization_option_frame, width=450, height=100, bg='#FF3C00',
                                           highlightbackground="black")
        self.visual_option_two.grid(row=1, column=0, padx=5, pady=5)
        self.visual_option_two.create_image(100, -45, image=self.density_logo, anchor="nw")
        self.visual_option_two.bind("<Button-1>", self.density_plot_page)
        self.visual_option_two.bind("<Enter>", self.on_enter)
        self.visual_option_two.bind("<Leave>", self.on_leave)

    def histogram_page(self, event):
        """Histogram visualization page."""
        self.destroy_widgets()
        self.title("Histogram Visualization")
        self.navigation_buttons(lambda: self.distribution_visualization_option_page(None))
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
        self.navigation_buttons(lambda: self.distribution_visualization_option_page(None))
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
        if event.widget == self.distribution_visualization_option:
            self.distribution_visualization_option.config(bg="cyan", relief="solid")
        if event.widget == self.statistic_visualization_option:
            self.statistic_visualization_option.config(bg="cyan", relief="solid")
        if event.widget == self.storytelling:
            self.storytelling.config(bg="#80FF00", relief="solid")
        if event.widget == self.exit_option:
            self.exit_option.config(bg="#FF2400", relief="solid")
        if event.widget == self.visual_option_one:
            self.visual_option_one.config(bg="#FF7600", relief="solid")
        if event.widget == self.visual_option_two:
            self.visual_option_two.config(bg="#FF7600", relief="solid")

    def on_leave(self, event):
        """Cursor go off the area."""
        if event.widget == self.distribution_visualization_option:
            self.distribution_visualization_option.config(bg="blue", relief="flat")
        if event.widget == self.statistic_visualization_option:
            self.statistic_visualization_option.config(bg="blue", relief="flat")
        if event.widget == self.storytelling:
            self.storytelling.config(bg="#03AC13", relief="flat")
        if event.widget == self.exit_option:
            self.exit_option.config(bg="#D30000", relief="flat")
        if event.widget == self.visual_option_one:
            self.visual_option_one.config(bg="#FF3C00", relief="flat")
        if event.widget == self.visual_option_two:
            self.visual_option_two.config(bg="#FF3C00", relief="flat")

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

    def on_destroy_window(self, event):
        """Exit."""
        self.destroy()

    def run(self):
        """Run the application."""
        self.mainloop()
