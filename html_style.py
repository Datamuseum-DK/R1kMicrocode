'''
   HTML boiler plates
'''

import platform

HTML_STYLE = '''
 <style>
      body { font-family: "Inconsolata", "Courier New", mono-space; }
      table { border-collapse: collapse; }
      table.border { border: 1px solid black; }
      th {
        border-right: 1px solid black;
        text-align: left;
      }
      tr.top { border-top: 1px solid black; }
      tr.trshade1 { background-color: #eeeeee; }
      td {
        border-right: 1px solid black;
        text-align: right;
      }
      td.left { text-align: left; }
      td.white { background-color: #ffffff; }
      td.OK { background-color: #99ff99; }
 </style>
'''

HTML_HEAD = '''<!DOCTYPE html>
<html>
<head>
<title>R1k Ucode</title>
''' + HTML_STYLE + '''
</head>
<body>
'''

HTML_TAIL = '''
</body>
</html>
'''

if platform.node() == 'critter.freebsd.dk':
    HTML_DIR = "/critter/R1kUcode"
elif platform.node() == 'static.ddhf.dk':
    HTML_DIR = "/usr/local/www/thttpd/aa/R1kMicrocode"
else:
    raise Exception("You need to set HTML_DIR in html_style.py")
