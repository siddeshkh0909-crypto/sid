// ═══════════════════════════════════════════════════════════════
// KARAVALI INSTITUTION OF TECHNOLOGY (KIT) — LANDING PAGE SCRIPT
// ═══════════════════════════════════════════════════════════════

(function () {
  // Institutional Legal Policies Knowledgebase
  const LEGAL_POLICIES = {
    privacy: {
      title: "🛡️ Privacy & Data Protection Policy (DPDP Act 2023 Compliant)",
      citation: "Compliance: Indian Digital Personal Data Protection Act 2023 & IT Act 2000 (Sec 43A) • Ref: KIT/DPO/POL-01",
      body: `
        <h4>1. Preamble & Scope</h4>
        <p>Karavali Institution of Technology (KIT), Mangalore is committed to protecting the privacy, confidentiality, and security of all personal identifiable information (PII) collected from students, faculty, staff, parents, and alumni. This policy governs the processing of data across the KIT SMART Attendance & Academic Portal, campus biometric access systems, RFID smart gates, and official administrative records.</p>

        <h4>2. Information Collected & Lawful Purpose</h4>
        <p>The institution collects only such information as is strictly necessary for academic administration, state university regulatory compliance with Visvesvaraya Technological University (VTU), and student welfare:</p>
        <ul>
          <li><strong>Student Identity Data:</strong> Full legal name, University Seat Number (USN), date of birth, blood group, government ID (Aadhaar/PAN), and photograph.</li>
          <li><strong>Academic & Attendance Telemetry:</strong> Course registration, semester timetable, real-time subject attendance percentages, internal assessment (IA) marks, and VTU examination SGPA/CGPA history.</li>
          <li><strong>Contact & Parent Details:</strong> Official institutional email, personal mobile number, permanent address, and emergency guardian contact.</li>
        </ul>

        <h4>3. Data Security & Storage Architecture</h4>
        <p>All sensitive academic records, authentication credentials, and user profiles are encrypted in transit using Transport Layer Security (TLS 1.3) and encrypted at rest using 256-bit Advanced Encryption Standard (AES-256) on enterprise Google Firebase Cloud servers. Password hashes utilize salted cryptographic key-derivation algorithms. Biometric scans and live attendance timestamps are immutably logged to prevent unauthorized modification.</p>

        <h4>4. Zero Commercial Sharing</h4>
        <p>KIT enforces a strict zero-tolerance prohibition against selling, renting, or commercializing student or faculty data to third-party advertisers, financial telemarketers, or commercial ed-tech providers. Data is shared exclusively with statutory regulatory bodies (VTU Belagavi, AICTE New Delhi, and Karnataka Examination Authority) pursuant to legal compliance mandates.</p>

        <h4>5. Rights of Data Principals & Grievances</h4>
        <p>Students and faculty possess the legal right to inspect their personal records, request factual rectification, and review access logs. For privacy inquiries or grievance redressal, contact our designated Data Protection Officer (DPO):</p>
        <p><strong>Data Protection Officer:</strong> Dr. Priya Shenoy, Dean (R&D)<br>
        <strong>Email:</strong> dpo@karavali.edu.in | <strong>Office:</strong> Administrative Block, KIT Campus, Mangalore</p>
      `
    },
    terms: {
      title: "⚖️ Terms of Service & Campus IT Acceptable Use Policy",
      citation: "Statutory Bylaws: Visvesvaraya Technological University & KIT Ordinance • Ref: KIT/IT/TOS-2026",
      body: `
        <h4>1. Acceptance of Terms</h4>
        <p>By accessing or utilizing the KIT SMART Attendance Portal, campus Wi-Fi infrastructure (KIT-SECURE-CAMPUS), laboratory compute servers, or digital library OPAC, all students, faculty members, and authorized visitors agree to be bound by these institutional terms and conditions.</p>

        <h4>2. User Account Security & USN Integrity</h4>
        <p>Every student is issued a unique University Seat Number (USN) account (e.g. 4KM22CS001). Users are strictly accountable for maintaining the confidentiality of their portal passwords. Permitting another student to access an account, sharing session tokens, or attempting to register proxy attendance via automated tools, spoofed geolocation, or cloned QR codes constitutes a severe violation of institutional ethics.</p>

        <h4>3. Prohibited Activities</h4>
        <p>Users must not engage in any of the following activities on college servers or networks:</p>
        <ul>
          <li>Unauthorized vulnerability scanning, penetration testing, or denial-of-service attempts on college infrastructure.</li>
          <li>Automated web scraping, data harvesting, or reverse-engineering of student records, faculty rosters, or attendance algorithms.</li>
          <li>Transmission of malicious software, phishing emails, or pirated copyright material over campus bandwidth.</li>
          <li>Falsification of academic records, VTU grade cards, internal assessment rubrics, or digital certificates.</li>
        </ul>

        <h4>4. Disciplinary Penalties</h4>
        <p>Violations will be adjudicated by the College Disciplinary Committee and Cyber Security Cell. Penalties may include immediate revocation of campus IT privileges, academic suspension, referral to the VTU Malpractice Committee, and formal reporting to law enforcement under the Information Technology Act 2000.</p>
      `
    },
    antiragging: {
      title: "🛑 Anti-Ragging Policy (Zero Tolerance Statutory Mandate)",
      citation: "Statutory Law: UGC Regulations on Curbing Ragging 2009 & Karnataka Education Act 1983 (Sec 116) • Ref: KIT/ARC/2026",
      body: `
        <h4>1. Zero Tolerance Mandate</h4>
        <p>Karavali Institution of Technology enforces an absolute <strong>ZERO TOLERANCE POLICY</strong> against ragging in any form. Ragging is a cognizable criminal offense punishable by rigorous imprisonment, permanent expulsion, and disqualification from seeking admission to any educational institution across India.</p>

        <h4>2. Statutory Definition of Ragging</h4>
        <p>Under UGC Regulations 2009, ragging includes any conduct by words spoken or written, or by an act which has the effect of teasing, treating or handling with rudeness a fresher or any other student; indulging in rowdy or undisciplined activities; asking any student to do any act which causes shame, torment, embarrassment, or physical/psychological harm.</p>

        <h4>3. Institutional Anti-Ragging Committee & Squad</h4>
        <p>The college maintains an active Anti-Ragging Committee headed by the Principal, comprising senior faculty, representatives of civil administration, local police officers (Surathkal/Kavoor Police Station), local media, parents, and student representatives. Dedicated flying squads carry out unannounced 24/7 inspections across hostels, canteens, sports arenas, and college buses.</p>

        <h4>4. 24x7 Emergency Helplines</h4>
        <p>Any student subjected to or witnessing ragging is urged to report immediately through any of the following confidential channels:</p>
        <ul>
          <li><strong>National Anti-Ragging Toll-Free Helpline:</strong> <a href="tel:18001805522" style="color:#0d9488; font-weight:700;">1800-180-5522</a> (24x7 Free)</li>
          <li><strong>National Anti-Ragging Portal:</strong> <a href="https://www.antiragging.in" target="_blank" style="color:#0d9488;">www.antiragging.in</a> | <strong>Email:</strong> helpline@antiragging.in</li>
          <li><strong>KIT Anti-Ragging Squad Mobile:</strong> <a href="tel:+919448123456" style="color:#0d9488; font-weight:700;">+91 94481 23456</a> / +91 824 2223785</li>
          <li><strong>Campus Email:</strong> antiragging@karavali.edu.in</li>
        </ul>

        <h4>5. Mandatory Penal Actions</h4>
        <p>Upon verification of any ragging complaint, the institution will immediately suspend the accused student, lodge an FIR with the local police station within 24 hours under non-bailable provisions, and enforce permanent expulsion with rustication.</p>
      `
    },
    conduct: {
      title: "📜 Code of Conduct & Academic Integrity Policy",
      citation: "Regulations: VTU Belagavi Academic Ordinances & Examination Ethics Guidelines • Ref: KIT/ACAD/2026",
      body: `
        <h4>1. Attendance Mandate (VTU 75% Rule)</h4>
        <p>In accordance with Visvesvaraya Technological University (VTU) academic regulations, every student must maintain a <strong>minimum of 75% physical attendance</strong> in each registered theory subject and laboratory course to be eligible to appear for semester-end university examinations. Students whose attendance falls between 60% and 74% due to verified medical emergencies may apply for condonation with authentic medical documentation, subject to university approval. Students below 60% will be detained.</p>

        <h4>2. Examination Conduct & Anti-Malpractice Rules</h4>
        <p>Academic honesty is the cornerstone of engineering education. The following are classified as severe examination malpractices:</p>
        <ul>
          <li>Possession of mobile phones, smartwatches, programmable calculators, or unauthorized study material in examination halls.</li>
          <li>Copying, seeking assistance, impersonation, or communication with peers during university or internal exams.</li>
          <li>Tampering with barcoded answer scripts, question papers, or digital grade rosters.</li>
        </ul>
        <p>All malpractice cases are forwarded directly to the VTU Examination Malpractice Committee, resulting in cancellation of results for the entire semester and potential debasement from writing university exams for up to three consecutive years.</p>

        <h4>3. Plagiarism & Project Intellectual Property</h4>
        <p>All final-year B.E. and M.Tech project theses, technical seminar reports, and research papers must undergo mandatory anti-plagiarism screening using Turnitin / DrillBit software. The maximum permissible similarity index is strictly <strong>15% (excluding bibliography)</strong>. Projects exceeding this threshold will be rejected for submission.</p>

        <h4>4. Campus Decorum & Substance-Free Campus</h4>
        <p>Karavali Institution of Technology is a strictly declared <strong>Substance-Free, Smoke-Free, and Alcohol-Free Zone</strong>. Possession, consumption, or distribution of narcotic substances or alcohol will lead to immediate criminal referral, police prosecution, and permanent rustication.</p>
      `
    },
    posh: {
      title: "🌸 Internal Complaints Committee (ICC) & POSH Compliance",
      citation: "Statutory Law: Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 • Ref: KIT/ICC/2026",
      body: `
        <h4>1. Objective & Legal Obligation</h4>
        <p>Pursuant to the provisions of the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 and UGC (Prevention, Prohibition and Redressal of Sexual Harassment in Higher Educational Institutions) Regulations 2015, Karavali Institution of Technology is deeply committed to providing an environment free from gender discrimination, sexual harassment, and intimidation.</p>

        <h4>2. Composition of the Committee (ICC)</h4>
        <p>The Internal Complaints Committee is a statutory body constituted with a majority of female members:</p>
        <ul>
          <li><strong>Presiding Officer:</strong> Dr. Priya Shenoy, Professor & Dean (R&D)</li>
          <li><strong>Faculty Representatives:</strong> Dr. Meenakshi Rao (Associate Prof, AI&DS) & Prof. Radhika Pai (Assistant Prof, CSE)</li>
          <li><strong>Non-Teaching Staff Member:</strong> Smt. Rekha Rai, Senior Administrative Superintendent</li>
          <li><strong>External Independent Member:</strong> Adv. Sujata Rao, Senior Legal Counsel & NGO Representative</li>
          <li><strong>Student Nominees:</strong> 2 Meritorious Postgraduate/Undergraduate Student Representatives</li>
        </ul>

        <h4>3. Redressal & Investigation Mechanism</h4>
        <p>Any aggrieved female student, employee, or visitor may submit a confidential complaint in writing or via email within 90 days of an incident. The committee guarantees absolute confidentiality, protects the complainant against retaliation, conducts fair time-bound inquiries completed within 90 days, and submits conclusive findings to the Principal and Governing Council for prompt disciplinary action.</p>

        <p><strong>Confidential Email:</strong> icc@karavali.edu.in | <strong>Helpline:</strong> +91 824 2223785 (Extn 104)</p>
      `
    },
    grievance: {
      title: "📋 Student Grievance Redressal Mechanism",
      citation: "Compliance: UGC (Redressal of Grievances of Students) Regulations 2023 • Ref: KIT/SGRC/2026",
      body: `
        <h4>1. Preamble & Framework</h4>
        <p>In accordance with UGC Regulations 2023, Karavali Institution of Technology has instituted a transparent, equitable, and multi-tiered Student Grievance Redressal Committee (SGRC) to address student grievances relating to admissions, examinations, faculty evaluation, library resources, hostel welfare, and fee payments.</p>

        <h4>2. Three-Tier Escalation Hierarchy</h4>
        <ul>
          <li><strong>Level 1 (Departmental Mentorship):</strong> The student discusses grievances with their designated Class Advisor or Head of Department (HOD) for immediate resolution within 3 working days.</li>
          <li><strong>Level 2 (Institutional SGRC):</strong> If unresolved, the grievance is formally logged with the Student Grievance Redressal Committee chaired by the Principal, with hearing and redressal within 15 working days.</li>
          <li><strong>Level 3 (University Ombudsperson):</strong> If the student remains unsatisfied with the SGRC decision, an appeal may be preferred to the designated independent Ombudsperson appointed by VTU Belagavi.</li>
        </ul>

        <p><strong>Online Grievance Submission:</strong> grievances@karavali.edu.in | <strong>Contact:</strong> Dean (Student Welfare), KIT Campus</p>
      `
    },
    refund: {
      title: "💰 Fee Refund & Cancellation Policy",
      citation: "Norms: All India Council for Technical Education (AICTE) & Karnataka Examination Authority (KEA) Guidelines • Ref: KIT/FEE/2026",
      body: `
        <h4>1. Admission Cancellation & Refund Guidelines</h4>
        <p>The fee refund policy of Karavali Institution of Technology strictly complies with the statutory guidelines issued annually by the All India Council for Technical Education (AICTE), UGC, and the Department of Higher Education, Government of Karnataka.</p>

        <h4>2. Refund Deduction Matrix (Prior to Formal Course Commencement)</h4>
        <table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:13px; text-align:left;">
          <thead>
            <tr style="background:#f1f5f9; border-bottom:2px solid #cbd5e1;">
              <th style="padding:10px; border:1px solid #e2e8f0;">Timeline of Withdrawal Application</th>
              <th style="padding:10px; border:1px solid #e2e8f0;">Percentage of Refund</th>
              <th style="padding:10px; border:1px solid #e2e8f0;">Deduction</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">15 days or more before the formally announced last date of admission</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0; font-weight:700; color:#10b981;">100% Refund</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">Max ₹1,000 Processing Fee</td>
            </tr>
            <tr>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">Less than 15 days before the formally announced last date</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0; font-weight:700; color:#0284c7;">90% Refund</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">10% Aggregate Fee Deduction</td>
            </tr>
            <tr>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">Less than 15 days after the formally announced last date</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0; font-weight:700; color:#f59e0b;">80% Refund</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">20% Aggregate Fee Deduction</td>
            </tr>
            <tr>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">Between 16 and 30 days after the formally announced last date</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0; font-weight:700; color:#ea580c;">50% Refund</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">50% Aggregate Fee Deduction</td>
            </tr>
            <tr>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">More than 30 days after the formally announced last date</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0; font-weight:700; color:#ef4444;">0% (No Refund)</td>
              <td style="padding:8px 10px; border:1px solid #e2e8f0;">Only Caution Deposit Refunded</td>
            </tr>
          </tbody>
        </table>

        <h4>3. Processing & Disbursement</h4>
        <p>Refund requests must be formally submitted through the Admissions Accounts Cell with original payment receipts and valid bank account credentials. Approved refunds will be transferred directly via NEFT/RTGS within 14 working days.</p>
      `
    },
    disclosures: {
      title: "📊 Mandatory Disclosures, Accreditations & NIRF Reports",
      citation: "Statutory Transparency Mandate: AICTE Section 10(1) & VTU Statutes • Ref: KIT/MANDATORY/2026",
      body: `
        <h4>1. Institutional Governance & Approvals</h4>
        <p>Karavali Institution of Technology (KIT) operates in strict compliance with the statutory norms prescribed by the Ministry of Education, All India Council for Technical Education (AICTE), New Delhi, and Visvesvaraya Technological University (VTU), Belagavi.</p>
        <ul>
          <li><strong>AICTE Permanent Institute ID:</strong> 1-303131703 (Current EOA valid for Academic Year 2026-27).</li>
          <li><strong>VTU Affiliation Order:</strong> Permanent affiliation for Core B.E. programs; annual extension for Emerging Tech programs (AI & DS).</li>
          <li><strong>NAAC Accreditation:</strong> Accredited with 'A+' Grade by National Assessment and Accreditation Council (NAAC).</li>
          <li><strong>Cadre Ratio Compliance:</strong> Maintaining faculty-to-student cadre ratio of 1:15 in accordance with AICTE model staffing norms.</li>
        </ul>

        <h4>2. Audited Balance Sheets & Annual Reports</h4>
        <p>Statutory audited financial statements, faculty qualifications registers, library accession registers, and physical infrastructure reports are publicly accessible in the administrative office during official working hours.</p>

        <p><strong>Office of the Registrar:</strong> Karavali Institution of Technology, NH-66, Mangalore - 575028, Karnataka | <strong>Email:</strong> registrar@karavali.edu.in</p>
      `
    }
  };

  // ════════ MODAL HANDLERS ════════
  window.openPolicyModal = function (policyKey) {
    const policy = LEGAL_POLICIES[policyKey] || LEGAL_POLICIES['privacy'];
    document.getElementById('policyModalTitle').innerHTML = policy.title;
    document.getElementById('policyModalBody').innerHTML = policy.body;
    document.getElementById('policyModalCitation').textContent = policy.citation;
    const modal = document.getElementById('policyModalBackdrop');
    if (modal) {
      modal.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closePolicyModal = function () {
    const modal = document.getElementById('policyModalBackdrop');
    if (modal) modal.style.display = 'none';
  };

  window.openEventModal = function (title, category, date, venue, prize) {
    document.getElementById('eventRegTitle').innerHTML = `<i data-lucide="calendar"></i> Register: ${title}`;
    document.getElementById('eventRegDetails').innerHTML = `
      <div style="font-weight:700; color:#0f172a; font-size:15px; margin-bottom:4px;">${title}</div>
      <div style="font-size:12.5px; color:#0d9488; font-weight:600; margin-bottom:8px;">Category: ${category}</div>
      <div style="font-size:13px; color:#64748b; line-height:1.5;">
        📅 <strong>Date:</strong> ${date} | 📍 <strong>Venue:</strong> ${venue}<br>
        🏆 <strong>Prizes & Certification:</strong> ${prize}
      </div>
    `;
    const modal = document.getElementById('eventModalBackdrop');
    if (modal) {
      modal.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closeEventModal = function () {
    const modal = document.getElementById('eventModalBackdrop');
    if (modal) modal.style.display = 'none';
  };

  window.handleEventRegSubmit = function (e) {
    e.preventDefault();
    const name = document.getElementById('evRegName').value;
    const usn = document.getElementById('evRegUsn').value;
    alert(`🎉 Registration Successful, ${name}!\n\nYour slot has been reserved for the event with USN/ID: ${usn}. Confirmation email and WhatsApp entry pass have been dispatched.`);
    closeEventModal();
  };

  window.openAdmissionsModal = function () {
    const modal = document.getElementById('admissionsModalBackdrop');
    if (modal) {
      modal.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closeAdmissionsModal = function () {
    const modal = document.getElementById('admissionsModalBackdrop');
    if (modal) modal.style.display = 'none';
  };

  window.handleAdmissionsSubmit = function (e) {
    e.preventDefault();
    const name = document.getElementById('admName').value;
    const prog = document.getElementById('admProg').value;
    alert(`🎓 Thank you, ${name}!\n\nYour admissions enquiry for ${prog} has been received. The 2026-27 Information Prospectus and seat allotment matrix will be sent to your WhatsApp and email shortly.`);
    closeAdmissionsModal();
  };

  window.openAlumniModal = function () {
    const modal = document.getElementById('alumniModalBackdrop');
    if (modal) {
      modal.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closeAlumniModal = function () {
    const modal = document.getElementById('alumniModalBackdrop');
    if (modal) modal.style.display = 'none';
  };

  window.handleAlumniSubmit = function (e) {
    e.preventDefault();
    const name = document.getElementById('alName').value;
    alert(`🤝 Welcome to the KIT Global Alumni Network, ${name}!\n\nYour profile has been enrolled in our alumni directory. You will receive invitations to upcoming regional chapter gatherings.`);
    closeAlumniModal();
  };

  window.openVirtualTourModal = function () {
    openLightbox('https://images.unsplash.com/photo-1562774053-701939374585?w=1200&q=80', 'KIT Campus 360° Virtual Experience', '35-acre sprawling campus in Mangalore featuring high-tech engineering blocks, sports complex, research centers, and scenic coastal greenery.');
  };

  window.openLightbox = function (src, title, desc) {
    document.getElementById('lightboxImg').src = src;
    document.getElementById('lightboxTitle').textContent = title;
    document.getElementById('lightboxDesc').textContent = desc;
    const modal = document.getElementById('lightboxBackdrop');
    if (modal) {
      modal.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closeLightbox = function () {
    const modal = document.getElementById('lightboxBackdrop');
    if (modal) modal.style.display = 'none';
  };

  window.toggleMobileNav = function () {
    const drawer = document.getElementById('kitMobileDrawer');
    if (drawer) {
      drawer.style.display = drawer.style.display === 'none' || drawer.style.display === '' ? 'block' : 'none';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  // ════════ FILTERING HANDLERS ════════
  window.filterFaculty = function (dept, btn) {
    const cards = document.querySelectorAll('#facultyGrid .kit-faculty-card');
    cards.forEach(card => {
      const cardDept = card.getAttribute('data-dept');
      if (dept === 'all' || cardDept === dept) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
    if (btn) {
      btn.parentElement.querySelectorAll('.kit-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
  };

  window.filterEvents = function (cat, btn) {
    const cards = document.querySelectorAll('#eventsGrid .kit-event-card');
    cards.forEach(card => {
      const cardCat = card.getAttribute('data-cat');
      if (cat === 'all' || cardCat === cat) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
    if (btn) {
      btn.parentElement.querySelectorAll('.kit-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
  };

  window.filterGallery = function (cat, btn) {
    const items = document.querySelectorAll('#galleryGrid .kit-gallery-item');
    items.forEach(item => {
      const itemCat = item.getAttribute('data-cat');
      if (cat === 'all' || itemCat === cat) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    if (btn) {
      btn.parentElement.querySelectorAll('.kit-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
  };

  // ════════ PORTAL & AUTH OVERLAY INTEGRATION ════════
  window.openAuthModal = function () {
    const authOverlay = document.getElementById('authOverlay');
    if (authOverlay) {
      authOverlay.style.display = 'flex';
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  };

  window.closeAuthModal = function () {
    const authOverlay = document.getElementById('authOverlay');
    if (authOverlay) {
      authOverlay.style.display = 'none';
    }
  };

  window.viewLandingPageFromApp = function () {
    const lp = document.getElementById('landingPage');
    const appShell = document.getElementById('appShell');
    if (lp) lp.style.display = 'block';
    if (appShell) appShell.style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  window.returnToAppShellFromLanding = function () {
    const lp = document.getElementById('landingPage');
    const appShell = document.getElementById('appShell');
    if (lp) lp.style.display = 'none';
    if (appShell) appShell.style.display = 'block';
  };

  // Window scroll navbar shadow
  window.addEventListener('scroll', function () {
    const navbar = document.getElementById('kitNavbar');
    if (navbar) {
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }
  });

  // Global escape key listener to close modals
  window.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closePolicyModal();
      closeEventModal();
      closeAdmissionsModal();
      closeAlumniModal();
      closeLightbox();
      closeAuthModal();
    }
  });

  // Re-run lucide icons initialization on page ready
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
})();