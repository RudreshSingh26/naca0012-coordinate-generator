# NACA 0012 Coordinate Generator

Python script that generates NACA 0012 airfoil coordinates from the analytical thickness equation, with cosine clustering toward the leading and trailing edges and a closed trailing edge. Output is formatted for direct import into ANSYS DesignModeler as a curve file.

## What it does

- Generates upper and lower surface points using the standard NACA 4-digit thickness formula
- Cosine-spaces points to concentrate resolution at LE and TE where curvature is highest
- Forces a closed trailing edge (modified last-term coefficient)
- Writes a `.txt` file in the 3-column `group X Y Z` format that DesignModeler expects

## Usage

```bash
python naca0012_coords.py
```

Edit the script header to change number of points or output filename.

## Output

A text file importable directly via DesignModeler → Concept → 3D Curve.

## Context

Built as part of a validated 2D RANS simulation of the NACA 0012 airfoil in ANSYS Fluent (SST k-ω, wall-resolved mesh, y⁺ < 1). Validation against NASA CFL3D reference and Ladson experimental data gave lift coefficients within ~2% across an AoA sweep of 0°–10°. Full report available on request.
