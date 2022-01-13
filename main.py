
def count_batteries_by_usage(cycles):
  l=0
  m=0
  h=0
  for item in count_batteries_by_usage:
    if item<400:
      l=l+1
    elif item>400 and item<919:
      m=m+1
    else:
      h=h+1
    return {"lowCount":l,"mediumCount":m,"highCount":h}
      
      
      
      
     

 
  
 
    
  



def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
