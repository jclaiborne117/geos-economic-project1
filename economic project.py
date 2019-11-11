import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from tkinter import messagebox
import matplotlib.patches as mpatches
import sys

fig = Figure(figsize=(9, 4.5), dpi=100)

Large_Font = ('verdana', 12)


##########3D graph data set up##########

df = pd.read_excel('moonlight_peak_surface.xlsx')
z0 = df['Z']
x0 = df['x']
y0 = df['y']
z1 = df['z1']
x1 = df['x1']
y1 = df['y1']
z2 = df['z2']
x2 = df['x2']
y2 = df['y2']
z3 = df['z3']
x3 = df['x3']
y3 = df['y3']
z4 = df['z4']
x4 = df['x4']
y4 = df['y4']
z5 = df['z5']
x5 = df['x5']
y5 = df['y5']
z6 = df['z6']
x6 = df['x6']
y6 = df['y6']
z7 = df['z7']
x7 = df['x7']
y7 = df['y7']
z8 = df['z8']
x8 = df['x8']
y8 = df['y8']
z9 = df['z9']
x9 = df['x9']
y9 = df['y9']
z10 = df['z10']
x10 = df['x10']
y10 = df['y10']
z11 = df['z11']
x11 = df['x11']
y11 = df['y11']
z12 = df['z12']
x12 = df['x12']
y12 = df['y12']

z50 = [4108]
x50 =[40.203101]
y50 =[120.774527]

c1_lat = [40.2238542601]
c1_long = [120.8029656165]
c1_elev = [5577]
c1_cdepth = [-1148]
c2_cdepth = [-689]
c3_lat = [40.2208591128]
c3_long = [120.8011246287]
c3_elev = [5846]
c3_cdepth = [-1270]
c4_lat = [40.2204305414]
c4_long = [120.8010432941]
c4_elev = [5846]
c4_cdepth = [-1210]
c5_lat = [40.2203575451]
c5_long = [120.8000468004]
c5_elev = [5965]
c5_cdepth = [-1276]
c6_cdepth = [-876]
c7_lat = [40.2242623708]
c7_long = [120.8029183470]
c7_elev = [5577]
c7_cdepth = [-40]
c8_lat = [40.2245189173]
c8_long = [120.8030020142]
c8_elev = [5577]
c8_cdepth = [-1100]
c9_lat = [40.2289568590]
c9_long = [120.7971468065]
c9_elev = [5695]
c9_cdepth = [-338]
c10_cdepth = [-485]
c11_cdepth = [-370]
c12_lat = [40.2283648942]
c12_long = [120.7971433051]
c12_elev = [5695]
c12_cdepth = [-406]
c13_lat = [40.2269315711]
c13_long = [120.8008800012]
c13_elev = [5580]
c13_cdepth = [-1181]

w_1 = [0.0002]
########################
##########Cu to Depth set up###########
df_1 = pd.read_excel('MN core log summary.xlsx')

########core 1#######
c1_depthi = df_1.iloc[6:36, 0].values.tolist()
c1_depthi.extend(df_1.iloc[38:73, 0].values.tolist())
c1_depthi.extend(df_1.iloc[75:110, 0].values.tolist())
c1_depthi.extend(df_1.iloc[112:117, 0].values.tolist())
c1_depthi.extend(df_1.iloc[119:147, 0].values.tolist())
c1_depthi.extend(df_1.iloc[149:183, 0].values.tolist())
c1_cu0 = df_1.iloc[6:36, 14].values.tolist()
c1_cu0.extend(df_1.iloc[38:73, 14].values.tolist())
c1_cu0.extend(df_1.iloc[75:110, 14].values.tolist())
c1_cu0.extend(df_1.iloc[112:117, 14].values.tolist())
c1_cu0.extend(df_1.iloc[119:147, 14].values.tolist())
c1_cu0.extend(df_1.iloc[149:183, 14].values.tolist())

f1 = Figure(figsize=(8, 5), dpi=100)
a1 = f1.add_subplot(111)
#########2########
c2_depthi = df_1.iloc[194:223, 0].values.tolist()
c2_depthi.extend(df_1.iloc[225:260, 0].values.tolist())
c2_depthi.extend(df_1.iloc[262:297, 0].values.tolist())
c2_depthi.extend(df_1.iloc[299:299, 0].values.tolist())
c2_cu0 = df_1.iloc[194:223, 14].values.tolist()
c2_cu0.extend(df_1.iloc[225:260, 14].values.tolist())
c2_cu0.extend(df_1.iloc[262:297, 14].values.tolist())
c2_cu0.extend(df_1.iloc[299:299, 14].values.tolist())
f2 = Figure(figsize=(8, 5), dpi=100)
a2 = f2.add_subplot(111)

###########3########
c3_depthi = df_1.iloc[311:318, 0].values.tolist()
c3_depthi.extend(df_1.iloc[320:335, 0].values.tolist())
c3_depthi.extend(df_1.iloc[337:358, 0].values.tolist())
c3_depthi.extend(df_1.iloc[361:389, 0].values.tolist())
c3_depthi.extend(df_1.iloc[392:401, 0].values.tolist())
c3_depthi.extend(df_1.iloc[403:419, 0].values.tolist())
c3_depthi.extend(df_1.iloc[421:429, 0].values.tolist())
c3_depthi.extend(df_1.iloc[431:435, 0].values.tolist())
c3_depthi.extend(df_1.iloc[437:449, 0].values.tolist())
c3_depthi.extend(df_1.iloc[451:469, 0].values.tolist())
c3_depthi.extend(df_1.iloc[471:489, 0].values.tolist())
c3_depthi.extend(df_1.iloc[492:504, 0].values.tolist())
c3_depthi.extend(df_1.iloc[506:509, 0].values.tolist())
c3_depthi.extend(df_1.iloc[511:518, 0].values.tolist())

c3_cu0 = df_1.iloc[311:318, 14].values.tolist()
c3_cu0.extend(df_1.iloc[320:335, 14].values.tolist())
c3_cu0.extend(df_1.iloc[337:358, 14].values.tolist())
c3_cu0.extend(df_1.iloc[361:389, 14].values.tolist())
c3_cu0.extend(df_1.iloc[392:401, 14].values.tolist())
c3_cu0.extend(df_1.iloc[403:419, 14].values.tolist())
c3_cu0.extend(df_1.iloc[421:429, 14].values.tolist())
c3_cu0.extend(df_1.iloc[431:435, 14].values.tolist())
c3_cu0.extend(df_1.iloc[437:449, 14].values.tolist())
c3_cu0.extend(df_1.iloc[451:469, 14].values.tolist())
c3_cu0.extend(df_1.iloc[471:489, 14].values.tolist())
c3_cu0.extend(df_1.iloc[492:504, 14].values.tolist())
c3_cu0.extend(df_1.iloc[506:509, 14].values.tolist())
c3_cu0.extend(df_1.iloc[511:518, 14].values.tolist())

