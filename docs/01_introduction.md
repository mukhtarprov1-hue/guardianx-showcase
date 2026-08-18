# GuardianX - Introduction and Project Overview

Welcome to the official documentation folder for the **GuardianX** project. This document provides a high-level overview of the application, its objectives, target audience, and key capabilities.

---

## 1. Project Description
**GuardianX** is an advanced Android security utility and threat-intelligence application designed to protect mobile devices from malware, spyware, unauthorized permissions, and data leaks. By performing comprehensive static and behavior-based analysis on installed apps, local files, and external links, GuardianX helps users retain full control over their digital privacy and device security.

---

## 2. Core Objectives
- **Automated Threat Detection**: Real-time monitoring of file downloads and package installations.
- **Synergistic Permission Auditing**: Identifying apps that request dangerous combinations of permissions (e.g., Camera + Microphone + Internet + SMS) which could indicate espionage.
- **Isolated Vault Storage**: Providing users with a password-protected environment for securing sensitive local files.
- **Comprehensive Logging & Visual Reporting**: Recording all database security incidents and presenting summaries via interactive charts.
- **Device Policy Enforcement**: Utilizing Android's Device Administrator framework to strengthen physical security (e.g., locking the device, stopping uninstallation by rogue applications).

---

## 3. Key Feature Modules
1. **Security Dashboard (Home)**: High-level overview of device safety, containing the real-time Security Score (0-100%) and quick-action buttons.
2. **Application Scanner**: Scans installed applications and local `.apk` packages using custom analyzers.
3. **File System Scanner & Explorer**: A custom file browser that allows users to scan files and view cryptographic hashes (SHA-256).
4. **Link / URL Monitor**: Direct link tester to flag malicious or phishing URLs.
5. **Secure Vault (الحزنة الرقمية)**: A secure compartment with local encryption to lock confidential files.
6. **Detailed Reports**: Graphs and summaries representing scan history categorized by timeframes (Day, Week, Month).
7. **Real-time Protection Service**: A low-overhead Android Foreground Service that actively watches the system.

---

## 4. Target Audience
- **Standard Users**: Looking for a simple, visual, and zero-configuration app-analyzer.
- **Privacy-Conscious Individuals**: Seeking fine-tuned control over permission groups and active background processes.
- **Academic & Technical Evaluators**: Reviewing security models and mobile development workflows.
