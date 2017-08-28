clean:
	@echo "deleting all .pyc files"
	find . -name *.pyc -exec rm {} \;
help:
	@echo "	clean"
	@echo "		Remove python artifacts."
	@echo "	run"
	@echo "		Run the file parser on your local machine."

run:
	@echo "start to initialize the parser..."
	python -m main

.PHONY:clean help run

