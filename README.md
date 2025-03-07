# 3D-molecule-viewer
# Molecular Viewer

A PyQt5 and VPython-based molecular viewer for visualizing molecules from `.xyz` files.

## Features
- Loads molecular structures from `.xyz` files.

- Draws bonds based on atomic distances. The bond detection logic used a threshold of 1.3 × (r₁ + r₂) to create bonds, where r₁ and r₂ are the covalent radii of the two atoms. For example, consider two carbon atoms, each with a covalent radius of 0.6, the threshold is computed as follows: 1.3 × (0.6 + 0.6) = 1.56.

<img width="624" alt="Screenshot 2025-03-07 at 17 56 08" src="https://github.com/user-attachments/assets/0b754f2a-21a8-4335-a7a2-751945eda6cc" />

## Requirements
- Python 3.x
- PyQt5
- VPython

## Usage
- Install dependencies and run the application.
- Click "Open" to load an .xyz molecular file.
The program will visualize atoms and bonds in 3D. By holding the pad/mouse you can rotate the molecule and zoom.

## License
This project is licensed under the MIT License.
