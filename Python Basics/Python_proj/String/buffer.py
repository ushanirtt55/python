import StringIO

out=StringIO.StringIO()
out.write('Hello welcome,')
print >>out, 'to python tutorial'
content=out.getvalue()
print content
print out
out.close()