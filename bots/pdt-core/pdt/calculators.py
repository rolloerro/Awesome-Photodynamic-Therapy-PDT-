# pdt/calculators.py
import math
from typing import Dict

# -------------------
# ФДТ Цервикальный канал
# -------------------
def calculate_cervix_fdt(length_cm: float, power_mw: float, dose_jcm2: float) -> Dict[str, int]:
    """
    Расчет экспозиции для ФДТ цервикального канала (fixed distance 0.1 см).

    Args:
        length_cm: длина диффузора в см
        power_mw: мощность лазера в мВт
        dose_jcm2: доза в Дж/см²

    Returns:
        dict с результатами: K, T_minutes, minutes, seconds
    """
    K = length_cm * 104  # коэффициент из формулы бота
    T_minutes = (dose_jcm2 * K) / (power_mw * 10.0)
    minutes = int(math.floor(T_minutes))
    seconds = int(round((T_minutes - minutes) * 60))
    if seconds == 60:
        minutes += 1
        seconds = 0
    return {
        "K": K,
        "T_minutes": round(T_minutes, 2),
        "minutes": minutes,
        "seconds": seconds
    }
def calculate_endoscopy_fdt(length_cm: float, power_mw: float, dose_jcm2: float, distance_cm: float) -> Dict[str, float]:
    """
    Расчет экспозиции для ФДТ эндоскопия/урология (variable distance).

    Args:
        length_cm: длина диффузора в см
        power_mw: мощность лазера в мВт
        dose_jcm2: доза в Дж/см²
        distance_cm: расстояние до ткани в см

    Returns:
        dict с результатами: K, T_minutes, exposure_seconds
    """
    K = length_cm * 104 / distance_cm  # дистанционный коэффициент
    T_minutes = (dose_jcm2 * K) / (power_mw * 10.0)
    minutes = int(math.floor(T_minutes))
    seconds = int(round((T_minutes - minutes) * 60))
    if seconds == 60:
        minutes += 1
        seconds = 0
    return {
        "K": K,
        "T_minutes": round(T_minutes, 2),
        "minutes": minutes,
        "seconds": seconds
    }
def calculate_skin_fdt(diameter_cm: float, power_mw: float, dose_jcm2: float, power_density: float) -> Dict[str, float]:
    """
    Расчет экспозиции для ФДТ кожи и шейки/вульвы.

    Args:
        diameter_cm: диаметр новообразования в см
        power_mw: мощность лазера в мВт
        dose_jcm2: доза в Дж/см²
        power_density: плотность мощности (0.2..0.7)

    Returns:
        dict с результатами: area, energy_j, T_minutes, minutes, seconds
    """
    area_cm2 = math.pi * (diameter_cm / 2) ** 2
    energy_j = dose_jcm2 * area_cm2
    T_minutes = energy_j / (power_mw * power_density)
    minutes = int(math.floor(T_minutes))
    seconds = int(round((T_minutes - minutes) * 60))
    if seconds == 60:
        minutes += 1
        seconds = 0
    return {
        "area_cm2": round(area_cm2, 2),
        "energy_j": round(energy_j, 2),
        "T_minutes": round(T_minutes, 2),
        "minutes": minutes,
        "seconds": seconds
    }
