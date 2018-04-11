# irene
## Interactive Recognition and Extraction of kNowledge and Entities

A spaCy-based system for populating relational tables using unstructured text. The user helps bootstrap the reader into extracting information efficiently.

Inspired by [IKE](https://github.com/allenai/ike), developed by the Allen Institute for Artificial Intelligence.

Setup:
Have python3. Irene is built on top of python3.
> pip install virtualenv
> virtualenv -p python3 __name_of_env__		# Create the python3 virtual environment
> source . __name_of_env__/bin/activate			# Activate the virtual environment
> pip install spacy							# Install spaCy
> spacy download en						# Download necessary modules for spaCy