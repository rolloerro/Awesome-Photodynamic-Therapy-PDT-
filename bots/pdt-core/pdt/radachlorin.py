"""
Radachlorin (Радахлорин)
Фотосенсибилизатор для ФДТ
"""

from dataclasses import dataclass
from pdt.models import PhotosensitizerDose


@dataclass(frozen=True)
class Radachlorin:
    """
    Эталонный фотосенсибилизатор Радахлорин.
    Все параметры заданы явно и неизменяемы.
    """

    name: str = "Radachlorin"
    active_substance: str = "Chlorin e6 sodium salt"

    # Pharmacology
    recommended_dose: PhotosensitizerDose = PhotosensitizerDose(
        mg_per_kg=1.0
    )

    # Optical properties
    absorption_peak_nm: int = 662

    # Clinical notes
    light_sensitivity_window_hours: int = 48
    typical_accumulation_time_minutes: int = 120
