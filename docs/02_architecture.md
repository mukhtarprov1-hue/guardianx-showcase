# GuardianX - Architecture and Directory Structure

This document details the architectural patterns, directory structure, package layout, and data-flow model employed in **GuardianX**.

---

## 1. Architectural Pattern
GuardianX is built using a modified **Model-View-ViewModel (MVVM)** design pattern with a repository abstraction layer.

---

## 2. Directory Layout & Package Structure
The Android packages are organized by features and technical layers under the parent namespace `com.example.guardianx`:

```
com.example.guardianx/
│
├── App.java (Application initialization, Global Exception Crash Catcher)
│
├── activities/
│   ├── MainActivity.java (Main interface, navigation drawer)
│   └── IntentScannerActivity.java (Handles incoming scan requests)
│
├── scanner/ (Deep File Scanning)
│   ├── YaraNativeEngine.java (C++ YARA bridge)
│   ├── FileScanEngine.java (Orchestrator for file analysis)
│   ├── ScanResultBridge.java (Java-C++ communication)
│   ├── model/ (Scan indicators and results)
│   └── modules/ (Pdf, Office, Image specialized analyzers)
│
├── linksecurity/ (URL & Web Security)
│   ├── UrlScanner.java (7-Layer defense orchestrator)
│   ├── VirusTotalScanner.java (Cloud intelligence API)
│   ├── DomainAgeAnalyzer.java (WHOIS-like age analysis)
│   ├── HtmlAnalyzer.java (Static content analysis)
│   ├── RedirectChainAnalyzer.java (Redirect/Shortener tracking)
│   └── UrlFeatureExtractor.java (Feature engineering for AI)
│
├── engine/ (App & Permission Risk)
│   ├── RiskEngine.java (Final threat orchestrator)
│   ├── PermissionAnalyzer.java (Audit of requested API configurations)
│   ├── BehaviorAnalyzer.java (Evaluating VPN and battery exemptions)
│   └── ComponentAnalyzer.java (Manifest structure analysis)
│
├── fragments/
│   ├── home/ (Dashboard, security status)
│   ├── reports/ (Visual graphing views - Pie, Bar, Line)
│   ├── files/ (Manual and automatic file scanning UI)
│   └── apps/ (Application audit and list)
│
├── data/
│   ├── db/
│   │   ├── AppDatabase.java (Room database configuration)
│   │   ├── ScanRepository.java (Data access orchestrator)
│   │   └── entities/ (ScanRecord, EventRecord, ReportCache)
│   └── BlacklistDatabase.java (SQLite database for malicious URLs)
│
└── utils/
    ├── AppScanner.java (Standard app package scanning)
    └── filescanner/ (FileSystem monitoring and observers)
```

---

## 3. Core Technologies
- **Language**: Java (Android SDK) & C++ (Native Layer).
- **AI Engine**: **ONNX Runtime** for local URL classification.
- **File Engine**: **Native YARA** for byte-level pattern matching.
- **Database**: **Room (SQLite)** for structured data & **Custom SQLite** for URL blacklists.
- **Charts**: **MPAndroidChart** for data visualization.
