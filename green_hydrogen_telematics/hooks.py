# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "green_hydrogen_telematics"
app_title = "Frappe Green Hydrogen Electrolyzer Telematics Cert"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Green Hydrogen Electrolyzer Telematics Cert - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/green_hydrogen_telematics/css/green_hydrogen_telematics.bundle.css"
app_include_js = "/assets/green_hydrogen_telematics/js/green_hydrogen_telematics.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Green Hydrogen Electrolyzer Telematics Cert Entry": {
        "validate": "green_hydrogen_telematics.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "green_hydrogen_telematics.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "green_hydrogen_telematics.tasks.hourly_sync"
    ],
    "daily": [
        "green_hydrogen_telematics.tasks.daily_reconciliation"
    ],
    "weekly": [
        "green_hydrogen_telematics.tasks.weekly_digest"
    ]
}
