# CAREFlow AI — Intelligent Patient Care Agent

> **"One patient. One journey. Every next step coordinated."**

CAREFlow AI is a production-grade healthcare coordination web application built for hackathons. A single, central **Patient Care Agent** reasons over real patient EHR data, guides new patient onboarding with a 3-panel conversational interface, and executes operations through 24 specialized tools with clinical safety guardrails.

---

## 🔒 Authentication, Multi-Role Access & Session Security

CAREflow AI implements an enterprise-grade, HIPAA-aligned authentication and session security architecture:

### 1. Multi-Role Demo Credentials
| Persona / Role | Email / Identifier | Password | Primary Destination & Permissions |
| :--- | :--- | :--- | :--- |
| **👤 Patient (Rahul Sharma)** | `rahul.sharma@example.com` or `P1024` | `password123` | Patient Dashboard (Authorized Record `P1024` only) |
| **🏥 Care Staff (Sarah Jenkins)**| `sarah.jenkins@careflow.ai` | `password123` | Care Coordination Portal & Patient Records |
| **🩺 Doctor (Dr. Anita Vance)** | `anita.vance@careflow.ai` | `password123` | Doctor Portal & Human-in-the-Loop Approvals |
| **🛡️ Admin (Michael Scott)** | `admin@careflow.ai` | `admin123` | System Operations & Immutable Audit Trail |

*Quick 1-click demo login buttons are provided on the Login page for instant evaluator access.*

### 2. Session Security Features
- **Session Tokens**: Cryptographically generated 256-bit session tokens (`CF-SESS-...`) with expiration tracking.
- **Horizontal Privilege Escalation Protection**: `PATIENT` role tokens are strictly isolated to their assigned `patient_id`. Cross-patient record requests are blocked with `403 Forbidden`.
- **Top-Right Account Menu**: Includes User Avatar, Name, Role badge, Profile navigation, Settings modal, Privacy & Security modal, and **Log Out** button.
- **Logout Confirmation & Instant Revocation**: A dedicated confirmation modal verifies sign-out intent. The session is immediately invalidated on the backend (`POST /api/auth/logout`), all DOM and in-memory health context is purged, and `window.history.replaceState` prevents browser Back-button access.
- **Session Timeout Monitor**: Active user event listener with a countdown warning modal (`[Stay Signed In]` / `[Log Out]`) and automatic secure termination upon expiration.
- **Tamper-Evident Audit Trail**: Records `LOGIN`, `LOGOUT`, `FAILED_LOGIN`, `SESSION_EXPIRED`, and agent tool executions.

---

## 🚀 Quick Start

