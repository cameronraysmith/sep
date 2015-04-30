.PHONY: default copybib copydownloadsbib linkbib dropbox arxiv thesis latexdiff clean cleanall test html htmlpandoc

#---------------------------------------------
# Define variables

# list of automatic variables
# http://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables

PROJECTNAME = sep2

TOPTEX = plos_template.tex

TOPPDFFILE = $(TOPTEX:.tex=.pdf)

TOPBBLFILE = $(TOPTEX:.tex=.bbl)

BIBFILES = bib/books.bib \
	   bib/papers.bib

TEMPLATE = plost2009.bst

FIGFILES = $(shell grep -v '^%' tex/*.tex | grep -ohP 'fig/.*(?=\})')

TEXFILES = $(shell ls tex/*.tex)

PREVIOUSCOMMIT = 71cea94

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
	mkdir -p ~/Dropbox/sharelatex/$(PROJECTNAME)/tex
	mkdir -p ~/Dropbox/sharelatex/$(PROJECTNAME)/fig
	mkdir -p ~/Dropbox/sharelatex/$(PROJECTNAME)/bib
	cp $(TOPTEX) ~/Dropbox/sharelatex/$(PROJECTNAME)
	cp *header.tex ~/Dropbox/sharelatex/$(PROJECTNAME)
	cp *.bst ~/Dropbox/sharelatex/$(PROJECTNAME)
	cp $(TEXFILES) ~/Dropbox/sharelatex/$(PROJECTNAME)/tex
	cp $(FIGFILES) ~/Dropbox/sharelatex/$(PROJECTNAME)/fig
	cp bib/*.bib ~/Dropbox/sharelatex/$(PROJECTNAME)/bib

arxiv:
	latexpand $(TOPTEX) > combined.tex
	sed -i 's/\\makeatletter{}//g' combined.tex
	cp $(TOPBBLFILE) combined.bbl
	tar --transform='flags=r;s|combined|paper|' -cvzf arxiv`date +"%m%d%Y"`.tar.gz combined.tex combined.bbl $(FIGFILES)

thesis:
	latexpand $(TOPTEX) > $(PROJECTNAME).tex
	sed -i 's/\\makeatletter{}//g' $(PROJECTNAME).tex
	cp $(FIGFILES) ~/projects/thesis/classicthesis/fig

# run as make latexdiff PREVIOUSCOMMIT="commit-hash"
# to diff with a different commit
latexdiff:
	git-latexdiff --ignore-latex-errors --latexmk --ignore-makefile --ln-untracked --main $(TOPTEX) $(PREVIOUSCOMMIT) HEAD

# TODO: automatically comment hypersetup colorlinks in header texfile
html: $(TOPPDFFILE)
	mkdir -p html
	mkdir -p html/fig
	htlatex $(TOPTEX) "html5mathjax,charset=utf-8,-css,3" " -cunihtf -utf8" "-dhtml/" "--interaction=nonstopmode"
	cp./html/$(TOPTEX:.tex=.html) ./html/index.html
	cp fig/*.png ./html/fig/

servehtml:
	cd html; sudo python -m SimpleHTTPServer 80; cd ../

htmlpandoc:
	pandoc -s -S --mathjax --toc -sw html5 --bibliography=bib/papers.bib --bibliography=bib/books.bib --csl=proceedings-of-the-royal-society-b.csl $(TOPTEX) -o $(TOPTEX:.tex=.html)

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
	      *.lot *.nav *.out *.pre *.snm *.synctex.gz *.toc *.html *.4ct \
	      *.4tc *.idv *.lg *.xref $(TOPTEX:.tex=.md) $(TOPTEX:.tex=.css) \
	      $(TOPTEX:.tex=.tmp) *.png

cleanall: clean
	rm -f $(TOPPDFFILE)

test:
	echo $(TOPPDFFILE)

#---------------------------------------------
