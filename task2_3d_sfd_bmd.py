import xarray as xr
import numpy as np
import plotly.graph_objects as go

from data.element import members
from data.node import nodes

# Load dataset
ds = xr.open_dataset("data/screening_task.nc")

girders = {
    1: [13,22,31,40,49,58,67,76,81],
    2: [14,23,32,41,50,59,68,77,82],
    3: [15,24,33,42,51,60,69,78,83],
    4: [16,25,34,43,52,61,70,79,84],
    5: [17,26,35,44,53,62,71,80,85],
}

scale = 0.4
fig = go.Figure()

for gid, elements in girders.items():

    for ele in elements:

        ni, nj = members[ele]

        xi = np.array(nodes[ni])
        xj = np.array(nodes[nj])

        # ✅ correct dataset access
        Vy_i = ds["forces"].sel(Element=ele, Component="Vy_i").values.item()
        Vy_j = ds["forces"].sel(Element=ele, Component="Vy_j").values.item()

        Mz_i = ds["forces"].sel(Element=ele, Component="Mz_i").values.item()
        Mz_j = ds["forces"].sel(Element=ele, Component="Mz_j").values.item()

        # base beam
        fig.add_trace(go.Scatter3d(
            x=[xi[0], xj[0]],
            y=[xi[1], xj[1]],
            z=[xi[2], xj[2]],
            mode='lines',
            line=dict(color='black', width=4),
            showlegend=False
        ))

        # shear extrusion
        fig.add_trace(go.Scatter3d(
            x=[xi[0], xj[0]],
            y=[xi[1] + Vy_i*scale, xj[1] + Vy_j*scale],
            z=[xi[2], xj[2]],
            mode='lines',
            line=dict(color='red', width=5),
            name="Shear"
        ))

        # moment extrusion
        fig.add_trace(go.Scatter3d(
            x=[xi[0], xj[0]],
            y=[xi[1] + Mz_i*scale, xj[1] + Mz_j*scale],
            z=[xi[2], xj[2]],
            mode='lines',
            line=dict(color='blue', width=5),
            name="Moment"
        ))

fig.update_layout(
    title="3D Shear & Bending Moment Diagram",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Force Scale",
        zaxis_title="Z"
    )
)

fig.show()