f3 = Figure(figsize=(8, 5), dpi=100)
a3 = f3.add_subplot(111)
#####06MN-04####
c4_depthi = df_1.iloc[574:583, 0].values.tolist()
c4_depthi.extend(df_1.iloc[585:599, 0].values.tolist())
c4_depthi.extend(df_1.iloc[601:603, 0].values.tolist())
c4_depthi.extend(df_1.iloc[605:623, 0].values.tolist())
c4_depthi.extend(df_1.iloc[625:643, 0].values.tolist())
c4_depthi.extend(df_1.iloc[646:663, 0].values.tolist())
c4_depthi.extend(df_1.iloc[665:683, 0].values.tolist())
c4_depthi.extend(df_1.iloc[685:703, 0].values.tolist())
c4_depthi.extend(df_1.iloc[705:723, 0].values.tolist())
c4_depthi.extend(df_1.iloc[725:743, 0].values.tolist())
c4_depthi.extend(df_1.iloc[745:763, 0].values.tolist())
c4_depthi.extend(df_1.iloc[765:768, 0].values.tolist())

c4_cu0 = df_1.iloc[574:583, 14].values.tolist()
c4_cu0.extend(df_1.iloc[585:599, 14].values.tolist())
c4_cu0.extend(df_1.iloc[601:603, 14].values.tolist())
c4_cu0.extend(df_1.iloc[605:623, 14].values.tolist())
c4_cu0.extend(df_1.iloc[625:643, 14].values.tolist())
c4_cu0.extend(df_1.iloc[646:663, 14].values.tolist())
c4_cu0.extend(df_1.iloc[665:683, 14].values.tolist())
c4_cu0.extend(df_1.iloc[685:703, 14].values.tolist())
c4_cu0.extend(df_1.iloc[705:723, 14].values.tolist())
c4_cu0.extend(df_1.iloc[725:743, 14].values.tolist())
c4_cu0.extend(df_1.iloc[745:763, 14].values.tolist())
c4_cu0.extend(df_1.iloc[765:768, 14].values.tolist())
f4 = Figure(figsize=(8, 5), dpi=100)
a4 = f4.add_subplot(111)

#####06MN-05####
c5_depthi = df_1.iloc[815:828, 0].values.tolist()
c5_depthi.extend(df_1.iloc[831:848, 0].values.tolist())
c5_depthi.extend(df_1.iloc[850:858, 0].values.tolist())
c5_depthi.extend(df_1.iloc[860:869, 0].values.tolist())
c5_depthi.extend(df_1.iloc[871:882, 0].values.tolist())
c5_depthi.extend(df_1.iloc[922:928, 0].values.tolist())
c5_depthi.extend(df_1.iloc[930:948, 0].values.tolist())
c5_depthi.extend(df_1.iloc[952:969, 0].values.tolist())
c5_depthi.extend(df_1.iloc[971:989, 0].values.tolist())
c5_depthi.extend(df_1.iloc[991:1009, 0].values.tolist())
c5_depthi.extend(df_1.iloc[1011:1029, 0].values.tolist())
c5_depthi.extend(df_1.iloc[1031:1038, 0].values.tolist())
c5_depthi.extend(df_1.iloc[1040:1050, 0].values.tolist())
c5_depthi.extend(df_1.iloc[1053:1063, 0].values.tolist())


c5_cu0 = df_1.iloc[815:828, 14].values.tolist()
c5_cu0.extend(df_1.iloc[831:848, 14].values.tolist())
c5_cu0.extend(df_1.iloc[850:858, 14].values.tolist())
c5_cu0.extend(df_1.iloc[860:869, 14].values.tolist())
c5_cu0.extend(df_1.iloc[871:882, 14].values.tolist())
c5_cu0.extend(df_1.iloc[922:928, 14].values.tolist())
c5_cu0.extend(df_1.iloc[930:948, 14].values.tolist())
c5_cu0.extend(df_1.iloc[952:969, 14].values.tolist())
c5_cu0.extend(df_1.iloc[971:989, 14].values.tolist())
c5_cu0.extend(df_1.iloc[991:1009, 14].values.tolist())
c5_cu0.extend(df_1.iloc[1011:1029, 14].values.tolist())
c5_cu0.extend(df_1.iloc[1031:1038, 14].values.tolist())
c5_cu0.extend(df_1.iloc[1040:1050, 14].values.tolist())
c5_cu0.extend(df_1.iloc[1053:1063, 14].values.tolist())
f5 = Figure(figsize=(8, 5), dpi=100)
a5 = f5.add_subplot(111)
#####06MN-06####
c6_depthi = df_1.iloc[1080:1086, 0].values.tolist()
c6_depthi.extend(df_1.iloc[1088:1095, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1097:1107, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1109:1127, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1129:1148, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1149:1167, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1169:1187, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1189:1207, 0].values.tolist())
c6_depthi.extend(df_1.iloc[1209:1221, 0].values.tolist())

c6_cu0 = df_1.iloc[1080:1086, 14].values.tolist()
c6_cu0.extend(df_1.iloc[1088:1095, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1097:1107, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1109:1127, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1129:1148, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1149:1167, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1169:1187, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1189:1207, 14].values.tolist())
c6_cu0.extend(df_1.iloc[1209:1221, 14].values.tolist())
f6 = Figure(figsize=(8, 5), dpi=100)
a6 = f6.add_subplot(111)
#####06MN-07####
c7_depthi = df_1.iloc[1244:1247, 0].values.tolist()
c7_cu0 = df_1.iloc[1244:1247, 14].values.tolist()
f7 = Figure(figsize=(8, 5), dpi=100)
a7 = f7.add_subplot(111)
#####06MN-08####
c8_depthi = df_1.iloc[1264:1282, 0].values.tolist()
c8_depthi.extend(df_1.iloc[1284:1302, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1304:1322, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1324:1330, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1344:1346, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1348:1362, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1364:1369, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1371:1382, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1384:1402, 0].values.tolist())
c8_depthi.extend(df_1.iloc[1404:1422, 0].values.tolist())

c8_cu0 = df_1.iloc[1264:1282, 14].values.tolist()
c8_cu0.extend(df_1.iloc[1284:1302, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1304:1322, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1324:1330, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1344:1346, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1348:1362, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1364:1369, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1371:1382, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1384:1402, 14].values.tolist())
c8_cu0.extend(df_1.iloc[1404:1422, 14].values.tolist())

f8 = Figure(figsize=(8, 5), dpi=100)
a8 = f8.add_subplot(111)
#####06MN-09####
c9_depthi = df_1.iloc[1458:1460, 0].values.tolist()
c9_depthi.extend(df_1.iloc[1462:1472, 0].values.tolist())
c9_depthi.extend(df_1.iloc[1475:1482, 0].values.tolist())
c9_depthi.extend(df_1.iloc[1484:1502, 0].values.tolist())
c9_depthi.extend(df_1.iloc[1504:1514, 0].values.tolist())

