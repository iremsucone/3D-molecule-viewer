import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox
from vpython import sphere, cylinder, vector, color, scene, mag

# Define element properties including display and covalent radii.
element_data = {
    'H': {'display_radius': 0.39, 'color': vector(0.04, 0.02, 0.86), 'covalent_radius': 0.42},
    'He': {'display_radius': 0.42, 'color': vector(0.20, 0.26, 0.39), 'covalent_radius': 0.96},
    'Li': {'display_radius': 0.43, 'color': vector(0.88, 0.17, 0.33), 'covalent_radius': 0.36},
    'Be': {'display_radius': 0.44, 'color': vector(1.00, 0.29, 0.09), 'covalent_radius': 0.81},
    'B': {'display_radius': 0.2, 'color': vector(0.13, 0.87, 0.60), 'covalent_radius': 0.36},
    'C': {'display_radius': 0.38, 'color': vector(0.83, 0.47, 0.73), 'covalent_radius': 0.6},
    'N': {'display_radius': 0.39, 'color': vector(0.35, 0.78, 0.47), 'covalent_radius': 1.33},
    'O': {'display_radius': 0.41, 'color': vector(0.19, 0.64, 0.10), 'covalent_radius': 1.11},
    'F': {'display_radius': 0.28, 'color': vector(0.34, 0.53, 0.28), 'covalent_radius': 1.23},
    'Ne': {'display_radius': 0.3, 'color': vector(0.35, 0.85, 0.50), 'covalent_radius': 0.92},
    'Na': {'display_radius': 0.3, 'color': vector(0.28, 0.23, 0.25), 'covalent_radius': 0.49},
    'Mg': {'display_radius': 0.32, 'color': vector(0.25, 0.26, 0.58), 'covalent_radius': 1.33},
    'Al': {'display_radius': 0.29, 'color': vector(0.49, 0.56, 0.26), 'covalent_radius': 0.65},
    'Si': {'display_radius': 0.39, 'color': vector(0.81, 0.51, 0.82), 'covalent_radius': 1.2},
    'P': {'display_radius': 0.43, 'color': vector(0.33, 0.02, 0.97), 'covalent_radius': 1.37},
    'S': {'display_radius': 0.29, 'color': vector(0.69, 0.00, 0.95), 'covalent_radius': 0.59},
    'Cl': {'display_radius': 0.39, 'color': vector(0.07, 0.04, 0.60), 'covalent_radius': 0.84},
    'Ar': {'display_radius': 0.34, 'color': vector(0.89, 0.95, 0.76), 'covalent_radius': 0.68},
    'K': {'display_radius': 0.25, 'color': vector(0.82, 0.64, 0.58), 'covalent_radius': 0.64},
    'Ca': {'display_radius': 0.2, 'color': vector(0.29, 0.51, 0.87), 'covalent_radius': 0.52},
    'Sc': {'display_radius': 0.35, 'color': vector(0.20, 0.43, 0.86), 'covalent_radius': 1.42},
    'Ti': {'display_radius': 0.24, 'color': vector(0.12, 0.38, 0.52), 'covalent_radius': 1.18},
    'V': {'display_radius': 0.31, 'color': vector(0.18, 0.85, 0.27), 'covalent_radius': 0.33},
    'Cr': {'display_radius': 0.42, 'color': vector(0.54, 0.55, 0.96), 'covalent_radius': 0.62},
    'Mn': {'display_radius': 0.33, 'color': vector(0.60, 0.97, 0.21), 'covalent_radius': 0.94},
    'Fe': {'display_radius': 0.49, 'color': vector(0.06, 0.36, 0.33), 'covalent_radius': 1.28},
    'Co': {'display_radius': 0.43, 'color': vector(0.90, 0.28, 0.04), 'covalent_radius': 1.45},
    'Ni': {'display_radius': 0.45, 'color': vector(0.39, 0.46, 0.19), 'covalent_radius': 1.33},
    'Cu': {'display_radius': 0.4, 'color': vector(0.96, 0.34, 1.00), 'covalent_radius': 1.15},
    'Zn': {'display_radius': 0.29, 'color': vector(0.80, 0.40, 0.26), 'covalent_radius': 0.48},
    'Ga': {'display_radius': 0.26, 'color': vector(0.27, 0.63, 0.40), 'covalent_radius': 1.02},
    'Ge': {'display_radius': 0.28, 'color': vector(0.74, 0.86, 0.44), 'covalent_radius': 0.63},
    'As': {'display_radius': 0.24, 'color': vector(0.52, 0.36, 0.94), 'covalent_radius': 1.14},
    'Se': {'display_radius': 0.35, 'color': vector(0.24, 0.28, 0.47), 'covalent_radius': 1.28},
    'Br': {'display_radius': 0.38, 'color': vector(0.06, 0.13, 0.26), 'covalent_radius': 0.85},
    'Kr': {'display_radius': 0.22, 'color': vector(0.76, 0.66, 0.72), 'covalent_radius': 1.22},
    'Rb': {'display_radius': 0.48, 'color': vector(0.48, 0.29, 0.53), 'covalent_radius': 0.37},
    'Sr': {'display_radius': 0.31, 'color': vector(0.59, 0.55, 0.74), 'covalent_radius': 1.4},
    'Y': {'display_radius': 0.28, 'color': vector(0.05, 0.40, 0.22), 'covalent_radius': 1.13},
    'Zr': {'display_radius': 0.24, 'color': vector(0.15, 0.84, 0.68), 'covalent_radius': 0.48},
    'Nb': {'display_radius': 0.39, 'color': vector(0.74, 0.22, 0.20), 'covalent_radius': 1.35},
    'Mo': {'display_radius': 0.4, 'color': vector(0.49, 0.63, 0.56), 'covalent_radius': 0.45},
    'Tc': {'display_radius': 0.38, 'color': vector(0.43, 0.31, 0.34), 'covalent_radius': 0.43},
    'Ru': {'display_radius': 0.45, 'color': vector(0.74, 0.16, 0.38), 'covalent_radius': 0.72},
    'Rh': {'display_radius': 0.39, 'color': vector(0.22, 0.12, 0.17), 'covalent_radius': 1.17},
    'Pd': {'display_radius': 0.23, 'color': vector(0.13, 0.13, 0.77), 'covalent_radius': 0.54},
    'Ag': {'display_radius': 0.22, 'color': vector(0.41, 0.34, 0.35), 'covalent_radius': 0.54},
    'Cd': {'display_radius': 0.35, 'color': vector(0.36, 0.05, 0.82), 'covalent_radius': 1.17},
    'In': {'display_radius': 0.37, 'color': vector(0.98, 0.57, 0.51), 'covalent_radius': 0.92},
    'Sn': {'display_radius': 0.46, 'color': vector(0.43, 0.52, 0.32), 'covalent_radius': 0.78},
    'Sb': {'display_radius': 0.4, 'color': vector(0.79, 0.09, 0.57), 'covalent_radius': 1.21},
    'Te': {'display_radius': 0.36, 'color': vector(0.91, 0.65, 0.62), 'covalent_radius': 0.49},
    'I': {'display_radius': 0.29, 'color': vector(0.02, 0.06, 0.75), 'covalent_radius': 1.17},
    'Xe': {'display_radius': 0.49, 'color': vector(0.38, 0.96, 0.06), 'covalent_radius': 0.73},
    'Cs': {'display_radius': 0.39, 'color': vector(0.27, 0.61, 0.73), 'covalent_radius': 1.0},
    'Ba': {'display_radius': 0.39, 'color': vector(0.64, 0.11, 0.80), 'covalent_radius': 1.47},
    'La': {'display_radius': 0.25, 'color': vector(0.44, 0.52, 0.33), 'covalent_radius': 1.16},
    'Ce': {'display_radius': 0.21, 'color': vector(0.16, 0.57, 0.42), 'covalent_radius': 0.33},
    'Pr': {'display_radius': 0.24, 'color': vector(0.89, 0.49, 0.60), 'covalent_radius': 1.26},
    'Nd': {'display_radius': 0.29, 'color': vector(0.23, 0.33, 0.21), 'covalent_radius': 0.98},
    'Pm': {'display_radius': 0.24, 'color': vector(0.24, 0.45, 0.92), 'covalent_radius': 1.26},
    'Sm': {'display_radius': 0.43, 'color': vector(0.45, 0.53, 0.40), 'covalent_radius': 1.22},
    'Eu': {'display_radius': 0.27, 'color': vector(0.82, 0.67, 0.52), 'covalent_radius': 1.36},
    'Gd': {'display_radius': 0.25, 'color': vector(0.18, 0.92, 0.65), 'covalent_radius': 1.32},
    'Tb': {'display_radius': 0.31, 'color': vector(0.29, 0.64, 0.86), 'covalent_radius': 1.44},
    'Dy': {'display_radius': 0.37, 'color': vector(0.54, 0.49, 0.23), 'covalent_radius': 0.88},
    'Ho': {'display_radius': 0.42, 'color': vector(0.89, 0.91, 0.40), 'covalent_radius': 0.61},
    'Er': {'display_radius': 0.23, 'color': vector(0.94, 0.79, 0.48), 'covalent_radius': 0.48},
    'Tm': {'display_radius': 0.27, 'color': vector(0.09, 0.38, 0.38), 'covalent_radius': 1.15},
    'Yb': {'display_radius': 0.38, 'color': vector(0.82, 0.54, 0.11), 'covalent_radius': 0.4},
    'Lu': {'display_radius': 0.3, 'color': vector(0.36, 0.98, 0.09), 'covalent_radius': 0.7},
    'Hf': {'display_radius': 0.48, 'color': vector(0.53, 0.48, 0.60), 'covalent_radius': 0.92},
    'Ta': {'display_radius': 0.3, 'color': vector(0.10, 0.06, 0.24), 'covalent_radius': 1.2},
    'W': {'display_radius': 0.48, 'color': vector(0.12, 0.71, 0.84), 'covalent_radius': 0.59},
    'Re': {'display_radius': 0.38, 'color': vector(0.01, 0.20, 0.56), 'covalent_radius': 1.4},
    'Os': {'display_radius': 0.28, 'color': vector(0.71, 0.98, 0.64), 'covalent_radius': 0.39},
    'Ir': {'display_radius': 0.29, 'color': vector(0.47, 0.73, 0.44), 'covalent_radius': 1.46},
    'Pt': {'display_radius': 0.2, 'color': vector(0.73, 0.15, 0.50), 'covalent_radius': 0.49},
    'Au': {'display_radius': 0.28, 'color': vector(0.97, 0.85, 0.86), 'covalent_radius': 0.77},
    'Hg': {'display_radius': 0.5, 'color': vector(0.25, 0.59, 0.71), 'covalent_radius': 0.81},
    'Tl': {'display_radius': 0.35, 'color': vector(0.10, 0.83, 0.41), 'covalent_radius': 0.3},
    'Pb': {'display_radius': 0.29, 'color': vector(0.13, 0.82, 0.27), 'covalent_radius': 0.44},
    'Bi': {'display_radius': 0.49, 'color': vector(0.31, 0.89, 0.56), 'covalent_radius': 1.03},
    'Th': {'display_radius': 0.21, 'color': vector(0.86, 0.13, 0.28), 'covalent_radius': 0.52},
    'Pa': {'display_radius': 0.39, 'color': vector(0.07, 0.02, 0.29), 'covalent_radius': 1.38},
    'U': {'display_radius': 0.48, 'color': vector(0.88, 0.59, 0.11), 'covalent_radius': 1.24},
}

