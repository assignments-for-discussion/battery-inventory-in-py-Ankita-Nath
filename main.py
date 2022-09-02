
def count_batteries_by_usage(cycles):
  d = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for i in cycles:
    # iterating over values and incrementing in accordance to given condition using keys.
    if i < 400:                    
      d['lowCount'] += 1
    elif i >= 400 and i <= 919:
      d['mediumCount'] += 1
    else:
      d['highCount'] += 1
  return d



def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000, 400, 399, 919, 920])
  # extra test cases added
  assert(counts["lowCount"] == 3)
  assert(counts["mediumCount"] == 5)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