c9_cu0 = df_1.iloc[1458:1460, 14].values.tolist()
c9_cu0.extend(df_1.iloc[1462:1472, 14].values.tolist())
c9_cu0.extend(df_1.iloc[1475:1482, 14].values.tolist())
c9_cu0.extend(df_1.iloc[1484:1502, 14].values.tolist())
c9_cu0.extend(df_1.iloc[1504:1514, 14].values.tolist())
f9 = Figure(figsize=(8, 5), dpi=100)
a9 = f9.add_subplot(111)
#####06MN-10####
c10_depthi = df_1.iloc[1536:1543, 0].values.tolist()
c10_depthi.extend(df_1.iloc[1545:1563, 0].values.tolist())
c10_depthi.extend(df_1.iloc[1565:1583, 0].values.tolist())
c10_depthi.extend(df_1.iloc[1585:1603, 0].values.tolist())
c10_depthi.extend(df_1.iloc[1605:1613, 0].values.tolist())

c10_cu0 = df_1.iloc[1536:1543, 14].values.tolist()
c10_cu0.extend(df_1.iloc[1545:1563, 14].values.tolist())
c10_cu0.extend(df_1.iloc[1565:1583, 14].values.tolist())
c10_cu0.extend(df_1.iloc[1585:1603, 14].values.tolist())
c10_cu0.extend(df_1.iloc[1605:1613, 14].values.tolist())
f10 = Figure(figsize=(8, 5), dpi=100)
a10 = f10.add_subplot(111)
#####06MN-11####
c11_depthi = df_1.iloc[1634:1643, 0].values.tolist()
c11_depthi.extend(df_1.iloc[1645:1656, 0].values.tolist())
c11_depthi.extend(df_1.iloc[1658:1664, 0].values.tolist())
c11_depthi.extend(df_1.iloc[1666:1684, 0].values.tolist())
c11_depthi.extend(df_1.iloc[1686:1694, 0].values.tolist())

c11_cu0 = df_1.iloc[1634:1643, 14].values.tolist()
c11_cu0.extend(df_1.iloc[1645:1656, 14].values.tolist())
c11_cu0.extend(df_1.iloc[1658:1664, 14].values.tolist())
c11_cu0.extend(df_1.iloc[1666:1684, 14].values.tolist())
c11_cu0.extend(df_1.iloc[1686:1694, 14].values.tolist())
f11 = Figure(figsize=(8, 5), dpi=100)
a11 = f11.add_subplot(111)
#####06MN-12####
c12_depthi = df_1.iloc[1715:1724, 0].values.tolist()
c12_depthi.extend(df_1.iloc[1726:1744, 0].values.tolist())
c12_depthi.extend(df_1.iloc[1746:1764, 0].values.tolist())
c12_depthi.extend(df_1.iloc[1766:1779, 0].values.tolist())

c12_cu0 = df_1.iloc[1715:1724, 14].values.tolist()
c12_cu0.extend(df_1.iloc[1726:1744, 14].values.tolist())
c12_cu0.extend(df_1.iloc[1746:1764, 14].values.tolist())
c12_cu0.extend(df_1.iloc[1766:1779, 14].values.tolist())
f12 = Figure(figsize=(8, 5), dpi=100)
a12 = f12.add_subplot(111)
#####06MN-13####
c13_depthi = df_1.iloc[1807:1810, 0].values.tolist()
c13_depthi.extend(df_1.iloc[1812:1830, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1832:1849, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1872:1890, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1892:1910, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1912:1930, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1932:1950, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1952:1961, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1963:1971, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1973:1991, 0].values.tolist())
c13_depthi.extend(df_1.iloc[1993:1998, 0].values.tolist())

c13_cu0 = df_1.iloc[1807:1810, 14].values.tolist()
c13_cu0.extend(df_1.iloc[1812:1830, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1832:1849, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1872:1890, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1892:1910, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1912:1930, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1932:1950, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1952:1961, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1963:1971, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1973:1991, 14].values.tolist())
c13_cu0.extend(df_1.iloc[1993:1998, 14].values.tolist())
f13 = Figure(figsize=(8, 5), dpi=100)
a13 = f13.add_subplot(111)
#####06MN-14####
c14_depthi = df_1.iloc[2019:2032, 0].values.tolist()
c14_depthi.extend(df_1.iloc[2034:2048, 0].values.tolist())
c14_depthi.extend(df_1.iloc[2054:2072, 0].values.tolist())
c14_depthi.extend(df_1.iloc[2074:2092, 0].values.tolist())
c14_depthi.extend(df_1.iloc[2094:2112, 0].values.tolist())
c14_depthi.extend(df_1.iloc[2114:2132, 0].values.tolist())
c14_depthi.extend(df_1.iloc[2134:2139, 0].values.tolist())

c14_cu0 = df_1.iloc[2019:2032, 14].values.tolist()
c14_cu0.extend(df_1.iloc[2034:2048, 14].values.tolist())
c14_cu0.extend(df_1.iloc[2054:2072, 14].values.tolist())
c14_cu0.extend(df_1.iloc[2074:2092, 14].values.tolist())
c14_cu0.extend(df_1.iloc[2094:2112, 14].values.tolist())
c14_cu0.extend(df_1.iloc[2114:2132, 14].values.tolist())
c14_cu0.extend(df_1.iloc[2134:2139, 14].values.tolist())
f14 = Figure(figsize=(8, 5), dpi=100)
a14 = f14.add_subplot(111)
#####08MN-15####
c15_depthi = df_1.iloc[2159:2169, 0].values.tolist()
c15_depthi.extend(df_1.iloc[2176:2190, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2192:2210, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2212:2223, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2225:2230, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2232:2246, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2252:2257, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2261:2270, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2272:2290, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2292:2310, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2312:2330, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2332:2350, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2352:2370, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2372:2390, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2392:2410, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2412:2430, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2432:2450, 0].values.tolist())
c15_depthi.extend(df_1.iloc[2452:2457, 0].values.tolist())

c15_cu0 = df_1.iloc[2159:2169, 15].values.tolist()
c15_cu0.extend(df_1.iloc[2176:2190, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2192:2210, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2212:2223, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2225:2230, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2232:2246, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2252:2257, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2261:2270, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2272:2290, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2292:2310, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2312:2330, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2332:2350, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2352:2370, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2372:2390, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2392:2410, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2412:2430, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2432:2450, 15].values.tolist())
c15_cu0.extend(df_1.iloc[2452:2457, 15].values.tolist())
f15 = Figure(figsize=(8, 5), dpi=100)
a15 = f15.add_subplot(111)
#####08MN-16####
c16_depthi = df_1.iloc[2471:2482, 0].values.tolist()
c16_depthi.extend(df_1.iloc[2484:2502, 0].values.tolist())
c16_depthi.extend(df_1.iloc[2504:2512, 0].values.tolist())

