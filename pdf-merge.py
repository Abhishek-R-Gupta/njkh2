import pikepdf

def merge_pdfs(output_path, input_paths):
    pdf = pikepdf.Pdf.new()

    for path in input_paths:
        with pikepdf.open(path) as src:
            pdf.pages.extend(src.pages)

    pdf.save(output_path)
    pdf.close()


if __name__ == "__main__":
    input_files = [
        r"C:\Users\Abhishek\Downloads\PDF_collection\pdf1.pdf",
        r"C:\Users\Abhishek\Downloads\PDF_collection\pdf2.pdf",
        r"C:\Users\Abhishek\Downloads\PDF_collection\pdf3.pdf"
    ]

    merge_pdfs("merged_output.pdf", input_files)
