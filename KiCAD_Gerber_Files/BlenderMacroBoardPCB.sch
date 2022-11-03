EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Switch:SW_Push Button2
U 1 1 6308EF94
P 6000 2200
F 0 "Button2" H 6000 2485 50  0000 C CNN
F 1 "SW_Push" H 6000 2394 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 6000 2400 50  0001 C CNN
F 3 "~" H 6000 2400 50  0001 C CNN
	1    6000 2200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button1
U 1 1 6308DFD0
P 3200 2200
F 0 "Button1" H 3200 2485 50  0000 C CNN
F 1 "SW_Push" H 3200 2394 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 3200 2400 50  0001 C CNN
F 3 "~" H 3200 2400 50  0001 C CNN
	1    3200 2200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button5
U 1 1 63096316
P 6000 2950
F 0 "Button5" H 6000 3235 50  0000 C CNN
F 1 "SW_Push" H 6000 3144 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 6000 3150 50  0001 C CNN
F 3 "~" H 6000 3150 50  0001 C CNN
	1    6000 2950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button4
U 1 1 63096A24
P 3200 2950
F 0 "Button4" H 3200 3235 50  0000 C CNN
F 1 "SW_Push" H 3200 3144 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 3200 3150 50  0001 C CNN
F 3 "~" H 3200 3150 50  0001 C CNN
	1    3200 2950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button7
U 1 1 630970E0
P 3200 3650
F 0 "Button7" H 3200 3935 50  0000 C CNN
F 1 "SW_Push" H 3200 3844 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 3200 3850 50  0001 C CNN
F 3 "~" H 3200 3850 50  0001 C CNN
	1    3200 3650
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button8
U 1 1 6309750D
P 6000 3650
F 0 "Button8" H 6000 3935 50  0000 C CNN
F 1 "SW_Push" H 6000 3844 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 6000 3850 50  0001 C CNN
F 3 "~" H 6000 3850 50  0001 C CNN
	1    6000 3650
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Reset1
U 1 1 630992A1
P 6000 1250
F 0 "Reset1" H 6000 1535 50  0000 C CNN
F 1 "SW_Push" H 6000 1444 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 6000 1450 50  0001 C CNN
F 3 "~" H 6000 1450 50  0001 C CNN
	1    6000 1250
	1    0    0    -1  
$EndComp
$Comp
L Device:Rotary_Encoder_Switch Rotary2
U 1 1 6309A834
P 5950 4450
F 0 "Rotary2" H 5950 4817 50  0000 C CNN
F 1 "Rotary_Encoder_Switch" H 5950 4726 50  0000 C CNN
F 2 "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm" H 5800 4610 50  0001 C CNN
F 3 "~" H 5950 4710 50  0001 C CNN
	1    5950 4450
	1    0    0    -1  
$EndComp
$Comp
L Device:Rotary_Encoder_Switch Rotary1
U 1 1 63099E7F
P 3150 4450
F 0 "Rotary1" H 3150 4817 50  0000 C CNN
F 1 "Rotary_Encoder_Switch" H 3150 4726 50  0000 C CNN
F 2 "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm" H 3000 4610 50  0001 C CNN
F 3 "~" H 3150 4710 50  0001 C CNN
	1    3150 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 3650 6200 2950
Wire Wire Line
	6200 2200 6200 2500
Connection ~ 6200 2200
Connection ~ 6200 2950
Wire Wire Line
	3400 2200 3400 2500
Wire Wire Line
	3400 3650 3400 2950
Connection ~ 3400 2950
Wire Wire Line
	6250 3650 6200 3650
Connection ~ 6200 3650
Wire Wire Line
	3450 3650 3400 3650
Connection ~ 3400 3650
Text Label 1200 5500 0    50   ~ 0
Button0
Wire Wire Line
	5800 3650 5450 3650
Wire Wire Line
	5800 2950 5400 2950
Wire Wire Line
	5800 2200 5400 2200
Wire Wire Line
	3000 2200 2550 2200
Wire Wire Line
	3000 2950 2550 2950
Wire Wire Line
	3000 3650 2550 3650
Text Label 2550 2200 0    50   ~ 0
Button1
Text Label 5400 2200 0    50   ~ 0
Button2
Text Label 2550 2950 0    50   ~ 0
Button4
Text Label 5400 2950 0    50   ~ 0
Button5
Text Label 2550 3650 0    50   ~ 0
Button7
Text Label 5450 3650 0    50   ~ 0
Button8
Wire Wire Line
	3800 5500 4550 5500
Wire Wire Line
	6200 1650 5450 1650
Wire Wire Line
	6200 1650 6200 2200
Text Label 5450 1650 0    50   ~ 0
Power
Text Label 4550 5500 0    50   ~ 0
Power
Wire Wire Line
	3450 3650 3450 4000
Wire Wire Line
	2850 4450 2700 4450
Wire Wire Line
	2700 4450 2700 4000