c16_cu0 = df_1.iloc[2471:2482, 14].values.tolist()
c16_cu0.extend(df_1.iloc[2484:2502, 14].values.tolist())
c16_cu0.extend(df_1.iloc[2504:2512, 14].values.tolist())
f16 = Figure(figsize=(8, 5), dpi=100)
a16 = f16.add_subplot(111)
#####08MN-17####
c17_depthi = df_1.iloc[2525:2533, 0].values.tolist()
c17_depthi.extend(df_1.iloc[2535:2553, 0].values.tolist())
c17_depthi.extend(df_1.iloc[2555:2566, 0].values.tolist())

c17_cu0 = df_1.iloc[2525:2533, 14].values.tolist()
c17_cu0.extend(df_1.iloc[2535:2553, 14].values.tolist())
c17_cu0.extend(df_1.iloc[2555:2566, 14].values.tolist())
f17 = Figure(figsize=(8, 5), dpi=100)
a17 = f17.add_subplot(111)
#####08MN-18####
c18_depthi = df_1.iloc[2580:2585, 0].values.tolist()
c18_depthi.extend(df_1.iloc[2587:2605, 0].values.tolist())
c18_depthi.extend(df_1.iloc[2607:2619, 0].values.tolist())

c18_cu0 = df_1.iloc[2580:2585, 14].values.tolist()
c18_cu0.extend(df_1.iloc[2587:2605, 14].values.tolist())
c18_cu0.extend(df_1.iloc[2607:2619, 14].values.tolist())
f18 = Figure(figsize=(8, 5), dpi=100)
a18 = f18.add_subplot(111)
#####08MN-19####
c19_depthi = df_1.iloc[2633:2637, 0].values.tolist()
c19_depthi.extend(df_1.iloc[2639:2657, 0].values.tolist())
c19_depthi.extend(df_1.iloc[2659:2674, 0].values.tolist())

c19_cu0 = df_1.iloc[2633:2637, 14].values.tolist()
c19_cu0.extend(df_1.iloc[2639:2657, 14].values.tolist())
c19_cu0.extend(df_1.iloc[2659:2674, 14].values.tolist())
f19 = Figure(figsize=(8, 5), dpi=100)
a19 = f19.add_subplot(111)

#####08MN-20####
c20_depthi = df_1.iloc[2690:2691, 0].values.tolist()
c20_depthi.extend(df_1.iloc[2693:2711, 0].values.tolist())
c20_depthi.extend(df_1.iloc[2713:2730, 0].values.tolist())

c20_cu0 = df_1.iloc[2690:2691, 14].values.tolist()
c20_cu0.extend(df_1.iloc[2693:2711, 14].values.tolist())
c20_cu0.extend(df_1.iloc[2713:2730, 14].values.tolist())
f20 = Figure(figsize=(8, 5), dpi=100)
a20 = f20.add_subplot(111)

#####08MN-21####
c21_depthi = df_1.iloc[2747:2765, 0].values.tolist()
c21_depthi.extend(df_1.iloc[2767:2775, 0].values.tolist())
c21_depthi.extend(df_1.iloc[2777:2785, 0].values.tolist())
c21_depthi.extend(df_1.iloc[2787:2788, 0].values.tolist())

c21_cu0 = df_1.iloc[2747:2765, 14].values.tolist()
c21_cu0.extend(df_1.iloc[2767:2775, 14].values.tolist())
c21_cu0.extend(df_1.iloc[2777:2785, 14].values.tolist())
c21_cu0.extend(df_1.iloc[2787:2788, 14].values.tolist())
f21 = Figure(figsize=(8, 5), dpi=100)
a21 = f21.add_subplot(111)


########Lith Controls##########

c1_disc = df.iloc[0:71, 51]
c2_disc = df.iloc[0:43, 54]
c3_disc = df.iloc[0:79, 57]
c4_disc = df.iloc[0:75, 60]
c5_disc = df.iloc[0:78, 63]
c6_disc = df.iloc[0:55, 65]
c7_disc = df.iloc[0:3, 68]
c8_disc = df.iloc[0:68, 71]
c9_disc = df.iloc[0:22, 74]
c10_disc = df.iloc[0:31, 77]
c11_disc = df.iloc[0:24, 80]
c12_disc = df.iloc[0:26, 83]
c13_disc = df.iloc[0:73, 86]
c14_disc = df.iloc[0:67, 89]
c15_disc = df.iloc[0:88, 92]
c16_disc = df.iloc[0:13, 95]
c17_disc = df.iloc[0:13, 98]
c18_disc = df.iloc[0:13, 101]
c19_disc = df.iloc[0:13, 104]
c20_disc = df.iloc[0:13, 107]
c21_disc = df.iloc[0:13, 110]

c1_min = df.iloc[0:71, 112]
c2_min = df.iloc[0:43, 113]
c3_min = df.iloc[0:79, 114]
c4_min = df.iloc[0:75, 115]
c5_min = df.iloc[0:78,116]
c6_min = df.iloc[0:55,117]
c7_min = df.iloc[0:3,118]
c8_min = df.iloc[0:68,119]
c9_min = df.iloc[0:22,120]
c10_min = df.iloc[0:31,121]
c11_min = df.iloc[0:24,122]
c12_min = df.iloc[0:26,123]
c13_min = df.iloc[0:73,124]
c14_min = df.iloc[0:67,125]
c15_min = df.iloc[0:88,126]
c16_min = df.iloc[0:13,127]
c17_min = df.iloc[0:13,128]
c18_min = df.iloc[0:13,129]
c19_min = df.iloc[0:13,130]
c20_min = df.iloc[0:13,131]
c21_min = df.iloc[0:13,132]

fig_l = Figure(figsize=(8, 5), dpi=100)
ax_l = fig_l.add_subplot(111)

def myround(x, base=5):
    return base * round(x/base)

def exit1():
    sys.exit(0)

bar_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
core_numbers = ['05MN-1', '05MN-2', '06MN-3', '06MN-04', '06MN-05', '06MN-06', '06MN-7', '06MN-8', '06MN-9',
                '06MN-10', '06MN-11', '06MN-12', '06MN-13', '06MN-14', '08MN-15', '08MN-16', '08MN-17',
                '08MN-18', '08MN-19', '08MN-20', '08MN-21']


coords = []
descY = []
descX = []
######controls how to switch windows#########
class claiborneLogPro(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_iconbitmap(self, default='icon1.ico')
        tk.Tk.wm_title(self, 'Claiborne log_pro')


        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, Core1page, Core2page, Core3page, Core4page, Core5page, Core6page, Core7page, Core8page, Core9page
                  , Core10page, Core11page, Core12page, Core13page, Core14page, Core15page, Core16page, Core17page, Core18page, Core19page, Core20page, Core21page, Lithpage):

            self.withdraw()

            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row=0, column = 0, sticky="nsew")


        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.configure(bg='#474747')
        frame.tkraise()





