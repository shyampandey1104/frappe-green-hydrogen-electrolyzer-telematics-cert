"""National Green Hydrogen Mission (NGHM) Electrolyzer Telematics & Guarantee of Origin Engine."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional

@dataclass
class ElectrolyzerHourlyTelemetry:
    stack_id: str
    timestamp: str
    renewable_energy_consumed_kwh: float
    hydrogen_produced_kg: float
    stack_temperature_celsius: float
    water_flow_litres_per_hr: float
    co2e_emissions_kg: float = 0.0      # Must be strictly < 2.0 kg CO2e / kg H2

class GreenHydrogenCertificationEngine:
    def __init__(self, facility_id: str):
        self.facility_id = facility_id
        self.telemetry_logs: List[ElectrolyzerHourlyTelemetry] = []
        self.certificates: List[Dict[str, Any]] = []

    def record_production_telemetry(self, tele: ElectrolyzerHourlyTelemetry) -> Dict[str, Any]:
        if tele.hydrogen_produced_kg <= 0:
            raise ValueError("Hydrogen produced must be greater than zero.")
        
        # Specific Energy Consumption (SEC): standard ~50-55 kWh / kg H2
        sec = round(tele.renewable_energy_consumed_kwh / tele.hydrogen_produced_kg, 2)
        carbon_intensity = round(tele.co2e_emissions_kg / tele.hydrogen_produced_kg, 3)
        
        # NGHM & EU RED II threshold: Carbon intensity must be <= 2.0 kg CO2e/kg H2
        is_green_certified = carbon_intensity <= 2.0
        self.telemetry_logs.append(tele)

        return {
            "stack_id": tele.stack_id,
            "specific_energy_consumption_kwh_per_kg": sec,
            "carbon_intensity_kg_co2e_per_kg": carbon_intensity,
            "qualifies_as_green_hydrogen": is_green_certified
        }

    def issue_guarantee_of_origin(self, batch_lot_no: str, total_kg: float) -> Dict[str, Any]:
        cert = {
            "cert_id": f"GO-H2-{self.facility_id}-{len(self.certificates) + 1:04d}",
            "batch_lot_no": batch_lot_no,
            "green_hydrogen_kg": total_kg,
            "verified_standard": "MNRE_NGHM_STANDARD_2026",
            "timestamp": datetime.now().isoformat()
        }
        self.certificates.append(cert)
        return cert
