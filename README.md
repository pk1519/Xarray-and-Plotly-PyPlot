# Bridge Visualizer - Shear Force & Bending Moment Analysis

A comprehensive Python application for visualizing structural analysis data of bridge girders using Xarray and Plotly. This project provides both 2D and 3D visualization capabilities for Shear Force Diagrams (SFD) and Bending Moment Diagrams (BMD).

## 🌟 Features

- **2D Visualization**: Traditional shear force and bending moment diagrams using Matplotlib
- **3D Interactive Visualization**: Interactive 3D plots using Plotly for enhanced analysis
- **Multi-Girder Support**: Analyze up to 5 bridge girders simultaneously
- **Data Inspection**: Built-in tools to explore NetCDF dataset structure
- **Force Scaling**: Adjustable scaling factors for better visualization

## 📁 Project Structure

```
bridge_visualizer/
├── data/
│   ├── element.py          # Element connectivity definitions
│   ├── node.py            # Node coordinates
│   └── screening_task.nc  # Structural analysis dataset (NetCDF)
├── task1_sfd_bmd.py        # 2D SFD and BMD visualization
├── task2_3d_sfd_bmd.py     # 3D interactive visualization
├── inspect_data.py         # Data inspection utility
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pk1519/Xarray-and-Plotly-PyPlot.git
cd Xarray-and-Plotly-PyPlot
```

2. Install dependencies:
```bash
pip install xarray numpy matplotlib plotly netcdf4
```

3. Run the visualizations:

**For 2D SFD and BMD (Central Girder Analysis):**
```bash
python task1_sfd_bmd.py
```

**For 3D Interactive Visualization (All Girders):**
```bash
python task2_3d_sfd_bmd.py
```

**To Inspect the Dataset:**
```bash
python inspect_data.py
```

## 📊 Data Structure

The project uses a NetCDF dataset (`screening_task.nc`) containing structural analysis results:

- **Forces Dataset**: Contains shear forces (Vy) and bending moments (Mz) for each element
- **Element Connectivity**: Defines how nodes are connected to form structural elements
- **Node Coordinates**: 3D positions of structural nodes

### Key Components

- **Elements**: Structural beam elements connecting nodes
- **Nodes**: 3D coordinate points defining the bridge geometry
- **Force Components**:
  - `Vy_i`, `Vy_j`: Shear forces at element start and end
  - `Mz_i`, `Mz_j`: Bending moments at element start and end

## 🛠️ Usage Examples

### 2D Visualization (task1_sfd_bmd.py)
Analyzes the central girder (elements 15, 24, 33, 42, 51, 60, 69, 78, 83) and generates:
- Shear Force Diagram with filled area plot
- Bending Moment Diagram with filled area plot
- Grid-based layout for easy reading

### 3D Visualization (task2_3d_sfd_bmd.py)
Provides interactive 3D visualization of all 5 girders:
- **Black lines**: Original bridge girder geometry
- **Red lines**: Shear force distribution (scaled)
- **Blue lines**: Bending moment distribution (scaled)
- Interactive rotation, zoom, and pan capabilities

### Customization

Adjust the scaling factor in `task2_3d_sfd_bmd.py`:
```python
scale = 0.4  # Modify this value to change force visualization scale
```

## 🔧 Technical Details

### Dependencies
- **xarray**: For NetCDF data handling
- **numpy**: Numerical computations
- **matplotlib**: 2D plotting
- **plotly**: Interactive 3D visualization
- **netcdf4**: NetCDF file support

### Data Processing Pipeline
1. Load NetCDF dataset using Xarray
2. Extract element connectivity from node definitions
3. Calculate element lengths and positions
4. Query force components for each element
5. Generate visualizations with appropriate scaling

## 📈 Output Examples

### 2D Plots
- Shear Force Diagram showing force distribution along girder length
- Bending Moment Diagram displaying moment variations
### Screenshot
<img width="802" height="685" alt="image" src="https://github.com/user-attachments/assets/c930f291-f488-4526-804b-b43394a62a1f" />

<img width="805" height="681" alt="image" src="https://github.com/user-attachments/assets/4c216b33-f15c-4180-b3bf-e3d799c2cc9a" />


### 3D Interactive Plot
- Multi-girder visualization with force overlays
- Color-coded force types (red for shear, blue for moment)
- Interactive controls for detailed analysis
### Screenshot
<img width="1919" height="989" alt="image" src="https://github.com/user-attachments/assets/3a2b1af8-e88e-4a5c-9c2d-1366a34e09f9" />

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Xarray for efficient data handling
- Visualizations powered by Matplotlib and Plotly
- Structural analysis concepts from civil engineering principles

## 📞 Contact

For questions or suggestions, please open an issue in the GitHub repository or contact [pk1519](https://github.com/pk1519).

---

**Note**: Ensure the `data/screening_task.nc` file is present in the data directory before running the visualization scripts.
