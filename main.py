import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, StringVar, Label, Entry, Button, Frame
import math

class ParametricPlotter:
    def __init__(self, master):
        self.master = master
        self.master.title("Parametric Plotter")
        
        # Entry fields for parametric plot parameters
        self.u_start = StringVar()
        self.u_end = StringVar()
        self.v_start = StringVar()
        self.v_end = StringVar()
        
        self.x_eq = StringVar()
        self.y_eq = StringVar()
        self.z_eq = StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Create widgets for input fields and buttons."""
        frame = Frame(self.master)
        frame.pack(padx=10, pady=10)

        Label(frame, text="u_start:").grid(row=0, column=0)
        Entry(frame, textvariable=self.u_start).grid(row=0, column=1)

        Label(frame, text="u_end:").grid(row=1, column=0)
        Entry(frame, textvariable=self.u_end).grid(row=1, column=1)

        Label(frame, text="v_start:").grid(row=2, column=0)
        Entry(frame, textvariable=self.v_start).grid(row=2, column=1)

        Label(frame, text="v_end:").grid(row=3, column=0)
        Entry(frame, textvariable=self.v_end).grid(row=3, column=1)

        Label(frame, text="x equation:").grid(row=4, column=0)
        Entry(frame, textvariable=self.x_eq).grid(row=4, column=1)

        Label(frame, text="y equation:").grid(row=5, column=0)
        Entry(frame, textvariable=self.y_eq).grid(row=5, column=1)

        Label(frame, text="z equation:").grid(row=6, column=0)
        Entry(frame, textvariable=self.z_eq).grid(row=6, column=1)

        Button(frame, text="Plot", command=self.plot_parametric).grid(row=7, columnspan=2)

    def safe_eval(self, expr, u=None, v=None):
        """Safely evaluate parametric expressions with np and math functions."""
        try:
            # Allow math and numpy functions, evaluate expressions like '2*np.pi'
            allowed_names = {"np": np, "math": math, "pi": np.pi}
            if u is not None and v is not None:
                return eval(expr, {"__builtins__": None}, {**allowed_names, "u": u, "v": v})
            else:
                return eval(expr, {"__builtins__": None}, allowed_names)
        except Exception as e:
            print(f"Error evaluating expression: {expr} -> {e}")
            return None

    def validate_input(self, val):
        """Validate if the input is not empty and is a valid number."""
        try:
            # Ensure it's a valid float number or expression
            if val.strip() == '':
                return None  # return None if empty
            return float(self.safe_eval(val))
        except Exception as e:
            print(f"Invalid input: {val} -> {e}")
            return None

    def plot_parametric(self):
        """Generate and plot the parametric surface."""
        try:
            # Get start and end values for u and v, with validation
            u_start = self.validate_input(self.u_start.get())
            u_end = self.validate_input(self.u_end.get())
            v_start = self.validate_input(self.v_start.get())
            v_end = self.validate_input(self.v_end.get())

            # If any values are invalid, exit early
            if None in [u_start, u_end, v_start, v_end]:
                raise ValueError("Invalid input for parameter ranges.")

            # Get the equations for x, y, z
            x_eq = self.x_eq.get()
            y_eq = self.y_eq.get()
            z_eq = self.z_eq.get()

            # Generate the meshgrid for u, v
            u_vals = np.linspace(u_start, u_end, 100)
            v_vals = np.linspace(v_start, v_end, 100)
            u_grid, v_grid = np.meshgrid(u_vals, v_vals)

            # Calculate the parametric coordinates
            x_vals = np.array([[self.safe_eval(x_eq, u, v) for u, v in zip(u_row, v_row)] for u_row, v_row in zip(u_grid, v_grid)])
            y_vals = np.array([[self.safe_eval(y_eq, u, v) for u, v in zip(u_row, v_row)] for u_row, v_row in zip(u_grid, v_grid)])
            z_vals = np.array([[self.safe_eval(z_eq, u, v) for u, v in zip(u_row, v_row)] for u_row, v_row in zip(u_grid, v_grid)])

            # Check if any of the values returned are None (error in evaluation)
            if np.any(np.array([x_vals, y_vals, z_vals]) == None):
                raise ValueError("Error in evaluating one of the parametric equations.")

            # Plot the 3D surface
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x_vals, y_vals, z_vals, cmap='inferno')

            # Set labels
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            # Show the plot
            plt.show()

        except Exception as e:
            print(f"Error in plotting parametric surface: {e}")

# Initialize the Tkinter window
root = Tk()
plotter = ParametricPlotter(root)
root.mainloop()
