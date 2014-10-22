from decimal import *
getcontext().prec = 2

##Get the last line of the current working file
currentfile = open('/root/build.sh.out')
for line in currentfile:
	matchline = line

match  = matchline[-30:]


##Start counting the lines in de reference file
#Use this line for 1.9.8
reference = open('/root/reference-PhantomJS1-9.out')
#Use this line for 2
#reference = open('/root/reference-PhantomJS2.out')
counter = 0

for line in reference:
	counter +=1

total = counter

##Find a match
counter = 0
#Use this line for 1.9.8
reference = open('/root/reference-PhantomJS1-9.out')
#Use this line for 2
#reference = open('/root/reference-PhantomJS2.out')
for line in reference:
	counter += 1
	if match in line:
		result = Decimal(counter) / Decimal(total)
		progress = 100 * result
		progress = str(progress) + "%"
		print progress