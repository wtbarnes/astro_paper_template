OUTDIR='output'
STYLESHEETS='stylesheets'
PYTHON='python'
PAPER='../tex/paper.pdf'
PROJECT_CONFIG='../project_config.yml'

all: publish

publish: stylesheets paper
	$(PYTHON) build_page.py --config_file $(PROJECT_CONFIG)

paper: outdir
	cp $(PAPER) $(OUTDIR)/

stylesheets: outdir
	cp -r $(STYLESHEETS) $(OUTDIR)/

outdir:
		mkdir -p $(OUTDIR)

clean:
	echo "Cleaning up site..."
	rm -r $(OUTDIR)/*
