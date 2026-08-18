# GuardianX - Database Schema and Data Models

This document details the database layer and local file vault features implemented in **GuardianX**.

---

## 1. Database Configuration (`AppDatabase.java`)
GuardianX uses the **Google Room Persistence Library** (an abstraction layer over SQLite) to maintain secure logs, caching systems, and historical scan results.
- **Database Name**: `"guardianx_database"`
- **Schema Version**: `2`
- **Migration Strategy**: `fallbackToDestructiveMigration()` (for developmental builds).

---

## 2. Room Data Schema and Entities

### A. ScanRecord (`ScanRecord.java`)
Stores individual file, app, or link scan details.
- `id` (Long, Primary Key, Auto-Generated)
- `sessionId` (Long): References the parent scan block.
- `scanType` (String): `"APP"`, `"FILE"`, or `"URL"`.
- `targetId` (String): Package Name / File Path / Target Destination.
- `targetName` (String): Display name of the item.
- `result` (String): Verdict output (`"SAFE"`, `"SUSPICIOUS"`, or `"MALICIOUS"`).
- `riskScore` (Int): Computed score ($0$ to $100$).
- `fileSize` (Long) / `sha256` (String) / `mimeType` (String) / `extension` (String).
- `isRealtime` (Boolean): Identifies files caught by the Background Foreground Service.
- `details` (String): Raw JSON insights.

### B. EventRecord (`EventRecord.java`)
Maintains a diagnostic security audit trail of all operations.
- `id` (Long, Primary Key)
- `title` (String) / `description` (String)
- `category` (String): `"FILE"`, `"APP"`, `"NETWORK"`, `"SCAN"`, `"SYSTEM"`, or `"SECURITY"`.
  - Note: permission-related audit events are stored under the `SECURITY` category in the current codebase; there is no `PERMISSION` constant in `EventRecord`.
- `severity` (String): `"INFO"`, `"WARNING"`, `"HIGH"`, or `"CRITICAL"`.
- `timestamp` (Long): UNIX time of insertion.
- `operationId` (String): Custom UUID representing logical work groups.

### C. ThreatHistory (`ThreatHistory.java`)
Tracks confirmed system threats that require remediation.
- `id` (Long, Primary Key)
- `recordId` (Long): Foreign key link to corresponding `ScanRecord`.
- `threatName` (String): Identified signature family.
- `severity` (String): `"HIGH"`, `"MEDIUM"`, `"LOW"`.
- `status` (String): `"DETECTED"`, `"RESOLVED"`.

### D. DailyStatistics (`DailyStatistics.java`)
Maintains atomic aggregates for the past 30 days to build performance reports.
- `date` (String, Primary Key): Date key format `"yyyy-MM-dd"`.
- `filesScanned` / `appsScanned` / `urlsScanned` (Int)
- `safeCount` / `suspiciousCount` / `maliciousCount` (Int)
- `removedThreats` (Int): Tracks user-triggered uninstallations.
- `securityScore` (Int): Computed aggregate safety level.

### E. ReportCache (`ReportCache.java`)
Stores pre-processed JSON data representing chart configurations.
- `id` (Int, Primary Key = 1): Singleton pattern.
- `lastSecurityScore` (Int): Overall safety percentage.
- `lastSummary` (String): Compiled reports textual context.
- `lastPieChartData` (String): JSON payload representing raw result segments.
- `lastBarChartData` (String): JSON representation of hourly scans.
- `updatedAt` (Long)

---

## 3. High Performance Aggregations (`ScanDao.java` & `EventDao.java`)
To prevent heavy main-thread database querying, custom SQLite statements extract charts data directly:
- **Hourly scan chart aggregates (BarChart)**: 
  ```sql
  SELECT strftime('%H', datetime(scanDate/1000, 'unixepoch', 'localtime')) as hour, COUNT(*) as count 
  FROM scan_records 
  WHERE scanDate >= :startOfDay 
  GROUP BY hour
  ```
- **Weekly activity chart aggregates (LineChart)**:
  ```sql
  SELECT strftime('%Y-%m-%d', datetime(timestamp/1000, 'unixepoch', 'localtime')) as day, COUNT(*) as count 
  FROM event_records 
  WHERE timestamp >= :since 
  GROUP BY day 
  ORDER BY day ASC
  ```

---

## 4. Secure File Vault (الخزنة الرقمية)
GuardianX provides an encrypted, hidden local vault directory. 
- **Setup & Authentication**: Controls are managed via local fragments (`SetupPasswordFragment`, `UnlockVaultFragment`, `ResetPasswordFragment`). Files are locked inside an isolated system directory.
- **File System Hiding**: Unvaulted file attributes are hashed, modified, and relocated to obfuscated folder layers, preventing files from appearing in common gallery systems or standard explorers.
