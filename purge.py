#!/usr/bin/env python
# Author: Jarrett B. <sircuddles@icloud.com> Made with Slovene pride
# coding: utf-8

import pymysql.cursors
import sys
import re
import datetime

cnx = pymysql.connect(user='root', db='altislife')
cursor = cnx.cursor()
cursor1 = cnx.cursor()
olderthan = 30 # in days
deleted = []

cursor.execute("SELECT * FROM gangs")
for (gangs) in cursor:
    newDuplicates = []
    regex = re.compile(r'[\d]{17}')
    for i in list(set(regex.findall(str(gangs[3])))):
        newDuplicates.append('`' + i + '`')
    newMembers = '"[' + ','.join(newDuplicates) + ']"'
    cursor1.execute("UPDATE gangs SET members = %s WHERE id IN(%s)", (newMembers, str(gangs[0])))
cnx.commit()
print "Removed duplicates in gangs, continuing..."

cursor.execute("SELECT * FROM players WHERE last_seen < DATE_SUB(NOW(), INTERVAL %d DAY)" % (olderthan))
for (players) in cursor:
  now = datetime.datetime.now()
  f = open(now.strftime("%Y-%m-%d-%H:%M"), 'w')
  information = ""
  for i in range(0, 26):
      information = information + "-" + str(players[i])
  f.write(information)
  deleted.append(players[3])

if len(deleted) == 0:
    print "Nothing to delete, exiting..."
    sys.exit()
else:
    print "Deleting " + str(len(deleted)) + " Users from the Database..."
    cursor.execute("DELETE FROM players WHERE last_seen < DATE_SUB(NOW(), INTERVAL %d DAY)" % (olderthan))

cursor.execute("SELECT * FROM containers WHERE pid IN(%s)" % ', '.join(deleted))
cursor.execute("DELETE FROM containers WHERE pid IN(%s)" % ', '.join(deleted))

cursor.execute("SELECT * FROM houses WHERE pid IN(%s)" % ', '.join(deleted))
cursor.execute("DELETE FROM houses WHERE pid IN(%s)" % ', '.join(deleted))

cursor.execute("SELECT * FROM vehicles WHERE pid IN(%s)" % ', '.join(deleted))
cursor.execute("DELETE FROM vehicles WHERE pid IN(%s)" % ', '.join(deleted))

cursor.execute("SELECT * FROM wanted WHERE wantedID IN(%s)" % ', '.join(deleted))
cursor.execute("DELETE FROM wanted WHERE wantedID IN(%s)" % ', '.join(deleted))

cursor.execute("SELECT * FROM gangs")
for (gangs) in cursor:
  m = re.search('|'.join(deleted), str(gangs[3]))
  if m:
      newMembers = re.sub(',`'+ m.group(0) +'`|`'+ m.group(0) +'`,', '', gangs[3])
      oldMembers = gangs[3]
      if newMembers == oldMembers:
          cursor1.execute("DELETE FROM gangs WHERE id = %s", (str(gangs[0])))
      else:
          cursor1.execute("UPDATE gangs SET members = %s WHERE id IN(%s)", (newMembers, str(gangs[0])))
  cnx.commit()

cursor.close()
cnx.close()