######home page#########
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Claiborne log pro', font=Large_Font, bg="#686868", fg="white", width=300)
        #label.pack(pady=10, padx=10)
        label.place(relx=0.5, rely=0.0, anchor='n')

        label2 = tk.Label(self, text='クレイボーン　ログプロ', font=Large_Font, bg="#474747", fg="white", width=20)
        label2.place(relx=0.95, rely=0.99, anchor='se')



        button1= tk.Button(self, text='About Us',  bg='#686868',fg='white',relief='groove',width=20,
                           command=lambda: controller.show_frame(PageOne))

        button1.place(relx=0.5, rely=0.3, anchor='center')

        button2 = tk.Button(self, text='Spacial refrence', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageTwo))

        button2.place(relx=0.5, rely=0.4, anchor='center')

        button3 = tk.Button(self, text='Copper at depth', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))

        button3.place(relx=0.5, rely=0.5, anchor='center')

        button5 = tk.Button(self, text='Exit', bg='#686868',fg='white',relief='groove',width=20, command=exit1)
        button5.place(relx=0.1, rely=0.9, anchor='sw')

        button6 = tk.Button(self, text='Lithology page', bg='#686868', fg='white', relief='groove', width=20,
                            command=lambda: controller.show_frame(Lithpage))

        button6.place(relx=0.5, rely=0.6, anchor='center')

######about us page#########
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='About Us', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        label2 = tk.Label(self, text='Claiborne log pro is an independent program that was created for the \n purpose of viewing geologic data relating to Moonlight Creek. \n'
                                     'and making Marios economic project look like a joke. This program allows \n for viewing the copper percentage for each documented core at certain depths\n'
                                    'in the View the Cores page. The Spacial reference  page shows the surface \n topography of the Moonlight Creek area and models for drill core depth. \n'
                                    'In the Lithology page the each core is shown and the lithology at different \n depths is noted. By pressing i you can see the documented information \n'
                                    'noted at that core interval.  By pressing m you can see the documented mineral information.'
                                      , font= Large_Font, bg="#474747", fg="white", width=300)
        label2.place(relx=0.5, rely=0.5, anchor='c')


        button1 = tk.Button(self, text='Home', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        button2 = tk.Button(self, text='Spacial Page', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(relx=0.5, rely=0.15, anchor='center')

        button3 = tk.Button(self, text='View the Cores', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button3.place(relx=0.5, rely=0.2, anchor='center')

######spacial reference page######
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Spacial Reference', font=Large_Font, bg="#686868", fg="white", width=300)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='back to home', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text='About Us', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = tk.Button(self, text='Copper at Depth', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        style.use('dark_background')

        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x0, y0, z0, color='blue', alpha=0.5)
        ax.plot(x1, y1, z1, color='red', alpha=0.5)
        ax.plot(x2, y2, z2, color='red', alpha=0.5)
        ax.plot(x3, y3, z3, color='blue', alpha=0.5)
        ax.plot(x4, y4, z4, color='blue', alpha=0.5)
        ax.plot(x5, y5, z5, color='blue', alpha=0.5)
        ax.plot(x6, y6, z6, color='blue', alpha=0.5)
        ax.plot(x7, y7, z7, color='blue', alpha=0.5)
        ax.plot(x8, y8, z8, color='red', alpha=0.5)
        ax.plot(x9, y9, z9, color='red', alpha=0.5)
        ax.plot(x10, y10, z10, color='red', alpha=0.5)
        ax.plot(x11, y11, z11, color='blue', alpha=0.5)
        ax.plot(x12, y12, z12, color='blue', alpha=0.5)
        ax.scatter(x50, y50, z50, color='brown')
        ax.bar3d(c1_lat, c1_long, c1_elev, w_1, w_1, c1_cdepth, color='blue')
        ax.bar3d(40.225, 120.8029656165, c1_elev, w_1, w_1, c2_cdepth, color='blue')
        ax.bar3d(c3_lat, c3_long, c3_elev, w_1, w_1, c3_cdepth, color='blue')
        ax.bar3d(c4_lat, c4_long, c4_elev, w_1, w_1, c4_cdepth, color='blue')
        ax.bar3d(c5_lat, c5_long, c5_elev, w_1, w_1, c5_cdepth, color='blue')
        ax.bar3d(40.2206, 120.80005, c5_elev, w_1, w_1, c6_cdepth, color='blue')
        ax.bar3d(c7_lat, c7_long, c7_elev, w_1, w_1, c7_cdepth, color='blue')
        ax.bar3d(c8_lat, c8_long, c8_elev, w_1, w_1, c8_cdepth, color='blue')
        ax.bar3d(c9_lat, c9_long, c9_elev, w_1, w_1, c9_cdepth, color='blue')
        ax.bar3d(40.23, 120.7971468065, c8_elev, w_1, w_1, c10_cdepth, color='blue')
        ax.bar3d(40.226, 120.7971468065, c9_elev, w_1, w_1, c11_cdepth, color='blue')
        ax.bar3d(c12_lat, c12_long, c12_elev, w_1, w_1, c12_cdepth, color='blue')
        ax.bar3d(c13_lat, c13_long, c13_elev, w_1, w_1, c13_cdepth, color='blue')


        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude (*-1)')
        ax.set_zlabel('altitude(feet)')
        #adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.6, anchor='center')

######core view page, core pages######
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Core List', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='back to home', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        button2 = tk.Button(self, text='05MN-1', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core1page))
        button2.place(relx=0.1, rely=0.3, anchor='center')

        button3 = tk.Button(self, text='05MN-2', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core2page))
        button3.place(relx=0.1, rely=0.4, anchor='center')

        button4 = tk.Button(self, text='06MN-3', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core3page))
        button4.place(relx=0.1, rely=0.5, anchor='center')

        button5 = tk.Button(self, text='06MN-04', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core4page))
        button5.place(relx=0.1, rely=0.6, anchor='center')

        button6 = tk.Button(self, text='06MN-05', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core5page))
        button6.place(relx=0.1, rely=0.7, anchor='center')

        button7 = tk.Button(self, text='06MN-06', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core6page))
        button7.place(relx=0.3, rely=0.3, anchor='center')

        button8 = tk.Button(self, text='06MN-7', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core7page))
        button8.place(relx=0.3, rely=0.4, anchor='center')

        button9 = tk.Button(self, text='06MN-8', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core8page))
        button9.place(relx=0.3, rely=0.5, anchor='center')

        button10 = tk.Button(self, text='06MN-9', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core9page))
        button10.place(relx=0.3, rely=0.6, anchor='center')

        button11 = tk.Button(self, text='06MN-10', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core10page))
        button11.place(relx=0.3, rely=0.7, anchor='center')

        button12 = tk.Button(self, text='06MN-11', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core11page))
        button12.place(relx=0.5, rely=0.3, anchor='center')

        button13 = tk.Button(self, text='06MN-12', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core12page))
        button13.place(relx=0.5, rely=0.4, anchor='center')

        button14 = tk.Button(self, text='06MN-13', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core13page))
        button14.place(relx=0.5, rely=0.5, anchor='center')

        button15 = tk.Button(self, text='06MN-14', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core14page))
        button15.place(relx=0.5, rely=0.6, anchor='center')

        button16 = tk.Button(self, text='08MN-15', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core15page))
        button16.place(relx=0.5, rely=0.7, anchor='center')

        button17 = tk.Button(self, text='08MN-16', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core16page))
        button17.place(relx=0.7, rely=0.3, anchor='center')

        button18 = tk.Button(self, text='08MN-17', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core17page))
        button18.place(relx=0.7, rely=0.4, anchor='center')

        button19 = tk.Button(self, text='08MN-18', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core18page))
        button19.place(relx=0.7, rely=0.5, anchor='center')

        button20 = tk.Button(self, text='08MN-19', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core19page))
        button20.place(relx=0.7, rely=0.6, anchor='center')

        button21 = tk.Button(self, text='08MN-20', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core20page))
        button21.place(relx=0.7, rely=0.7, anchor='center')

        button22 = tk.Button(self, text='08MN-21', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(Core21page))
        button22.place(relx=0.9, rely=0.5, anchor='center')

