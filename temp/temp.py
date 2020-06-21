import sqlite3 as sq
import matplotlib.pyplot as plt
import numpy as np
def study_country(country,_time,city):
    time=[]
    temp=[]
    con=sq.connect("TEMP.db")
    exe=con.cursor()
    if _time=="month":
        mnth=[1,2,3,4,5,6,7,8,9]
        reult_month = []
        for month in range(1,10):
            avg=[]
            exe.execute("""SELECT AvgTemperature FROM city_temperature WHERE city="{}"  and Country="{}" and month="{}" """.format(city,country,month))
            for res in exe.fetchall():
                if not(res[0]=="NaN" ) or not(res[0]=="nan" ) or not( res[0]==""):
                    avg.append(int(float(res[0])))
            reult_month.append(int(float(np.mean(avg))))

        print(reult_month)
        print(mnth)
        plt.bar(mnth,reult_month)
        plt.show()
    if _time=="year":
        mnth=[]
        reult_month = []
        for month in range(1995,2021):
            mnth.append(month)
            avg=[]
            exe.execute("""SELECT AvgTemperature FROM city_temperature WHERE city="{}"  and Country="{}" and year="{}" """.format(city,country,month))
            for res in exe.fetchall():
                if not(res[0]=="NaN" ) or not(res[0]=="nan" ) or not( res[0]==""):
                    avg.append(int(float(res[0])))
            reult_month.append(int(float(np.mean(avg))))

        print(reult_month)
        print(mnth)
        plt.bar(mnth,reult_month)
        plt.show()
    if _time=="day":
        mnth=[]
        reult_month = []
        for month in range(1,31):
            mnth.append(month)
            avg=[]
            exe.execute("""SELECT AvgTemperature FROM city_temperature WHERE city="{}"  and Country="{}" and day="{}" """.format(city,country,month))
            for res in exe.fetchall():
                if not(res[0]=="NaN" ) or not(res[0]=="nan" ) or not( res[0]==""):
                    avg.append(int(float(res[0])))
            reult_month.append(int(float(np.mean(avg))))

        print(reult_month)
        print(mnth)
        plt.bar(mnth,reult_month)
        plt.show()



#choose country nd study time and place 
study_country("Nigeria","day","Niamey")