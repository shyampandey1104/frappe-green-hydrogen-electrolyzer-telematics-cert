# Frappe Green Hydrogen Electrolyzer Telematics & Guarantee of Origin (GO) Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![NGHM India](https://img.shields.io/badge/MNRE-Green%20Hydrogen%20Mission-emerald.svg)]()
[![EU RED II](https://img.shields.io/badge/EU%20RED%20II-RFNEO%20Standard-green.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under the **National Green Hydrogen Mission (NGHM)** and European Union **RED II (Renewable Energy Directive)**:
1. Hydrogen qualifies as "Green" ONLY if its lifecycle carbon intensity is strictly **below 2.0 kg $CO_2e$ per kg $H_2$**.
2. Electrolyzer plants (PEM and Alkaline stacks) require continuous monitoring of **Specific Energy Consumption (SEC - kWh per kg of $H_2$)** to optimize stack degradation and electrical efficiency.
3. International buyers (green ammonia and steel mills) demand cryptographic **Guarantee of Origin (GO)** certificates verifying hourly matching with dedicated solar/wind renewable power purchase agreements (PPAs).

This Frappe application bridges SCADA electrolyzer telemetry directly into green compliance ledgers.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Electrolyzer SCADA Telemetry (Modbus / OPC-UA)"] -->|Hourly kWh & Flow Ingestion| B["Electrolyzer Telematics Gateway"]
    C["Solar & Wind PPA Metering (Wheeled Renewable Power)"] --> B
    B -->|Calculate Specific Energy Consumption (kWh/kg)| D["Efficiency & SEC Curve Engine"]
    B -->|Calculate Lifecycle Carbon Intensity| E{"Carbon Intensity <= 2.0 kg CO2e / kg H2?"}
    E -->|Yes (Compliant Green Hydrogen)| F["Issue Digital Guarantee of Origin (GO) Certificate"]
    E -->|No (Grid Excursion Detected)| G["Flag Non-Green Batch: Downgrade to Grey/Blue Hydrogen"]
    F --> H["PLI Subsidy Claim & Export Manifest Documentation"]
```

---

## 🚀 Key Engineering Capabilities

- **Hourly Stack Telemetry Ingestion:** Captures power consumption, hydrogen mass flow, cell voltage, and demineralized water flow.
- **Specific Energy Consumption (SEC) Benchmarking:** Tracks stack efficiency degradation over operational lifetime.
- **Guarantee of Origin (GO) Generator:** Issues verifiable batch certificates aligned with MNRE and CertifHy standards.
- **Renewable PPA Wheeling Reconciler:** Verifies 100% green power matching to prevent greenwashing claims.

---

## 📂 Frappe DocType Schema & Data Structure

```text
green_hydrogen_telematics/
├── green_hydrogen_telematics_core/
│   ├── doctype/
│   │   ├── electrolyzer_stack_log/
│   │   │   ├── electrolyzer_stack_log.json
│   │   │   ├── electrolyzer_stack_log.py
│   │   │   └── electrolyzer_stack_log.js
│   │   └── guarantee_of_origin_cert/
│   │       └── guarantee_of_origin_cert.json
│   └── workspace/
│       └── green_hydrogen_telematics_workspace/
│           └── green_hydrogen_telematics_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/green_hydrogen_telematics.api.record_production_telemetry`
- **Whitelisted Method:** `@frappe.whitelist() def issue_guarantee_of_origin(batch_lot_no, total_kg)`
- **Hooks Event:** `scheduler_events.hourly` audits hourly renewable power matching ratios.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/frappe-green-hydrogen-electrolyzer-telematics-cert
bench --site erp.yourdomain.com install-app green_hydrogen_telematics
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Green Ammonia Plants, Hydrogen Mobility Operators, and Clean Energy Developers.
