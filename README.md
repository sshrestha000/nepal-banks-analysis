# nepal-banks-analysis
End-to-end analysis of Nepal's commercial banking sector: data cleaning, financial ratio analysis and visualization

# Nepal Commercial Banks — Sector Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Banks](https://img.shields.io/badge/banks-20%20Class%20A-red)

**Author:** Sushmita Shrestha  
**Tools:** Python · Pandas · Matplotlib  
**Data:** [Nepal Banks Web Scraper](https://github.com/sshrestha000/nepal-banks-scraper) — Class A Commercial Banks, Wikipedia  

---

## Overview

Exploratory analysis of Nepal's 20 Class A Commercial Banks using data collected by a companion web scraper. Covers asset concentration, branch networks, capital efficiency, leverage ratios, and geographic distribution.

This is the analysis layer of an end-to-end pipeline:

```
Scrape (BeautifulSoup) → Clean (Pandas) → Analyze (Pandas) → Visualize (Matplotlib)
```

---

## Sector Summary

| Metric | Value |
|--------|-------|
| Banks analyzed | 20 |
| Total branches | 5,229 |
| Total sector assets | रु 76.56 Arab NPR |
| Average branches per bank | 261 |
| Average assets per branch | रु 1.87 Billion |
| Average leverage ratio | 20.34x |

---

## Key Findings

### 1. Asset Concentration
The top 3 banks — Global IME, Nabil, and Nepal Investment Mega Bank — together hold a disproportionate share of total sector assets, while smaller banks like Kumari and Citizens cluster well below average.

| Bank | Total Assets | Branches |
|------|-------------|----------|
| Global IME Bank | रु 675B | 439 |
| Nabil Bank | रु 651B | 293 |
| Nepal Investment Mega Bank | रु 606B | 339 |
| Rastriya Banijya Bank | रु 553B | 382 |
| Laxmi Sunrise Bank | रु 428B | 300 |

### 2. Branch Network vs Assets — Not Correlated
A scatter plot of branches vs total assets shows **no strong linear relationship**. Global IME leads by assets (रु 675B) with 439 branches, but NIC Asia Bank maintains a wider network despite lower assets — a deliberate retail expansion strategy targeting mass-market customers.

### 3. Branch Efficiency — Standard Chartered is an Outlier
Standard Chartered generates **रु 8.7B per branch** — nearly 4x the sector average of रु 1.87B. With only 18 branches, it operates a premium corporate-focused model, the opposite of domestic banks that prioritize geographic reach.

| Bank | Assets per Branch |
|------|------------------|
| Standard Chartered Bank | रु 8.7B |
| Everest Bank | रु 2.3B |
| Nabil Bank | रु 2.2B |
| Himalayan Bank | रु 1.9B |
| Sanima Bank | रु 1.8B |

### 4. Leverage — Rastriya Banijya Bank Most Aggressive
Leverage ratios range from **13.44x (Kumari Bank)** to **35.34x (Rastriya Banijya Bank)**, with a sector average of 20.34x. Higher leverage means a bank is operating with significantly more assets relative to its capital base — amplifying both growth potential and risk exposure.

### 5. Geographic Concentration
The majority of banks are headquartered in Kathmandu, reflecting Nepal's centralized financial infrastructure. The City/District split reveals most are concentrated in a handful of Kathmandu localities (Kamaladi, Lazimpat, Durbar Marg).

---

## Visualizations

| Chart | Insight |
|-------|---------|
| Pie chart — Top 10 by assets | Market share concentration |
| Scatter — Branches vs Assets | No strong size-reach correlation |
| Bar — Assets per branch | Standard Chartered efficiency outlier |
| Histogram grid (4 panels) | Distribution of branches, assets, efficiency, leverage |

---

## Project Structure

```
nepal-banks-analysis/
│
├── README.md
├── nepal_banks_analysis.py     ← full analysis script
└── data/
    └── ClassA_Commercial_Banks.csv    ← input from scraper
```

---

## How to Run

```bash
git clone https://github.com/sshrestha000/nepal-banks-analysis
cd nepal-banks-analysis
pip install pandas matplotlib
python nepal_banks_analysis.py
```

Charts open interactively and summary statistics print to terminal.

---

## Engineering Notes

- Currency strings (`रु 674.84 Arab`) converted to float by stripping symbols and multiplying by 1,000,000,000 — preserves precision for ratio calculations
- `Headquarters` column split into `City` and `District` for geographic analysis
- Duplicates removed with `drop_duplicates()` before metric calculation
- Derived metrics (`assets_per_branch`, `leverage_ratio`) calculated after cleaning to avoid propagating dirty values

---

## Related Project

This analysis uses data collected by the companion scraper:  
→ [Nepal Banks Web Scraper](https://github.com/sshrestha000/nepal-banks-scraper)

---

**Sushmita Shrestha** · [GitHub](https://github.com/sshrestha000) · [LinkedIn](https://www.linkedin.com/in/sushmita-shrestha-7a3288215/)
