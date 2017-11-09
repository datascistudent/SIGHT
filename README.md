# SIGHT
Smart and Interactive Glossary-based Helper Tool

### Usage (from Python Shell)

```
python <project-path>/SIGHT.py <project-path>/image/N.png <project-path>/data/SIGHT_KnowledgeBase.txt
```

### Usage (Automated)

```bash
sh SIGHT_daemon.sh project-path
```

*Some pre-requisites (using bash method):*
* The image of the screen shot should be stored as .png (under `<project-path>/image/`)
* The screen shot images to get placed in folder that has to be polled (passed to the bash script) by default 

**Please Note**: 
* Keyboard Interrupt is needed to kill the bash job
* Manual cleanup is needed for the images used (under `<project-path>/image/`)

#### Packages Required

```
brew install opencv
brew install imagemagick
pip install pillow
pip install pytesseract
pip install tesseract
pip install opencv-python
pip install tesseract-ocr
pip install matplotlib
pip install pyscreenshot
pip install pymouse
```