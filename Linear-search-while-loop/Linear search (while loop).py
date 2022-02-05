def LinearSearch(lst, trgt):
  i = 0
  Found = False
  while i < len(lst):
    if lst[i] == trgt:
      print ("Found")
      Found = True
      break
    i = i + 1
  if Found != True:
    print("Not found")

lst = ["cat", "dog", "python"]
trgt = "mouse"
LinearSearch(lst, trgt)