def setupPycharmDebug(inputFile, outputFile):
  """
  redirect input stream to input file for PyCharm debug ref. https://stackoverflow.com/a/39482389/248616
  redirect output stream to output file for PyCharm debug ref https://stackoverflow.com/a/4675744/248616
  """

  import sys
  import StringIO

  #input
  lines = "".join(open(inputFile, "r").readlines())
  sys.stdin = StringIO.StringIO(lines)

  #output
  sys.stdout = open(outputFile, 'w')
