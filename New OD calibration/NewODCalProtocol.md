# New OD Calibration Protocol

We have noticed that the glass vial has a strong impact on the OD measurements. In order to improve this, we have changed the calibration protocol. Instead of rotating the 16 vials around the different smart-sleeves, we now keep a vial at the same position and we sequentially add cells manually in each vial to the desired OD values that define the calibration range. This way we never move the vials.

However, we must then edit the calibration file to permute the measurements, as eVOLVER believes that we are rotating the vials. For this, you can use any of the scripts provided here.

## Step-by-step protocol

### Initial calculations
- Calculate:
    - Calibration range.
    - Inoculation volume of each of the 15 steps.
    - Approximate concentration of cells stock used to inoculate
    - Total amount of of cells needed.

### eVOLVER preparation
- Prepare 500 mL of PBS and keep it at calibration temperature (e.g. 32ºC, 10 units of stirring)
- Prepare 16 glass vials. Clean the outside with isopropanol and dust-free cloth or paper towel.
- Fill vials, place them in eVOLVER and start a mock experiment: set configuration to calibration temperature and no dilution.
- Open the plots and wait until temperature is stable.
- Stop experiment

### Cell Handling
1. Grow your cells to exponential phase (OD of around 0.45 for S. pombe)
2. Spin them down and wash them with PBS
3. Spin them down and resuspend to the desired concentration (e.g. 12 ODs)
4. Measure OD of this stock in triplicate. Make sure you use the linear range of the spectrophotometer (for instance, by doing two sequential 1:10 and 1:5 dilution)
5. Fine tune the calculations using the measured OD

### Calibration
DO NOT ADD ANY CELLS!
1. Start calibration software
2. First thing to do is to take the BLANK MEASUREMENT
3. Wait until the measurement are taken.
4. Vortex cell stock and inoculate the desired volume in all vials.
5. Wait about 30s for the cells to properly mix.
6. Take measurements
7. Repeat steps 3-6 untill all the measurements are taken.
8. Save calibration
9. OPTIONAL: Measure final OD of vials after calibration. Again, make sure the spectrophotometer is used in the linear range.

### Finalising
If you used the original OD calibration software, we need to reorganise the calibration data, since it is stored as if we had been rotating the vials around. For this purpose, you can use any of the provided scripts.