import sys
import collections
def findFrequentEntries(pairs):
  # Your code here. Writes to standard out.
  # Format for output lines: "Name: 1230 1240 1245"
  occur = collections.defaultdict(list)
  #pairs = sorted(pairs, key=lambda list: list[0])
  for l in pairs:
    occur[l[0]].append(int(l[1]))
  #occur = sorted(occur)
  badge = {}
  for k,v in occur.items():
    occur[k]=sorted(v)
  for k,v in occur.items():
    setofhr = []
    for i in v:
      new = [k for k in v if i<= k <= (i+100)]
      if len(new)>=3:
        setofhr.append(new)
    badge[k] = setofhr
  lb = []
  for k,v in badge.items():
    lb.append((k,v))
  lb.sort(key = lambda x:x[0])
  #print(lb)
  if len(lb)==1:
    for i in lb:
      if not i[1]:
        print(None)
      else:
        n = []
        for d in i[1][0]:
          n.append(d)
        print(str(i[0])+": " + ' '.join(map(str, n)))
  else:
    for i in lb:
      if not i[1]:
        continue
      else:
        n = []
        for d in i[1][0]:
          n.append(d)
        print(str(i[0])+": " + ' '.join(map(str, n)))

# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = [["pag", "1234"], ["gal", "845"], ["pag", "1156"], ["jan", "923"], ["pag", "1141"], ["gal", "922"], ["jan", "1001"], ["jan", "912"],["jan","1010"]]

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()
    pairs.append(line.split(" "))

  findFrequentEntries(pairs)

main()
