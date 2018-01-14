#!/usr/bin/env python
# Author: Jarrett B. <sircuddles@icloud.com> Made with Slovene pride
# coding: utf-8

import pymysql.cursors
import sys
import re

cnx = pymysql.connect(user='root', db='altislife')
cursor = cnx.cursor()
cursor1 = cnx.cursor()

compensated = []

cursor.execute("SELECT * FROM players WHERE civ_licenses NOT LIKE \"[[`license_civ_driver`,0],[`license_civ_boat`,0],[`license_civ_pilot`,0],[`license_civ_trucking`,0],[`license_civ_gun`,0],[`license_civ_dive`,0],[`license_civ_home`,0],[`license_civ_Woodcutting`,0],[`license_civ_tcf`,0],[`license_civ_oil`,0],[`license_civ_diamond`,0],[`license_civ_salt`,0],[`license_civ_sand`,0],[`license_civ_iron`,0],[`license_civ_copper`,0],[`license_civ_cement`,0],[`license_civ_medmarijuana`,0],[`license_civ_cocaine`,0],[`license_civ_heroin`,0],[`license_civ_marijuana`,0],[`license_civ_rebel`,0],[`license_civ_cloth`,0],[`license_civ_steelplate`,0],[`license_civ_C4`,0],[`license_civ_rubber`,0],[`license_civ_gunpowder`,0],[`license_civ_phosphorus`,0],[`license_civ_corn`,0],[`license_civ_blood_diamond`,0],[`license_civ_ruby`,0],[`license_civ_gold_dust`,0],[`license_civ_taxi`,0]]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET civ_licenses = \"[[`license_civ_driver`,0],[`license_civ_boat`,0],[`license_civ_pilot`,0],[`license_civ_trucking`,0],[`license_civ_gun`,0],[`license_civ_dive`,0],[`license_civ_home`,0],[`license_civ_Woodcutting`,0],[`license_civ_tcf`,0],[`license_civ_oil`,0],[`license_civ_diamond`,0],[`license_civ_salt`,0],[`license_civ_sand`,0],[`license_civ_iron`,0],[`license_civ_copper`,0],[`license_civ_cement`,0],[`license_civ_medmarijuana`,0],[`license_civ_cocaine`,0],[`license_civ_heroin`,0],[`license_civ_marijuana`,0],[`license_civ_rebel`,0],[`license_civ_cloth`,0],[`license_civ_steelplate`,0],[`license_civ_C4`,0],[`license_civ_rubber`,0],[`license_civ_gunpowder`,0],[`license_civ_phosphorus`,0],[`license_civ_corn`,0],[`license_civ_blood_diamond`,0],[`license_civ_ruby`,0],[`license_civ_gold_dust`,0],[`license_civ_taxi`,0]]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

cursor.execute("SELECT * FROM players WHERE cop_licenses NOT LIKE \"[[`license_cop_MetroBadge`,0],[`license_cop_TrooperBadge`,0],[`license_cop_CoastBadge`,0],[`license_cop_cAir`,0],[`license_cop_cg`,0],[`license_cop_swat`,0]]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET cop_licenses = \"[[`license_cop_MetroBadge`,0],[`license_cop_TrooperBadge`,0],[`license_cop_CoastBadge`,0],[`license_cop_cAir`,0],[`license_cop_cg`,0],[`license_cop_swat`,0]]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

cursor.execute("SELECT * FROM players WHERE med_licenses NOT LIKE \"[[`license_med_mAir`,0],[`license_med_mBoat`,0]]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET med_licenses = \"[[`license_med_mAir`,0],[`license_med_mBoat`,0]]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

print "Removed + Compensated for licenses.."

cursor.execute("SELECT * FROM players WHERE civ_gear NOT LIKE \"[]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET civ_gear = \"[]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

cursor.execute("SELECT * FROM players WHERE cop_gear NOT LIKE \"[]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET cop_gear = \"[]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

cursor.execute("SELECT * FROM players WHERE med_gear NOT LIKE \"[]\"")
for (players) in cursor:
    cursor1.execute("UPDATE players SET med_gear = \"[]\" WHERE pid IN(%s)", (str(players[3])))
    if players[3] not in compensated:
        compensated.append(players[3])
cnx.commit()

print "Removed + Compensated for gear.."

cursor1.execute("UPDATE players SET bankacc = bankacc + 250000 WHERE pid IN(%s)" % ', '.join(compensated))

cursor.execute("SELECT * FROM vehicles")
for (vehicles) in cursor:
    price = 0
    if (vehicles[2] == 'I_C_Offroad_02_unarmed_F'):
        price = 25000
    elif (vehicles[2] == 'O_T_VTOL_02_infantry_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_infantry_ghex_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_infantry_hex_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_vehicle_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_vehicle_ghex_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_vehicle_hex_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_vehicle_grey_F'):
        price = 1750000
    elif (vehicles[2] == 'O_T_VTOL_02_infantry_grey_F'):
        price = 1750000
    elif (vehicles[2] == 'B_T_VTOL_01_vehicle_olive_F'):
        price = 2950000
    elif (vehicles[2] == 'B_T_VTOL_01_infantry_olive_F'):
        price = 2950000
    elif (vehicles[2] == 'B_T_VTOL_01_vehicle_blue_FF'):
        price = 2950000
    elif (vehicles[2] == 'B_T_VTOL_01_infantry_blue_F'):
        price = 2950000
    elif (vehicles[2] == 'B_Plane_CAS_01_F'):
        price = 10000000
    elif (vehicles[2] == 'O_Plane_CAS_02_F'):
        price = 7500000
    elif (vehicles[2] == 'I_Plane_Fighter_03_AA_F'):
        price = 5000000
    elif (vehicles[2] == 'C_PLANE_Civil_01_F'):
        price = 575000
    elif (vehicles[2] == 'C_PLANE_Civil_01_racing_F'):
        price = 575000
    elif (vehicles[2] == 'I_C_Plane_Civil_01_F'):
        price = 375000
    elif (vehicles[2] == 'B_LSV_01_unarmed_black_F'):
        price = 250000
    elif (vehicles[2] == 'O_T_LSV_02_unarmed_black_F'):
        price = 250000
    elif (vehicles[2] == 'O_T_LSV_02_unarmed_ghex_F'):
        price = 250000
    elif (vehicles[2] == 'B_T_LSV_01_unarmed_CTRG_F'):
        price = 250000
    elif (vehicles[2] == 'C_Scooter_Transport_01_F'):
        price = 250000
    elif (vehicles[2] == 'I_Truck_02_medical_F'):
        price = 250000
    elif (vehicles[2] == 'C_Truck_02_box_F'):
        price = 250000
    elif (vehicles[2] == 'O_Truck_03_medical_F'):
        price = 45000
    elif (vehicles[2] == 'B_Truck_01_medical_F'):
        price = 60000
    elif (vehicles[2] == 'C_Rubberboat'):
        price = 15000
    elif (vehicles[2] == 'I_Heli_light_03_unarmed_F'):
        price = 950000
    elif (vehicles[2] == 'B_Heli_Transport_01_F'):
        price = 1250000
    elif (vehicles[2] == 'B_Heli_Transport_03_black_F'):
        price = 1250000
    elif (vehicles[2] == 'B_MRAP_01_hmg_F'):
        price = 1500000
    elif (vehicles[2] == 'O_APC_Wheeled_02_rcws_F'):
        price = 2500000
    elif (vehicles[2] == 'I_MRAP_03_F'):
        price = 1250000
    elif (vehicles[2] == 'B_Boat_Armed_01_minigun_F'):
        price = 600000
    elif (vehicles[2] == 'B_Boat_Transport_01_F'):
        price = 15000
    elif (vehicles[2] == 'O_Truck_03_transport_F'):
        price = 200000
    elif (vehicles[2] == 'O_Truck_03_device_F'):
        price = 1250000
    elif (vehicles[2] == 'O_T_Truck_03_ammo_ghex_F'):
        price = 550000
    elif (vehicles[2] == 'B_G_Offroad_01_F'):
        price = 20000
    elif (vehicles[2] == 'B_G_Offroad_01_armed_F'):
        price = 1950000
    elif (vehicles[2] == 'O_MRAP_02_hmg_F'):
        price = 5500000
    elif (vehicles[2] == 'C_Offroad_02_unarmed_F'):
        price = 25000
    elif (vehicles[2] == 'C_Boat_Civil_01_F'):
        price = 75000
    elif (vehicles[2] == 'C_Boat_Civil_01_police_F'):
        price = 75000
    elif (vehicles[2] == 'B_Truck_01_box_F'):
        price = 650000
    elif (vehicles[2] == 'B_Truck_01_transport_F'):
        price = 275000
    elif (vehicles[2] == 'O_MRAP_02_F'):
        price = 950000
    elif (vehicles[2] == 'C_Offroad_01_F'):
        price = 20000
    elif (vehicles[2] == 'C_Kart_01_Blu_F'):
        price = 15000
    elif (vehicles[2] == 'C_Hatchback_01_sport_F'):
        price = 100000
    elif (vehicles[2] == 'B_Quadbike_01_F'):
        price = 4500
    elif (vehicles[2] == 'I_Truck_02_covered_F'):
        price = 125000
    elif (vehicles[2] == 'I_Truck_02_transport_F'):
        price = 100000
    elif (vehicles[2] == 'O_Truck_03_covered_F'):
        price = 250000
    elif (vehicles[2] == 'C_Hatchback_01_F'):
        price = 13500
    elif (vehicles[2] == 'C_SUV_01_F'):
        price = 45000
    elif (vehicles[2] == 'C_Van_01_transport_F'):
        price = 55000
    elif (vehicles[2] == 'C_Van_01_box_F'):
        price = 95000
    elif (vehicles[2] == 'B_MRAP_01_F'):
        price = 950000
    elif (vehicles[2] == 'B_Heli_Light_01_stripped_F'):
        price = 275000
    elif (vehicles[2] == 'I_Heli_Transport_02_F'):
        price = 950000
    elif (vehicles[2] == 'B_Heli_Transport_03_unarmed_green_F'):
        price = 1250000
    elif (vehicles[2] == 'O_Heli_Transport_04_Box_F'):
        price = 2250000
    elif (vehicles[2] == 'O_Heli_Transport_04_covered_F'):
        price = 950000
    elif (vehicles[2] == 'O_Heli_Transport_04_fuel_F'):
        price = 950000
    elif (vehicles[2] == 'O_Heli_Transport_04_medevac_F'):
        price = 950000
    elif (vehicles[2] == 'O_Heli_Transport_04_repair_F'):
        price = 950000
    elif (vehicles[2] == 'B_Heli_Light_01_F'):
        price = 250000
    elif (vehicles[2] == 'C_Heli_Light_01_civil_F'):
        price = 250000
    elif (vehicles[2] == 'O_Heli_Light_02_unarmed_F'):
        price = 750000
    elif (vehicles[2] == 'B_SDV_01_F'):
        price = 150000
    elif (vehicles[2] == 'C_Van_01_fuel_F'):
        price = 175000
    elif (vehicles[2] == 'I_Truck_02_fuel_F'):
        price = 250000
    elif (vehicles[2] == 'B_Truck_01_fuel_F'):
        price = 300000
    else:
        price = 0
    cursor1.execute("UPDATE players SET bankacc = bankacc + %s WHERE pid IN(%s)", (price, str(vehicles[4])))
    cursor1.execute("DELETE FROM vehicles WHERE id IN(%s)", (vehicles[0]))
cnx.commit()

print "Removed + Compensated for vehicles.."

cursor1.execute("UPDATE players SET bankacc = bankacc * 0.175")
cursor1.execute("UPDATE players SET cash = cash * 0.175")
cursor1.execute("UPDATE gangs SET bank = bank * 0.175")

print "Nerfed money... DONE"
