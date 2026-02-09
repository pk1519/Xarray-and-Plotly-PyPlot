import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

from data.element import members
from data.node import nodes

# -------------------
# Load dataset
# -------------------
ds = xr.open_dataset("data/screening_task.nc")

central_elements = [15,24,33,42,51,60,69,78,83]

x_positions = []
shear = []
moment = []

current_length = 0

for ele in central_elements:

    ni, nj = members[ele]

    xi = np.array(nodes[ni])
    xj = np.array(nodes[nj])

    length = np.linalg.norm(xj - xi)

    # ---- Select force components ----
    Vy_i = ds["forces"].sel(Element=ele, Component="Vy_i").values.item()
    Vy_j = ds["forces"].sel(Element=ele, Component="Vy_j").values.item()

    Mz_i = ds["forces"].sel(Element=ele, Component="Mz_i").values.item()
    Mz_j = ds["forces"].sel(Element=ele, Component="Mz_j").values.item()

    x_positions.extend([current_length, current_length + length])
    shear.extend([Vy_i, Vy_j])
    moment.extend([Mz_i, Mz_j])

    current_length += length

# -------------------
# Plot SFD
# -------------------
plt.figure()
plt.plot(x_positions, shear)
plt.fill_between(x_positions, shear, 0, alpha=0.3)
plt.title("Shear Force Diagram")
plt.xlabel("Girder Length")
plt.ylabel("Vy")
plt.grid()
plt.show()

# -------------------
# Plot BMD
# -------------------
plt.figure()
plt.plot(x_positions, moment)
plt.fill_between(x_positions, moment, 0, alpha=0.3)
plt.title("Bending Moment Diagram")
plt.xlabel("Girder Length")
plt.ylabel("Mz")
plt.grid()
plt.show()