Wire Wire Line
	2700 4000 3450 4000
Connection ~ 3450 4000
Wire Wire Line
	3450 4000 3450 4350
Wire Wire Line
	6250 3650 6250 4000
Wire Wire Line
	5650 4450 5500 4450
Wire Wire Line
	5500 4000 6250 4000
Connection ~ 6250 4000
Wire Wire Line
	6250 4000 6250 4350
Wire Wire Line
	2850 4550 2000 4550
Wire Wire Line
	2850 4350 2000 4350
Wire Wire Line
	5650 4550 4900 4550
Text Label 2000 4350 0    50   ~ 0
Rotary1A
Text Label 2000 4550 0    50   ~ 0
Rotary1B
Text Label 4900 4350 0    50   ~ 0
Rotary2A
Text Label 4900 4550 0    50   ~ 0
Rotary2B
Text Label 7750 4350 0    50   ~ 0
Rotary3A
Text Label 7750 4550 0    50   ~ 0
Rotary3B
Wire Wire Line
	5800 1250 5250 1250
Wire Wire Line
	3800 6500 4600 6500
Text Label 5250 1250 0    50   ~ 0
Reset
Text Label 4600 6500 0    50   ~ 0
Reset
Wire Wire Line
	3800 6600 4600 6600
Wire Wire Line
	3450 4550 3450 4650
Wire Wire Line
	3450 4650 3550 4650
Wire Wire Line
	6250 4550 6250 4650
Wire Wire Line
	6250 4650 6350 4650
Text Label 3550 4650 0    50   ~ 0
Rotary1Push
Text Label 6350 4650 0    50   ~ 0
Rotary2Push
Text Label 9250 4650 0    50   ~ 0
Rotary3Push
Wire Wire Line
	9150 4650 9250 4650
Wire Wire Line
	9150 4550 9150 4650
Wire Wire Line
	8550 4550 7750 4550
Wire Wire Line
	8550 4350 7750 4350
Wire Wire Line
	9150 4000 9150 4350
Connection ~ 9150 4000
Wire Wire Line
	8400 4000 9150 4000
Wire Wire Line
	8400 4450 8400 4000
Wire Wire Line
	8550 4450 8400 4450
Wire Wire Line
	9150 3650 9150 4000
Text Label 8300 3650 0    50   ~ 0
Button9
Text Label 8250 2950 0    50   ~ 0
Button6
Text Label 8250 2200 0    50   ~ 0
Button3
Wire Wire Line
	8600 3650 8300 3650
Wire Wire Line
	8600 2950 8250 2950
Wire Wire Line
	8600 2200 8250 2200
Text Label 8350 1350 0    50   ~ 0
Button0
Wire Wire Line
	8600 1350 8350 1350
Connection ~ 9000 3650
Wire Wire Line
	9150 3650 9000 3650
Connection ~ 9000 2200
Connection ~ 9000 2950
Wire Wire Line
	9000 2950 9000 2500
Wire Wire Line
	9000 2950 9000 3650
Wire Wire Line
	9000 1350 9000 2200
$Comp
L Switch:SW_Push Button3
U 1 1 630912A4
P 8800 2200
F 0 "Button3" H 8800 2485 50  0000 C CNN
F 1 "SW_Push" H 8800 2394 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 8800 2400 50  0001 C CNN
F 3 "~" H 8800 2400 50  0001 C CNN
	1    8800 2200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button0
U 1 1 63097FEA
P 8800 1350
F 0 "Button0" H 8800 1635 50  0000 C CNN
F 1 "SW_Push" H 8800 1544 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 8800 1550 50  0001 C CNN
F 3 "~" H 8800 1550 50  0001 C CNN
	1    8800 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:Rotary_Encoder_Switch Rotary3
U 1 1 6309B9D4
P 8850 4450
F 0 "Rotary3" H 8850 4817 50  0000 C CNN
F 1 "Rotary_Encoder_Switch" H 8850 4726 50  0000 C CNN
F 2 "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm" H 8700 4610 50  0001 C CNN
F 3 "~" H 8850 4710 50  0001 C CNN
	1    8850 4450
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button9
U 1 1 630979F8
P 8800 3650
F 0 "Button9" H 8800 3935 50  0000 C CNN
F 1 "SW_Push" H 8800 3844 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 8800 3850 50  0001 C CNN
F 3 "~" H 8800 3850 50  0001 C CNN
	1    8800 3650
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Button6
U 1 1 63095E40
P 8800 2950
F 0 "Button6" H 8800 3235 50  0000 C CNN
F 1 "SW_Push" H 8800 3144 50  0000 C CNN
F 2 "Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB" H 8800 3150 50  0001 C CNN
F 3 "~" H 8800 3150 50  0001 C CNN
	1    8800 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 7400 4600 7400
Wire Wire Line
	3800 6100 4600 6100
