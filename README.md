# pywork
python mini code pushing forward efficient working.

---

**batch_prefix** Used for batch adding prefix to prevent problems checking file or somehow else.

**copy2root** Alone copy all files to root path, and with **split_folder** you can resend it (specific file format) to separate directory it generated. *It's cool,* and kinda like what an *apt* or *pip* mirror do.

**office2pdf** Literally convert common office document to pdf (*traversely*, walk into every subdirs, which is pretty convenient). Basically depending on *win32com* - which means if you want to go outside Windows (*which is next to impossible*), you have to implement Windows's COM interface.

**pdf_merge** Merge pdf files existing in *root* directory. Personally, I use it for merging (putting together) pdfs and split it with some reasonable blocks of pages (see **pdf_split**), used for LLM's knowledge base. Again it use "win32com" which is Windows-based, and also you need an *Acrobat*.

**pdf_split** Split PDF files (Specific name). Use "win32com" and Acrobat.

**random_name** Use UUID to give each file an unique name (*traversely*).For me, I use it for processing photo stocks to avoid repeated name.

**unzip_uniquify_name** A shell covering **random_name** to conveniently processing zip file photo stocks, free from changing names or running python code (At least reduce the frequency).

---

You are welcome to commit changes, for open-source and cross-platform manipulator of MSOffice documents and Acrobat PDFs.
