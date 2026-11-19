# MediBridge Realistic Demonstration Seed Data Generator
import sqlite3
import json
import base64
from datetime import datetime, timedelta
from database import get_db, init_db, seed_emergency_facilities, hash_password

def generate_sample_prescription_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="600" height="800">
  <defs>
    <filter id="paper-texture" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="4" result="noise"/>
      <feDiffuseLighting in="noise" lighting-color="#fffdf7" surfaceScale="1.5" result="light">
        <feDistantLight azimuth="45" elevation="60" />
      </feDiffuseLighting>
      <feBlend mode="multiply" in="SourceGraphic" in2="light" />
    </filter>
  </defs>
  <rect width="600" height="800" fill="#fcfbf7"/>
  <!-- Clinic Header -->
  <rect x="25" y="25" width="550" height="105" fill="#f0f7ff" stroke="#0284c7" stroke-width="2" rx="6"/>
  <text x="50" y="58" font-family="'Segoe UI', Arial, sans-serif" font-weight="bold" font-size="20" fill="#0369a1">DR. RAJESH SHARMA, M.B.B.S., M.D.</text>
  <text x="50" y="78" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Consultant Physician &amp; Rural Health Specialist | Reg. No: MCI-2014-48291</text>
  <text x="50" y="96" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Community Health Centre, Sonpur Block | Tel: 06224-274112</text>
  <line x1="25" y1="135" x2="575" y2="135" stroke="#cbd5e1" stroke-width="1.5"/>

  <!-- Patient Details -->
  <text x="40" y="160" font-family="Arial" font-size="13" font-weight="bold" fill="#1e293b">Patient: Ramu Patil</text>
  <text x="280" y="160" font-family="Arial" font-size="13" fill="#334155">Age/Sex: 48 / Male</text>
  <text x="440" y="160" font-family="Arial" font-size="13" fill="#334155">Date: 04-Nov-2026</text>
  <text x="40" y="182" font-family="Arial" font-size="12" fill="#64748b">Village: Sonpur, Ward 3 | BP: 130/84 mmHg | Temp: 101.4°F</text>
  <line x1="25" y1="195" x2="575" y2="195" stroke="#94a3b8" stroke-dasharray="4,4"/>

  <!-- Rx symbol -->
  <text x="45" y="245" font-family="Georgia, serif" font-weight="bold" font-size="38" fill="#0284c7">℞</text>

  <!-- Handwritten-style prescription medicines -->
  <!-- 1. Paracetamol -->
  <text x="90" y="260" font-family="'Brush Script MT', 'Segoe Script', cursive, Arial" font-size="22" fill="#1e293b">1. Tab. Dolo / Paracetamol 650 mg</text>
  <text x="115" y="285" font-family="Arial" font-size="13" fill="#475569">   1 Tab TDS (Thrice Daily) x 3 days - After food</text>

  <!-- 2. Cetirizine -->
  <text x="90" y="325" font-family="'Brush Script MT', 'Segoe Script', cursive, Arial" font-size="22" fill="#1e293b">2. Tab. Cetirizine 10 mg</text>
  <text x="115" y="350" font-family="Arial" font-size="13" fill="#475569">   1 Tab HS (At bedtime) x 5 days</text>

  <!-- 3. Pantoprazole -->
  <text x="90" y="390" font-family="'Brush Script MT', 'Segoe Script', cursive, Arial" font-size="22" fill="#1e293b">3. Cap. Pantoprazole 40 mg (Pan-40)</text>
  <text x="115" y="415" font-family="Arial" font-size="13" fill="#475569">   1 Cap OD before breakfast (Empty stomach) x 5 days</text>

  <!-- 4. Unclear handwritten cursive smudge (Testing OCR verification flag) -->
  <g transform="rotate(-1 90 455)">
    <text x="90" y="455" font-family="'Brush Script MT', 'Segoe Script', cursive" font-size="20" fill="#334155" opacity="0.85">4. Syp. C-tr... / Amox.. 10ml (?) bd</text>
  </g>
  <rect x="85" y="468" width="360" height="20" fill="#fef08a" opacity="0.5" rx="3"/>
  <text x="90" y="482" font-family="Arial" font-size="11" fill="#854d0e" font-weight="bold">[OCR Flag: Cursive script ambiguous - Doctor confirmation required]</text>

  <!-- Doctor Instructions -->
  <text x="50" y="540" font-family="Arial" font-size="14" font-weight="bold" fill="#1e293b">Advice &amp; Instructions:</text>
  <text x="60" y="565" font-family="Arial" font-size="12" fill="#334155">• Increase warm oral fluids and hydration. Avoid cold exposure.</text>
  <text x="60" y="585" font-family="Arial" font-size="12" fill="#334155">• Steam inhalation twice daily for nasal congestion.</text>
  <text x="60" y="605" font-family="Arial" font-size="12" fill="#334155">• If fever persists &gt; 101°F after 48 hrs, repeat CBC and consult immediately.</text>

  <!-- Stamp and Signature -->
  <g transform="translate(380, 640)">
    <circle cx="90" cy="50" r="42" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2" opacity="0.75"/>
    <text x="50" y="45" font-family="Arial" font-size="9" fill="#2563eb" font-weight="bold">GOVT. OF BIHAR</text>
    <text x="52" y="60" font-family="Arial" font-size="8" fill="#2563eb">CHC SONPUR</text>
    <!-- Signature squiggle -->
    <path d="M 40 70 Q 70 30, 95 65 T 140 45 T 160 60" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
    <text x="45" y="95" font-family="Arial" font-size="11" font-weight="bold" fill="#1e293b">Dr. Rajesh Sharma</text>
    <text x="45" y="108" font-family="Arial" font-size="10" fill="#64748b">Reg: MCI-2014-48291</text>
  </g>
