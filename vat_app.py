import streamlit as st

# ตั้งค่าหน้าเว็บ (แสดง Icon และ Title บน Tab เบราว์เซอร์)
st.set_page_config(page_title="คำนวณ VAT 7%", page_icon="🛒")

# แสดงชื่อแอปพลิเคชั่น
st.title("🛒 แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

# สร้างช่องรับข้อมูลตัวเลขราคา
price = st.number_input("💵 กรอกราคาสินค้า (บาท):", value=0.0, step=1.0)

# ตัวแปร vat คำนวณ 7%
vat = price * 0.07

# ตัวแปร net_price คำนวณราคา - vat
net_price = price - vat

st.caption(f"ราคาตั้งต้น (รวม VAT): {price:,.2f} บาท")

# จัดเลย์เอาต์การแสดงผลเป็น 2 คอลัมน์ให้ดูสวยงาม
col1, col2 = st.columns(2)

with col1:
    # แสดงจำนวน Vat
    st.metric(label="📊 ภาษีมูลค่าเพิ่ม (VAT 7%)", value=f"{vat:,.2f} บาท")

with col2:
    # แสดงราคาสุทธิ
    st.metric(label="🏷️ ราคาสินค้าก่อน VAT", value=f"{net_price:,.2f} บาท")

# สร้างเส้นกั้น
st.divider()

# แสดงข้อมูลนักเรียน
st.success("👨‍🎓 **ผู้จัดทำ:** จารุภัทร อรุณสิทธิ์ เลขที่ 9 ม.4/6")
