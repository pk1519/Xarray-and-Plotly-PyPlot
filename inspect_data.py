import xarray as xr

ds = xr.open_dataset("data/screening_task.nc")

print(ds)
print("\nVariables:")
print(ds.data_vars)

print("\nComponents:")
print(ds["Component"].values)