To launch or restart the server:
```powershell
python run.py
```
Open **[http://127.0.0.1:8080](http://127.0.0.1:8080)** in your browser.

---

## ✨ Key Feature: Conversational Patient Onboarding (3-Panel UI)

When a new patient joins or clicks **"✨ Start New Patient Setup"**:
1. **Left Panel (Progress Stepper)**: 10-step progress checklist (`Welcome → Profile → Health & Allergies → Medications → Ongoing Care → Appointments → Tests & Reports → Specialist Care → Goals → Review`) with percentage bar.
2. **Center Panel (Conversational Intake)**: Patient Care Agent conducts a structured conversational intake with inline widgets (quick buttons, date pickers, allergy tags, medication builders, and file upload simulation).
3. **Right Panel (Live Care Profile Preview)**: Real-time visual EHR summary card updating as the patient types or selects options.
4. **Care Journey Generation**: Upon confirmation, automatically initializes the patient's EHR records and generates their 9-stage care lifecycle.

---

## 🏛️ Architecture: ONE Agent + Multiple Tools

```
                              ┌────────────────────────────────────────┐
                              │          PATIENT CARE AGENT            │
                              │       (Central Reasoning Layer)        │
                              └──────────────────┬─────────────────────┘
                                                 │
      ┌───────────────┬──────────────────────────┼──────────────────────────┬────────────────┐
      ▼               ▼                          ▼                          ▼                ▼
[Profile Tools] [History Tools]          [Medication Tools]        [Appointment Tools]  [Test/Report Tools]
      │               │                          │                          │                │
      ▼               ▼                          ▼                          ▼                ▼
[Progress Tools][Next Steps Tools]       [Specialist Tools]        [Preference Tools]   [Audit Log Tools]
```

- **Single Reasoning Engine**: [`backend/agent_engine.py`](file:///d:/CodingX/backend/agent_engine.py)
- **24 Discrete Backend Tools**: Executes operations against SQLite database without state hallucinations.
- **Visible 9-Step Agentic Loop**: Tracks `OBSERVE` → `UNDERSTAND` → `REASON` → `PLAN` → `ACT` → `VERIFY` → `UPDATE` → `NOTIFY` → `MONITOR`.
- **Human-In-The-Loop & Safety Guardrails**:
  - **Clinical Safety**: Medication alterations and diagnoses cannot be prescribed autonomously by the agent and are routed to physician review in the Staff Approval Center.
  - **Emergency Redirect**: Acute symptoms trigger an immediate urgent medical alert to contact emergency services.

---

## 🧭 13 Core Application Sections + Onboarding

0. **Patient Intake & Setup**: 3-panel progressive conversational onboarding engine.
1. **Dashboard**: Patient greeting, Journey Status (`🟢 ON TRACK`), Next Appointment countdown, Next Step banner, Latest Prescription, Latest Report, Milestone Stepper, AI Priority Alert bar.
2. **Profile**: Demographics, Blood group, Contact, Emergency contacts, Allergies, Chronic conditions, Insurance, and RBAC authorization.
3. **Medical History**: Chronological timeline of clinical consultations, procedures, lab panels, diagnoses codes, and clinician notes.
4. **Prescriptions**: Active therapies vs previous medications, dosages, frequencies, instructions, prescribing doctor, and clinical safety locks.
5. **Appointments**: Upcoming, completed, rescheduled, and cancelled appointments with interactive slot booking, reschedule, and cancellation.
6. **Tests & Reports**: Diagnostic tests with statuses (`✓ Completed`, `✓ Available`, `◷ Awaiting Report`) and interactive lab parameter modal with reference ranges and flags.
7. **Specialist Care**: Referral tracking across Cardiology, Endocrinology, Orthopedics, Pulmonology, and General Medicine with specialist notes and next recommendations.
8. **Progress**: 9-Stage interactive care lifecycle (`Registration → Consultation → Test Ordered → Test Completed → Report Available → Specialist Care → Appointment → Follow-up → Next Step`).
9. **Next Steps**: Actionable patient checklist with deadlines, priority badges (`HIGH`, `MEDIUM`, `LOW`), source contexts, and "Mark Complete" toggle.
10. **AI Assistant**: Interactive Patient Care Agent chat with real-time tool execution cards, suggested prompt chips, dynamic additions (medications, tests), and live Agentic Reasoning Loop step breakdown.
11. **Notifications**: Event-driven notification center for appointments, lab results, medication reminders, and journey transitions.
12. **Admin / Staff View**: Operations analytics with Chart.js caseloads, patient search, and **Human-In-The-Loop Approval Center** (Approve / Modify / Reject).
13. **Audit & Security**: Immutable, tamper-evident audit log recording every user action, tool call, actor, target record, context, and security verification status.

---

## 🎭 5 Seeded Patient Personas + Dynamic Intake

1. **Rahul Sharma** (`P1024` - Primary Hero Demo): Cardiology Specialist Consultation scheduled for 25 Aug at 10:30 AM (`🟢 ON TRACK`).
2. **Elena Rostova** (`P1025`): Type 2 Diabetes; awaiting HbA1c lab report release (`🟡 ATTENTION REQUIRED`).
3. **Marcus Chen** (`P1026`): Post-arthroscopic knee repair; Week 4 physical therapy follow-up (`🟢 ON TRACK`).
4. **Priya Patel** (`P1027`): Pulmonology; asthma maintenance inhaler and spirometry review (`🟢 ON TRACK`).
5. **James Wilson** (`P1028`): Annual executive wellness evaluation; preventive health (`🟢 ON TRACK`).
6. **New Patient Onboarding**: Full conversational intake supporting live profile generation (e.g. *Aarav Mehta* / custom patient).

---

## 🧪 Verification & Testing

- Automated Test Suite: `python verify_onboarding_and_agent.py`
- Live HTTP verification: `python verify_live_server.py`
- Database reset: `python backend/seed_data.py`
