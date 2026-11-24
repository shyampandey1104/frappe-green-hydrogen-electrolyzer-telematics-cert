import unittest
from green_hydrogen_telematics.engine import ElectrolyzerHourlyTelemetry, GreenHydrogenCertificationEngine

class TestGreenHydrogenCertificationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GreenHydrogenCertificationEngine("PLANT-KUTCH-H2-01")

    def test_telemetry_sec_and_certification(self):
        tele = ElectrolyzerHourlyTelemetry(
            stack_id="PEM-STACK-04", timestamp="2026-03-01T12:00:00",
            renewable_energy_consumed_kwh=5250.0, hydrogen_produced_kg=100.0,
            stack_temperature_celsius=68.5, water_flow_litres_per_hr=900.0,
            co2e_emissions_kg=85.0
        )
        res = self.engine.record_production_telemetry(tele)
        self.assertEqual(res["specific_energy_consumption_kwh_per_kg"], 52.5)
        self.assertTrue(res["qualifies_as_green_hydrogen"])

    def test_guarantee_of_origin_issuance(self):
        cert = self.engine.issue_guarantee_of_origin("LOT-GREEN-H2-2026-09", 1000.0)
        self.assertTrue(cert["cert_id"].startswith("GO-H2-"))
        self.assertEqual(cert["verified_standard"], "MNRE_NGHM_STANDARD_2026")

if __name__ == "__main__":
    unittest.main()
