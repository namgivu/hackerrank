def setupPycharmDebug(inputFile):
  """redirect input stream to input file for PyCharm debug"""
  import sys
  import StringIO
  input = "".join(open(inputFile, "r").readlines())
  sys.stdin = StringIO.StringIO(input)
