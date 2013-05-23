.PHONY: default copybib clean cleanall test

#---------------------------------------------
# Define variables

# list of automatic variables
# http://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables

TOPTEX = plos_template.tex

BIBFILES = bib/books.bib \
	   bib/papers.bib

TEMPLATE = plost2009.bst

FIGFILES =

TEXFILES =

TOPPDFFILE = $(TOPTEX:.tex=.pdf)

#---------------------------------------------
# Default target
# will run with
# >make
# alone

default: $(TOPPDFFILE)

#----------------------------------------------
# Additional targets

copybib:
	cp /home/cameron/Downloads/bibtex/theoreticalbiology.bib bib/papers.bib
	cp /home/cameron/Downloads/bibtex/books.bib bib/
	perl bib/remove_url.pl bib/papers.bib
	perl bib/remove_url.pl bib/books.bib

$(BIBFILES):
	copybib

$(TEMPLATE):
	echo $(TEMPLATE)

$(TOPPDFFILE): $(TOPTEX) $(BIBFILES) $(TEMPLATE)
	if which latexmk > /dev/null 2>&1 ;\
	then latexmk -pdf $<;\
	else echo "Install latexmk"; fi

clean:
	rm -f *.brf *.pre *.log *.aux *.dvi *.bbl *.snm *.toc *.synctex.gz \
	      *.blg *.fls *.nav *.out *.fdb_latexmk

cleanall: clean
	rm -f $(TOPPDFFILE)

test:
	echo $(TOPPDFFILE)

#---------------------------------------------
