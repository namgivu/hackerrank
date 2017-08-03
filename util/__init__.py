INPUT_FILE='input.txt'
OUTPUT_FILE='output.txt'


def flushOutput():
  """
  you may need to re-sync the selected output file in PyCharm - as NN setting, ctrl-shift-` will do
  write/flush immediately ref. https://stackoverflow.com/a/230774/248616
  """
  import sys
  sys.stdout.flush()


def setupPycharmDebug(inputFile=INPUT_FILE, outputFile=OUTPUT_FILE):
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
  sys.stdout = open(outputFile, mode='w', buffering=0)
