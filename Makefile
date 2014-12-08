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
	cp ~/Downloads/bibtex/theoreticalbiology.bib bib/papers.bib
	cp ~/Downloads/bibtex/books.bib bib/
	python bib/remove_url.py bib/papers.bib
	python bib/remove_url.py bib/books.bib

copydownloadsbib:
	cp ~/Downloads/bibtex/theoreticalbiology.bib ~/Downloads/bib/papers.bib
	cp ~/Downloads/bibtex/books.bib ~/Downloads/bib/
	python ~/Downloads/bib/remove_url.py ~/Downloads/bib/papers.bib
	python ~/Downloads/bib/remove_url.py ~/Downloads/bib/books.bib

linkbib:
	ln -s ~/Downloads/bib bib

dropbox:
	mkdir -p ~/Dropbox/sharelatex/sep2/tex
	mkdir -p ~/Dropbox/sharelatex/sep2/fig
	mkdir -p ~/Dropbox/sharelatex/sep2/bib
	cp plos_template.tex ~/Dropbox/sharelatex/sep2
	cp *header.tex ~/Dropbox/sharelatex/sep2
	cp *.bst ~/Dropbox/sharelatex/sep2
	cp tex/* ~/Dropbox/sharelatex/sep2/tex
	cp fig/*.pdf ~/Dropbox/sharelatex/sep2/fig
	cp bib/*.bib ~/Dropbox/sharelatex/sep2/bib

arxiv:
	latexpand plos_template.tex > combined.tex
	sed -i 's/\\makeatletter{}//g' combined.tex
	tar --transform='flags=r;s|combined|paper|' --transform='flags=r;s|plos_template|paper|' -cvzf arxiv`date +"%m%d%Y"`.tar.gz combined.tex plos_template.bbl fig/*.pdf

$(BIBFILES):
	copybib

$(TEMPLATE):
	echo $(TEMPLATE)

$(TOPPDFFILE): $(TOPTEX) $(BIBFILES) $(TEMPLATE)
	if which latexmk > /dev/null 2>&1 ;\
	then latexmk -pdf $<;\
	else echo "Install latexmk"; fi

clean:
	rm -f *.aux *.bbl *.blg *.brf *.dvi *.fdb_latexmk *.fls *.lof *.log \
	      *.lot *.nav *.out *.pre *.snm *.synctex.gz *.toc

cleanall: clean
	rm -f $(TOPPDFFILE)

test:
	echo $(TOPPDFFILE)

#---------------------------------------------
