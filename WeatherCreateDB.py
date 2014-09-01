#!/usr/bin/env python

import MySQLdb
import time
#import Adafruit_BMP.BMP085 as BMP085



#open the MySQL database
db = MySQLdb.connect("localhost", "sensors", "raptor50", "Weather")
curs=db.cursor()

#CREATE THE PRESSURE TABLE FOR PRESSURE AND TEMP FROM BMP085

#print (time.strftime("%m/%d/%Y"))
var0 = time.strftime("%Y/%m/%d:%H:%M:%S")
var1 = time.strftime("%Y/%m/%d")
var2 = time.strftime("%H:%M:%S")
var3 = 25.5
var4 = 3280.84
var5 = 9999.01
var6 = 8888.01

with db:
    curs.execute("DROP TABLE IF EXISTS Pressure")
    curs.execute("CREATE TABLE Pressure(Id INT PRIMARY KEY AUTO_INCREMENT,\
                    MeasTime DATETIME, DateColumn DATE,TimeColumn TIME,Temp DOUBLE(5,2), Altitude DOUBLE(8,2), Pressure DOUBLE(8,2), SeaLevelPress DOUBLE(8,2) ) ")

    curs.execute ("""
                INSERT INTO Pressure (MeasTime,DateColumn,TimeColumn,Temp,Altitude,Pressure,SeaLevelPress)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s)
                """,(var0,var1,var2,var3,var4,var5,var6) )

curs.execute ("SELECT * FROM Pressure")



print "\n\n\nId        MeasTime               Date          Time         Temperature  Altitude     Pressure     SeaLevelPressure"
print "========================================================================================================================="

for reading in curs.fetchall():
    print str(reading[0])+"    "+str(reading[1])+"     "+str(reading[2])+"      "+str(reading[3])+"          "+str(reading[4])+"      "+str(reading[5])\
        +"      "+str(reading[6])+"      "+str(reading[7])


#CREATE THE TEMPTMP35 TABLE FOR TEMP

var3 = 25.5

with db:
    curs.execute("DROP TABLE IF EXISTS TempTMP35")
    curs.execute("CREATE TABLE TempTMP35(Id INT PRIMARY KEY AUTO_INCREMENT,\
                    MeasTime DATETIME, DateColumn DATE,TimeColumn TIME, Temperature DOUBLE(5,2) ) ")

    curs.execute ("""
                INSERT INTO TempTMP35 (MeasTime,DateColumn,TimeColumn,Temperature)
                VALUES
                    (%s, %s, %s, %s)
                """,(var0,var1,var2,var3) )

curs.execute ("SELECT * FROM TempTMP35")



print "\n\n\nId      MeasTime             Date             Time       Temperature  "
print "============================================================================"

for reading in curs.fetchall():
    print str(reading[0])+"    "+str(reading[1])+"     "+str(reading[2])+"      "+str(reading[3])+"       "+str(reading[4])






#CREATE THE HUMIDITY SENSOR TABLE FOR HUMIDITY

var3 = 24.5
var4 = 36.80
var5 = 23.8

with db:
    curs.execute("DROP TABLE IF EXISTS Humidity")
    curs.execute("CREATE TABLE Humidity(Id INT PRIMARY KEY AUTO_INCREMENT,\
                    MeasTime DATETIME, DateColumn DATE,TimeColumn TIME, HTemperature DOUBLE(5,2), Humidity DOUBLE(6,2) ) ")

    curs.execute ("""
                INSERT INTO Humidity (MeasTime,DateColumn,TimeColumn,HTemperature,Humidity)
                VALUES
                    (%s, %s, %s, %s, %s)
                """,(var0,var1,var2,var3,var4) )

curs.execute ("SELECT * FROM Humidity")



print "\n\n\nId      MeasTime             Date             Time       Humidity Temp      Humidity  "
print "============================================================================================"

for reading in curs.fetchall():
    print str(reading[0])+"    "+str(reading[1])+"     "+str(reading[2])+"      "+str(reading[3])+"       "+str(reading[4])+"            "+str(reading[5])




#CREATE THE RAIN GUAGE TABLE FOR RAIN

var3 = .01

with db:
    curs.execute("DROP TABLE IF EXISTS Rain")
    curs.execute("CREATE TABLE Rain(Id INT PRIMARY KEY AUTO_INCREMENT,\
                    MeasTime DATETIME, DateColumn DATE,TimeColumn TIME, RainSample DOUBLE(5,2) ) ")

    curs.execute ("""
                INSERT INTO Rain (MeasTime,DateColumn,TimeColumn,RainSample)
                VALUES
                    (%s, %s, %s, %s)
                """,(var0,var1,var2,var3) )

curs.execute ("SELECT * FROM Rain")



print "\n\n\nId      MeasTime             Date              Time       Rain "
print "====================================================================="

for reading in curs.fetchall():
    print str(reading[0])+"    "+str(reading[1])+"     "+str(reading[2])+"      "+str(reading[3])+"     "+str(reading[4])










db.close()


