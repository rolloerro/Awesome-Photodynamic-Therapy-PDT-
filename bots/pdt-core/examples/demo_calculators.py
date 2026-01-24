# examples/demo_calculators.py
from pdt.calculators import (
    calculate_cervix_fdt,
    calculate_endoscopy_fdt,
    calculate_skin_fdt
)

def demo():
    print("=== PDT Calculators Demo ===\n")

    # --- Cervix module example ---
    cervix_result = calculate_cervix_fdt(length_cm=3, power_mw=500, dose_jcm2=300)
    print("Cervix FDT Result:", cervix_result)

    # --- Endoscopy / Urology module example ---
    endoscopy_result = calculate_endoscopy_fdt(length_cm=4, power_mw=800, dose_jcm2=400, distance_cm=0.5)
    print("Endoscopy FDT Result:", endoscopy_result)

    # --- Skin / Neck module example ---
    skin_result = calculate_skin_fdt(diameter_cm=2, power_mw=600, dose_jcm2=250, power_density=0.5)
    print("Skin FDT Result:", skin_result)

if __name__ == "__main__":
    demo()
