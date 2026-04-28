# 🏢 ERP System Analysis & Odoo 18 Custom Module

## 🎯 Project Overview
A comprehensive project featuring a deep-dive analysis of **Amazon's ERP business cycles** (P2P, O2C, Inventory) and a custom-built **Odoo 18 module** for Supplier Behavioral Drift Analysis.

## 👥 Team Members
- **Youssef Hamdy**
- **Youssef Ahmed**
- **Amr Farag Gamal**

## 📂 Quick Links to Assets
* **📄 Full Technical Report:** [Project ERP.pdf](./Project%20ERP.pdf)
* **💻 Implementation Presentation:** [Egypt Motors PDF](./WEBSITE%20EGYPT%20MOTORS.pdf)
* **⚙️ Odoo Custom Module Code:** [Explore Module](./custom_addons/supplier_drift_analyzer/)

## 📊 Business Process Models (Diagrams)
* [Context Diagram](./Context%20Diagram%20For%20Amazon.drawio)
* [DFD Level 0](./DFD%200%20FOR%20PROJECT%20ERB.drawio)
* [P2P Process BPMN](./P2P%20PROCESS%20BPMN.drawio)
* [O2C Process BPMN](./O2C%20PROCESS%20BPMN.drawio)

## 🛠️ Custom Module: Supplier Drift Analyzer
This module calculates risk based on price deviations in the last 5 Purchase Orders:
- ✅ **Stable:** Deviation < 100
- ⚠️ **Warning:** Deviation 100 - 300
- 🚨 **Risky:** Deviation > 300