</svg>'''
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode('utf-8')).decode('utf-8')

def generate_sample_lab_report_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="600" height="800">
  <rect width="600" height="800" fill="#ffffff"/>
  <!-- Lab Header -->
  <rect x="20" y="20" width="560" height="95" fill="#ecfdf5" stroke="#059669" stroke-width="2" rx="4"/>
  <text x="40" y="52" font-family="Arial, sans-serif" font-weight="bold" font-size="20" fill="#065f46">JAN SEVA CLINICAL DIAGNOSTICS &amp; PATHOLOGY</text>
  <text x="40" y="72" font-family="Arial, sans-serif" font-size="12" fill="#047857">NABL Accredited Rural Collection Center | Lic: BR-LAB-9921</text>
  <text x="40" y="90" font-family="Arial, sans-serif" font-size="11" fill="#475569">Main Market Road, Rampur | Ph: +91 94318 88990</text>

  <!-- Patient & Sample info -->
  <rect x="20" y="125" width="560" height="70" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="35" y="148" font-family="Arial" font-size="12" font-weight="bold" fill="#1e293b">Patient Name: Sunita Devi</text>
  <text x="250" y="148" font-family="Arial" font-size="12" fill="#334155">Age/Gender: 54 Yrs / Female</text>
  <text x="430" y="148" font-family="Arial" font-size="12" fill="#334155">Ref: Self / Dr. Ananya</text>
  <text x="35" y="175" font-family="Arial" font-size="11" fill="#64748b">Sample Collected: 03-Nov-2026 08:30 AM | Sample: Fluoride Plasma &amp; Whole Blood (EDTA)</text>

  <!-- Table Header -->
  <rect x="20" y="210" width="560" height="32" fill="#0f766e"/>
  <text x="35" y="231" font-family="Arial" font-size="12" font-weight="bold" fill="#ffffff">INVESTIGATION (TEST NAME)</text>
  <text x="260" y="231" font-family="Arial" font-size="12" font-weight="bold" fill="#ffffff">RESULT</text>
  <text x="360" y="231" font-family="Arial" font-size="12" font-weight="bold" fill="#ffffff">REFERENCE RANGE</text>
  <text x="500" y="231" font-family="Arial" font-size="12" font-weight="bold" fill="#ffffff">UNIT</text>

  <!-- Row 1: Fasting Blood Sugar (High) -->
  <rect x="20" y="244" width="560" height="38" fill="#fef2f2"/>
  <text x="35" y="268" font-family="Arial" font-size="12" font-weight="bold" fill="#1e293b">Fasting Blood Sugar (FBS)</text>
  <text x="260" y="268" font-family="Arial" font-size="13" font-weight="bold" fill="#b91c1c">184.0 ▲ HIGH</text>
  <text x="360" y="268" font-family="Arial" font-size="12" fill="#475569">70.0 - 100.0</text>
  <text x="500" y="268" font-family="Arial" font-size="12" fill="#475569">mg/dL</text>
  <line x1="20" y1="282" x2="580" y2="282" stroke="#e2e8f0"/>

  <!-- Row 2: HbA1c (Critical High) -->
  <rect x="20" y="283" width="560" height="38" fill="#fee2e2"/>
  <text x="35" y="307" font-family="Arial" font-size="12" font-weight="bold" fill="#1e293b">HbA1c (Glycated Hemoglobin)</text>
  <text x="260" y="307" font-family="Arial" font-size="13" font-weight="bold" fill="#991b1b">8.6 ▲ CRITICAL</text>
  <text x="360" y="307" font-family="Arial" font-size="12" fill="#475569">4.0 - 5.6 (Normal)</text>
  <text x="500" y="307" font-family="Arial" font-size="12" fill="#475569">%</text>
  <line x1="20" y1="321" x2="580" y2="321" stroke="#e2e8f0"/>

  <!-- Row 3: Hemoglobin (Low) -->
  <rect x="20" y="322" width="560" height="38" fill="#fffbeb"/>
  <text x="35" y="346" font-family="Arial" font-size="12" font-weight="bold" fill="#1e293b">Hemoglobin (Hb)</text>
  <text x="260" y="346" font-family="Arial" font-size="13" font-weight="bold" fill="#b45309">10.2 ▼ LOW</text>
  <text x="360" y="346" font-family="Arial" font-size="12" fill="#475569">12.0 - 15.5</text>
  <text x="500" y="346" font-family="Arial" font-size="12" fill="#475569">g/dL</text>
  <line x1="20" y1="360" x2="580" y2="360" stroke="#e2e8f0"/>

  <!-- Row 4: Serum Creatinine (Normal) -->
  <rect x="20" y="361" width="560" height="38" fill="#f8fafc"/>
  <text x="35" y="385" font-family="Arial" font-size="12" fill="#1e293b">Serum Creatinine</text>
  <text x="260" y="385" font-family="Arial" font-size="12" font-weight="bold" fill="#15803d">0.90 Normal</text>
  <text x="360" y="385" font-family="Arial" font-size="12" fill="#475569">0.60 - 1.20</text>
  <text x="500" y="385" font-family="Arial" font-size="12" fill="#475569">mg/dL</text>
  <line x1="20" y1="399" x2="580" y2="399" stroke="#e2e8f0"/>

  <!-- Row 5: Platelet Count (Normal) -->
  <rect x="20" y="400" width="560" height="38" fill="#ffffff"/>
  <text x="35" y="424" font-family="Arial" font-size="12" fill="#1e293b">Platelet Count</text>
  <text x="260" y="424" font-family="Arial" font-size="12" font-weight="bold" fill="#15803d">2.40 Normal</text>
  <text x="360" y="424" font-family="Arial" font-size="12" fill="#475569">1.50 - 4.50</text>
  <text x="500" y="424" font-family="Arial" font-size="12" fill="#475569">lakhs/cumm</text>
  <line x1="20" y1="438" x2="580" y2="438" stroke="#cbd5e1"/>

  <!-- Pathology Interpretation Note -->
  <rect x="20" y="460" width="560" height="95" fill="#f1f5f9" rx="4"/>
  <text x="35" y="485" font-family="Arial" font-size="12" font-weight="bold" fill="#334155">Pathologist's Clinical Impression:</text>
  <text x="35" y="505" font-family="Arial" font-size="11" fill="#475569">• Elevated fasting glucose &amp; HbA1c &gt; 8% indicate uncontrolled glycemic status (Diabetes Mellitus).</text>
  <text x="35" y="522" font-family="Arial" font-size="11" fill="#475569">• Mild microcytic/normocytic anemia noted. Serum Creatinine normal; renal function stable.</text>
  <text x="35" y="539" font-family="Arial" font-size="11" fill="#475569">• Please correlate clinically with treating physician for oral hypoglycemic management.</text>

  <!-- Signatures -->
  <text x="40" y="680" font-family="Arial" font-size="11" fill="#64748b">Verified by: Lab Tech (DMLT)</text>
  <g transform="translate(380, 640)">
    <path d="M 10 30 Q 30 10, 50 35 T 90 20 T 110 35" fill="none" stroke="#047857" stroke-width="2"/>
    <text x="10" y="55" font-family="Arial" font-size="11" font-weight="bold" fill="#065f46">Dr. K. S. Verma, MD</text>
    <text x="10" y="68" font-family="Arial" font-size="10" fill="#475569">Consultant Pathologist</text>
  </g>
</svg>'''
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode('utf-8')).decode('utf-8')

