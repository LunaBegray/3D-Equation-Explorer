# 3D-Equation-Explorer

**3D-Equation-Explorer** is a Python-based tool for visualizing 3D parametric surfaces. It provides an intuitive graphical interface for inputting parametric equations and generating interactive 3D plots.

## Features
- User-friendly interface for specifying parameter ranges and equations.
- Supports parametric equations in terms of `u` and `v`.
- Interactive 3D visualization using Matplotlib.
- Safe evaluation of mathematical expressions with `numpy` and `math`.

## Requirements
- Python 3.7+
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `tkinter` (bundled with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd parametric-plotter
   ```
2. Install the required libraries:
   ```bash
   pip install numpy matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python parametric_plotter.py
   ```
2. Enter the parameter ranges and parametric equations in the GUI fields:
   - `u_start`, `u_end`: Range for the `u` parameter.
   - `v_start`, `v_end`: Range for the `v` parameter.
   - `x equation`, `y equation`, `z equation`: Parametric equations for the surface.
3. Click **Plot** to visualize the 3D surface.

## Example
To plot a torus:
- `u_start`: `0`
- `u_end`: `2*np.pi`
- `v_start`: `0`
- `v_end`: `2*np.pi`
- `x equation`: `(2 + np.cos(v)) * np.cos(u)`
- `y equation`: `(2 + np.cos(v)) * np.sin(u)`
- `z equation`: `np.sin(v)`

Click **Plot** to view the torus in 3D.
