#! /usr/bin/python

import os
import pdfrw

INVOICE_TEMPLATE_PATH = 'pdfform.pdf'
INVOICE_OUTPUT_PATH = 'fillform.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY='/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_kEY='/Widget'

def write_fillable_pdf(input_pdf_path,output_pdf_path,data_dict):
    template_pdf=pdfrw.PdfReader(input_pdf_path)
    annotations=template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY]==WIDGET_SUBTYPE_kEY:
            key=annotation[ANNOT_FIELD_KEY][1:-1]
            if key in data_dict.keys():
                annotation.update(
                    pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                )

    pdfrw.PdfWriter().write(output_pdf_path,template_pdf)


data_dict={
    'name':'齋藤さん',
    'gender':'男'
}

if __name__ == '__main__':
    write_fillable_pdf(INVOICE_TEMPLATE_PATH,INVOICE_OUTPUT_PATH,data_dict)