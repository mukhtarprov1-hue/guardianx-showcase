# GuardianX - Core Security Engine and Threat Analysis

This document describes the inner workings of the GuardianX Security Scanning Engines, including Risk Assessment, URL Analysis, and File Forensics.

---

## 1. Orchestrated Risk Calculation (`RiskEngine.java`)
The `RiskEngine` compiles assessments from multiple subsystems into a final **Risk Score (0 to 100)** and maps it to a **Risk Level**:
- **آمن (Safe)**: Risk Score $< 15$. System apps default here with a hardcoded threat score of $5$.
- **مشبوه (Suspicious)**: Risk Score $\ge 15$ and $< 40$.
- **خطر (Dangerous)**: Risk Score $\ge 40$.

---

## 2. 7-Layer URL Security Engine (`UrlScanner.java`)
GuardianX implements a comprehensive 7-layer defense mechanism to analyze URLs for phishing, malware, and deceptive practices.

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Layer 0** | **Domain Age Analyzer** | Checks the registration age of the domain. New domains (< 30 days) are flagged as high risk. |
| **Layer 1** | **White List** | Checks against a local database of trusted domains (e.g., Google, Microsoft, Social Media) to avoid false positives. |
| **Layer 2** | **Black List** | Querying local SQLite database containing known malicious URLs (PhishTank/OpenPhish feeds). |
| **Layer 3** | **Redirect Chain Analyzer** | Follows URL shorteners and redirects to find the ultimate destination and assess the risk of the chain. |
| **Layer 4** | **Static HTML Analyzer** | Inspects the destination's HTML structure for phishing indicators (e.g., hidden forms, deceptive scripts). |
| **Layer 5** | **AI Model (ONNX Runtime)** | Uses a deep learning model to analyze 43 structural features of the URL (length, special chars, sensitive words). |
| **Layer 6** | **VirusTotal API** | A final cloud-based check against 90+ antivirus engines for global threat intelligence. |

> **Technical Note**: The AI model is executed locally using the **ONNX Runtime** for high performance and privacy, replacing traditional TensorFlow Lite implementations.

---

## 3. Native File Scanning Engine (`YaraNativeEngine.java`)
For deep file analysis, GuardianX integrates the industry-standard **YARA** engine.

### A. Native Integration (C++)
The core engine is written in **C++** and compiled into a native library (`yara_native.so`). This allows for:
- **High Performance**: Scanning large files without blocking the main Android thread.
- **Deep Inspection**: Byte-level pattern matching against sophisticated malware signatures.

### B. Specialized Forensic Modules
Beyond YARA, the engine uses specialized modules for specific file types:
- **OfficeScanModule**: Analyzes Excel, Word, and PowerPoint files for malicious macros.
- **PdfScanModule**: Detects embedded JavaScript and malicious URI actions in PDF documents.
- **ImageScanModule**: Checks for steganography or malicious payloads hidden in image metadata.

---

## 4. Heuristic Rules and Security Parameters

### A. Permission Auditor (`PermissionAnalyzer.java`)
This module evaluates requested Android permissions by applying custom risk weights:

| Permission | Technical Name | Assessment Weight | Rationale |
| :--- | :--- | :--- | :--- |
| **Device Admin** | `BIND_DEVICE_ADMIN` | **+30** | Prevents app uninstallation and enables remote controls. |
| **System Overlay** | `SYSTEM_ALERT_WINDOW` | **+15** | Can intercept clicks or display phishing layers. |
| **Accessibility Service** | `BIND_ACCESSIBILITY_SERVICE` | **+20** | Captures keystrokes and reads screen contents. |
| **App Installer** | `REQUEST_INSTALL_PACKAGES` | **+15** | Allows background execution of sub-installers. |
| **SMS Records** | `SMS` Related | **+15** | Can read sensitive OTP codes or send premium numbers. |

#### Synergy Penalty Rules
- **Full Spyware Profile**: `CAMERA` + `RECORD_AUDIO` + `LOCATION` + `SMS` + `CONTACTS` + `INTERNET` $\rightarrow$ **+30 Synergy Penalty**.

### B. Installer Verification Engine
- **Sideload Penalty**: Apps from outside Google Play receive a **+20 Risk Penalty**.
- **Enforcement Rule**: Sideloaded app + Dangerous Permission $\rightarrow$ **Forced Risk Score 40 (Dangerous)**.
