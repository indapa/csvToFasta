import streamlit as st
import pandas as pd

def convert_to_fasta(df):
    fasta_lines = []
    for _, row in df.iterrows():
        header = f">{row['ID']}\n"
        sequence = f"{row['Sequence']}\n"
        fasta_lines.append(header + sequence)
    return "".join(fasta_lines)

def main():
    st.title("CSV to FASTA converter")

    # Upload CSV file
    st.header("Upload CSV File")
    st.write("CSV must have columns 'ID' and 'Sequence'")
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file is not None:
        # Read CSV file
        df = pd.read_csv(csv_file)

        # Display the CSV file contents
        st.subheader("CSV File Contents")
        st.write(df)

        # Convert to FASTA
        st.subheader("FASTA Format")
        st.write("Paste output from by mousing over upper right corner of results")
        fasta_output = convert_to_fasta(df)
        st.code(fasta_output, language="plaintext")

if __name__ == "__main__":
    main()
