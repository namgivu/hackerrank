INPUT_FILE  = 'input.txt'
OUTPUT_FILE = 'output.txt'


def flushOutput():
  """
  you may need to re-sync the selected output file in PyCharm - as NN setting, ctrl-shift-` will do
  write/flush immediately ref. https://stackoverflow.com/a/230774/248616
  """
  import sys
  sys.stdout.flush()


def redirectStdio2File(inputFile=INPUT_FILE, outputFile=OUTPUT_FILE):
  """
  redirect input stream to input file for PyCharm debug ref. https://stackoverflow.com/a/39482389/248616
  redirect output stream to output file for PyCharm debug ref https://stackoverflow.com/a/4675744/248616
  """

  import sys
  from io import StringIO

  #redirect stdin to file
  lines = "".join(open(inputFile, "r").readlines())
  sys.stdin = StringIO(lines)

  #redirect stdout to file
  sys.stdout = open(outputFile, mode='w')


def sortDictArray(objArray, keyLambda):
  #ref. https://stackoverflow.com/a/73050/248616
  sortedArr = sorted(objArray, key=keyLambda)
  return sortedArr

  #testing
  # a = [
  #   dict(index=1, value=1),
  #   dict(index=0, value=333),
  #   dict(index=2, value=22),
  # ]
  #
  # print(sortDictArray(a, keyLambda=lambda k: k['value']))
  # print(sortDictArray(a, keyLambda=lambda k: k['index']))
