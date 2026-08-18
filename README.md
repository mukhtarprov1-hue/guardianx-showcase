<p align="center">
  <img src="assets/branding/logo.png" width="180" alt="GuardianX Logo">
</p>

<h1 align="center">🛡️ GuardianX: Next-Generation Mobile Intelligence</h1>

<p align="center">
  <b>The Enterprise-Grade Android Security Framework for the 2026 Cyber Landscape.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Investor%20Ready-gold?style=for-the-badge" alt="Investor Ready">
  <img src="https://img.shields.io/badge/Security-YARA%20Inside-red?style=for-the-badge&logo=shield" alt="YARA">
  <img src="https://img.shields.io/badge/AI-Realtime%20ONNX-blue?style=for-the-badge&logo=ai" alt="AI">
  <img src="https://img.shields.io/badge/Portfolio-World_Class-blueviolet?style=for-the-badge" alt="Portfolio">
</p>

---

## 📽️ Hero Showcase & Vision
**GuardianX** is a breakthrough in mobile security architecture. Designed as a proactive defense ecosystem, it leverages **Heuristic Intelligence** and **Native Forensics** to protect high-value assets and sensitive user data from sophisticated threats like 0-day exploits, phishing, and surveillance malware.

<p align="center">
  <img src="assets/branding/university.jpg" width="600" alt="Banner">
</p>

---

## 📱 Interactive Interface Gallery (UI/UX Deep-Dive)

> **Instructions**: Explore the modules below. Each section represents a core system interface with a detailed technical breakdown of the underlying logic.

<table align="center">
  <tr>
    <td>
      <details>
        <summary><b>🔍 1. Real-Time Risk Dashboard</b></summary>
        <p align="center"><img src="assets/ui/page_042_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> تمثل هذه الواجهة "مركز القيادة". يتم هنا عرض <b>Security Score</b> اللحظي. يقوم المحرك بفحص 25 معلمة أمنية في الخلفية، مع تطبيق نظام تلوين ديناميكي يعتمد على درجة الخطورة (Safe=Green, Danger=Red). التصميم يعتمد على Material 3 مع تأثيرات الزجاج (Glassmorphism) لتقليل تشتت المستخدم.
      </details>
    </td>
    <td>
      <details>
        <summary><b>🛡️ 2. Comprehensive System Scanner</b></summary>
        <p align="center"><img src="assets/ui/page_166_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> شاشة الفحص الشامل التي تدمج بين <b>YARA Engine</b> وفحص الروابط. يمكن للمستخدم اختيار "الفحص العميق" الذي يحلل هيكل الملف (File Structure) وليس فقط الاسم أو الحجم. يتم استغلال طاقة المعالج بالكامل عبر مكتبات C++ Native لضمان سرعة الفحص دون التأثير على أداء الهاتف.
      </details>
    </td>
    <td>
      <details>
        <summary><b>📊 3. Intelligence Reports</b></summary>
        <p align="center"><img src="assets/ui/page_203_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> لوحة البيانات التحليلية. تستخدم مكتبات رسم بياني متطورة لعرض توزيع التهديدات (Malware, Phishing, Permissions). توفر تصفية زمنية (يومي/أسبوعي/شهري) لمراقبة تطور حالة الأمان، مما يساعد مدراء الأنظمة أو المستخدمين المحترفين على اتخاذ قرارات مبنية على البيانات.
      </details>
    </td>
  </tr>
  <tr>
    <td>
      <details>
        <summary><b>🔐 4. The Encrypted Vault</b></summary>
        <p align="center"><img src="assets/ui/page_191_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> نظام العزل الفيزيائي للملفات. أي ملف مشبوه يتم نقله إلى هذه الخزنة حيث يتم تشفيره فوراً باستخدام <b>AES-256</b>. يتم عزل الملف عن نظام الملفات العام للأندرويد، بحيث لا يمكن لأي تطبيق آخر الوصول إليه، ويتم التحكم في المفاتيح عبر كلمة مرور Master Key مؤمنة.
      </details>
    </td>
    <td>
      <details>
        <summary><b>🚫 5. Real-time Threat Monitor</b></summary>
        <p align="center"><img src="assets/ui/page_215_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> نظام التنبيهات العائم. يستخدم <b>Accessibility Service</b> لاعتراض الروابط والملفات بمجرد تحميلها. عند اكتشاف تهديد، تظهر هذه الواجهة التحذيرية التي توفر للمستخدم "قراراً لحظياً" (حذف/تجاهل/حجر)، مع شرح سبب التصنيف كخطر.
      </details>
    </td>
    <td>
      <details>
        <summary><b>🔎 6. Forensic Package Details</b></summary>
        <p align="center"><img src="assets/ui/page_210_img_00.jpeg" width="280"></p>
        <hr>
        <b>الوصف الفني:</b> تحليل تفصيلي لحزمة التطبيق (APK). تظهر هذه الشاشة "البصمة الرقمية" للتطبيق، وتشمل الصلاحيات المطلوبة، التوقيع الرقمي، ومسار التثبيت. يتم هنا كشف "التآزر المشبوه" (Synergy) بين الصلاحيات التي قد تشير إلى برمجيات تجسس.
      </details>
    </td>
  </tr>