Text Label 4600 7400 0    50   ~ 0
Rotary1A
Text Label 4550 6800 0    50   ~ 0
Button4
Text Label 4600 6100 0    50   ~ 0
Rotary0Push
Wire Wire Line
	3400 2500 4500 2500
Connection ~ 3400 2500
Wire Wire Line
	3400 2500 3400 2950
Connection ~ 6200 2500
Wire Wire Line
	6200 2500 6200 2950
Wire Wire Line
	6200 2500 9000 2500
Connection ~ 9000 2500
Wire Wire Line
	9000 2500 9000 2200
Wire Wire Line
	5650 4350 4900 4350
Wire Wire Line
	5500 4450 5500 4000
$Comp
L Device:Rotary_Encoder_Switch Rotary0
U 1 1 6317F81A
P 3100 1450
F 0 "Rotary0" H 3100 1817 50  0000 C CNN
F 1 "Rotary_Encoder_Switch" H 3100 1726 50  0000 C CNN
F 2 "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm" H 2950 1610 50  0001 C CNN
F 3 "~" H 3100 1710 50  0001 C CNN
	1    3100 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2800 1450 2650 1450
Wire Wire Line
	2650 1450 2650 1000
Wire Wire Line
	2650 1000 3400 1000
Wire Wire Line
	2800 1550 1950 1550
Wire Wire Line
	2800 1350 1950 1350
Text Label 1950 1350 0    50   ~ 0
Rotary0A
Text Label 1950 1550 0    50   ~ 0
Rotary0B
Wire Wire Line
	3400 1550 3400 1650
Wire Wire Line
	3400 1650 3500 1650
Text Label 3500 1650 0    50   ~ 0
Rotary0Push
Wire Wire Line
	4500 2500 4500 1100
Connection ~ 4500 2500
Wire Wire Line
	4500 2500 6200 2500
Text Label 1200 6100 0    50   ~ 0
Button2
Text Label 6200 1250 0    50   ~ 0
Ground
Text Label 1200 5700 0    50   ~ 0
Ground
Text Label 1200 6300 0    50   ~ 0
Button5
Text Label 1200 6400 0    50   ~ 0
Button3
Text Label 1200 6500 0    50   ~ 0
Button6
Wire Wire Line
	3400 1000 3400 1100
Wire Wire Line
	4500 1100 3400 1100
Connection ~ 3400 1100
Wire Wire Line
	3400 1100 3400 1350
Text Label 1200 6600 0    50   ~ 0
Button9
Text Label 1200 6800 0    50   ~ 0
Rotary3Push
Text Label 1200 6900 0    50   ~ 0
Rotary2Push
Wire Wire Line
	3800 6800 4550 6800
Text Label 4600 6600 0    50   ~ 0
Button1
Wire Wire Line
	3800 6900 4600 6900
Text Label 4600 6900 0    50   ~ 0
Button7
Wire Wire Line
	3800 7000 4600 7000
Text Label 4600 7000 0    50   ~ 0
Button8
Wire Wire Line
	3800 7100 4600 7100
Text Label 4600 7100 0    50   ~ 0
Rotary1Push
Wire Wire Line
	3800 6300 4600 6300
Text Label 4600 6300 0    50   ~ 0
Rotary0B
Wire Wire Line
	3800 6400 4600 6400
Text Label 4600 6400 0    50   ~ 0
Rotary0A
Text Label 1200 7000 0    50   ~ 0
Rotary2B
Text Label 1200 7100 0    50   ~ 0
Rotary2A
Text Label 1200 7300 0    50   ~ 0
Rotary3B
Text Label 1200 7400 0    50   ~ 0
Rotary3A
Text Label 4600 7300 0    50   ~ 0
Rotary1B
Wire Wire Line
	2400 7400 1200 7400
Wire Wire Line
	2400 7300 1200 7300
Wire Wire Line
	2400 7100 1200 7100
Wire Wire Line
	2400 7000 1200 7000
Wire Wire Line
	1200 6900 2400 6900
Wire Wire Line
	1200 6800 2400 6800
Wire Wire Line
	1200 6600 2400 6600
Wire Wire Line
	1200 6500 2400 6500
Wire Wire Line
	1200 6400 2400 6400
Wire Wire Line
	1200 6300 2400 6300
Wire Wire Line
	1200 6100 2400 6100
Wire Wire Line
	1200 5700 2400 5700
Wire Wire Line
	1200 5500 2400 5500
Wire Wire Line
	4600 7300 3800 7300
$Comp
L MCU_RaspberryPi_and_Boards:Pico Pico1
U 1 1 6318FD82
P 3100 6450
F 0 "Pico1" H 3100 7665 50  0000 C CNN
F 1 "Pico" H 3100 7574 50  0000 C CNN
F 2 "RPi_Pico:RPi_Pico_SMD_TH" V 3100 6450 50  0001 C CNN
F 3 "" H 3100 6450 50  0001 C CNN
	1    3100 6450
	1    0    0    -1  
$EndComp
$EndSCHEMATC
