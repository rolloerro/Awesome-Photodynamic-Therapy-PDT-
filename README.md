# Awesome Photodynamic Therapy (PDT)

A curated list of resources, tools, bots, protocols, and research papers on photodynamic therapy (PDT) — from theory and clinical practice to digital tools and conference highlights.

## Table of Contents
- [Overview](#overview)
- [Bots & Calculators](#bots--calculators)
- [Clinical Guidelines and Protocols](#clinical-guidelines-and-protocols)
- [Equipment and Dosage](#equipment-and-dosage)
- [Master Classes and Tutorials](#master-classes-and-tutorials)
- [Research and Conference Highlights](#research-and-conference-highlights)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Photodynamic therapy (PDT) is a minimally invasive treatment using photosensitizers and light to target diseased cells. This list covers theoretical knowledge, clinical applications, digital tools, bots, and community resources.

---

## Bots & Calculators

### 1️⃣ FDTcalc05_bot
**Type:** Telegram Bot  
**Description:** Multi‑module PDT calculator (Cervical, Endoscopy/Urology, Skin, Cervix/Vulva/Vagina). Step‑by‑step parameter selection: diffuser length, power, distance, dose. Calculates K-factor, exposure time, total energy, recommended power density. Engineered for research and educational purposes — clinical use only per protocol.  
**GitHub:** [FDTcalc05_bot](https://github.com/rolloerro/fdtcalc05_bot)  
**Example:**
```python
# Start interaction in Telegram
# /start → select module → enter parameters
# Bot returns K-factor, exposure time, total energy
2️⃣ pdt-core
Type: Python Module
Description: Core PDT calculator module used by bots to compute K-factor, dosage and exposure time.
GitHub: pdt-core
Example:

from pdt.calculators import calculate_cervix_fdt
result = calculate_cervix_fdt(length_cm=2.5, power_mw=150, dose_j_cm2=50)
print(result)
3️⃣ Radapharma Bot
Type: Telegram Bot
Description: Provides PDT session assistance and clinical references under Radapharma umbrella.
GitHub: [fill_in_real_URL]
Example:

# /start → choose clinical guidance → bot returns protocols or links
4️⃣ Gynecology PDT Bot
Type: Telegram Bot
Description: PDT calculator and guidance for gynecological indications.
GitHub: [fill_in_real_URL]
Example:

# /start → select "Gynecology" → input parameters
5️⃣ Urology PDT Bot
Type: Telegram Bot
Description: Urological PDT parameters and calculators.
GitHub: [fill_in_real_URL]
Example:

# /start → choose "Urology" → input data
6️⃣ Assessment Bot
Type: Telegram Bot
Description: Tracks PDT outcomes and assessments for clinical research logging.
GitHub: [fill_in_real_URL]
Example:

# /start → log treatment → bot saves summary/outcome
7️⃣ Basaloma PDT Bot
Type: Telegram Bot
Description: PDT support tool for basal cell carcinoma and dermatology workflows.
GitHub: [fill_in_real_URL]
Example:

# /start → choose "Basaloma" → bot calculates exposure & protocols
8️⃣ Practice Bot
Type: Telegram Bot
Description: Practical PDT tutorial / step‑by‑step state machine for clinical learners.
GitHub: [fill_in_real_URL]
Example:

# /start → choose practice module → walk-through tutorial
9️⃣ Procedure Bot
Type: Telegram Bot
Description: Guides through PDT procedure steps with prompts and checks.
GitHub: [fill_in_real_URL]
Example:

# /start → choose procedure type → bot guides actions
🔟 Clinical Assistant Bot
Type: Telegram Bot
Description: Combines reference protocols and decision support for PDT clinics.
GitHub: [fill_in_real_URL]
Example:

# /start → choose clinical assistant → bot offers structured guidance
1️⃣1️⃣ FDT Manual Bot
Type: Telegram Bot
Description: Offers educational PDT manuals, PDFs (linked), and quick‑reference cards.
GitHub: [fill_in_real_URL]
Example:

# /start → choose manual → bot returns link or summary
Clinical Guidelines and Protocols
Protocols for urology, gynecology, dermatology, and oncology applications.

Step-by-step treatment algorithms for specific conditions.

Evidence-based recommendations from peer-reviewed studies.

Equipment and Dosage
Overview of lasers, light sources, and photosensitizers.

Recommended dosages and treatment planning guides.

Integration with bots for automated calculations and patient management.

Master Classes and Tutorials
Dermatology PDT Master Class

Gynecology PDT Master Class

Urology PDT Master Class

Video tutorials, webinars, and hands-on demonstrations from experts.

Research and Conference Highlights
🧪 IPA World Congress 2025 — Shanghai, China
19th International Photodynamic Association World Congress (IPA 2025): global conference on PDT, June 10–16, 2025, Shanghai. (official site)

Key Topics: Photosensitizers, dosimetry, clinical applications, nanotechnology, antimicrobial PDT.

Notable Speakers: Prof. Tayyaba Hasan, Prof. Xiuli Wang.

Awards 2025: Recognizing contributions in clinical and translational PDT.
# Awesome Photodynamic Therapy (PDT)

This repository collects **tools, bots, calculators, tutorials, and master classes** for Photodynamic Therapy (PDT) applications across dermatology, gynecology, urology, and clinical practice.

---

## Bots

- [FDTcalc05_bot](bots/fdtcalc05_bot/fdtcalc05_bot.py) — Universal PDT calculator for cervical, endoscopy, skin, and vulvar modules.
- [RADAPHARMA Bot](bots/radafarma_bot) — Educational & reference bot for PDT protocols.
- [Gynecology Bot](bots/gynecology_bot) — PDT guidance for gynecological procedures.
- [Urology Bot](bots/urology_bot) — PDT endoscopy & urology support bot.
- [Assessment Bot](bots/assessment_bot) — Calculates dose, exposure, and K-factors.
- [Basalioma Bot](bots/basalioma_bot) — Focused on basal cell carcinoma PDT.
- [Practice Bot](bots/practice_bot) — Interactive exercises for hands-on learning.
- [Procedure Bot](bots/procedure_bot) — Step-by-step PDT procedure guide.
- [Clinical Assistant Bot](bots/clinical_assistant_bot) — Clinical PDT assistance and reference.
- [PDT Manual Bot](bots/pdt_manual_bot) — Reference bot for PDT educational materials.

- **Core Module:** [pdt-core](bots/pdt-core) — shared library for calculations and utilities used by all bots.

---

## Master Classes and Tutorials

- **Dermatology PDT Master Class**  
  Step-by-step tutorials and practical sessions for skin-related PDT procedures. Includes guidance on basal cell carcinoma, dosimetry, and micro/macrolens techniques.

- **Gynecology PDT Master Class**  
  Covers cervical and vulvar PDT applications, diffuser selection, laser settings, dose calculations, and clinical protocols.  

- **Urology PDT Master Class**  
  Focused on endoscopic PDT procedures in urology. Includes guidance on laser power, diffuser lengths, and distance considerations.  

- **Clinical Simulation & Practice Modules**  
  Interactive exercises with FDTcalc05_bot for hands-on learning of dose calculation, exposure time, and K-factor estimations.

- **ShangHai PDT Conference 2025 Highlights** 🧪  
  - **Event:** 19th International Photodynamic Association World Congress (IPA 2025), June 10–16, Shanghai, China  
  - **Topics Covered:** Photosensitizers, dosimetry, clinical applications, nanotechnology, antimicrobial PDT  
  - **Speakers:** Prof. Tayyaba Hasan, Prof. Xiuli Wang  
  - **Awards & Innovations 2025:** Recognizing contributions in clinical and translational PDT  
  - [Official Conference Site](https://www.internationalphotodynamic.com/other-pdt-events-1/2025/6/10/19th-international-photodynamic-association-world-congress?utm_source=chatgpt.com)  

> ⚠️ PDFs and slides from the conference are not included due to copyright. Publicly available resources can be linked or stored in a separate repository.

---

## Installation

```bash
# Clone repo
git clone https://github.com/rolloerro/Awesome-Photodynamic-Therapy-PDT-.git
cd Awesome-Photodynamic-Therapy-PDT-

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install bot dependencies
pip install -r bots/fdtcalc05_bot/requirements.txt

📄 Key Publications
Clinical Study on PDT for Basal Cell Carcinoma (2024)

Photodynamic Therapy for Gynecological Conditions

Antimicrobial PDT Applications

PDT Dosimetry Innovations

Running FDTcalc05_bot
# Copy your Telegram token
cp bots/fdtcalc05_bot/.env.example bots/fdtcalc05_bot/.env

# Run bot
python3 bots/fdtcalc05_bot/fdtcalc05_bot.py

Make sure pdt-core folder is in bots/ for local imports.

Contributing

Add your own modules, bots, or educational materials.

Follow the folder structure: bots/<bot_name> or docs/<material_name>.

Pull requests and issues are welcome.

⚠️ PDFs are linked only if publicly accessible. Personal PDFs / slides can be added to a separate repo: awesome-pdt-resources.

Contributing
We welcome contributions! Please follow these guidelines:

Use Markdown format.

Include a short description and link.

Submit PRs for new bots, tools, studies, or tutorials.

Ensure resources are open-access or link to official publications.

License
MIT License
