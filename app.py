import streamlit as st
import sqlite3
import pandas as pd
from datetime import date
from utils import CROPS, ACTIVITY_CATEGORIES

# ---------------- Sidebar: Logo and About Section ----------------
# Display logo from the relative path in the sidebar
st.sidebar.image("other files/foot-logo.png", use_container_width=True)

# About section with developer information and data sources
st.sidebar.header("About")
st.sidebar.markdown("""
**Developed by: Shashi Singh**

I am an IIT alumnus, an accomplished Data Scientist and Insights Manager with over 2.5 years of  
experience in delivering advanced machine learning solutions and data-driven insights within the finance  
and entertainment sectors.

**Linkedin:** [https://www.linkedin.com/in/shashiiit/](https://www.linkedin.com/in/shashiiit/)

**Data Sources:**  
[https://agritech.tnau.ac.in](https://agritech.tnau.ac.in)  
Krishi Vigyan Kendras (KVK) websites
""")

# ---------------- Main App Code ----------------
st.title("🌾 Crop Expense Tracker")

# Connect to DB
conn = sqlite3.connect("expenses.db", check_same_thread=False)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop TEXT,
    date TEXT,
    activity TEXT,
    amount REAL,
    notes TEXT
)''')
conn.commit()

# Load crop growth data
@st.cache_data
def load_crop_data():
    # Use a relative path to load the dataset from the 'other files' folder.
    df = pd.read_excel("other files/Crop_Dataset.xlsx")
    df = df.dropna(subset=["Crop"])
    df.fillna(0, inplace=True)
    return df

crop_df = load_crop_data()
STAGES = crop_df.columns[1:-1].tolist()  # All stages excluding 'Crop' and 'Total Life Cycle'

# Define Tabs
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Expense", "📋 View Expenses", "📊 Summary", "📈 Crop Timeline"])

# ---------------- Tab 1: Add Expense ----------------
with tab1:
    if 'primary_activity' not in st.session_state:
        st.session_state.primary_activity = list(ACTIVITY_CATEGORIES.keys())[0]

    crop = st.selectbox("Crop Name", options=CROPS)
    exp_date = st.date_input("Date", value=date.today())

    col1, col2 = st.columns(2)
    primary_activity = col1.selectbox("Activity Category", options=list(ACTIVITY_CATEGORIES.keys()), key='primary_activity')
    secondary_activity = col2.selectbox("Activity", options=ACTIVITY_CATEGORIES[st.session_state.primary_activity], key='secondary_activity')

    with st.form("expense_form"):
        amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
        notes = st.text_area("Notes (optional)")
        submitted = st.form_submit_button("Save")

        if submitted:
            c.execute("INSERT INTO expenses (crop, date, activity, amount, notes) VALUES (?, ?, ?, ?, ?)",
                      (crop, exp_date.strftime("%Y-%m-%d"), secondary_activity, amount, notes))
            conn.commit()
            st.success("Expense saved!")

# ---------------- Tab 2: View Expenses ----------------
with tab2:
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = c.fetchall()
    if rows:
        for row in rows:
            col1, col2 = st.columns([3, 1])
            col1.write(f" {row[2]} - **{row[1]}** - ₹{row[4]} ({row[3]})")
            if col2.button("Delete", key=row[0]):
                c.execute("DELETE FROM expenses WHERE id = ?", (row[0],))
                conn.commit()
                st.experimental_rerun()
            if row[5]:
                st.caption(row[5])
            st.markdown("---")
    else:
        st.info("No expenses logged yet.")

# ---------------- Tab 3: Summary ----------------
with tab3:
    c.execute("SELECT crop, SUM(amount) FROM expenses GROUP BY crop")
    data = c.fetchall()
    if data:
        st.subheader("💰 Total Expense per Crop")
        for row in data:
            st.write(f"**{row[0]}**: ₹{row[1]:,.2f}")
    else:
        st.info("Nothing to summarize yet.")

# ---------------- Tab 4: Crop Growth Timeline Calculator ----------------
with tab4:
    st.subheader("📈 Crop Growth Timeline Calculator")

    crop_list = crop_df["Crop"].tolist()
    crop_selected = st.selectbox("Select Crop", options=crop_list)
    stage_selected = st.selectbox("Select Current Stage", options=STAGES)
    stage_date = st.date_input("Date Crop Entered This Stage", value=date.today())

if st.button("Generate Timeline"):
    row = crop_df[crop_df["Crop"] == crop_selected]
    if row.empty:
        st.error("No data found for the selected crop.")
    else:
        # Read durations from all stage columns (as integers)
        durations = row.iloc[0, 1:-1].astype(int).tolist()
        stage_index = STAGES.index(stage_selected)
        
        # Check for invalid consecutive 0-day stages in the upcoming durations.
        # We check from stage_index+1 onward because the duration to be added starts from the next stage.
        for i in range(stage_index + 1, len(durations) - 1):
            if durations[i] == 0 and durations[i + 1] == 0:
                st.warning("⚠️ Data unavailable for this crop due to zero duration between stages.")
                break
        else:
            timeline = []
            current_date = stage_date

            # Add current stage without any time addition
            timeline.append((STAGES[stage_index], current_date))

            # For each subsequent stage, add the duration given in the next stage column.
            # E.g., if 'Sowing / Transplanting' is selected then the time to reach 'Germination / Emergence'
            # will be determined by durations[stage_index+1] (e.g., 6 days)
            for i in range(stage_index + 1, len(STAGES)):
                current_date += pd.Timedelta(days=durations[i])
                timeline.append((STAGES[i], current_date))

            st.success(f"Timeline starting from '{stage_selected}' on {stage_date.strftime('%d %b %Y')} for **{crop_selected}**:")
            for stage_name, date_estimate in timeline:
                st.write(f"➡️ **{stage_name}**: `{date_estimate.strftime('%d %b %Y')}`")
