import fitz
import os

FILE_PATH = "C:/Users/tydav/OneDrive - weber.edu/Documents/Random School Stuff/23-24 Schoolyear/Fall2023/ECE 3110/Microelectronic Circuits (6th edition) by Sedra and Smith LICA2.pdf"
OUTPUT_PATH = "./pdf_sections/"


def main():
    doc = fitz.open(FILE_PATH)
    toc_lvl2 = [x for x in doc.get_toc() if x[0] <= 2]
    mapping = str.maketrans('\r', ' ')
    for i in range(len(toc_lvl2)):
        new_doc = fitz.Document()
        print(i, len(toc_lvl2) - 1)
        if i == 0:
            page1 = 0
            page2 = toc_lvl2[i+1][2]
        elif i < len(toc_lvl2) - 1:
            page1 = toc_lvl2[i][2]
            page2 = toc_lvl2[i+1][2]
        else:
            page1 = toc_lvl2[i][2]
            page2 = doc.page_count
        new_doc.insert_pdf(doc, page1 - 1, page2 - 2)

        title = toc_lvl2[i][1].translate(mapping)
        print(title)
        output_filename = os.path.join(OUTPUT_PATH, title + '.pdf')
        print(output_filename)
        new_doc.save(output_filename)

        # get_doc_segment(doc, item[2], item[2] + 2, 'title')
        # if 'e' in input(""):
        #     exit()
        # print(item)

def get_doc_segment(document: fitz.Document, page1, page2, sec_title):
    pages = document.pages(page1, page2)
    new_doc = fitz.Document()
    for page in pages:
        new_doc.add_page
    print(pages, len(pages))
    # doc.save(os.path.join(OUTPUT_PATH, sec_title))



if __name__ == '__main__':
    main()
