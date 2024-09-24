import os

import numpy as np

from pylatex import (
    Alignat,
    #Axis,
    Command,
    Description,
    Document,
    Figure,
    Math,
    Matrix,
    Package,
    #Plot,
    Section,
    Subsection,
    Tabular,
    #TikZ,
)

from pylatex.utils import NoEscape


class LaTeX(Document):
	def __init__(self, title):
		super().__init__()
		self.packages.append(Package('amsmath'))
		self.packages.append(Package('amssymb'))

		self.preamble.append(Command("title", title))
		self.append(NoEscape(r"\maketitle"))
		
	def fill(self, history, data=0):
		with self.create(Section("Elenco transizioni")):
			with self.create(Description()) as desc:
				for row in history:
					desc.add_item(NoEscape(r"$\Uparrow$"), row)

	def compile(self):
		self.generate_pdf("full", clean_tex=False)
		os.system(r"pdflatex full.tex") 




















