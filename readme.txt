# AI/ML-Based EV Motor Energy Efficiency & Predictive Health Monitoring System

## Overview

An intelligent BLDC motor monitoring system designed to analyse electrical energy consumption, monitor motor operating conditions, and explore AI/ML-driven predictive health monitoring for Electric Vehicle (EV) propulsion systems.

The project integrates embedded systems, real-time sensor data acquisition, Python-based visualization, and machine learning techniques to investigate abnormal motor behaviour, improve energy efficiency, and support preventive maintenance strategies aimed at extending motor service life.

## System Architecture

The system consists of:
- **ESP32 Development Board:** Central controller for motor monitoring and data acquisition.
- **BLDC Motor:** Brushless DC motor used for the motor monitoring setup.
- **FOC Mini BLDC Driver:** Controls BLDC motor operation.
- **24V Power Supply:** Main power source for the motor system.
- **DC-DC Buck Converter:** Steps down 24V to a regulated 5V supply.
- **Current Sensor:** Measures electrical current consumption.
- **Voltage Sensor:** Monitors supply voltage.
- **Python Monitoring Interface:** Receives and visualizes real-time motor telemetry.

## Software & Technologies

- Python
- ESP32 / Embedded Systems
- PySerial
- PyQtGraph
- NumPy
- Pandas
- Machine Learning

## Real-Time Data Monitoring

The Python monitoring application receives serial telemetry from the ESP32 and visualizes:

- Motor Speed (SPD)
- Q-axis Voltage (Vq)
- Q-axis Current (Iq)
- Motor Temperature

The visualization interface uses PyQtGraph for continuously updated motor parameter plots and PySerial for serial communication.

## AI/ML Integration

The planned machine learning component focuses on:

- Analysing motor electrical consumption patterns.
- Identifying abnormal operating conditions.
- Exploring anomaly detection techniques.
- Evaluating motor performance under different operating conditions.
- Supporting predictive maintenance and motor health assessment.

## Project Objectives

1. Monitor BLDC motor electrical parameters in real time.
2. Analyse power and energy consumption.
3. Identify abnormal operating patterns.
4. Explore predictive monitoring using AI/ML.
5. Support improved energy efficiency and extended EV motor service life.

## Project Status

**Under Development**

Embedded motor monitoring and Python-based real-time visualization are implemented. AI/ML integration and predictive analysis are ongoing development objectives.