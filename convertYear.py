Python
import streamlit as st

# 1. ตั้งค่าไอคอนและชื่อแท็บของเว็บไซต์บนเบราว์เซอร์
st.set_page_config(
    page_title="โปรแกรมคำนวณปีศักราชอัตโนมัติ",
    page_icon="📅",
    layout="centered"
)

# 2. ปรับแต่งความสวยงามของหน้าเว็บด้วย Custom CSS (แต่งสี, ขอบมน และใส่เงา)
custom_css = """
<style>
/* ตกแต่งการ์ดหัวข้อด้านบน */
.header-card {
    background: linear-gradient(135deg, #1d976c 0%, #93f9b9 100%);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 35px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}
.header-card h1 {
    color: white !important;
    font-size: 2.2rem !important;
    margin: 0;
    font-weight: bold;
}
.header-card p {
    color: #f0fff4 !important;
    margin-top: 10px;
    font-size: 1.1rem;
}

/* ตกแต่งการ์ดแสดงผลลัพธ์ */
.result-box-green {
    background-color: #f0fdf4;
    border-left: 6px solid #16a34a;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.result-box-blue {
    background-color: #eff6ff;
    border-left: 6px solid #2563eb;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.result-title {
    font-weight: bold;
    font-size: 1rem;
    margin-bottom: 5px;
    color: #374151;
}
.result-value {
    font-size: 1.8rem;
    font-weight: bold;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. แสดงแบนเนอร์หัวข้อที่ได้รับการตกแต่งสีสันแล้ว
st.markdown(
    """
    <div class="header-card">
        <h1>📅 ระบบคำนวณและแปลงปีศักราช</h1>
        <p>เครื่องมืออำนวยความสะดวกในการแปลงปี พ.ศ. และ ค.ศ. แบบทันใจ</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 4. สร้างการจัดวางแบบ 2 คอลัมน์ (ซ้ายแปลง พ.ศ. เป็น ค.ศ. / ขวาแปลง ค.ศ. เป็น พ.ศ.)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟢 แปลง พ.ศ. เป็น ค.ศ.")
    # รับค่าปี พ.ศ.
    bh_year = st.number_input("กรอกปี พ.ศ. ที่ต้องการ:", value=2569, min_value=1, step=1, key="bh_to_ce")
    ce_result = bh_year - 543
    
    # แสดงการ์ดผลลัพธ์สีเขียว
    st.markdown(
        f"""
        <div class="result-box-green">
            <div class="result-title">ผลลัพธ์การคำนวณ</div>
            <div class="result-value" style="color: #166534;">ค.ศ. {ce_result}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.subheader("🔵 แปลง ค.ศ. เป็น พ.ศ.")
    # รับค่าปี ค.ศ.
    ce_year = st.number_input("กรอกปี ค.ศ. ที่ต้องการ:", value=2026, min_value=1, step=1, key="ce_to_bh")
    bh_result = ce_year + 543
    
    # แสดงการ์ดผลลัพธ์สีน้ำเงิน
    st.markdown(
        f"""
        <div class="result-box-blue">
            <div class="result-title">ผลลัพธ์การคำนวณ</div>
            <div class="result-value" style="color: #1e40af;">พ.ศ. {bh_result}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
