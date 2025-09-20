import io
import pandas as pd
import streamlit as st

def main():
    st.title("File Conversor")

    option = st.selectbox("Choose the conversion", ["Parquet to CSV", "CSV to Parquet"])

    uploaded_file = st.file_uploader("Upload your file", type=["parquet", "csv"])

    if uploaded_file is not None:
        try:
            if option == "Parquet to CSV":
                df = pd.read_parquet(io.BytesIO(uploaded_file.getvalue()))

                st.write("DataFrame preview")
                st.dataframe(df.head())

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='converted_file.csv',
                    mime='text/csv',
                )

            elif option == "CSV to Parquet":
                df = pd.read_csv(io.StringIO(uploaded_file.getvalue().decode('utf-8')))

                st.write("DataFrame preview")
                st.dataframe(df.head())

                buffer = io.BytesIO()
                df.to_parquet(buffer, index=False)
                buffer.seek(0)
                
                st.download_button(
                    label="Download Parquet",
                    data=buffer,
                    file_name='converted_file.parquet',
                    mime='application/octet-stream',
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload a file to convert.")

if __name__ == "__main__":
    main()

            


    
 