</table>

---

## ⚙️ System Intelligence & Brain Structure (Flowcharts)

<p align="center">
  <b>The Architecture of GuardianX is built on logical rigor and high-performance algorithms.</b>
</p>

| Diagram | Technical Deep-Dive |
| :--- | :--- |
| <img src="assets/diagrams/page_131_img_00.png" width="300"> | **Risk Assessment Algorithm**: المخطط يوضح تسلسل اتخاذ القرار في محرك المخاطر. يبدأ باستلام بيانات الحزمة، ثم يمر عبر مرشحات (Filters) للأذونات الحساسة (Admin, Accessibility, Overlay). يتم جمع النقاط (Weights) لتحديد التصنيف النهائي (Safe/Warning/Danger). |
| <img src="assets/diagrams/page_134_img_00.png" width="300"> | **File Forensic Pipeline**: يوضح هذا المخطط مراحل فحص الملفات العميقة. يبدأ بحساب SHA-256، ثم تحليل الهيكل (Structure Analysis)، ثم فحص المحتوى عبر محرك YARA، وينتهي بحساب درجة الثقة (Confidence Level) قبل عرض النتيجة للمستخدم. |
| <img src="assets/diagrams/page_139_img_00.png" width="300"> | **Data Flow Diagram (Level 1)**: يوضح تدفق البيانات بين المستخدم، المحرك الأمني، وقواعد بيانات التهديدات (Threat DB). يظهر كيف يتم تخزين سجلات الفحص (Scan Logs) واسترجاع التقارير الإحصائية بشكل منظم. |
| <img src="assets/diagrams/page_036_img_00.png" width="300"> | **Agile Development Cycle**: يوضح المنهجية التي اتبعت في بناء المشروع، حيث تم تقسيم العمل إلى Sprint دورية تشمل التحليل، التصميم، البرمجة، والاختبار، مما يضمن مرونة النظام وقابليته للتحديث المستمر. |

---

## 📚 Literature Review & Comparative Research

لقد قمنا بإجراء دراسات مكثفة لمقارنة **GuardianX** مع العمالقة في مجال الأمن السيبراني لضمان التفوق التقني.

<p align="center">
  <img src="assets/studies/page_081_img_00.jpeg" width="600" alt="Comparison Table">
</p>

### 🔬 Summary of Scientific Findings:
*   **Superiority in Offline Detection**: بينما تعتمد معظم تطبيقات الـ Antivirus على Cloud Scanning، يتفوق GuardianX بقدرته على التحليل المحلي العميق عبر محرك YARA.
*   **Privacy-First AI**: استخدام نماذج ONNX محلياً يزيل خطر تسريب بيانات المستخدم إلى الخوادم الخارجية، وهو ما تفشل فيه الأنظمة التقليدية.
*   **Permission Heuristics**: الابتكار في اكتشاف "التآزر الجاسوسي" بين الصلاحيات يضع GuardianX في فئة الأنظمة الاستخباراتية (Intelligence) وليس مجرد ماسح فيروسات.

---

## 🛠️ Global Enterprise Tech Stack

| Component | Technology | Why? |
| :--- | :--- | :--- |
| **Core Logic** | Java 21 / Kotlin | Performance & Modern API support. |
| **Forensic Layer** | C++20 / JNI | Native speed for Byte-level scanning. |
| **Scanning Engine** | LibYara | Industry standard for malware patterns. |
| **AI Processing** | ONNX Runtime | High-speed, local model execution. |
| **Encryption** | AES-256 / SQLCipher | Military-grade data protection. |
| **Design** | Material 3 / Figma | User-centric, futuristic visual language. |

---

<div align="center">
  <img src="https://img.shields.io/badge/2026-Future_Ready-blue?style=for-the-badge" alt="Future Ready">
  <p><b>GuardianX Pro Project</b> - Defining the Standard of Mobile Security.</p>
  <p><i>Developed by: Mukhtar Alawady</i></p>
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-green.svg" alt="Maintained">
</div>
