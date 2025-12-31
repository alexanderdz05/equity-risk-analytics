# Equity Risk & Volatility Analytics

A Python-based financial analytics project that analyzes historical equity price data to measure risk using volatility, drawdowns, Value at Risk (VaR), and correlation. The project focuses on understanding market, sector, and single-stock risk through quantitative metrics and visualizations.

---

## Overview

This project uses historical market data for a small set of representative equities to evaluate and compare risk characteristics across assets. By transforming price data into daily returns, the analysis computes standard risk metrics commonly used in finance and risk management. Visualizations are used to communicate differences in volatility, downside risk, and diversification in an intuitive way.

The goal of the project is to demonstrate practical risk analytics skills rather than maximize asset coverage.

---

## Features

- Downloads and processes historical adjusted price data  
- Cleans and validates financial time-series data  
- Computes daily return series  
- Calculates key risk metrics:
  - Annualized volatility
  - Maximum drawdown
  - Best and worst daily returns
  - Historical Value at Risk (95%)
- Visualizes risk through:
  - Normalized price performance
  - Rolling volatility
  - Drawdown curves
  - Correlation heatmap
- Exports cleaned data, metrics, and charts for reproducibility  

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- yfinance  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## Data Source

Historical daily price data is retrieved from **Yahoo Finance** using the `yfinance` Python library. Adjusted closing prices are used to account for dividends and stock splits.

---

## Assets Analyzed

- **SPY** — Broad U.S. market benchmark (S&P 500 ETF)  
- **QQQ** — Technology-heavy index ETF (Nasdaq-100)  
- **AAPL** — Large-cap technology stock  
- **MSFT** — Large-cap technology stock  

This asset set enables comparison of:
- Market vs. sector risk  
- ETF vs. single-stock risk  
- Correlation and diversification effects  
