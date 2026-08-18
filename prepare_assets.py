import shutil
import os

src = r'F:\C\Users\mukhtar\guardianx2\ducomants\structured_report\Media_and_Diagrams'
dst_base = r'F:\C\Users\mukhtar\guardianx-public\assets'

mapping = {
    # UI
    'page_166_img_00.jpeg': 'ui/full_scan_view.jpg',
    'page_203_img_00.jpeg': 'ui/analytics_dashboard.jpg',
    'page_042_img_00.jpeg': 'ui/antivirus_status.jpg',
    'page_191_img_00.jpeg': 'ui/vault_storage.jpg',
    'page_210_img_00.jpeg': 'ui/app_details_risk.jpg',
    'page_215_img_00.jpeg': 'ui/realtime_alerts.jpg',

    # Diagrams
    'page_131_img_00.png': 'diagrams/risk_engine_logic.png',
    'page_134_img_00.png': 'diagrams/file_scan_flow.png',
    'page_036_img_00.png': 'diagrams/development_methodology.png',
    'page_139_img_00.png': 'diagrams/data_flow_context.png',

    # Marketing
    'page_001_img_00.jpeg': 'marketing/amran_university.jpg'
}

for s_name, d_path in mapping.items():
    s_full = os.path.join(src, s_name)
    d_full = os.path.join(dst_base, d_path)
    if os.path.exists(s_full):
        shutil.copy(s_full, d_full)
        print(f"Copied {s_name} to {d_path}")

# Logo copy
logo_src = r'F:\C\Users\mukhtar\guardianx2\app\src\main\res\drawable\app_logo.png'
if os.path.exists(logo_src):
    shutil.copy(logo_src, os.path.join(dst_base, 'marketing/logo_main.png'))
