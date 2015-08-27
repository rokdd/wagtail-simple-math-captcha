import pandoc
import os

pandoc.core.PANDOC_PATH = r'C:\Program Files (x86)\Pandoc\pandoc.exe'

doc = pandoc.Document()
doc.markdown = open('README.md').read()
f = open('README.txt','w+')
f.write(doc.rst)
f.close()
#os.system("setup.py register -r pypitest")
#os.system("setup.py sdist upload -r pypitest")
os.system("setup.py register -r pypi")
#os.system("setup.py sdist upload -r pypi")
os.remove('README.txt')