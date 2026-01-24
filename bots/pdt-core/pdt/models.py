from dataclasses import dataclass
from typing import Optional


@dataclass
class Patient:
    """
    Пациент для ФДТ.
    Минимальный набор, без персональных данных.
    """
    weight_kg: float
    age_years: Optional[int] = None


@dataclass
class Tumor:
    """
    Опухолевый очаг / зона воздействия ФДТ.
    """
    location: str  # кожа, шейка матки, цервикальный канал и т.д.
    diameter_cm: Optional[float] = None  # для поверхностных форм
    depth_cm: Optional[float] = None     # опционально


@dataclass
class PhotosensitizerDose:
    """
    Доза фотосенсибилизатора.
    """
    mg_per_kg: float


@dataclass
class LightExposure:
    """
    Параметры светового воздействия.
    """
    wavelength_nm: int
    energy_j_cm2: float
    power_mw: Optional[int] = None
    duration_minutes: Optional[float] = None


@dataclass
class PDTProtocol:
    """
    Итоговый протокол ФДТ.
    """
    drug_name: str
    patient: Patient
    tumor: Tumor
    dose: PhotosensitizerDose
    light: LightExposure
    notes: Optional[str] = None
