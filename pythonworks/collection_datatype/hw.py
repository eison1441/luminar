text="ABBACB"
repeart={}
for ch in text:
    if ch in repeart:
      print(f"the recursive character is",{ch})
      break
    else:
        repeart[ch]=1


