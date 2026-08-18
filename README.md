<p align="center">
  <img src="assets/logo.png" width="120" alt="GuardianX Logo">
</p>

<h1 align="center">🛡️ GuardianX: The Sentinel of Android Security</h1>

<p align="center">
  <strong>An Intelligent, Multi-Layered Threat Intelligence & Forensic System for Modern Mobile Environments.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Release-v2.5.0-0078D4?style=for-the-badge&logo=github" alt="Release">
  <img src="https://img.shields.io/badge/Platform-Android_14+-3DDC84?style=for-the-badge&logo=android" alt="Platform">
  <img src="https://img.shields.io/badge/Security-YARA_Certified-red?style=for-the-badge&logo=shield" alt="Security">
  <img src="https://img.shields.io/badge/AI-ONNX_Runtime-5B2D90?style=for-the-badge&logo=ai" alt="AI">
</p>

---

## 📖 Overview
**GuardianX** is not just an application; it's a comprehensive security infrastructure designed to combat the evolving landscape of mobile threats. Developed as a high-end graduation project, it integrates **Native C++ Forensics**, **Heuristic Risk Engines**, and **Deep Learning** to provide a zero-compromise security experience.

> 🔒 **Security Notice**: This repository acts as a **Technical Showcase**. The proprietary source code is hosted in a private, encrypted environment to protect intellectual property.

---

## 📱 Visual Experience
<p align="center">
  <img src="assets/screenshots/scan_main.jpg" width="30%" alt="Main Scanner">
  <img src="assets/screenshots/reports.jpg" width="30%" alt="Analytics Dashboard">
</p>

---

## 🚀 Core Capabilities (The Pillars)

### 🧠 1. Heuristic Risk Assessment
Our custom **RiskEngine** performs multi-vector analysis on applications:
*   **Behavioral Auditing**: Detects dangerous permission combinations (e.g., Camera + SMS + Internet).
*   **Sideload Verification**: Identifies apps installed outside of official stores.
*   **Component Inspection**: Scans background services and receivers for hidden activities.

### 🌐 2. 7-Layer URL Intelligence
A military-grade scanning pipeline for links and phishing attempts:
1.  **Metadata Check**: Analyzing domain age and registration patterns.
2.  **AI Analysis**: Utilizing a local **ONNX model** to inspect 43 structural URL features.
3.  **Cloud Sync**: Live validation via **VirusTotal API** (leveraging 90+ global scanners).

### 🔍 3. Deep File Forensics (YARA Integration)
We've ported the world-renowned **YARA Engine** to Android using **C++20**:
*   **Static Pattern Matching**: Finding malware signatures at the byte level.
*   **Specialized Forensic Modules**: Deep inspection of Office, PDF, and Image files.

---

## 🛠️ System Architecture & Logic

### 🔄 Algorithm Workflows
<p align="center">
  <img src="assets/screenshots/risk_flow.png" width="45%" alt="Risk Logic">
  <img src="assets/screenshots/file_algo.png" width="45%" alt="File Algorithm">
</p>

<details>
<summary><b>📐 Technical Stack 2026</b></summary>

- **Language**: Java 21, C++20 (JNI)
- **AI Framework**: ONNX Runtime Mobile
- **Forensics**: LibYara Native
- **Storage**: SQLCipher / Room (Local Encryption)
- **Architecture**: Clean Architecture / MVVM
</details>

---

## 📂 Project Resources

| Category | Link | Description |
| :--- | :--- | :--- |
| **Documentation** | [📚 Technical Docs](docs/) | Architecture, ERD, and Security Engine logic. |
| **Reports** | [📄 Official Reports](reports/) | Comprehensive PDF & Word project reports. |
| **Assets** | [🖼️ Branding](assets/) | Brand identity and UI elements. |

---

## 👤 Development Team
**Lead Architect**: Mukhtar Alawady
**Focus**: Mobile Security, Malware Analysis, and AI Integration.

---

<p align="center">
  <b>GuardianX Pro</b> • Protecting your Digital Frontier in 2026 and Beyond.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-green.svg" alt="Maintained">
  <img src="https://img.shields.io/badge/Security%20Score-100%25-brightgreen.svg" alt="Security Score">
</p>
