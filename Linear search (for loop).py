def LinearSearch(lst, trgt):
  Found = False
  for i in range(len(lst)):
    if lst[i] == trgt:
      print("Found")
      Found = True
      break
  if Found != True:
    print("Not found")
lst = ["cat", "dog", "python"]
trgt = "cat"
LinearSearch(lst, trgt)