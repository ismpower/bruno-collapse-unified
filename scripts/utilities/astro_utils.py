# scripts/utilities/astro_utils.py
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.cosmology import Planck18 as cosmo
import numpy as np

def hms_to_deg(ra_str, dec_str):
    """Convert RA/Dec from HMS/DMS strings to decimal degrees."""
    coord = SkyCoord(ra_str, dec_str, unit=(u.hourangle, u.deg))
    return coord.ra.deg, coord.dec.deg

def redshift_to_distance(z):
    """Convert redshift to luminosity distance in Mpc using Planck18."""
    return cosmo.luminosity_distance(z).value  # in Mpc

def fluence_from_distance(distance_mpc, energy_erg=1e51):
    """Compute fluence at Earth in J/m² from energy and distance."""
    d_m = distance_mpc * 3.0857e22  # Mpc to meters
    fluence = energy_erg / (4 * np.pi * d_m**2)  # in erg/cm² → J/m²
    return fluence