class Core1page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='05MN-1, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a1.plot(c1_depthi, c1_cu0, color='#FC6700',label='cu')
        a1.legend()
        a1.set_xlabel('depth in m')
        a1.set_ylabel('Cu %')

        canvas = FigureCanvasTkAgg(f1, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core2page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='05MN-2, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        style.use('ggplot')
        a2.plot(c2_depthi, c2_cu0, color = '#FC6700')
        a2.set_xlabel('depth in m')
        a2.set_ylabel('Cu %')

        canvas = FigureCanvasTkAgg(f2, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core3page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-3, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a3.plot(c3_depthi, c3_cu0, color = '#FC6700')
        a3.set_xlabel('depth in m')
        a3.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f3, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core4page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-4, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a4.plot(c4_depthi, c4_cu0, color = '#FC6700')
        a4.set_xlabel('depth in m')
        a4.set_ylabel('Cu %')

        canvas = FigureCanvasTkAgg(f4, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core5page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-05, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a5.plot(c5_depthi, c5_cu0, color = '#FC6700')
        a5.set_xlabel('depth in m')
        a5.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f5, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core6page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-06, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a6.plot(c6_depthi, c6_cu0, color = '#FC6700')
        a6.set_xlabel('depth in m')
        a6.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f6, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core7page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-7, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a7.plot(c7_depthi, c7_cu0, color = '#FC6700')
        a7.set_xlabel('depth in m')
        a7.set_ylabel('Cu %')

        canvas = FigureCanvasTkAgg(f7, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core8page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-8, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a8.plot(c8_depthi, c8_cu0, color = '#FC6700')
        a8.set_xlabel('depth in m')
        a8.set_ylabel('Cu %')

        canvas = FigureCanvasTkAgg(f8, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core9page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-9, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a9.plot(c9_depthi, c9_cu0, color = '#FC6700')
        a9.set_xlabel('depth in m')
        a9.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f9, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core10page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-10, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a10.plot(c10_depthi, c10_cu0, color = '#FC6700')
        a10.set_xlabel('depth in m')
        a10.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f10, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core11page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-11, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a11.plot(c11_depthi, c11_cu0, color = '#FC6700')
        a11.set_xlabel('depth in m')
        a11.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f11, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core12page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-12, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a12.plot(c12_depthi, c12_cu0, color = '#FC6700')
        a12.set_xlabel('depth in m')
        a12.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f12, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core13page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-13, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a13.plot(c13_depthi, c13_cu0, color = '#FC6700')
        a13.set_xlabel('depth in m')
        a13.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f13, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core14page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='06MN-14, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a14.plot(c14_depthi, c14_cu0, color = '#FC6700')
        a14.set_xlabel('depth in m')
        a14.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f14, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core15page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-15, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a15.plot(c15_depthi, c15_cu0, color = '#FC6700')
        a15.set_xlabel('depth in ft')
        a15.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f15, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core16page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-16, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a16.plot(c16_depthi, c16_cu0, color = '#FC6700')
        a16.set_xlabel('depth in ft')
        a16.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f16, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core17page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-17, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a17.plot(c17_depthi, c17_cu0, color = '#FC6700')
        a17.set_xlabel('depth in ft')
        a17.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f17, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core18page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-18, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a18.plot(c18_depthi, c18_cu0, color = '#FC6700')
        a18.set_xlabel('depth in ft')
        a18.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f18, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core19page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-19, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a19.plot(c19_depthi, c19_cu0, color = '#FC6700')
        a19.set_xlabel('depth in ft')
        a19.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f19, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core20page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-20, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a20.plot(c20_depthi, c20_cu0, color = '#FC6700')
        a20.set_xlabel('depth in ft')
        a20.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f20, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Core21page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='08MN-21, copper% vs. depth', font=Large_Font, bg="#686868", fg="white", width=300)
        label.place(relx=0.5, rely=0.0, anchor='n')

        button1 = tk.Button(self, text='Core list', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(PageThree))
        button1.place(relx=0.5, rely=0.1, anchor='center')

        a21.plot(c21_depthi, c21_cu0, color='#FC6700')
        a21.set_xlabel('depth in ft')
        a21.set_ylabel('Cu %')


        canvas = FigureCanvasTkAgg(f21, self)
        canvas.draw()
        style.use('ggplot')
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ## adds toolbar to the canvas
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')

class Lithpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Lithology page, press m for mineral info, press i for core info', font=Large_Font, bg="#686868", fg="white", width=300)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='back to home', bg='#686868',fg='white',relief='groove',width=20,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        def onclick(event):
            global ix, iy
            ix, iy = event.xdata, event.ydata
            descY = int(myround(iy, 5) / 5)
            descX = int(round(ix))

            if event.key == 'p':
                messagebox.showinfo('Hello', 'Mario Sucks, and Justin is awesome')

            if event.key == 'i':
                if descX == 1:
                    if descY < 0:
                        messagebox.showinfo('description', c1_disc[0])
                    if descY > 71:
                        print(c1_disc[70])
                        messagebox.showinfo('description', c1_disc[70])
                    if descY > 0 and descY < 71:
                        messagebox.showinfo('description', c1_disc[descY])
                if descX == 2:
                    if descY < 0:
                        messagebox.showinfo('description', c2_disc[0])
                    if descY > 43:
                        messagebox.showinfo('description', c2_disc[42])
                    if descY > 0 and descY < 43:
                        messagebox.showinfo('description', c2_disc[descY])
                if descX == 3:
                    if descY < 0:
                        messagebox.showinfo('description', c3_disc[0])
                    if descY > 79:
                        messagebox.showinfo('description', c3_disc[78])
                    if descY > 0 and descY < 79:
                        messagebox.showinfo('description', c3_disc[descY])
                if descX == 4:
                    if descY < 0:
                        messagebox.showinfo('description', c4_disc[0])
                    if descY > 75:
                        messagebox.showinfo('description', c4_disc[74])
                    if descY > 0 and descY < 75:
                        messagebox.showinfo('description', c4_disc[descY])
                if descX == 5:
                    if descY < 0:
                        messagebox.showinfo('description', c5_disc[0])
                    if descY > 79:
                        messagebox.showinfo('description', c5_disc[78])
                    if descY > 0 and descY < 79:
                        messagebox.showinfo('description', c5_disc[descY])
                if descX == 6:
                    if descY < 0:
                        messagebox.showinfo('description', c6_disc[0])
                    if descY > 55:
                        messagebox.showinfo('description', c6_disc[54])
                    if descY > 0 and descY < 55:
                        messagebox.showinfo('description', c6_disc[descY])
                if descX == 7:
                    if descY < 0:
                        messagebox.showinfo('description', c7_disc[0])
                    if descY > 4:
                        messagebox.showinfo('description', c7_disc[2])
                    if descY > 0 and descY < 4:
                        messagebox.showinfo('description', c7_disc[descY])
                if descX == 8:
                    if descY < 0:
                        messagebox.showinfo('description', c8_disc[0])
                    if descY > 68:
                        messagebox.showinfo('description', c8_disc[67])
                    if descY > 0 and descY < 68:
                        messagebox.showinfo('description', c8_disc[descY])
                if descX == 9:
                    if descY < 0:
                        messagebox.showinfo('description', c9_disc[0])
                    if descY > 22:
                        messagebox.showinfo('description', c9_disc[21])
                    if descY > 0 and descY < 22:
                        messagebox.showinfo('description', c1_disc[descY])
                if descX == 10:
                    if descY < 0:
                        messagebox.showinfo('description', c10_disc[0])
                    if descY > 31:
                        messagebox.showinfo('description', c10_disc[30])
                    if descY > 0 and descY < 31:
                        messagebox.showinfo('description', c10_disc[descY])
                if descX == 11:
                    if descY < 0:
                        messagebox.showinfo('description', c11_disc[0])
                    if descY > 24:
                        messagebox.showinfo('description', c11_disc[23])
                    if descY > 0 and descY < 24:
                        messagebox.showinfo('description', c11_disc[descY])
                if descX == 12:
                    if descY < 0:
                        messagebox.showinfo('description', c12_disc[0])
                    if descY > 26:
                        messagebox.showinfo('description', c12_disc[25])
                    if descY > 0 and descY < 26:
                        messagebox.showinfo('description', c12_disc[descY])
                if descX == 13:
                    if descY < 0:
                        messagebox.showinfo('description', c13_disc[0])
                    if descY > 71:
                        messagebox.showinfo('description', c13_disc[70])
                    if descY > 0 and descY < 71:
                        messagebox.showinfo('description', c13_disc[descY])
                if descX == 14:
                    if descY < 0:
                        messagebox.showinfo('description', c14_disc[0])
                    if descY > 47:
                        messagebox.showinfo('description', c14_disc[46])
                    if descY > 0 and descY < 47:
                        messagebox.showinfo('description', c14_disc[descY])
                if descX == 15:
                    if descY < 0:
                        messagebox.showinfo('description', c15_disc[0])
                    if descY > 88:
                        messagebox.showinfo('description', c15_disc[87])
                    if descY > 0 and descY < 88:
                        messagebox.showinfo('description', c15_disc[descY])
                if descX == 16:
                    if descY < 0:
                        messagebox.showinfo('description', c16_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c16_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c16_disc[descY])
                if descX == 17:
                    if descY < 0:
                        messagebox.showinfo('description', c17_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c17_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c17_disc[descY])
                if descX == 18:
                    if descY < 0:
                        messagebox.showinfo('description', c18_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c18_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c18_disc[descY])
                if descX == 19:
                    if descY < 0:
                        messagebox.showinfo('description', c19_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c19_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c19_disc[descY])
                if descX == 20:
                    if descY < 0:
                        messagebox.showinfo('description', c20_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c20_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c20_disc[descY])
                if descX == 21:
                    if descY < 0:
                        messagebox.showinfo('description', c21_disc[0])
                    if descY > 13:
                        messagebox.showinfo('description', c21_disc[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo('description', c21_disc[descY])

            if event.key == 'm':
                if descX == 1:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c1_min[0])
                    if descY > 71:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c1_min[70])
                    if descY > 0 and descY < 71:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c1_min[descY])
                if descX == 2:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c2_min[0])
                    if descY > 43:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c2_min[42])
                    if descY > 0 and descY < 43:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c2_min[descY])
                if descX == 3:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c3_min[0])
                    if descY > 79:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c3_min[78])
                    if descY > 0 and descY < 79:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] arg[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c3_min[descY])
                if descX == 4:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c4_min[0])
                    if descY > 75:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c4_min[74])
                    if descY > 0 and descY < 75:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c4_min[descY])
                if descX == 5:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c5_min[0])
                    if descY > 79:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c5_min[78])
                    if descY > 0 and descY < 79:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c5_min[descY])
                if descX == 6:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c6_min[0])
                    if descY > 55:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c6_min[54])
                    if descY > 0 and descY < 55:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c6_min[descY])
                if descX == 7:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c7_min[0])
                    if descY > 4:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c7_min[2])
                    if descY > 0 and descY < 4:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c7_min[descY])
                if descX == 8:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c8_min[0])
                    if descY > 68:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c8_min[67])
                    if descY > 0 and descY < 68:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c8_min[descY])
                if descX == 9:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c9_min[0])
                    if descY > 22:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c9_min[21])
                    if descY > 0 and descY < 22:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c9_min[descY])
                if descX == 10:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c10_min[0])
                    if descY > 31:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c10_min[30])
                    if descY > 0 and descY < 31:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c10_min[descY])
                if descX == 11:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c11_min[0])
                    if descY > 24:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c11_min[23])
                    if descY > 0 and descY < 24:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c11_min[descY])
                if descX == 12:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c12_min[0])
                    if descY > 26:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c12_min[25])
                    if descY > 0 and descY < 26:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c12_min[descY])
                if descX == 13:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c13_min[0])
                    if descY > 71:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c13_min[70])
                    if descY > 0 and descY < 71:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c13_min[descY])
                if descX == 14:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c14_min[0])
                    if descY > 47:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c14_min[46])
                    if descY > 0 and descY < 47:
                        messagebox.showinfo(
                            'mineral info  ser[] tour[] chlepi[] mag[] pot[] cu[] cu%[] Au g/ton[] Ag g/ton[]',
                            c14_min[descY])
                if descX == 15:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c15_min[0])
                    if descY > 88:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c15_min[87])
                    if descY > 0 and descY < 88:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c15_min[descY])
                if descX == 16:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c16_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c16_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c16_min[descY])
                if descX == 17:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c17_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c17_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c17_min[descY])
                if descX == 18:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c18_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c18_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c18_min[descY])
                if descX == 19:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c19_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c19_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c19_min[descY])
                if descX == 20:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c20_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c20_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c20_min[descY])
                if descX == 21:
                    if descY < 0:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c21_min[0])
                    if descY > 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c21_min[12])
                    if descY > 0 and descY < 13:
                        messagebox.showinfo(
                            'mineral info  Ble[] tour[] chlepi[] mag[] spec[] sil[] Cumin[] Cu%[] Ag g/ton[]',
                            c21_min[descY])

            global coords
            coords.append((ix, iy))

            if len(coords) == 1000:
                fig_l.canvas.mpl_disconnect(cid)

            return coords

        cid = fig_l.canvas.mpl_connect('key_press_event', onclick)


        ax_l.bar(1, 246, color='red', width=0.2, hatch='x')
        ax_l.bar(1, 4, bottom=246, color='grey', width=0.2, hatch='.')
        ax_l.bar(1, 100, bottom=250, color='red', width=0.2, hatch='x')
        ax_l.bar(2, 210, color='red', width=0.2, hatch='x')
        ax_l.bar(3, 387, color='red', width=0.2, hatch='x')
        ax_l.bar(4, 369, color='red', width=0.2, hatch='x')
        ax_l.bar(5, 389, color='red', width=0.2, hatch='x')
        ax_l.bar(6, 267, color='red', width=0.2, hatch='x')
        ax_l.bar(7, 11.6, color='brown', width=0.2, hatch='o')

        ax_l.bar(8, 8, color='brown', width=0.2, hatch='o')
        ax_l.bar(8, 118, bottom=8, color='red', width=0.2, hatch='x')
        ax_l.bar(8, 6, bottom=126, color='purple', width=0.2, hatch='-')
        ax_l.bar(8, 22, bottom=132, color='grey', width=0.2, hatch='.')
        ax_l.bar(8, 158, bottom=154, color='red', width=0.2, hatch='x')
        ax_l.bar(8, 8, bottom=312, color='blue', width=0.2, hatch='|')
        ax_l.bar(8, 10, bottom=320, color='red', width=0.2, hatch='x')
        ax_l.bar(8, 5.4, bottom=330, color='blue', width=0.2, hatch='|')

        ax_l.bar(9, 103.3, color='red', width=0.2, hatch='x')
        ax_l.bar(10, 147.9, color='red', width=0.2, hatch='x')
        ax_l.bar(11, 112.8, color='red', width=0.2, hatch='x')
        ax_l.bar(12, 124, color='red', width=0.2, hatch='x')

        ax_l.bar(13, 98, color='red', width=0.2, hatch='x')
        ax_l.bar(13, 18, bottom=98, color='blue', width=0.2, hatch='|')
        ax_l.bar(13, 244, bottom=116, color='red', width=0.2, hatch='x')

        ax_l.bar(14, 56, color='red', width=0.2, hatch='x')
        ax_l.bar(14, 10, bottom=56, color='blue', width=0.2)
        ax_l.bar(14, 163, bottom=66, color='red', width=0.2, hatch='x')

        ax_l.bar(15, 12, color='grey', width=0.2, hatch='o')
        ax_l.bar(15, 2, bottom=12, color='blue', width=0.2, hatch='|')
        ax_l.bar(15, 3, bottom=14, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 8, bottom=17, color='grey', width=0.2, hatch='o')
        ax_l.bar(15, 2, bottom=25, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 3, bottom=27, color='grey', width=0.2, hatch='o')
        ax_l.bar(15, 2, bottom=30, color='brown', width=0.2, hatch='o')
        ax_l.bar(15, 3, bottom=32, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=33, color='brown', width=0.2, hatch='o')
        ax_l.bar(15, 8, bottom=35, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=43, color='grey', width=0.2, hatch='o')
        ax_l.bar(15, 11, bottom=45, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 3, bottom=56, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=59, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=61, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=63, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 3, bottom=65, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=68, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=70, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=72, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=74, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=76, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=78, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=80, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=82, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=84, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=86, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=88, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=90, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=92, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=94, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 3, bottom=96, color='blue', width=0.2, hatch='|')
        ax_l.bar(15, 2, bottom=99, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=101, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=103, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=105, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=107, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=109, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=111, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=113, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=115, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=117, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=119, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=121, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=123, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=125, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=127, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=129, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=131, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=133, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=135, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=137, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=139, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=141, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=143, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=145, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=147, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=149, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=151, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=153, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=155, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=157, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=159, color='brown', width=0.2, hatch='o')
        ax_l.bar(15, 3, bottom=161, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=164, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=166, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=168, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 2, bottom=170, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 2, bottom=172, color='red', width=0.2, hatch='x')
        ax_l.bar(15, 3, bottom=174, color='brown', width=0.2, hatch='o')
        ax_l.bar(15, 18, bottom=177, color='grey', width=0.2, hatch='.')
        ax_l.bar(15, 264, bottom=195, color='red', width=0.2, hatch='x')

        ax_l.bar(16, 61, color='red', width=0.2, hatch='x')
        ax_l.bar(17, 61, color='red', width=0.2, hatch='x')
        ax_l.bar(18, 58, color='red', width=0.2, hatch='x')
        ax_l.bar(19, 61, color='red', width=0.2, hatch='x')
        ax_l.bar(20, 61, color='red', width=0.2, hatch='x')

        ax_l.bar(21, 42, color='red', width=0.2, hatch='x')
        ax_l.bar(21, 12, bottom=42, color='blue', width=0.2, hatch='|')
        ax_l.bar(21, 6, bottom=54, color='red', width=0.2, hatch='x')

        ax_l.set_xticks(bar_numbers)
        ax_l.set_xticklabels(core_numbers, rotation=90, size=7)
        ax_l.set_ylabel('Depth (m)')

        monz = mpatches.Patch(color='red', label='Quartz Monzonite')
        dike = mpatches.Patch(color='blue', label='post min dike')
        metav = mpatches.Patch(color='grey', label='Metavolcanics')
        matrix = mpatches.Patch(color='brown', label='Blk matrix')
        horn = mpatches.Patch(color='purple', label='hornfels')

        ax_l.legend(handles=[monz, dike, metav, matrix, horn],framealpha=5, prop={'size':8})
        style.use('default')

        canvas = FigureCanvasTkAgg(fig_l, self)
        canvas.draw()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(relx=0.5, rely=0.55, anchor='center')
        canvas.mpl_connect('key_press_event', onclick)




app = claiborneLogPro()
app.geometry('800x600+500+200')
app.iconbitmap('icon1.ico')
app.deiconify()
app.mainloop()

