Fill PDF From by Python
-----------------------
PythonでPDFフォームにデータを埋め込みたい。
[このサイト](https://bostata.com/post/how_to_populate_fillable_pdfs_with_python/)のサンプルがクールに思えた。
だから、試してみた。

## 環境
僕の環境は下記の通り
多分、LinuxやmacOSでも上手く動くと思う。

- Windows10
- Python3.5.5 64bit (include LibreOffice)
- pdfrw

### Sample PDF
Sample PDFはLibreOffice Drawで作った。
[invoice_template](https://bostata.com/download/post/fillable_pdf/invoice_template.pdf)は上手くいかなかった。
データがフォームに埋め込まれている。
テキストボックスの名前の表示が邪魔してデータが埋め込まれた状態では印字されない。


## 参考文献
[How to Populate Fillable PDF's with Python](https://bostata.com/post/how_to_populate_fillable_pdfs_with_python/)