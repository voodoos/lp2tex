# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import sys
import re

with open(sys.argv[1], 'r') as theFile:
    lpCode = theFile.read()

print(lpCode)

# Regex for inference rules
infer_r = r"(.*?):-(.*?)\."
infer_s = r"\\infer{\g<1>}{\g<2>}"

# Regex for identifiers
ident_r = r"([a-z]\w*)"
ident_s = r"\\text{\g<1>}"

# Regex for idents
ident_r = r"(^|\n|\r|\t|\W)([a-z]\w*)"
ident_s = r"\g<1>\\texttt{\g<2>}"

# Regex for lone backaslahes
back_r = r"\\(?!texttt)"
back_s = r"\\backslash"

step1 = re.sub(
    ident_r, ident_s, lpCode, 0, re.MULTILINE)

step2 = re.sub(
    back_r, back_s, step1, 0, re.MULTILINE)

step3 = step2.replace(
    "=>", "\\Rightarrow").replace(r" ", "~")


# Moving to inference rules
result = re.sub(infer_r, infer_s, step3, 0, re.MULTILINE)

print(result)
