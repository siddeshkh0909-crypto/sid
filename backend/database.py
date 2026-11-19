# MediBridge Database Module
import sqlite3
import json
import os
import hashlib
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "medibridge.db")

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str) -> str:
    return hashlib.sha256(password.strip().encode('utf-8')).hexdigest()

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        role TEXT NOT NULL, -- 'patient' or 'doctor'
        full_name TEXT NOT NULL,
        phone_number TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        preferred_language TEXT DEFAULT 'English',
        village_location TEXT,
        doctor_reg_no TEXT,
        doctor_specialty TEXT,
        doctor_hospital TEXT,
        created_at TEXT NOT NULL
    )
    ''')

    # Consultations Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS consultations (
        id TEXT PRIMARY KEY,
        patient_id TEXT NOT NULL,
        patient_name TEXT NOT NULL,
        patient_phone TEXT NOT NULL,
        patient_age INTEGER,
        patient_gender TEXT,
        patient_language TEXT DEFAULT 'English',
        village_location TEXT,
        file_type TEXT NOT NULL, -- 'prescription' or 'report'
        original_filename TEXT,
        image_data TEXT, -- Base64 encoded or data URI
        original_size_kb REAL,
        compressed_size_kb REAL,
        compression_ratio REAL,
        symptoms TEXT, -- JSON list
        existing_conditions TEXT,
        allergies TEXT,
        has_voice_note INTEGER DEFAULT 0,
        voice_note_duration INTEGER DEFAULT 0,
        voice_note_transcript TEXT,
        status TEXT NOT NULL, -- 'PENDING_REVIEW', 'UNDER_REVIEW', 'COMPLETED'
        emergency_warning INTEGER DEFAULT 0,
        is_synced INTEGER DEFAULT 1,
        offline_queued_at TEXT,
        synced_at TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES users (id)
    )
    ''')

    # OCR Extractions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ocr_extractions (
        id TEXT PRIMARY KEY,
        consultation_id TEXT UNIQUE NOT NULL,
        raw_text TEXT,
        medicines_json TEXT, -- JSON array of medicine objects
        lab_tests_json TEXT, -- JSON array of lab test objects
        doctor_notes TEXT,
        uncertain_items_json TEXT, -- JSON array of uncertain items requiring verification
        ai_summary TEXT,
        missing_info_json TEXT,
        processed_at TEXT NOT NULL,
        FOREIGN KEY (consultation_id) REFERENCES consultations (id)
    )
    ''')

    # Doctor Responses Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctor_responses (
        id TEXT PRIMARY KEY,
        consultation_id TEXT UNIQUE NOT NULL,
        doctor_id TEXT NOT NULL,
        doctor_name TEXT NOT NULL,
        doctor_reg_no TEXT NOT NULL,
        doctor_specialty TEXT NOT NULL,
        doctor_hospital TEXT,
        possible_condition TEXT NOT NULL,
        clinical_observations TEXT NOT NULL,
        approved_prescription_json TEXT, -- JSON array of prescribed medicines
        recommended_tests_json TEXT, -- JSON array of test names
        treatment_instructions TEXT NOT NULL,
        lifestyle_advice TEXT,
        follow_up_date TEXT,
        voice_explanation_text TEXT,
        reviewed_at TEXT NOT NULL,
        FOREIGN KEY (consultation_id) REFERENCES consultations (id),
        FOREIGN KEY (doctor_id) REFERENCES users (id)
    )
    ''')

    # Emergency Facilities Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emergency_facilities (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        facility_type TEXT NOT NULL, -- 'Primary Health Centre (PHC)', 'Community Health Centre (CHC)', 'District Hospital'
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        distance_km REAL NOT NULL,
        phone TEXT NOT NULL,
        ambulance_number TEXT NOT NULL,
        address TEXT NOT NULL,
        available_24_7 INTEGER DEFAULT 1,
        has_oxygen INTEGER DEFAULT 1,
        has_emergency_ward INTEGER DEFAULT 1
    )
    ''')

    conn.commit()
    conn.close()

def seed_emergency_facilities():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM emergency_facilities")
    if cursor.fetchone()[0] == 0:
        facilities = [
            ("fac_1", "Sonpur Primary Health Centre (PHC)", "Primary Health Centre (PHC)", "Sonpur", "Bihar", 3.2, "+91 94310 11223", "108 / 112", "Main Road, Opp. Panchayat Bhavan, Sonpur", 1, 1, 0),
            ("fac_2", "Hajipur Community Health Centre (CHC)", "Community Health Centre (CHC)", "Vaishali", "Bihar", 8.5, "+91 6224 274112", "108", "Station Road, Hajipur", 1, 1, 1),
            ("fac_3", "Vaishali District Civil Hospital", "District Hospital", "Vaishali", "Bihar", 16.0, "+91 6224 272200", "108 / 102", "Civil Lines, Hajipur, Vaishali", 1, 1, 1),
            ("fac_4", "Rampur Gram Panchayat Sub-Centre", "Sub-Health Centre", "Rampur", "Bihar", 1.8, "+91 94318 88990", "108", "Near Government Primary School, Rampur", 0, 0, 0),
            ("fac_5", "AIIMS Patna Emergency Trauma Center", "Apex Medical Hospital", "Patna", "Bihar", 28.5, "+91 612 245 1070", "108 / 112", "Phulwarisharif, Patna", 1, 1, 1)
        ]
        cursor.executemany('''
        INSERT INTO emergency_facilities (
            id, name, facility_type, district, state, distance_km, phone, ambulance_number, address, available_24_7, has_oxygen, has_emergency_ward
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', facilities)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    seed_emergency_facilities()
    print("Database initialized & emergency facilities seeded successfully.")
