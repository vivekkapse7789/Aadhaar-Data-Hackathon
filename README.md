
# 🏛️ Aadhaar Demographic Update Analytics

### UDAI Data Hackathon | Open Government Data (OGD)

## 📌 Project Summary

This repository contains a **data analytics and visualization project** developed for the **UDAI Data Hackathon**, using **UIDAI Aadhaar demographic update datasets** published on the **Open Government Data (data.gov.in) platform**.

The project analyzes **age-wise, state-wise, and district-wise Aadhaar demographic update trends** to uncover patterns relevant to **governance, service delivery, and public awareness planning**.

---

## 🎯 Purpose of the Study

The primary goals of this project are to:

* Process and standardize large-scale Aadhaar demographic datasets
* Analyze **temporal, regional, and demographic patterns**
* Generate **policy-relevant insights** rather than raw statistics
* Present findings through **Power BI dashboards** and a **government-grade LaTeX report**
* Ensure **reproducibility and clarity**, aligned with NIC / UIDAI evaluation standards

---

## 📂 Repository Structure

```
Aadhaar-Data-Hackathon/
│
├── All CSV files ( After Cleaning up)/
│   └── Final, analysis-ready datasets
│
├── Data Cleanup/
│   ├── National level Data Cleanup/
│   │   └── Python scripts for preprocessing & standardization
│   └── State level Cleanup/
│       └── District/state aggregation logic
│
├── Data Visualization Using Power Bi/
│   └── Interactive Power BI dashboard (.pbix)
│
├── Required Datasets Provided By Platform/
│   └── Raw UIDAI datasets as provided by the hackathon
│
├── ScreenShots of Dashboard/
│   └── Key visual outputs for quick review
│
├── .gitattributes
└── README.md
```

---

## 📊 Datasets Used

The analysis is based on **aggregated, anonymized Aadhaar datasets**, including:

* Aadhaar Enrolment Data
* Aadhaar Demographic Update Data

**Granularity covered:**

* National level
* State level
* District level (with focus on Maharashtra and Pune district)

**Key attributes used:**

* State / District
* Time period
* Age group
* Update counts

> ⚠️ No personally identifiable information (PII) is used.
> All datasets comply with UIDAI open data and privacy guidelines.

---

## 🧹 Data Cleaning & Processing

Raw datasets required extensive preprocessing due to size and structural inconsistencies.

Processing steps include:

* Removal of incomplete and inconsistent records
* Standardization of state and district naming
* Age-group normalization
* Aggregation from district → state → national level
* Generation of derived metrics (ratios, trends)

All preprocessing was performed using **Python (pandas)**.

---

## 📈 Analysis & Visualisation

Analysis focuses on:

* Age-wise dominance of demographic updates
* State and district-level variation in update intensity
* Temporal trends linked to migration, education, and awareness cycles

Visualization is done using **Power BI**, emphasizing:

* Interpretability over decoration
* Comparative insights
* Trend-based storytelling

Dashboard screenshots are included for quick evaluation.

---

## 📄 LaTeX Report (Government-Grade)

A **professional PDF report** is generated separately using **LaTeX**, following a structure optimized for:

* Government hackathon evaluation
* Judge scanning efficiency
* Policy relevance
* Reusability for future OGD challenges

The report follows a strict flow:

```
Dataset → Preprocessing → Analysis → Visual Evidence → Policy Insights
```

---

## 🛠️ Tools & Technologies

* **Python** (pandas, NumPy)
* **Power BI**
* **Git & GitHub**
* **Git LFS** (large CSV handling)
* **LaTeX (Overleaf-compatible)**

---

## 👥 Team

* **Shivshankar Dhareppa Mali**
  *Data Processing, Analysis, Repository Management*
  GitHub: [https://github.com/shiv123-coder](https://github.com/shiv123-coder)

* **Vivek Kapse**
  *Data Analysis & Visualization*

---

## 🏆 Hackathon Context

This project was developed specifically for the **UDAI Data Hackathon**, demonstrating:

* Real-world government data handling
* Analytical reasoning over descriptive statistics
* Visualization-led insight communication
* Reproducible, policy-focused documentation

---

## 📄 Usage & Disclaimer

This repository is intended for:

* Hackathon evaluation
* Educational and analytical purposes
* Demonstration of open government data analytics

Not intended for production or operational UIDAI use.

---
