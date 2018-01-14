#!/usr/bin/env python
# Author: Jarrett B. <sircuddles@icloud.com> Made with Slovene pride
# coding: utf-8

import pymysql.cursors
import sys
import re
import datetime

cnx = pymysql.connect(user='root', db='altislife')
cursor = cnx.cursor()

cursor.execute("SET @var:=0;")
cnx.commit()

cursor.execute("UPDATE players SET uid=(@var:=@var+1)")
cnx.commit()

cursor.execute("ALTER TABLE players AUTO_INCREMENT=1")
cnx.commit()
