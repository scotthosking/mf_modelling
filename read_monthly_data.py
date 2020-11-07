import xarray as xr

'''

Aim: To build a multifidelity ML model to predict high-resolution gridded
	surface temperature climate simulation out from contemporaneous 
	coarse-resolution climate simulation output

hi  = high fidelity data
lo  = low fidelity data

t2m  = temperature at 2 meters above the ground
u10, v10 = wind components (eastward, northward) at 10m above the ground

lat = latitude
lon = longitude

'''

### Regional gridded output from a Regional Climate Model (RCM)
hi_t2 = xr.open_dataset('data/hifid_t2m_monthly.nc').T2
hi_lat_grid = hi_t2.lat.values
hi_lon_grid = hi_t2.lon.values 

### Global gridded reanalysis (data assimilated) used to update/force the 
### lateral boundaries of the RCM
lo_t2  = xr.open_dataset('data/lofid_t2m_monthly.nc').t2m
lo_u10 = xr.open_dataset('data/lofid_u10_monthly.nc').u10
lo_v10 = xr.open_dataset('data/lofid_v10_monthly.nc').v10

### work with numpy arrays
hi_t2_arr  = hi_t2.values
lo_t2_arr  = lo_t2.values 
lo_u10_arr = lo_u10.values
lo_v10_arr = lo_v10.values
time_dim   = lo_t2.time.values 
