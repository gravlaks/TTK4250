# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:47:25 2020

@author: torstein
"""
from fpdf import FPDF


ifiles = ["ekf.py", "runekf.py", "measurmentmodels.py", "dynamicmodels.py"]
outfiles = [filename.replace(".py", ".pdf") for filename in ifiles]

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
with open("ekf.py", 'r') as f:
    text = f.read()
    pdf.cell( txt=text, align="C")
pdf.output("ekf.pdf")