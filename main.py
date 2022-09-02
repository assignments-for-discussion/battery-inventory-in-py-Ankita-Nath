
def count_batteries_by_usage(cycles):
  d = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for i in cycles:
    if i < 400:
      d['lowCount'] += 1
    elif i >= 400 and i <= 919:
      d['mediumCount'] += 1
    else:
      d['highCount'] += 1
  return d



def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