def load_xyz(filename):
    """Load an XYZ file and return a list of atoms with element symbols and positions."""
    atoms = []
    

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]  # Remove empty lines
            print(f"Lines read from {filename}: {lines}")  # Debugging info
            
            if len(lines) < 2:
                print(f"File {filename} is too short to be a valid XYZ file.")
                return []

            try:
                n_atoms = int(lines[0])  # Read atom count
                print(f"Expected number of atoms: {n_atoms}")  # Debugging info
            except ValueError:
                print(f"Invalid atom count in {filename}: {lines[0]}")
                return []
            
            if len(lines) < n_atoms + 2:
                print(f"Incomplete data in {filename}. Expected {n_atoms} atoms but found {len(lines)-2}.")
                return []

            for line in lines[2:2 + n_atoms]:  # Read exactly n_atoms lines after the comment
                parts = line.split()
                print(f"Processing line: {line}")  # Debugging info
                if len(parts) != 4:
                    print(f"Skipping invalid line in {filename}: {line}")
                    continue  # Skip malformed lines
                
                element = parts[0]
                if element not in element_data:
                    print(f"Unknown element '{element}' in {filename}, skipping.")
                    continue  # Skip unknown elements
                
                try:
                    x, y, z = map(float, parts[1:])
                except ValueError:
                    print(f"Invalid coordinate format in {filename}: {line}")
                    continue  # Skip lines with invalid coordinates
                
                atoms.append({'element': element, 'pos': vector(x, y, z)})

    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return []
    
    if not atoms:
        print(f"No valid atoms found in {filename}.")
    
    return atoms


