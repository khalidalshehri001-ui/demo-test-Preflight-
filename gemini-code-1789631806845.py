import streamlit as st

# 1. Page Configuration & Styling
st.set_page_config(
    page_title="Preflight — PDPL Compliance Agent",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS injection matching the Preflight visual design system
st.markdown(
    """
    <style>
    :root {
        --ink: #16202B;
        --paper: #F0F2EE;
        --card: #FFFFFF;
        --chart: #A2306E;
        --chart-wash: #F7E9F1;
        --caution: #B5751B;
        --caution-wash: #FBF0DC;
        --clear: #1C6B5A;
        --clear-wash: #E2EFEA;
        --rule: #CFD5CE;
    }
    
    .main {
        background-color: var(--paper);
    }
    
    .pf-top {
        background: #16202B;
        color: #F0F2EE;
        padding: 24px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    
    .pf-id {
        font-family: monospace;
        font-size: 12px;
        color: #8FA3B4;
        margin-bottom: 8px;
        letter-spacing: 0.04em;
    }
    
    .pf-title {
        font-size: 48px;
        font-weight: 700;
        line-height: 1.0;
        margin-bottom: 10px;
        color: #FFFFFF;
    }
    
    .pf-sub {
        font-size: 16px;
        color: #C2CCD4;
    }

    .pf-rule {
        background: #FFFFFF;
        border-left: 4px solid #A2306E;
        padding: 16px;
        margin: 16px 0;
        border-radius: 2px;
    }
    
    .owner-tag {
        display: inline-block;
        font-family: monospace;
        font-size: 12px;
        color: #A2306E;
        background: #F7E9F1;
        padding: 2px 8px;
        border-radius: 2px;
        margin-bottom: 12px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Masthead Header Component
st.markdown(
    """
    <div class="pf-top">
        <div class="pf-id">PDPL COMPLIANCE AGENT / AGENTIC AI BOOTCAMP</div>
        <div class="pf-title">Preflight</div>
        <div class="pf-sub">Checks whether a Saudi founder's product breaks the Personal Data Protection Law — <b>by reading their code, before they launch.</b></div>
    </div>
""",
    unsafe_allow_html=True,
)

# 2. Navigation Stage Selection (Simulating Flight Strip)
stages = [
    "0. The Idea",
    "1. The 3 Laws",
    "2. Agent 1: Scan",
    "3. Agent 2: Ask",
    "4. Agent 3: Match",
    "5. Agent 4: Judge",
    "6. Agent 5: Plan",
    "7. Build & Test",
]

selected_stage = st.radio(
    "Navigation Flight Strip", stages, horizontal=True, label_visibility="collapsed"
)

st.markdown("---")

# 3. Panel Content Routing
if selected_stage == "0. The Idea":
  st.header("What the system does")
  st.write(
      "A founder is building an app that collects personal data. They usually"
      " find out they broke the law after launch, when fixing it means"
      " rebuilding a live product."
  )
  st.write(
      "Preflight moves that check to the cheapest possible moment. It reads"
      " the founder's GitHub repository, extracts personal data interactions,"
      " queries targeted unknowns, correlates against real PDPL text, and"
      " outputs actionable fixes."
  )

  st.markdown(
      """
    <div class="pf-rule">
        <b>The scope limit that keeps this safe:</b><br>
        Preflight never connects to or submits anything to a real government system. It produces human-readable advice carrying a mandatory legal disclaimer[cite: 1].
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.subheader("Five agents in a line")
  st.write(
      "All agents read and write to **one shared JSON object** that expands"
      " sequentially down the pipe[cite: 1]:"
  )

  st.code(
      """state = {
  "repo": {...},             # Agent 1
  "scan": {...},             # Agent 1
  "unknowns": [...],         # Agent 1 → hands off to Agent 2
  "answers": {...},          # Agent 2
  "matched_articles": [...], # Agent 3
  "findings": [...],         # Agent 4
  "action_plan": [...],      # Agent 5
  "verdict": "..."           # Agent 5
}""",
      language="python",
  )

elif selected_stage == "1. The 3 Laws":
  st.header("Three documents, not one")
  st.write("We load official legal PDFs which stack together[cite: 1]:")

  st.markdown(
      """
    - **LAW:** The Personal Data Protection Law (Royal Decree M/19, amended by M/148)[cite: 1, 2]. Says *what* you must do.
    - **IR:** The Implementing Regulation[cite: 1, 4]. The instruction manual containing 38 articles telling *how* to comply.
    - **TRANSFER:** The Transfer Regulation[cite: 1, 3] (9 articles governing data crossing Saudi borders).
    """
  )

  st.markdown(
      """
    <div class="pf-rule">
        <b>The Article 5 Trap:</b><br>
        All three documents have an "Article 5" with completely different contexts. Numbers never travel alone; they always carry their parent document tag (e.g., <i>Implementing Regulation, Article 5</i>)[cite: 1].
    </div>
    """,
      unsafe_allow_html=True,
  )

elif selected_stage == "2. Agent 1: Scan":
  st.header("Agent 1 — Repo Scanning")
  st.markdown(
      '<span class="owner-tag">Member 1 Responsibility</span>',
      unsafe_allow_html=True,
  )
  st.write(
      "Parses codebase structures via regular expressions and Python's `ast`"
      " module to extract factual footprints of personal data processing."
  )

  st.subheader("Sample Scanner Output State")
  st.code(
      """{
  "repo": { "url": "github.com/example/shopapp", "commit_sha": "a3f9c21" },
  "personal_data_fields": [
    { "field": "national_id", "source": "models/user.py", "line": 14, "category": "sensitive_identifier" }
  ],
  "third_party_sdks": [
    { "package": "mixpanel", "purpose_guess": "analytics", "data_leaves_country": "likely" }
  ],
  "unknowns": ["purpose_processing", "legal_basis", "retention_period"]
}""",
      language="json",
  )

elif selected_stage == "3. Agent 2: Ask":
  st.header("Agent 2 — Clarifying Questions")
  st.markdown(
      '<span class="owner-tag">Member 1 Partnership</span>',
      unsafe_allow_html=True,
  )
  st.write(
      "Inspects code scan gaps (`unknowns`) and prompts the founder with"
      " **2 to 4 precise questions** contextually matched to code realities"
      "[cite: 1]."
  )

  st.code(
      """{
  "questions": [
    {
      "id": "q1",
      "topic": "legal_basis",
      "question": "Your signup endpoint collects national_id. What is your legal basis — consent or contract?",
      "why_asked": "national_id found at models/user.py:14 with no local consent implementation."
    }
  ],
  "answers": {
    "q1": "We use it for identity verification at signup without user consent tokens."
  }
}""",
      language="json",
  )

elif selected_stage == "4. Agent 3: Match":
  st.header("Agent 3 — Legal Compliance / RAG")
  st.markdown(
      '<span class="owner-tag">Member 2 Responsibility</span>',
      unsafe_allow_html=True,
  )
  st.write(
      "Maps code artifacts and founder questionnaire answers against the 90+"
      " chunked statutory articles using structured `kind` tags and cross-reference"
      " dictionaries[cite: 1]."
  )

  st.markdown(
      """
    * **Chunking Rule:** Split strictly by article/paragraph rather than blind word counts to preserve textual integrity[cite: 1].
    * **Strict Citation Rule:** Citations are dropped if they cannot trace directly back to a real document chunk source[cite: 1].
    """
  )

elif selected_stage == "5. Agent 4: Judge":
  st.header("Agent 4 — Gap & Risk Analysis")
  st.markdown(
      '<span class="owner-tag">Member 3 Responsibility</span>',
      unsafe_allow_html=True,
  )
  st.write(
      "Evaluates matched articles against evidence to categorize compliance"
      " statuses (`violated`, `unclear`, `satisfied`) and assign risk levels"
      " (`high`, `medium`, `low`)[cite: 1]."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.markdown("#### Status Definitions")
    st.markdown(
        "- 🔴 **Violated:** Unambiguous non-compliance evidence[cite: 1].\n"
        "- 🟡 **Unclear:** Ambiguous boundaries requiring human review.\n"
        "- 🟢 **Satisfied:** Explicit compliance footprint detected[cite: 1]."
    )
  with col2:
    st.markdown("#### Severity Tiers")
    st.markdown(
        "- 🔴 **High:** Sensitive data exposed or unauthorized cross-border"
        " flow[cite: 1].\n"
        "- 🟡 **Medium:** Operational documentation / process gaps[cite: 1].\n"
        "- 🟢 **Low:** Minor statutory housekeeping."
    )

elif selected_stage == "6. Agent 5: Plan":
  st.header("Agent 5 — Action Plan & Verdict")
  st.markdown(
      '<span class="owner-tag">Member 4 Responsibility</span>',
      unsafe_allow_html=True,
  )
  st.write(
      "Transforms regulatory findings into an organized, prioritized remediation"
      " checklist complete with a deployment verdict[cite: 1]."
  )

  st.code(
      """{
  "action_plan": [
    {
      "priority": 1,
      "severity": "high",
      "action": "Add an explicit consent mechanism before collecting national_id at app/routes.py:33."
    }
  ],
  "verdict": "Not ready to launch",
  "disclaimer": "Automated advisory output. Not official legal advice."
}""",
      language="json",
  )

elif selected_stage == "7. Build & Test":
  st.header("Build Strategy & Testing Milestones")
  st.write(
      "To ensure zero false-positive tolerance, build isolated target codebases"
      " early in the development lifecycle[cite: 1]."
  )

  st.markdown(
      """
    - [ ] **The Broken Test Repo:** A Flask app intentionally bundling un-consented `national_id` fields, third-party trackers, and EU cloud storage endpoints[cite: 1].
    - [ ] **The Clean Test Repo:** A baseline app ensuring zero false flags fire up during scanning[cite: 1].
    - [ ] **Line-Number Enforcement:** Validate that every generated finding maps directly to a physical repository file and line number[cite: 1].
    """
  )

# Footer Disclaimer
st.markdown("---")
st.caption(
    "Preflight Presentation App • Built with Streamlit[cite: 1]"
)