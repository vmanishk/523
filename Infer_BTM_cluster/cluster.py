fp = open("k16.pz_d")
all_lines = fp.readlines()

k = 16

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
#list17 = []

count = 1

for line in all_lines:
  number = line.split(" ")
  cluster_no = number.index(max(number)) + 1
  if cluster_no == 1:
    list1.append(count)
  if cluster_no == 2:
    list2.append(count)
  if cluster_no == 3:
    list3.append(count)
  if cluster_no == 4:
    list4.append(count)
  if cluster_no == 5:
    list5.append(count)
  if cluster_no == 6:
    list6.append(count)
  if cluster_no == 7:
    list7.append(count)
  if cluster_no == 8:
    list8.append(count)
  if cluster_no == 9:
    list9.append(count)
  if cluster_no == 10:
    list10.append(count)
  if cluster_no == 11:
    list11.append(count)
  if cluster_no == 12:
    list12.append(count)
  if cluster_no == 13:
    list13.append(count)
  if cluster_no == 14:
    list14.append(count)
  if cluster_no == 15:
    list15.append(count)
  if cluster_no == 16:
    list16.append(count)
  # if cluster_no == 17:
  #   list17.append(count)

  count+=1

print count

print "list {} & len {}".format(list1[0:15], len(list1))
print "list {} & len {}".format(list2[0:15], len(list2))

print "list {} & len {}".format(list3[0:15], len(list3))

print "list {} & len {}".format(list4[0:15], len(list4))

print "list {} & len {}".format(list5[0:15], len(list5))

print "list {} & len {}".format(list6[0:15], len(list6))

print "list {} & len {}".format(list7[0:15], len(list7))

print "list {} & len {}".format(list8[0:15], len(list8))

print "list {} & len {}".format(list9[0:15], len(list9))

print "list {} & len {}".format(list10[0:15], len(list10))

print "list {} & len {}".format(list11[0:15], len(list11))

print "list {} & len {}".format(list12[0:15], len(list12))

print "list {} & len {}".format(list13[0:15], len(list13))

print "list {} & len {}".format(list14[0:15], len(list14))

print "list {} & len {}".format(list15[0:15], len(list15))

print "list {} & len {}".format(list16[0:15], len(list16))

# print "list {} & len {}".format(list17[0:15], len(list17))