def visualize_molecule(atoms):
    """Visualize atoms as spheres and draw bonds based on covalent radii."""
    # Clear any existing objects in the scene.
    scene.delete()
    # Draw atoms.
    for atom in atoms:
        prop = element_data.get(atom['element'],
                                  {'display_radius': 0.3, 'color': color.green, 'covalent_radius': 0.7})
        sphere(pos=atom['pos'], radius=prop['display_radius'], color=prop['color'])
    # Draw bonds.
    draw_bonds(atoms)

def draw_bonds(atoms):
    """Draw bonds between atoms if their separation is less than the threshold multiplier times the sum of their covalent radii."""
    threshold_multiplier = 1.3 
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            pos1 = atoms[i]['pos']
            pos2 = atoms[j]['pos']
            d = mag(pos2 - pos1)
            r1 = element_data.get(atoms[i]['element'], {'covalent_radius': 0.7})['covalent_radius']
            r2 = element_data.get(atoms[j]['element'], {'covalent_radius': 0.7})['covalent_radius']
            if d < threshold_multiplier * (r1 + r2):
                cylinder(pos=pos1, axis=pos2 - pos1, radius=0.1, color=color.gray(0.5))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Molecular Viewer GUI")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def create_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open XYZ File", "",
                                                  "XYZ Files (*.xyz);;All Files (*)", options=options)
        if filename:
            atoms = load_xyz(filename)
            if atoms:
                visualize_molecule(atoms)
            else:
                QMessageBox.warning(self, "Error", "Failed to load molecule from file.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
