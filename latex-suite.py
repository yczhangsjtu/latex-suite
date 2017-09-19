#!/usr/bin/python

import sys

def itemize(argv):
	lines = sys.stdin.readlines()
	nonempty = False
	for line in lines:
		if line.strip() == "":
			continue
		nonempty = True
		indent = len(line)-len(line.lstrip())
		indentpart = line[:indent]
		break
	if not nonempty:
		return
	print "%s\\begin{itemize}"%indentpart
	for line in lines:
		if line.strip() == "":
			continue
		indent = len(line)-len(line.lstrip())
		print "%s\\item %s"%(line[:indent],line[indent:].strip())
	print "%s\\end{itemize}"%indentpart

def usage(progname):
	print "%s command options"%(progname)
	print
	print "command"
	print "  print a itemize environment, each nonempty line is prefixed with \\item"

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "itemize":
			itemize(sys.argv[1:])
		else:
			usage(sys.argv[0])
