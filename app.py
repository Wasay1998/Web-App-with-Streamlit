import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the app layout
st.set_page_config(page_title="🧹 Data Sweeper", layout='wide')

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5968/5968350.png", width=80)
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Upload & Transform", "About"])

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by **Abdul Wasay**")


# Home Page
if page == "Home":
    st.title("🧹 Data Sweeper - Sterling Integrator By Abdul Wasay")
    st.write("### 🚀 The Ultimate Data Cleaning & Transformation Tool")
    st.write("Easily clean, transform, and convert your CSV & Excel files with just a few clicks!")
   
    
    st.markdown("## 🌟 Features:")
    st.markdown("- 📂 Upload multiple CSV & Excel files")
    st.markdown("- 🛠️ Remove duplicates & fill missing values intelligently")
    st.markdown("- 📊 Select columns, filter data, & visualize insights")
    st.markdown("- 🔄 Convert files between CSV & Excel formats seamlessly")
    st.markdown("- ⬇️ Download processed files instantly")
    
    st.success("🚀 Transform your data like a pro!")

# Upload & Transform Page
elif page == "Upload & Transform":
    st.title("📂 Upload & Transform Data")
    st.write("✨ Upload your CSV or Excel files and start transforming them with ease!")
    
    uploaded_files = st.file_uploader("Upload files", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            
            # Read file
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue
            
            st.subheader(f"📄 File: {file.name}")
            st.write(f"📏 File Size: {file.size / 1024:.2f} KB")
            st.dataframe(df.head())
            
            # Data Cleaning Options
            with st.expander("🛠️ Data Cleaning Options"):
                if st.button(f"🚮 Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed successfully!")
                
                if st.button(f"🩹 Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")
            
            # Column Selection
            with st.expander("📊 Select Columns"):
                selected_columns = st.multiselect("Select columns to keep", df.columns, default=df.columns)
                df = df[selected_columns]
            
            # Data Visualization
            with st.expander("📈 Data Visualization"):
                if st.checkbox("Show Bar Chart"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
            
            # Conversion Options
            with st.expander("🔄 Convert File"):
                conversion_type = st.radio("Convert to:", ["CSV", "Excel"], key=file.name)
                buffer = BytesIO()
                file_name = file.name.replace(file_ext, f".{conversion_type.lower()}")
                mime_type = "text/csv" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                
                if st.button(f"🔄 Convert {file.name}"):
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)
                    else:
                        df.to_excel(buffer, index=False)
                    buffer.seek(0)
                    
                    st.download_button(
                        label=f"⬇️ Download {file.name} as {conversion_type}",
                        data=buffer,
                        file_name=file_name,
                        mime=mime_type
                    )

    st.success("🎉 All files processed successfully! 🚀")

# About Page
elif page == "About":
    st.title("ℹ️ About Data Sweeper")
    st.write("### 🚀 The Most Advanced Data Cleaning & Transformation Tool")
    st.write("Data Sweeper helps you clean, transform, and convert your data seamlessly.")
    st.markdown("## 🔥 Why Choose Data Sweeper?")
    st.markdown("- 🚀 **Super Fast Processing** - Handles large datasets with ease")
    st.markdown("- 🛠️ **Advanced Cleaning Features** - Automatically fills missing values & removes duplicates")
    st.markdown("- 📊 **Data Visualization** - Quickly analyze trends in your data")
    st.markdown("- 🔄 **Multiple File Formats** - Convert between CSV & Excel effortlessly")
    st.markdown("- 🎯 **User-Friendly Interface** - Designed for both beginners & professionals")
    
    
    st.success("💡 Take control of your data like a pro!")