def seed_all():
    init_db()
    seed_emergency_facilities()
    conn = get_db()
    cursor = conn.cursor()

    # Clear existing demo entries if needed
    cursor.execute("DELETE FROM doctor_responses")
    cursor.execute("DELETE FROM ocr_extractions")
    cursor.execute("DELETE FROM consultations")
    cursor.execute("DELETE FROM users")

    now = datetime.now()
    t_minus_2h = (now - timedelta(hours=2)).isoformat()
    t_minus_5h = (now - timedelta(hours=5)).isoformat()
    t_minus_1d = (now - timedelta(days=1)).isoformat()

    # Seed Doctors
    doctors = [
        (
            "doc_1", "doctor", "Dr. Rajesh Sharma, MD", "9876543210", hash_password("doctor123"),
            45, "Male", "Hindi", "Sonpur Block", "MCI-2014-48291",
            "General Physician & Rural Health Specialist", "District Civil Hospital & Telemedicine Center",
            t_minus_1d
        ),
        (
            "doc_2", "doctor", "Dr. Ananya Iyer, MBBS, DNB", "9876543211", hash_password("doctor123"),
            38, "Female", "English", "Vaishali District", "KMC-56782",
            "Family Medicine & Diabetology", "Rural Community Health Centre (CHC)",
            t_minus_1d
        )
    ]
    cursor.executemany('''
    INSERT INTO users (id, role, full_name, phone_number, password_hash, age, gender, preferred_language, village_location, doctor_reg_no, doctor_specialty, doctor_hospital, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', doctors)

    # Seed Patients
    patients = [
        (
            "pat_1", "patient", "Ramu Patil", "9123456780", hash_password("patient123"),
            48, "Male", "Hindi", "Sonpur, Ward 3", None, None, None, t_minus_1d
        ),
        (
            "pat_2", "patient", "Sunita Devi", "9123456781", hash_password("patient123"),
            54, "Female", "Hindi", "Rampur, Sector 2", None, None, None, t_minus_1d
        ),
        (
            "pat_3", "patient", "Balwant Singh", "9123456782", hash_password("patient123"),
            62, "Male", "English", "Kheri Village", None, None, None, t_minus_1d
        )
    ]
    cursor.executemany('''
    INSERT INTO users (id, role, full_name, phone_number, password_hash, age, gender, preferred_language, village_location, doctor_reg_no, doctor_specialty, doctor_hospital, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', patients)

    rx_svg = generate_sample_prescription_svg()
    lab_svg = generate_sample_lab_report_svg()

    # Consultation 1: Ramu Patil - Prescription (PENDING_REVIEW)
    c1_id = "cons_101"
    cursor.execute('''
    INSERT INTO consultations (
        id, patient_id, patient_name, patient_phone, patient_age, patient_gender, patient_language,
        village_location, file_type, original_filename, image_data,
        original_size_kb, compressed_size_kb, compression_ratio,
        symptoms, existing_conditions, allergies,
        has_voice_note, voice_note_duration, voice_note_transcript,
        status, emergency_warning, is_synced, offline_queued_at, synced_at, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        c1_id, "pat_1", "Ramu Patil", "9123456780", 48, "Male", "Hindi",
        "Sonpur, Ward 3", "prescription", "ramu_prescription_scan.jpg", rx_svg,
        3420.5, 118.4, 96.5,
        json.dumps(["High Fever (101°F)", "Dry Cough", "Severe Body Ache", "Headache"]),
        "Mild Hypertension (managed on lifestyle)", "No known drug allergies",
        1, 24, "Namaste Doctor babu, I have severe body ache and fever for 3 days. Medicine shop gave these tablets but cough is disturbing sleep at night.",
        "PENDING_REVIEW", 0, 1, None, t_minus_2h, t_minus_2h
    ))

    # OCR Extraction for Consultation 1
    medicines_1 = [
        {
            "name": "Paracetamol",
            "category": "Antipyretic / Analgesic",
            "dosage": "650 mg",
            "frequency": "Thrice daily (TDS)",
            "instructions": "After meals",
            "duration": "3 days",
            "confidence_score": 0.96,
            "is_uncertain": False,
            "raw_line": "1. Tab. Dolo / Paracetamol 650 mg TDS x 3d pc"
        },
        {
            "name": "Cetirizine",
            "category": "Antihistamine / Allergy",
            "dosage": "10 mg",
            "frequency": "Once daily at night (HS)",
            "instructions": "After dinner",
            "duration": "5 days",
            "confidence_score": 0.92,
            "is_uncertain": False,
            "raw_line": "2. Tab. Cetirizine 10 mg HS x 5d"
        },
        {
            "name": "Pantoprazole",
            "category": "Antacid / Proton Pump Inhibitor",
            "dosage": "40 mg",
            "frequency": "Once daily morning (OD)",
            "instructions": "Before breakfast (Empty stomach)",
            "duration": "5 days",
            "confidence_score": 0.89,
            "is_uncertain": False,
            "raw_line": "3. Cap. Pantoprazole 40 mg (Pan-40) OD ac x 5d"
        }
    ]
    uncertain_items_1 = [
        {
            "text": "4. Syp. C-tr... / Amox.. 10ml (?) bd",
            "reason": "Cursive ligature illegible - suspected Cough Syrup (Ascoril) or Ciprofloxacin suspension",
            "requires_doctor_verification": True,
            "suggested_action": "Doctor must manually inspect line 4 of prescription photograph"
        }
    ]
    cursor.execute('''
    INSERT INTO ocr_extractions (
        id, consultation_id, raw_text, medicines_json, lab_tests_json, doctor_notes, uncertain_items_json, ai_summary, missing_info_json, processed_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        "ocr_101", c1_id,
        "DR. RAJESH SHARMA, M.B.B.S., M.D. Reg: MCI-2014-48291\nPatient: Ramu Patil Age: 48\n1. Tab. Dolo / Paracetamol 650 mg TDS\n2. Tab. Cetirizine 10 mg HS\n3. Cap. Pantoprazole 40 mg OD before breakfast\n4. Syp. C-tr... / Amox.. 10ml (?) bd\nAdvice: Warm fluids, avoid cold exposure.",
        json.dumps(medicines_1), json.dumps([]),
        "Increase warm oral fluids and hydration. Avoid cold exposure. Steam inhalation twice daily.",
        json.dumps(uncertain_items_1),
        "Prescription outlines 3 identified pharmacological agents (Analgesic, Antihistamine, PPI) for symptomatic acute viral fever and upper respiratory congestion. 1 cursive entry on line 4 is ambiguous and marked for physician verification.",
        json.dumps(["Body temperature record past 12 hrs", "Sputum coloration check", "History of asthma"]),
        t_minus_2h
    ))

    # Consultation 2: Sunita Devi - Lab Report (PENDING_REVIEW)
    c2_id = "cons_102"
    cursor.execute('''
    INSERT INTO consultations (
        id, patient_id, patient_name, patient_phone, patient_age, patient_gender, patient_language,
        village_location, file_type, original_filename, image_data,
        original_size_kb, compressed_size_kb, compression_ratio,
        symptoms, existing_conditions, allergies,
        has_voice_note, voice_note_duration, voice_note_transcript,
        status, emergency_warning, is_synced, offline_queued_at, synced_at, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        c2_id, "pat_2", "Sunita Devi", "9123456781", 54, "Female", "Hindi",
        "Rampur, Sector 2", "report", "sunita_blood_test.jpg", lab_svg,
        2890.0, 94.2, 96.7,
        json.dumps(["Frequent Urination at night", "Excessive Thirst", "Weakness / Fatigue", "Mild burning in feet"]),
        "Type 2 Diabetes Mellitus (Uncontrolled), Anemia", "None",
        1, 18, "Doctor saheb, I got my blood test done in Rampur market. Test boy said sugar is very high. Please tell me which medicine to take.",
        "PENDING_REVIEW", 0, 1, None, t_minus_5h, t_minus_5h
    ))

    # OCR Extraction for Consultation 2
    lab_tests_2 = [
        {
            "test_name": "Fasting Blood Sugar (FBS)",
            "recorded_value": 184.0,
            "unit": "mg/dL",
            "reference_range": "70 - 100 mg/dL",
            "status": "HIGH",
            "is_abnormal": True,
            "severity": "WARNING",
            "confidence_score": 0.98
        },
        {
            "test_name": "HbA1c (Glycated Hemoglobin)",
            "recorded_value": 8.6,
            "unit": "%",
            "reference_range": "4.0 - 5.6 %",
            "status": "HIGH",
            "is_abnormal": True,
            "severity": "CRITICAL",
            "confidence_score": 0.99
        },
        {
            "test_name": "Hemoglobin (Hb)",
            "recorded_value": 10.2,
            "unit": "g/dL",
            "reference_range": "12.0 - 15.5 g/dL",
            "status": "LOW",
            "is_abnormal": True,
            "severity": "WARNING",
            "confidence_score": 0.96
        },
        {
            "test_name": "Serum Creatinine",
            "recorded_value": 0.9,
            "unit": "mg/dL",
            "reference_range": "0.60 - 1.20 mg/dL",
            "status": "NORMAL",
            "is_abnormal": False,
            "severity": "NORMAL",
            "confidence_score": 0.95
        },
        {
            "test_name": "Platelet Count",
            "recorded_value": 2.4,
            "unit": "lakhs/cumm",
            "reference_range": "1.50 - 4.50 lakhs/cumm",
            "status": "NORMAL",
            "is_abnormal": False,
            "severity": "NORMAL",
            "confidence_score": 0.94
        }
    ]
    cursor.execute('''
    INSERT INTO ocr_extractions (
        id, consultation_id, raw_text, medicines_json, lab_tests_json, doctor_notes, uncertain_items_json, ai_summary, missing_info_json, processed_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        "ocr_102", c2_id,
        "JAN SEVA CLINICAL DIAGNOSTICS. Patient: Sunita Devi, 54/F.\nFasting Blood Sugar: 184.0 mg/dL (High)\nHbA1c: 8.6% (Critical)\nHemoglobin: 10.2 g/dL (Low)\nCreatinine: 0.9 mg/dL\nPlatelets: 2.40 lakhs/cumm",
        json.dumps([]), json.dumps(lab_tests_2),
        "Elevated fasting glucose & HbA1c > 8% indicate uncontrolled glycemic status. Mild anemia noted.",
        json.dumps([]),
        "Blood report shows markedly elevated Fasting Glucose (184 mg/dL) and HbA1c (8.6%), confirming poorly controlled Diabetes Mellitus. Patient also exhibits mild anemia (Hb 10.2 g/dL). Renal filtration (Creatinine 0.9) is currently preserved.",
        json.dumps(["Current dosage of Metformin or other oral antidiabetics", "Blood pressure log", "Urine microalbumin test"]),
        t_minus_5h
    ))

    # Consultation 3: Balwant Singh - COMPLETED with Doctor's response
    c3_id = "cons_103"
    cursor.execute('''
    INSERT INTO consultations (
        id, patient_id, patient_name, patient_phone, patient_age, patient_gender, patient_language,
        village_location, file_type, original_filename, image_data,
        original_size_kb, compressed_size_kb, compression_ratio,
        symptoms, existing_conditions, allergies,
        has_voice_note, voice_note_duration, voice_note_transcript,
        status, emergency_warning, is_synced, offline_queued_at, synced_at, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        c3_id, "pat_3", "Balwant Singh", "9123456782", 62, "Male", "English",
        "Kheri Village", "prescription", "balwant_hypertension_rx.jpg", rx_svg,
        2100.0, 88.0, 95.8,
        json.dumps(["Mild Morning Dizziness", "Occasional Neck Stiffness"]),
        "Essential Hypertension (5 years)", "None",
        0, 0, "",
        "COMPLETED", 0, 1, None, t_minus_1d, t_minus_1d
    ))

    medicines_3 = [
        {
            "name": "Telmisartan",
            "category": "Antihypertensive",
            "dosage": "40 mg",
            "frequency": "Once daily morning (OD)",
            "instructions": "After breakfast",
            "duration": "30 days",
            "confidence_score": 0.98,
            "is_uncertain": False,
            "raw_line": "Tab Telmisartan 40mg OD"
        },
        {
            "name": "Amlodipine",
            "category": "Calcium Channel Blocker",
            "dosage": "5 mg",
            "frequency": "Once daily morning (OD)",
            "instructions": "After breakfast",
            "duration": "30 days",
            "confidence_score": 0.96,
            "is_uncertain": False,
            "raw_line": "Tab Amlodipine 5mg OD"
        }
    ]
    cursor.execute('''
    INSERT INTO ocr_extractions (
        id, consultation_id, raw_text, medicines_json, lab_tests_json, doctor_notes, uncertain_items_json, ai_summary, missing_info_json, processed_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        "ocr_103", c3_id,
        "Dr. Rajesh Sharma. Patient: Balwant Singh 62M. Tab Telmisartan 40mg OD, Tab Amlodipine 5mg OD x 30 days.",
        json.dumps(medicines_3), json.dumps([]),
        "Strict low-sodium diet. Daily 30 min morning walk.",
        json.dumps([]),
        "Standard dual antihypertensive maintenance regimen for Grade 1 essential hypertension.",
        json.dumps([]),
        t_minus_1d
    ))

    # Doctor Response for Consultation 3
    approved_rx_3 = [
        {
            "name": "Telmisartan",
            "dosage": "40 mg",
            "frequency": "Once daily in morning (OD)",
            "instructions": "Take after breakfast with water",
            "duration": "30 days"
        },
        {
            "name": "Amlodipine",
            "dosage": "5 mg",
            "frequency": "Once daily in morning (OD)",
            "instructions": "Take alongside Telmisartan",
            "duration": "30 days"
        }
    ]
    cursor.execute('''
    INSERT INTO doctor_responses (
        id, consultation_id, doctor_id, doctor_name, doctor_reg_no, doctor_specialty, doctor_hospital,
        possible_condition, clinical_observations, approved_prescription_json, recommended_tests_json,
        treatment_instructions, lifestyle_advice, follow_up_date, voice_explanation_text, reviewed_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        "resp_103", c3_id, "doc_1", "Dr. Rajesh Sharma, MD", "MCI-2014-48291",
        "General Physician & Rural Health Specialist", "District Civil Hospital & Telemedicine Center",
        "Essential Hypertension (Well Controlled on Dual Regimen)",
        "Patient has stabilized blood pressure with current combination. Morning dizziness is mild and postural. No signs of target organ damage.",
        json.dumps(approved_rx_3),
        json.dumps(["Serum Electrolytes (Sodium, Potassium)", "Serum Creatinine (Annual Check)"]),
        "Continue combination therapy regularly without skipping. Avoid sudden standing from lying posture to prevent postural dizziness.",
        "Restrict dietary salt to less than 1 teaspoon (4 grams) per day. Avoid pickles, papads, and processed snacks. Maintain brisk morning walk for 25-30 minutes.",
        (now + timedelta(days=25)).strftime("%Y-%m-%d"),
        "Namaste Balwant ji. Your blood pressure medicines are working well. Please continue Telmisartan and Amlodipine every morning. Keep salt low in food.",
        t_minus_1d
    ))

    conn.commit()
    conn.close()
    print("Database seeded with sample doctors, patients, prescriptions, reports, OCR extractions, and responses!")

if __name__ == "__main__":
    seed_all()
