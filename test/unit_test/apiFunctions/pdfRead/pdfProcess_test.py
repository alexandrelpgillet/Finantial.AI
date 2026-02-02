from api.pdfRead import pdf_Process


def test_pdf_Process():
    
    with open("test/unit_test/apiFunctions/pdfRead/pdfRead_test_case/example.pdf","rb") as archive:
        
        test_pdf = archive.read()
        
    test_output = pdf_Process(test_pdf)
    
    with open("test/unit_test/apiFunctions/pdfRead/pdfRead_test_case/output.txt", "r" , encoding="utf-8") as archive:
        
        valid_input = archive.read()
        
    assert test_output.strip() == valid_input.strip()         