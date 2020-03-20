class Elements():
    def __init__(self):
        self.elementName = ""
        self.atomicSymbol = ""
        self.atomicNumber = 0
        self.atomicWeight = 0.0
        self.density = 0.0
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 0
        self.groupNumber = 0
        self.group = ""
        self.elementGroup = ""
        self.electronConfiguration = ""

    def element_1(self):
        self.elementName = "Hydrogen"
        self.atomicSymbol = "H"
        self.atomicNumber = 1
        self.atomicWeight = 1.0078
        self.density = 0.0000899
        self.meltingPointKelvin = 14.01
        self.boilingPointKelvin = 20.28
        self.oxidationState = [-1,1]
        self.electronegativity = 2.2
        self.period = 1
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = "1s\u00B1"

    def element_2(self):
        self.elementName = "Helium"
        self.atomicSymbol = "He"
        self.atomicNumber = 2
        self.atomicWeight = 4.0026
        self.density = 0.00017846
        self.meltingPointKelvin = 0.95
        self.boilingPointKelvin = 4.25
        self.oxidationState = [1]
        self.electronegativity = 0.0
        self.period = 1
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = "1s\u00B2"
    
    def element_3(self):
        self.elementName = "Lithium"
        self.atomicSymbol = "Li"
        self.atomicNumber = 3
        self.atomicWeight = 6.941
        self.density = 0.534
        self.meltingPointKelvin = 453.65
        self.boilingPointKelvin = 1615.15
        self.oxidationState = [1]
        self.electronegativity = 0.98
        self.period = 2
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = "1s\u00B22s\u00B1"

    def element_4(self):
        self.elementName = "Beryllium"
        self.atomicSymbol = "Be"
        self.atomicNumber = 4
        self.atomicWeight = 9.0121
        self.density = 1.848
        self.meltingPointKelvin = 1551.15
        self.boilingPointKelvin = 3243.15
        self.oxidationState = [2]
        self.electronegativity = 1.57
        self.period = 2
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "Alkaline Earth Metals"
        self.electronConfiguration = "1s\u00B22s\u00B2"

    def element_5(self):
        self.elementName = "Boron"
        self.atomicSymbol = "B"
        self.atomicNumber = 5
        self.atomicWeight = 10.811
        self.density = 2.34
        self.meltingPointKelvin = 2348.95
        self.boilingPointKelvin = 4199.95
        self.oxidationState = [3]
        self.electronegativity = 2.04
        self.period = 2
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Metalloids"
        self.electronConfiguration = "1s\u00B22s\u00B22p\u00B1"

    def element_6(self):
        self.elementName = "Carbon"
        self.atomicSymbol = "C"
        self.atomicNumber = 6
        self.atomicWeight = 12.0107
        self.density = 2.26
        self.meltingPointKelvin = 3823.15
        self.boilingPointKelvin = 5100.15
        self.oxidationState = [2,4,-4]
        self.electronegativity = 2.55
        self.period = 2
        self.groupNumber = 14
        self.group = "IVA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = "1s\u00B22s\u00B22p\u00B2"

    def element_7(self):
        self.elementName = "Nitrogen"
        self.atomicSymbol = "N"
        self.atomicNumber = 7
        self.atomicWeight = 14.0067
        self.density = 0.001251
        self.meltingPointKelvin = 63.25
        self.boilingPointKelvin = 77.35
        self.oxidationState = [1,2,3,4,5,-1,-2,-3,-4,-5]
        self.electronegativity = 3.04
        self.period = 2
        self.groupNumber = 15
        self.group = "VB"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = "1s\u00B22s\u00B22p\u00B3"

    def element_8(self):
        self.elementName = "Oxygen"
        self.atomicSymbol = "O"
        self.atomicNumber = 8
        self.atomicWeight = 15.9994
        self.density = 0.00142897
        self.meltingPointKelvin = 54.36
        self.boilingPointKelvin = 90.19
        self.oxidationState = []
        self.electronegativity = 3.44
        self.period = 2
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = ""

    def element_9(self):
        self.elementName = "Fluorine"
        self.atomicSymbol = "F"
        self.atomicNumber = 9
        self.atomicWeight = 18.9984
        self.density = 0.001696
        self.meltingPointKelvin = 53.48
        self.boilingPointKelvin = 85.04
        self.oxidationState = []
        self.electronegativity = 3.98
        self.period = 2
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""	
        
    def element_10(self):
        self.elementName = "Neon"
        self.atomicSymbol = "Ne"
        self.atomicNumber = 10
        self.atomicWeight = 20.1797
        self.density =0.0009002
        self.meltingPointKelvin = 24.48
        self.boilingPointKelvin = 27.1
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 2
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""  
        
    def element_11(self):
        self.elementName = "Sodium"
        self.atomicSymbol = "Na"
        self.atomicNumber = 11
        self.atomicWeight = 22.9897
        self.density = 0.971
        self.meltingPointKelvin = 370.95
        self.boilingPointKelvin = 1156.09
        self.oxidationState = []
        self.electronegativity = 0.93
        self.period = 3
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = ""    
        
    def element_12(self):
        self.elementName = "Magnesium"
        self.atomicSymbol = "Mg"
        self.atomicNumber = 12
        self.atomicWeight = 24.3050
        self.density = 1.738
        self.meltingPointKelvin = 923.15
        self.boilingPointKelvin = 1363.15
        self.oxidationState = []
        self.electronegativity = 1.31
        self.period = 3
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "Alkaline Earth Metals"
        self.electronConfiguration = ""
        
    def element_13(self):
        self.elementName = "Aluminum"
        self.atomicSymbol = "Al"
        self.atomicNumber = 13
        self.atomicWeight = 26.9815
        self.density = 2.6989
        self.meltingPointKelvin = 933.15
        self.boilingPointKelvin = 2791.97
        self.oxidationState = []
        self.electronegativity = 1.61
        self.period = 3
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_14(self):
        self.elementName = "Silicon"
        self.atomicSymbol = "Si"
        self.atomicNumber = 14
        self.atomicWeight = 28.0855
        self.density = 2.33
        self.meltingPointKelvin = 1688.0
        self.boilingPointKelvin = 3538.15
        self.oxidationState = []
        self.electronegativity = 1.9
        self.period = 3
        self.groupNumber = 14
        self.group = "VIA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_15(self):
        self.elementName = "Phosphorus"
        self.atomicSymbol = "P"
        self.atomicNumber = 15
        self.atomicWeight = 30.9737
        self.density = 2.82
        self.meltingPointKelvin = 317.3
        self.boilingPointKelvin = 553.65
        self.oxidationState = []
        self.electronegativity = 2.19
        self.period = 3
        self.groupNumber = 15
        self.group = "VA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = ""
        
    def element_16(self):
        self.elementName = "Sulfur"
        self.atomicSymbol = "S"
        self.atomicNumber = 16
        self.atomicWeight = 32.065
        self.density = 2.070
        self.meltingPointKelvin = 385.95
        self.boilingPointKelvin = 717.82
        self.oxidationState = []
        self.electronegativity =2.58
        self.period = 3
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = ""
        
    def element_17(self):
        self.elementName = "Chlorine"
        self.atomicSymbol = "Cl"
        self.atomicNumber = 17
        self.atomicWeight = 35.453
        self.density = 0.00321
        self.meltingPointKelvin = 172.17
        self.boilingPointKelvin = 238.55
        self.oxidationState = []
        self.electronegativity = 3.16
        self.period = 3
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""
        
    def element_18(self):
        self.elementName = "Argon"
        self.atomicSymbol = "Ar"
        self.atomicNumber = 18
        self.atomicWeight = 39.948
        self.density = 0.001784
        self.meltingPointKelvin = 88.81
        self.boilingPointKelvin = 87.3
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 3
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""
        
    def element_19(self):
        self.elementName = "Potassium"
        self.atomicSymbol = "K"
        self.atomicNumber = 19
        self.atomicWeight = 39.0983
        self.density = 0.856
        self.meltingPointKelvin = 336.53
        self.boilingPointKelvin = 1031.95
        self.oxidationState = []
        self.electronegativity = 0.82
        self.period = 4
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = ""
        
    def element_20(self):
        self.elementName = "Calcium"
        self.atomicSymbol = "Ca"
        self.atomicNumber = 20
        self.atomicWeight = 40.078
        self.density = 1.55
        self.meltingPointKelvin = 1115.15
        self.boilingPointKelvin = 1757.15
        self.oxidationState = []
        self.electronegativity = 1
        self.period = 4
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "ALKALI EARTH METALS"
        self.electronConfiguration = ""
        
    def element_21(self):
        self.elementName = "Scandium"
        self.atomicSymbol = "Sc"
        self.atomicNumber = 21
        self.atomicWeight = 44.9559
        self.density = 2.99
        self.meltingPointKelvin = 1814.15
        self.boilingPointKelvin = 3109.15
        self.oxidationState = []
        self.electronegativity = 1.36
        self.period = 4
        self.groupNumber = 3
        self.group = "IIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_22(self):
        self.elementName = "Titanium"
        self.atomicSymbol = "Ti"
        self.atomicNumber = 22
        self.atomicWeight = 47.867
        self.density = 4.54
        self.meltingPointKelvin = 1933.15
        self.boilingPointKelvin = 3560.15
        self.oxidationState = []
        self.electronegativity = 1.54
        self.period = 4
        self.groupNumber = 4
        self.group = "IVB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_23(self):
        self.elementName = "Vanadium"
        self.atomicSymbol = "V"
        self.atomicNumber = 23
        self.atomicWeight = 50.9415
        self.density = 6.11
        self.meltingPointKelvin = 2183.15
        self.boilingPointKelvin = 3860.15
        self.oxidationState = []
        self.electronegativity = 1.63
        self.period = 4
        self.groupNumber = 5
        self.group = "VB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_24(self):
        self.elementName = "Chromium"
        self.atomicSymbol = "Cr"
        self.atomicNumber = 24
        self.atomicWeight = 51.9961
        self.density = 7.19
        self.meltingPointKelvin = 2180.15
        self.boilingPointKelvin = 2945.15
        self.oxidationState = []
        self.electronegativity = 1.66
        self.period = 4
        self.groupNumber = 6
        self.group = "VIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_25(self):
        self.elementName = "Manganese"
        self.atomicSymbol = "Mn"
        self.atomicNumber = 25
        self.atomicWeight = 54.9380
        self.density = 7.21
        self.meltingPointKelvin = 1518.15
        self.boilingPointKelvin = 2334.15
        self.oxidationState = []
        self.electronegativity = 1.55
        self.period = 4
        self.groupNumber = 7
        self.group = "VIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_26(self):
        self.elementName = "Iron"
        self.atomicSymbol = "Fe"
        self.atomicNumber = 26
        self.atomicWeight = 55.845
        self.density = 7.88
        self.meltingPointKelvin = 1812.15
        self.boilingPointKelvin = 3135.15
        self.oxidationState = []
        self.electronegativity = 1.83
        self.period = 4
        self.groupNumber = 8
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_27(self):
        self.elementName = "Cobalt"
        self.atomicSymbol = "Co"
        self.atomicNumber = 27
        self.atomicWeight = 58.9331
        self.density = 8.9
        self.meltingPointKelvin = 1766.15
        self.boilingPointKelvin = 3143.15
        self.oxidationState = []
        self.electronegativity = 1.88
        self.period = 4
        self.groupNumber = 9
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_28(self):
        self.elementName = "Nickel"
        self.atomicSymbol = "Ni"
        self.atomicNumber = 28
        self.atomicWeight = 58.6934
        self.density = 8.902
        self.meltingPointKelvin = 1728.15
        self.boilingPointKelvin = 3188.15
        self.oxidationState = []
        self.electronegativity = 1.91
        self.period = 4
        self.groupNumber = 10
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_29(self):
        self.elementName = "Copper"
        self.atomicSymbol = "Cu"
        self.atomicNumber = 29
        self.atomicWeight = 63.546
        self.density = 8.92
        self.meltingPointKelvin = 1357.77
        self.boilingPointKelvin = 2835.15
        self.oxidationState = []
        self.electronegativity = 1.9
        self.period = 4
        self.groupNumber = 11
        self.group = "IB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_30(self):
        self.elementName = "Zinc"
        self.atomicSymbol = "Zn"
        self.atomicNumber = 30
        self.atomicWeight = 65.409
        self.density = 7.133
        self.meltingPointKelvin = 692.65
        self.boilingPointKelvin = 1179.15
        self.oxidationState = []
        self.electronegativity = 1.65
        self.period = 4
        self.groupNumber = 12
        self.group = "IIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_31(self):
        self.elementName = "Gallium"
        self.atomicSymbol = "Ga"
        self.atomicNumber = 31
        self.atomicWeight = 69.723
        self.density =5.91
        self.meltingPointKelvin = 302.95
        self.boilingPointKelvin = 2476.15
        self.oxidationState = []
        self.electronegativity = 1.81
        self.period = 4
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_32(self):
        self.elementName = "Germanium"
        self.atomicSymbol = "Ge"
        self.atomicNumber = 32
        self.atomicWeight = 72.64
        self.density = 5.323
        self.meltingPointKelvin = 1210.65
        self.boilingPointKelvin = 3106.15
        self.oxidationState = []
        self.electronegativity = 2.01
        self.period = 4
        self.groupNumber = 14
        self.group = "IVA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_33(self):
        self.elementName = "Arsenic"
        self.atomicSymbol = "As"
        self.atomicNumber = 33
        self.atomicWeight = 74.9216
        self.density = 5.72
        self.meltingPointKelvin = 1089.95
        self.boilingPointKelvin = 886.15
        self.oxidationState = []
        self.electronegativity = 2.18
        self.period = 4
        self.groupNumber = 15
        self.group = "VA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_34(self):
        self.elementName = "Selenium"
        self.atomicSymbol = "Se"
        self.atomicNumber = 34
        self.atomicWeight = 78.96
        self.density = 4.79
        self.meltingPointKelvin = 490.15
        self.boilingPointKelvin = 957.95
        self.oxidationState = []
        self.electronegativity = 2.55
        self.period = 4
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "Non-metals"
        self.electronConfiguration = ""
        
    def element_35(self):
        self.elementName = "Bromine"
        self.atomicSymbol = "Br"
        self.atomicNumber = 35
        self.atomicWeight = 79.904
        self.density = 3.14
        self.meltingPointKelvin = 265.9
        self.boilingPointKelvin = 331.95
        self.oxidationState = []
        self.electronegativity = 2.96
        self.period = 4
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""
        
    def element_36(self):
        self.elementName = "Krypton"
        self.atomicSymbol = "Kr"
        self.atomicNumber = 36
        self.atomicWeight = 88.798
        self.density = 0.003749
        self.meltingPointKelvin = 115.78
        self.boilingPointKelvin = 119.75
        self.oxidationState = []
        self.electronegativity = 3
        self.period = 4
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""
        
    def element_37(self):
        self.elementName = "Rubidium"
        self.atomicSymbol = Rb""
        self.atomicNumber = 37
        self.atomicWeight = 85.467
        self.density = 1.53
        self.meltingPointKelvin = 312.47
        self.boilingPointKelvin = 960.35
        self.oxidationState = []
        self.electronegativity = 0.82
        self.period = 5
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = ""
        
    def element_38(self):
        self.elementName = "Strontium"
        self.atomicSymbol = "Sr"
        self.atomicNumber = 38
        self.atomicWeight = 87.62
        self.density = 2.54
        self.meltingPointKelvin = 1050.15
        self.boilingPointKelvin = 1655.15
        self.oxidationState = []
        self.electronegativity = 0.95
        self.period = 5
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "Alkaline Earth Metals"
        self.electronConfiguration = ""
        
    def element_39(self):
        self.elementName = "Yttrium"
        self.atomicSymbol = "Y"
        self.atomicNumber = 39
        self.atomicWeight = 88.905
        self.density = 4.47
        self.meltingPointKelvin = 1799.15
        self.boilingPointKelvin = 3611.15
        self.oxidationState = []
        self.electronegativity = 1.22
        self.period = 5
        self.groupNumber = 3
        self.group = "IIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_40(self):
        self.elementName = "Zirconium"
        self.atomicSymbol = "Zr"
        self.atomicNumber = 40
        self.atomicWeight = 91.224
        self.density = 6.51
        self.meltingPointKelvin = 2128.15
        self.boilingPointKelvin = 4862.15
        self.oxidationState = []
        self.electronegativity = 1.33
        self.period = 5
        self.groupNumber = 4
        self.group = "IVB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_41(self):
        self.elementName = "Niobium"
        self.atomicSymbol = "Nb"
        self.atomicNumber = 41
        self.atomicWeight = 92.906
        self.density = 8.58
        self.meltingPointKelvin = 2750.15
        self.boilingPointKelvin = 5200.15
        self.oxidationState = []
        self.electronegativity = 1.6
        self.period = 5
        self.groupNumber = 4
        self.group = "VB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_42(self):
        self.elementName = "Molybdenum"
        self.atomicSymbol = "Mo"
        self.atomicNumber = 42
        self.atomicWeight = 95.94
        self.density = 10.22
        self.meltingPointKelvin = 2896.15
        self.boilingPointKelvin = 4912.15
        self.oxidationState = []
        self.electronegativity = 2.16
        self.period = 5
        self.groupNumber = 6
        self.group = "VIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_43(self):
        self.elementName = "Technetium"
        self.atomicSymbol = "Tc"
        self.atomicNumber = 43
        self.atomicWeight = 98.906
        self.density = 11.49
        self.meltingPointKelvin = 2430.15
        self.boilingPointKelvin = 4538.15
        self.oxidationState = []
        self.electronegativity = 1.9
        self.period = 5
        self.groupNumber = 7
        self.group = "VIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_44(self):
        self.elementName = "Ruthenium"
        self.atomicSymbol = "Ru"
        self.atomicNumber = 44
        self.atomicWeight = 101.07
        self.density = 12.41
        self.meltingPointKelvin = 2607.15
        self.boilingPointKelvin = 4350.15
        self.oxidationState = []
        self.electronegativity = 2.2
        self.period = 5
        self.groupNumber = 8
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_45(self):
        self.elementName = "Rhodium"
        self.atomicSymbol = "Rh"
        self.atomicNumber = 45
        self.atomicWeight = 102.905
        self.density = 12.41
        self.meltingPointKelvin = 2237.15
        self.boilingPointKelvin = 4000.15
        self.oxidationState = []
        self.electronegativity = 2.28
        self.period = 5
        self.groupNumber = 9
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
    
    def element_46(self):
        self.elementName = "Palladium"
        self.atomicSymbol = "Pd"
        self.atomicNumber = 46
        self.atomicWeight = 106.42
        self.density = 12.02
        self.meltingPointKelvin = 1828.15
        self.boilingPointKelvin = 3236.15
        self.oxidationState = []
        self.electronegativity = 2.2
        self.period = 5
        self.groupNumber = 10
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""

    def element_47(self):
        self.elementName = "Silver"
        self.atomicSymbol = "Ag"
        self.atomicNumber = 47
        self.atomicWeight = 107.868
        self.density = 10.49
        self.meltingPointKelvin = 1234.95
        self.boilingPointKelvin = 2435.15
        self.oxidationState = []
        self.electronegativity = 1.93
        self.period = 5
        self.groupNumber = 11
        self.group = "IB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
    
    def element_48(self):
        self.elementName = "Cadmium"
        self.atomicSymbol = "Cd"
        self.atomicNumber = 48
        self.atomicWeight = 112.411
        self.density = 8.64
        self.meltingPointKelvin = 592.25
        self.boilingPointKelvin = 1039.95
        self.oxidationState = []
        self.electronegativity = 1.69
        self.period = 5
        self.groupNumber = 12
        self.group = "IIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_49(self):
        self.elementName = "Indium"
        self.atomicSymbol = "In"
        self.atomicNumber = 49
        self.atomicWeight = 114.818
        self.density = 7.31
        self.meltingPointKelvin = 429.75
        self.boilingPointKelvin = 2345.15
        self.oxidationState = []
        self.electronegativity = 1.78
        self.period = 5
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_50(self):
        self.elementName = "Tin"
        self.atomicSymbol = "Sn"
        self.atomicNumber = 50
        self.atomicWeight = 118.710
        self.density = 7.29
        self.meltingPointKelvin = 505.08
        self.boilingPointKelvin = 2875.15
        self.oxidationState = []
        self.electronegativity = 1.96
        self.period = 5
        self.groupNumber = 14
        self.group = "IVA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_51(self):
        self.elementName = "Antimony"
        self.atomicSymbol = "Sb"
        self.atomicNumber = 51
        self.atomicWeight = 121.760
        self.density = 6.69
        self.meltingPointKelvin = 903.9
        self.boilingPointKelvin = 1860.15
        self.oxidationState = []
        self.electronegativity = 2.05
        self.period = 5
        self.groupNumber = 15
        self.group = "VA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_52(self):
        self.elementName = "Tellerium"
        self.atomicSymbol = "Te"
        self.atomicNumber = 52
        self.atomicWeight = 127.60
        self.density = 6.25
        self.meltingPointKelvin = 727.7
        self.boilingPointKelvin = 1260.95
        self.oxidationState = []
        self.electronegativity = 2.1
        self.period = 5
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_53(self):
        self.elementName = "Iodine"
        self.atomicSymbol = "I"
        self.atomicNumber = 53
        self.atomicWeight = 126.904
        self.density = 4.94
        self.meltingPointKelvin = 386.7
        self.boilingPointKelvin = 457.5
        self.oxidationState = []
        self.electronegativity = 2.66
        self.period = 5
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""
    
    def element_54(self):
        self.elementName = "Xenon"
        self.atomicSymbol = "Xe"
        self.atomicNumber = 54
        self.atomicWeight = 131.293
        self.density = 0.005894
        self.meltingPointKelvin = 161.35
        self.boilingPointKelvin = 165.05
        self.oxidationState = []
        self.electronegativity = 2.6
        self.period = 5
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""
        
    def element_55(self):
        self.elementName = "Caesium"
        self.atomicSymbol = "Cs"
        self.atomicNumber = 55
        self.atomicWeight = 132.905
        self.density = 1.9
        self.meltingPointKelvin = 301.6
        self.boilingPointKelvin = 943.95
        self.oxidationState = []
        self.electronegativity = 0.79
        self.period = 6
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = ""

    def element_56(self):
        self.elementName = "Barium"
        self.atomicSymbol = "Ba"
        self.atomicNumber = 56
        self.atomicWeight = 137.327
        self.density = 3.5
        self.meltingPointKelvin = 1000.15
        self.boilingPointKelvin = 2170.15
        self.oxidationState = []
        self.electronegativity = 0.89
        self.period = 6
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "ALINE EARTH METALS"
        self.electronConfiguration = ""
    
    def element_57(self):
        self.elementName = "Lanthanium"
        self.atomicSymbol = "La"
        self.atomicNumber = 57
        self.atomicWeight =138.905
        self.density = 6.16
        self.meltingPointKelvin = 1193.15
        self.boilingPointKelvin = 3737.15
        self.oxidationState = []
        self.electronegativity = 1.1
        self.period = 6
        self.groupNumber = 3
        self.group = "IIIB"
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
    
    def element_58(self):
        self.elementName = "Cerium"
        self.atomicSymbol = "Ce"
        self.atomicNumber = 58
        self.atomicWeight = 140.116
        self.density = 6.77
        self.meltingPointKelvin = 1068.15
        self.boilingPointKelvin = 3716.15
        self.oxidationState = []
        self.electronegativity = 1.12
        self.period = 6
        self.groupNumber = 4
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_59(self):
        self.elementName = "Praseodymium"
        self.atomicSymbol = "Pr"
        self.atomicNumber = 59
        self.atomicWeight = 140.904
        self.density = 6.773
        self.meltingPointKelvin = 1204.15
        self.boilingPointKelvin = 3785.15
        self.oxidationState = []
        self.electronegativity = 1.13
        self.period = 6
        self.groupNumber = 5
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_60(self):
        self.elementName = "Neodymium"
        self.atomicSymbol = "Nd"
        self.atomicNumber = 60
        self.atomicWeight = 144.242
        self.density = 7
        self.meltingPointKelvin = 1283.15
        self.boilingPointKelvin = 3347.15
        self.oxidationState = []
        self.electronegativity = 1.14
        self.period = 6
        self.groupNumber = 6
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_61(self):
        self.elementName = "Promethium"
        self.atomicSymbol = "Pm"
        self.atomicNumber = 61
        self.atomicWeight = 144.912
        self.density = 7.2
        self.meltingPointKelvin = 1440.15
        self.boilingPointKelvin = 3273.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 6
        self.groupNumber = 7
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_62(self):
        self.elementName = "Samarium"
        self.atomicSymbol = "Sm"
        self.atomicNumber = 62
        self.atomicWeight = 150.36
        self.density = 7.54
        self.meltingPointKelvin = 1345.15
        self.boilingPointKelvin = 2067.15
        self.oxidationState = []
        self.electronegativity = 1.1
        self.period = 6
        self.groupNumber = 8
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_63(self):
        self.elementName = "Europium"
        self.atomicSymbol = "Eu"
        self.atomicNumber = 63
        self.atomicWeight = 151.964
        self.density = 5.25
        self.meltingPointKelvin = 1095.15
        self.boilingPointKelvin = 1870.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 6
        self.groupNumber = 9
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_64(self):
        self.elementName = "Gadolinium"
        self.atomicSymbol = "Gd"
        self.atomicNumber = 64
        self.atomicWeight = 157.25
        self.density = 7.89
        self.meltingPointKelvin = 1584.15
        self.boilingPointKelvin = 3545.15
        self.oxidationState = []
        self.electronegativity = 1.2
        self.period = 6
        self.groupNumber = 10
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_65(self):
        self.elementName = "Terbium"
        self.atomicSymbol = "Tb"
        self.atomicNumber = 65
        self.atomicWeight = 158.925
        self.density = 8.25
        self.meltingPointKelvin = 1633.15
        self.boilingPointKelvin = 3500.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 6
        self.groupNumber = 11
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
    
    def element_66(self):
        self.elementName = "Dysprosium"
        self.atomicSymbol = "Dy"
        self.atomicNumber = 66
        self.atomicWeight = 162.500
        self.density = 8.56
        self.meltingPointKelvin = 1682.15
        self.boilingPointKelvin = 2840.15
        self.oxidationState = []
        self.electronegativity = 1.22
        self.period = 6
        self.groupNumber = 12
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_67(self):
        self.elementName = "Holmium"
        self.atomicSymbol = "Ho"
        self.atomicNumber = 67
        self.atomicWeight = 164.93
        self.density = 8.78
        self.meltingPointKelvin = 1743.15
        self.boilingPointKelvin = 2968.15
        self.oxidationState = []
        self.electronegativity = 1.23
        self.period = 6
        self.groupNumber = 13
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_68(self):
        self.elementName = "Erbium"
        self.atomicSymbol = "Er"
        self.atomicNumber = 68
        self.atomicWeight = 167.259
        self.density = 9.05
        self.meltingPointKelvin = 1802.15
        self.boilingPointKelvin = 3140.15
        self.oxidationState = []
        self.electronegativity = 1.24
        self.period = 6
        self.groupNumber = 14
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_69(self):
        self.elementName = "Thulium"
        self.atomicSymbol = "Tm"
        self.atomicNumber = 69
        self.atomicWeight = 168.934
        self.density = 9.32
        self.meltingPointKelvin = 1818.15
        self.boilingPointKelvin = 2220.15
        self.oxidationState = []
        self.electronegativity = 1.25
        self.period = 6
        self.groupNumber = 15
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_70(self):
        self.elementName = "Ytterbium"
        self.atomicSymbol = "Yb"
        self.atomicNumber = 70
        self.atomicWeight = 173.04
        self.density = 6.97
        self.meltingPointKelvin = 1097.15
        self.boilingPointKelvin = 1466.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 6
        self.groupNumber = 16
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_71(self):
        self.elementName = "Lutetium"
        self.atomicSymbol = "Lu"
        self.atomicNumber = 71
        self.atomicWeight = 174.967
        self.density = 9.84
        self.meltingPointKelvin = 1936.15
        self.boilingPointKelvin = 3668.15
        self.oxidationState = []
        self.electronegativity = 1.27
        self.period = 6
        self.groupNumber = 17
        self.group = ""
        self.elementGroup = "Lanthanides"
        self.electronConfiguration = ""
        
    def element_72(self):
        self.elementName = "Hafnium"
        self.atomicSymbol = "Hf"
        self.atomicNumber = 72
        self.atomicWeight = 178.49
        self.density = 13.31
        self.meltingPointKelvin = 2506.15
        self.boilingPointKelvin = 4875.15
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 6
        self.groupNumber = 4
        self.group = "IVB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_73(self):
        self.elementName = "Tantalum"
        self.atomicSymbol = "Ta"
        self.atomicNumber = 73
        self.atomicWeight = 180.947
        self.density = 16.68
        self.meltingPointKelvin = 3290.15
        self.boilingPointKelvin = 5731.15
        self.oxidationState = []
        self.electronegativity = 1.5
        self.period = 6
        self.groupNumber = 5 
        self.group = "VB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_74(self):
        self.elementName = "Tungsten"
        self.atomicSymbol = "W"
        self.atomicNumber = 74
        self.atomicWeight = 183.84
        self.density = 19.26
        self.meltingPointKelvin = 3695.15
        self.boilingPointKelvin = 5828.15
        self.oxidationState = []
        self.electronegativity = 2.36
        self.period = 6
        self.groupNumber = 6 
        self.group = "VIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_75(self):
        self.elementName = "Rhenium"
        self.atomicSymbol = "Re"
        self.atomicNumber = 75
        self.atomicWeight = 186.207
        self.density = 21.03
        self.meltingPointKelvin = 3453.15
        self.boilingPointKelvin = 5900.15
        self.oxidationState = []
        self.electronegativity = 1.9
        self.period = 6
        self.groupNumber = 7 
        self.group = "VIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_76(self):
        self.elementName = "Osmium"
        self.atomicSymbol = "Os"
        self.atomicNumber = 76
        self.atomicWeight = 190.23
        self.density = 22.587
        self.meltingPointKelvin = 3306.15
        self.boilingPointKelvin = 5870.15
        self.oxidationState = []
        self.electronegativity = 2.2
        self.period = 6
        self.groupNumber = 8 
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_77(self):
        self.elementName = "Iridium"
        self.atomicSymbol = "Ir"
        self.atomicNumber = 77
        self.atomicWeight = 192.217
        self.density = 22.562
        self.meltingPointKelvin = 2683.15
        self.boilingPointKelvin = 4403.15
        self.oxidationState = []
        self.electronegativity = 2.2
        self.period = 6
        self.groupNumber = 9
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_78(self):
        self.elementName = "Platinum"
        self.atomicSymbol = "Pt"
        self.atomicNumber = 78
        self.atomicWeight = 195.084
        self.density = 21.45
        self.meltingPointKelvin = 2041.15
        self.boilingPointKelvin = 4098.15
        self.oxidationState = []
        self.electronegativity = 2.28
        self.period = 6
        self.groupNumber = 10
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_79(self):
        self.elementName = "Gold"
        self.atomicSymbol = "Au"
        self.atomicNumber = 79
        self.atomicWeight = 196.966
        self.density = 19.3
        self.meltingPointKelvin = 1337.58
        self.boilingPointKelvin = 2973.15
        self.oxidationState = []
        self.electronegativity = 2.54
        self.period = 6
        self.groupNumber = 11 
        self.group = "IB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_80(self):
        self.elementName = "Mercury"
        self.atomicSymbol = "Hg"
        self.atomicNumber = 80
        self.atomicWeight = 200.59
        self.density = 13.55
        self.meltingPointKelvin = 234.26
        self.boilingPointKelvin = 629.85
        self.oxidationState = []
        self.electronegativity = 2
        self.period = 6
        self.groupNumber = 12
        self.group = "IIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_81(self):
        self.elementName = "Thallium"
        self.atomicSymbol = "Tl"
        self.atomicNumber = 81
        self.atomicWeight = 204.383
        self.density = 11.85
        self.meltingPointKelvin = 576.75
        self.boilingPointKelvin = 1746.15
        self.oxidationState = []
        self.electronegativity = 1.62
        self.period = 6
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_82(self):
        self.elementName = "Lead"
        self.atomicSymbol = "Pb"
        self.atomicNumber = 82
        self.atomicWeight = 207.2
        self.density = 11.34
        self.meltingPointKelvin = 600.55
        self.boilingPointKelvin = 2022.15
        self.oxidationState = []
        self.electronegativity = 2.23
        self.period = 6
        self.groupNumber = 14
        self.group = "IVA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_83(self):
        self.elementName = "Bismuth"
        self.atomicSymbol = "Bi"
        self.atomicNumber = 83
        self.atomicWeight = 208.9804
        self.density = 9.8
        self.meltingPointKelvin = 544.45
        self.boilingPointKelvin = 1833.15
        self.oxidationState = []
        self.electronegativity = 2.02
        self.period = 6
        self.groupNumber = 15
        self.group = "VA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_84(self):
        self.elementName = "Polonium"
        self.atomicSymbol = "Po"
        self.atomicNumber = 84
        self.atomicWeight = 208.9824
        self.density = 9.2
        self.meltingPointKelvin = 527.15
        self.boilingPointKelvin = 1235.15
        self.oxidationState = []
        self.electronegativity = 2
        self.period = 6
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "METALLOIDS"
        self.electronConfiguration = ""
        
    def element_85(self):
        self.elementName = "Astatine"
        self.atomicSymbol = "At"
        self.atomicNumber = 85
        self.atomicWeight = 209.9871
        self.density = 6.4
        self.meltingPointKelvin = 503.15
        self.boilingPointKelvin = 609.95
        self.oxidationState = []
        self.electronegativity = 2.2
        self.period = 6
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""
        
    def element_86(self):
        self.elementName = "Radon"
        self.atomicSymbol = "Rn"
        self.atomicNumber = 86
        self.atomicWeight = 222.0176
        self.density = 0.0098
        self.meltingPointKelvin = 202.0
        self.boilingPointKelvin = 211.45
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 6
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""
        
    def element_87(self):
        self.elementName = "Francium"
        self.atomicSymbol = "Fr"
        self.atomicNumber = 87
        self.atomicWeight = 223.0197
        self.density = 2.48
        self.meltingPointKelvin = 281.15
        self.boilingPointKelvin = 949.95
        self.oxidationState = []
        self.electronegativity = 0.7
        self.period = 7
        self.groupNumber = 1
        self.group = "IA"
        self.elementGroup = "Alkali Metals"
        self.electronConfiguration = ""
        
    def element_88(self):
        self.elementName = "Radium"
        self.atomicSymbol = "Ra"
        self.atomicNumber = 88
        self.atomicWeight = 226.0254
        self.density = 5.5
        self.meltingPointKelvin = 969.15
        self.boilingPointKelvin = 2010.15
        self.oxidationState = []
        self.electronegativity = 0.9
        self.period = 7
        self.groupNumber = 2
        self.group = "IIA"
        self.elementGroup = "Alkaline Earth Metals"
        self.electronConfiguration = ""
        
    def element_89(self):
        self.elementName = "Actinium"
        self.atomicSymbol = "Ac"
        self.atomicNumber = 89
        self.atomicWeight = 227.0278
        self.density = 10.07
        self.meltingPointKelvin = 1323.15
        self.boilingPointKelvin = 3470.15
        self.oxidationState = []
        self.electronegativity = 1.1
        self.period = 7
        self.groupNumber = 3
        self.group = "IIIB"
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_90(self):
        self.elementName = "Thorium"
        self.atomicSymbol = "Th"
        self.atomicNumber = 90
        self.atomicWeight = 232.0380
        self.density = 11.72
        self.meltingPointKelvin = 2023.15
        self.boilingPointKelvin = 5060.15
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 4
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_91(self):
        self.elementName = "Protactinium"
        self.atomicSymbol = "Pa"
        self.atomicNumber = 91
        self.atomicWeight = 231.0358
        self.density = 15.37
        self.meltingPointKelvin = 2113.15
        self.boilingPointKelvin = 4300.15
        self.oxidationState = []
        self.electronegativity = 1.5
        self.period = 7
        self.groupNumber = 5
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_92(self):
        self.elementName = "Uranium"
        self.atomicSymbol = "U"
        self.atomicNumber = 92
        self.atomicWeight = 238.0289
        self.density = 19.05
        self.meltingPointKelvin = 1405.55
        self.boilingPointKelvin = 4404.15
        self.oxidationState = []
        self.electronegativity = 1.38
        self.period = 7
        self.groupNumber = 6
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_93(self):
        self.elementName = "Neptunium"
        self.atomicSymbol = "Np"
        self.atomicNumber = 93
        self.atomicWeight = 237.0482
        self.density = 20.48
        self.meltingPointKelvin = 917.15
        self.boilingPointKelvin = 4175.15
        self.oxidationState = []
        self.electronegativity = 1.36
        self.period = 7
        self.groupNumber = 7
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_94(self):
        self.elementName = "Plutonium"
        self.atomicSymbol = "Pu"
        self.atomicNumber = 94
        self.atomicWeight = 244.0642
        self.density = 19.74
        self.meltingPointKelvin = 914.15
        self.boilingPointKelvin = 3505.15
        self.oxidationState = []
        self.electronegativity = 1.28
        self.period = 7
        self.groupNumber = 8
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_95(self):
        self.elementName = "Americium"
        self.atomicSymbol = "Am"
        self.atomicNumber = 95
        self.atomicWeight = 243.0614
        self.density = 13.67
        self.meltingPointKelvin = 1449.15
        self.boilingPointKelvin = 2880.152
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 9
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_96(self):
        self.elementName = "Curium"
        self.atomicSymbol = "Cm"
        self.atomicNumber = 96
        self.atomicWeight = 247.0703
        self.density = 13.51
        self.meltingPointKelvin = 1618.15
        self.boilingPointKelvin = 3383.15
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 10
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_97(self):
        self.elementName = "Berkelium"
        self.atomicSymbol = "Bk"
        self.atomicNumber = 97
        self.atomicWeight = 247.0703
        self.density = 13.25
        self.meltingPointKelvin = 1259.15
        self.boilingPointKelvin = 2900.15
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 11
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_98(self):
        self.elementName = "Californium"
        self.atomicSymbol = "Cf"
        self.atomicNumber = 98
        self.atomicWeight = 251.0796
        self.density = 15.1
        self.meltingPointKelvin = 1173.15
        self.boilingPointKelvin = 1745.15
        self.oxidationState = []
        self.electronegativity = 1.3 
        self.period = 7
        self.groupNumber = 12
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_99(self):
        self.elementName = "Einsteinium"
        self.atomicSymbol = "Es"
        self.atomicNumber = 99
        self.atomicWeight = 252.0829
        self.density = 13.5
        self.meltingPointKelvin = 1133.15
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 13
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_100(self):
        self.elementName = "Fermium"
        self.atomicSymbol = "Fm"
        self.atomicNumber = 100
        self.atomicWeight = 257.0951
        self.density = 19.050
        self.meltingPointKelvin = 1798.15
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 14
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_101(self):
        self.elementName = "Mendelevium"
        self.atomicSymbol = "Md"
        self.atomicNumber = 101
        self.atomicWeight = 258.0951
        self.density = 0.0
        self.meltingPointKelvin = 1098.15
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 15 
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_102(self):
        self.elementName = "Nobelium"
        self.atomicSymbol = "No"
        self.atomicNumber = 102
        self.atomicWeight = 259.1009
        self.density = 0.0
        self.meltingPointKelvin = 1098.15
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 1.3
        self.period = 7
        self.groupNumber = 16
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_103(self):
        self.elementName = "Lawrencium"
        self.atomicSymbol = "Lr"
        self.atomicNumber = 103
        self.atomicWeight = 266.1193
        self.density = 0.0
        self.meltingPointKelvin = 1898.15
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 17
        self.group = ""
        self.elementGroup = "Actinides"
        self.electronConfiguration = ""
        
    def element_104(self):
        self.elementName = "Rutherfordium"
        self.atomicSymbol = "Rf"
        self.atomicNumber = 104
        self.atomicWeight = 261
        self.density = 23
        self.meltingPointKelvin = 2373.15
        self.boilingPointKelvin = 5773.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 4
        self.group = "IVB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_105(self):
        self.elementName = "Dubnium"
        self.atomicSymbol = "Db"
        self.atomicNumber = 105
        self.atomicWeight = 262
        self.density = 29
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 5
        self.group = "VB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_106(self):
        self.elementName = "Seaborgium"
        self.atomicSymbol = "Sg"
        self.atomicNumber = 106
        self.atomicWeight = 269
        self.density = 35
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 6
        self.group = "VIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_107(self):
        self.elementName = "Bohrium"
        self.atomicSymbol = "Bh"
        self.atomicNumber = 107
        self.atomicWeight = 267
        self.density = 37
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 7
        self.group = "VIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_108(self):
        self.elementName = "Hassium"
        self.atomicSymbol = "Hs"
        self.atomicNumber = 108
        self.atomicWeight = 269
        self.density = 0.0
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 8
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_109(self):
        self.elementName = "Meitnerium"
        self.atomicSymbol = "Mt"
        self.atomicNumber = 109
        self.atomicWeight = 278
        self.density = 34.4
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 9
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_110(self):
        self.elementName = "Darmstadtium"
        self.atomicSymbol = "Ds"
        self.atomicNumber = 110
        self.atomicWeight = 281.1620
        self.density = 34.8
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 10
        self.group = "VIIIB"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_111(self):
        self.elementName = "Roentgenium"
        self.atomicSymbol = "Rg"
        self.atomicNumber = 111
        self.atomicWeight = 281.1684
        self.density = 0.0
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 11
        self.group = "IA"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_112(self):
        self.elementName = "Copernicium"
        self.atomicSymbol = "Cn"
        self.atomicNumber = 112
        self.atomicWeight = 285.1744
        self.density = 20
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 12
        self.group = "IIA"
        self.elementGroup = "Transition Metals"
        self.electronConfiguration = ""
        
    def element_113(self):
        self.elementName = "Nihonium"
        self.atomicSymbol = "Nh"
        self.atomicNumber = 113
        self.atomicWeight = 286.1810
        self.density = 16
        self.meltingPointKelvin = 698.15
        self.boilingPointKelvin = 1428.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 13
        self.group = "IIIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_114(self):
        self.elementName = "Flerovium"
        self.atomicSymbol = "Fl"
        self.atomicNumber = 114
        self.atomicWeight = 289
        self.density = 14
        self.meltingPointKelvin = 341.15
        self.boilingPointKelvin = 419.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 14 
        self.group = "IVA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_115(self):
        self.elementName = "Moscovium"
        self.atomicSymbol = "Mc"
        self.atomicNumber = 115
        self.atomicWeight = 289
        self.density = 13.5
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 15
        self.group = "VA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_116(self):
        self.elementName = "Livermorium"
        self.atomicSymbol = "Lv"
        self.atomicNumber = 116
        self.atomicWeight = 293
        self.density = 0.0
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 16
        self.group = "VIA"
        self.elementGroup = "Post-Transition Metals"
        self.electronConfiguration = ""
        
    def element_117(self):
        self.elementName = "Tennessine"
        self.atomicSymbol = "Ts"
        self.atomicNumber = 117
        self.atomicWeight = 294
        self.density = 0.0
        self.meltingPointKelvin = 0.0
        self.boilingPointKelvin = 0.0
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 17
        self.group = "VIIA"
        self.elementGroup = "Halogens"
        self.electronConfiguration = ""
        
    def element_118(self):
        self.elementName = "Oganesson"
        self.atomicSymbol = "Og"
        self.atomicNumber = 118
        self.atomicWeight = 294
        self.density = 5
        self.meltingPointKelvin = 0.0 
        self.boilingPointKelvin = 368.15
        self.oxidationState = []
        self.electronegativity = 0.0
        self.period = 7
        self.groupNumber = 18
        self.group = "VIIIA"
        self.elementGroup = "Noble Gases"
        self.electronConfiguration = ""
        

'''
element = Elements()

for i in range (1,4):
    eval(f"element.element_{i}()")
    eval(f"print(element.elementName)")
'''
