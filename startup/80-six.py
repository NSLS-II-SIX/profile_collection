﻿import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

	
									# DATA FROM OLEG	
	
energy = [139.458530239435,141.444392791253,143.559979210818,145.804204119565,148.175977479049,150.674204590942,153.297786097036,156.045617979241,
		 158.916591559587,161.90959350022,165.023505803409,168.257205811538,171.609566207111,175.079455012751, 178.665735591199,182.367266645316,
		 186.18290221808,190.11149169259,194.151879792061,198.302906579829,202.563407459347,206.932213174189,211.408149808044,215.990038784724,
		 220.676696868157,225.466936162391,230.359564111591,235.353383500043,240.447192452151,245.639784432436,250.92994824554,256.316468036223,
		 261.798123289363,267.373688829957,273.041934823122,278.801626774092,284.65152552822,290.59038727098,296.616963527961,302.730001164874,
		 308.928242387547,315.210424741927,321.575281114079,328.021539730189,334.547924156559,341.153153299612,
		 347.835941405888, 354.594998062047, 361.429028194866, 368.336732071244, 375.316805298195,  382.367938822854, 389.488818932475, 396.678127254427,
		 403.934540756203, 411.256731745412, 418.643367869782, 426.093112117158, 433.604622815508, 441.176553632915, 448.807553577581, 456.496266997829,
		 464.241333582098, 472.041388358949, 479.895061697059, 487.800979305224, 495.757762232359, 503.764026867499, 511.818384939796, 519.919443518522,
		 528.065805013067, 536.25606717294, 544.488823087768, 552.762661187298, 561.076165241395, 569.427914360043, 577.816482993344, 586.240440931519,
		 594.69835330491, 603.188780583973, 611.710278579286, 620.261398441547, 628.840686661569, 637.446685070287, 646.077930838752, 654.732956478137,
		 663.41028983973, 672.108454114939, 680.825967835294, 689.561344872439, 698.313094438138, 707.079721084276, 715.859724702856, 724.651600525996,
		 733.453839125938, 742.264926415039, 751.083343645777, 759.907567410748, 768.736069642664, 777.567317614362, 786.399773938792, 795.231896569024,
		 804.062138798248, 812.888949259774, 821.710771927027, 830.526046113552, 839.333206473016, 848.130682999199, 856.916901026004, 865.690281227452,
		 874.449239617682, 883.192187550953, 891.917531721639, 900.623674164238, 909.309012253363, 917.971938703747, 926.610841570242, 935.224104247818,
		 943.810105471564, 952.367219316688, 960.893815198516, 969.388257872493, 977.848907434185, 986.274119319273, 994.662244303559, 1003.01162850296,
		 1011.32061337352, 1019.5875357114, 1027.81072765286, 1035.98851667431, 1044.11922559226, 1052.20117256335, 1060.23267108431, 1068.21202999203,
		 1076.13755346349, 1084.0075410158, 1091.82028750619, 1099.574083132, 1107.26721343069, 1114.89795927984, 1122.46459689717, 1129.96539784048,
		 1137.39862900772, 1144.76255263694, 1152.05542630632, 1159.27550293415, 1166.42103077885, 1173.49025343895, 1180.4814098531, 1187.39273430006,
		 1194.22245639874, 1200.96880110813, 1207.62998872736, 1214.20423489568, 1220.68975059244, 1227.08474213714, 1233.38741118937, 1239.59595474884,
		 1245.70856515541, 1251.72343008902, 1257.63873256975, 1263.4526509578, 1269.16335895348, 1274.76902559721, 1280.26781526956, 1285.65788769119,
		 1290.93739792288, 1296.10449636555, 1301.15732876022, 1306.09403618803, 1310.91275507025, 1315.61161716826, 1320.18874958356, 1324.64227475776,
		 1328.97031047262, 1333.17096984997, 1337.2423613518, 1341.1825887802, 1344.98975127739, 1348.66194332569, 1352.19725474756, 1355.59377070556,
		 1358.84957170238, 1361.96273358083, 1364.93132752384, 1367.75342005444, 1370.4270730358, 1372.9503436712, 1375.32128450404, 1377.53794341784,
		 1379.59836363624, 1381.50058372299, 1383.24263758197, 1384.82255445717, 1386.23835893271, 1387.48807093281, 1388.56970572182, 1389.48127390421,
		 1390.22078142458, 1390.78622956762]
	
	
gap = [16.0, 16.2211055276, 16.4422110553, 16.6633165829, 16.8844221106, 17.1055276382, 17.3266331658, 17.5477386935, 17.7688442211, 17.9899497487,
		 18.2110552764, 18.432160804, 18.6532663317, 18.8743718593, 19.0954773869, 19.3165829146, 19.5376884422, 19.7587939698, 19.9798994975, 20.2010050251,
		 20.4221105528, 20.6432160804, 20.864321608, 21.0854271357, 21.3065326633, 21.527638191, 21.7487437186, 21.9698492462, 22.1909547739, 22.4120603015,
		 22.6331658291, 22.8542713568, 23.0753768844, 23.2964824121, 23.5175879397, 23.7386934673, 23.959798995, 24.1809045226, 24.4020100503, 24.6231155779,
		 24.8442211055, 25.0653266332, 25.2864321608, 25.5075376884, 25.7286432161, 25.9497487437, 26.1708542714, 26.391959799, 26.6130653266, 26.8341708543,
		 27.0552763819, 27.2763819095, 27.4974874372, 27.7185929648, 27.9396984925, 28.1608040201, 28.3819095477, 28.6030150754, 28.824120603, 29.0452261307,
		 29.2663316583, 29.4874371859, 29.7085427136, 29.9296482412, 30.1507537688, 30.3718592965, 30.5929648241, 30.8140703518, 31.0351758794, 31.256281407,
		 31.4773869347, 31.6984924623, 31.9195979899, 32.1407035176, 32.3618090452, 32.5829145729, 32.8040201005, 33.0251256281, 33.2462311558, 33.4673366834,
		 33.6884422111, 33.9095477387, 34.1306532663, 34.351758794, 34.5728643216, 34.7939698492, 35.0150753769, 35.2361809045, 35.4572864322, 35.6783919598,
		 35.8994974874, 36.1206030151, 36.3417085427, 36.5628140704, 36.783919598, 37.0050251256, 37.2261306533, 37.4472361809, 37.6683417085, 37.8894472362,
		 38.1105527638, 38.3316582915, 38.5527638191, 38.7738693467, 38.9949748744, 39.216080402, 39.4371859296, 39.6582914573, 39.8793969849, 40.1005025126,
		 40.3216080402, 40.5427135678, 40.7638190955, 40.9849246231, 41.2060301508, 41.4271356784, 41.648241206, 41.8693467337, 42.0904522613, 42.3115577889,
		 42.5326633166, 42.7537688442, 42.9748743719, 43.1959798995, 43.4170854271, 43.6381909548, 43.8592964824, 44.0804020101, 44.3015075377, 44.5226130653,
		 44.743718593, 44.9648241206, 45.1859296482, 45.4070351759, 45.6281407035, 45.8492462312, 46.0703517588, 46.2914572864, 46.5125628141, 46.7336683417,
		 46.9547738693, 47.175879397, 47.3969849246, 47.6180904523, 47.8391959799, 48.0603015075, 48.2814070352, 48.5025125628, 48.7236180905, 48.9447236181,
		 49.1658291457, 49.3869346734, 49.608040201, 49.8291457286, 50.0502512563, 50.2713567839, 50.4924623116, 50.7135678392, 50.9346733668, 51.1557788945,
		 51.3768844221, 51.5979899497, 51.8190954774, 52.040201005, 52.2613065327, 52.4824120603, 52.7035175879, 52.9246231156, 53.1457286432, 53.3668341709,
		 53.5879396985, 53.8090452261, 54.0301507538, 54.2512562814, 54.472361809, 54.6934673367, 54.9145728643, 55.135678392, 55.3567839196, 55.5778894472,
		 55.7989949749, 56.0201005025, 56.2412060302, 56.4623115578, 56.6834170854, 56.9045226131, 57.1256281407, 57.3467336683, 57.567839196, 57.7889447236,
		 58.0100502513, 58.2311557789, 58.4522613065, 58.6733668342, 58.8944723618, 59.1155778894, 59.3366834171, 59.5577889447, 59.7788944724, 60.0]


def e2g(ph_en):
	''' usage: e2g(photon_energy) 
			Select the photon_energy (140,1390) and returns the corresponding 
			gap interpolated from Oleg data.
	'''								
	
	etog = interp1d(energy, gap)
	if (ph_en >= 140 and ph_en <= 1390.7): 
		print('\t gap = %5.3f' %(etog(ph_en)))
		return etog(ph_en)
	else:
		print('energy out of range (140, 1390)')

def e2g_1390(ph_en):
	''' usage: e2g_1390(photon_energy) 
			Select the photon_energy and returns the corresponding 
			gap interpolated from Oleg data. This allows for extrapolation E>1390.7eV
	'''								
	
	etog = interp1d(energy, gap,fill_value="extrapolate")
	if (ph_en >= 140 and ph_en <= 1390.7): 
		print('\t gap = %5.3f' %(etog(ph_en)))
		return etog(ph_en)
	else:
		print('\t using extrapolated output from e2g_1390')	
		print('\t gap = %5.3f' %(etog(ph_en)))
		return etog(ph_en)	

def g2e(g):
	''' usage: g2e(gap) 
			Select the gap (16,60) and returns the corresponding 
			photon energy interpolated from Oleg data.
	'''								
	
	gtoe = interp1d(gap, energy)
	if (g >= 16 and g <=60): 
		print('\t photon energy = %5.3f' %(gtoe(g)))
	else:
		print('gap out of range (16, 60)')
	

def Sic2f(ph_en, i):
	''' Given the photon energy (in eV) and the XUV Si-diode current (in Ampere), returns the
		flux (ph/sec). It uses the QY for a typical XUV Si-diode.
		Usage: Sic2f(hv(eV), i(A))
	'''									
									# XUV QY data: number of electrons per 1 photons of a given photon energy	
	
	E_eV = [1,1.25,2,2.75,3,4,5,6,7,8,9,10,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500
			,520,540,560,580,600,620,640,740,760,780,800,820,840,860,880,900,920,940,960,980,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800
			,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200,5400,5600,5800,6000]
	
	
	QY = [0.023, 0.32 ,0.64,0.57,0.49,0.432,0.45,0.5,0.7,1,1.05,1.1,3.25,8.38,12.18,17.85,22.72,26.42,31.37,33.5,42.95,50.68,60.61,66.12,71.63,77.13
			,82.64,88.15,93.66,99.17,104.68,110.19,115.7,121.21,126.72,132.23,137.74,143.25,148.76,154.27,159.78,165.29,170.8,176.31,203.86,209.37,
			214.88,220.39,225.9,231.41,236.91,242.42,247.94,253.44,258.95,264.46,269.97,275.48,330.58,385.67,440.77,495.87,550.96,606.06,661.18,716.35
			,771.35,826.45,881.54,936.64,991.74,1046.83,1101.93,1157.02,1212.12,1267.22,1322.31,1377.41,1432.51,1487.6,1542.7,1597.8,1652.89]

	Sictof = interp1d(E_eV, QY)
	print('min, max = %f, %f' %(min(E_eV), max(E_eV)))
	if (ph_en >= min(E_eV) and ph_en <= max(E_eV)):
		print('QY = %f' %(round(Sictof(ph_en),2)))
	else:
		print("Energy out of range")

	print('flux = %.4g ph/sec' %((i)/(1.6E-19)/Sictof(ph_en)))	

# above functions and data is from ESM
	
      
def gr500_info(eV, mm=1,r2=42636):
    # calculate various information for the 500 mm-1 grating for SIX
    # eV is the energy in electron volts
    # r2 is the monochromator exit arm in mm, nominally 42636 mm
    r1 = 55000  # input arm length in mm
    k0 = 500    # grating central line density in mm-1
    a1 = 0.0328411  # grating focusing constant in mm-2
    #mm = 1      # diffraction order
    
    wl = 0.0012398/eV  # wavelength in mm
    rr = r2/r1 # unitless
    b2 = -0.5*a1*(1/k0)  # convert grating focusing term to Ruben's standard
    A0 = mm*k0*wl
    B2 = r2*b2

    term1 = 2*A0*B2+4*B2*B2+(4+2*A0*B2-A0*A0)*rr
    term2 = -4*B2*np.sqrt((1+rr)*(1+rr)+2*A0*B2*(1+rr)-A0*A0*rr)
    term3 = -4+A0*A0-4*A0*B2+4*B2*B2
    cff = np.sqrt((term1+term2)/term3)
    
    term4=(cff*A0)/(cff*cff-1)
    alpha=np.arcsin(-A0/(cff*cff-1)+np.sqrt(1+np.power(term4,2)))
    beta=np.arcsin(A0-np.sin(alpha))
    phi=0.5*(alpha-beta)
    # this changes depending on angular conventions
    thetaPM = phi
    thetaGR = -beta
    
    print("cff =", cff)
    print("alpha (deg) =", alpha*180/np.pi, " inc angle on grating")
    print("beta (deg) =", beta*180/np.pi, " diffraction angle")
    print("phi (deg) =", phi*180/np.pi, " inc angle on premirror")
    print("pitch angles relative to vertical")
    print("PM pitch (deg) =", thetaPM*180/np.pi)
    print("GR pitch (deg) =", thetaGR*180/np.pi)

    return cff
    
def monoInfo2(eV, k0, mm, cff):
    # calculate various information for a grating
    # eV is the energy in electron volts
    # k0 is the central line density in mm-1
    # mm is the order
    # cff is cos(beta)/cos(alpha)
    
    wl = 0.0012398/eV  # wavelength in mm
    A0 = mm*k0*wl    
    term4=(cff*A0)/(cff*cff-1)
    alpha=np.arcsin(-A0/(cff*cff-1)+np.sqrt(1+np.power(term4,2)))
    beta=np.arcsin(A0-np.sin(alpha))
    phi=0.5*(alpha-beta)
    # this changes depending on angular conventions
    thetaPM = phi
    thetaGR = -beta
    
    print("cff =", cff)
    print("alpha (deg) =", alpha*180/np.pi, " inc angle on grating")
    print("beta (deg) =", beta*180/np.pi, " diffraction angle")
    print("phi (deg) =", phi*180/np.pi, " inc angle on premirror")
    print("pitch angles relative to vertical")
    print("PM pitch (deg) =", thetaPM*180/np.pi)
    print("GR pitch (deg) =", thetaGR*180/np.pi)

    return

def gr500mv1(eV, cff):
    # move the 500 mm-1 BL grating based on energy and cff value
    # thru bluesky
    # Upm, Ugr are the EPICS user values for the premirr and grating pitch
    # OFFpm and OFFgr are the angular offsets for premirr and grating pitch
    # untested

    # right now I list these in addition to EPICS offsets
    # at some point these could be incoorporated into the EPICS values
    # and then these should be set to zero   
    OFFpm = -0.46801   # value in deg, these are in addition to EPICS offsets
    OFFgr = -0.35772   # value in deg, these are in addition to EPICS offsets
    wl = 0.0012398/eV  # wavelength in mm
    k0 = 500 # grating central line density, hard coded
    #mm = 1 # diffraction order, hard coded
    pi=3.14159265359
    A0 = mm*k0*wl   
    term4=(cff*A0)/(cff*cff-1)
    alpha=np.arcsin(-A0/(cff*cff-1)+np.sqrt(1+np.power(term4,2)))
    beta=np.arcsin(A0-np.sin(alpha))
    phi=0.5*(alpha-beta)
    # this changes depending on angular conventions, these are for SIX
    # U stands for EPICS user value
    Upm = phi*(180./pi) + OFFpm
    Ugr = -beta*(180./pi) + OFFgr

    yield from bp.mv(pgm.m2_pit, Upm) 
    yield from bp.mv(pgm.gr_pit, Ugr)

def getThetaPMdeg(eV, thetaGR_deg, k_invmm, m):
    """
    calculate premirror angle from energy and grating angle, in degrees
        eV - energy in eV
        thetaGR_deg - grating angle in degrees
        k_invmm - central line density in mm-1
        m - diffraction order, + is inside order
    """
    # error check ok
    thetaGR = thetaGR_deg*(np.pi/180)
    lambda_mm = 0.001239842/eV  # wavelength in mm
    if (m==0):
        thetaPM = thetaGR
    else:    
        thetaPM = 0.5*(np.arcsin(m*k_invmm*lambda_mm+np.sin(thetaGR))+thetaGR)
    thetaPM_deg = thetaPM*(180/np.pi)
    return thetaPM_deg

def generatePGMscan(eV, k_invmm, 
                 startGR=84.0, stopGR=90.0, 
                 startPM=84.0, stopPM=90.0, gridDelta=0.2,
                 fineRange=0.02, fineDelta=0.001,
                 mm=[1,0], collAng=2, info=False):
    """
    visualize a PGM smart mesh scan before running it
        input description (all angles in deg)
        eV: undulator fixed energy in eV
        k_invmm: grating line density in mm^-1
        GR range: startGR, stopGR
        PM range: startPM, stopPM
        gridDelta: course step size
        fine range: fineRange, fineDelta determine fine grating scan about
            the constant energy contour
        mm: list of orders to scan
        collAng: safety collision angle, 4 deg appropriate for SIX
        info: print out scan information
    """

    # this part should run without modification
    GRang=np.zeros(0)
    PMang=np.zeros(0)
    diffAng=np.zeros(0)
    order=np.zeros(0)
    nPntsGrid = int((stopGR-startGR)/gridDelta+1)
    for j in mm: # loop for orders
        # for one value of m, calculate the constant energy contour
        GRangTmp = np.linspace(startGR, stopGR, nPntsGrid)
        PMangTmp = getThetaPMdeg(eV, GRangTmp, k_invmm, j)
        diffAngTmp = PMangTmp-GRangTmp
        orderTmp = np.full(len(GRangTmp), j)
        # check and remove nan pnts, collision pnts, and angles > 90 deg
        GRangTmp2 = GRangTmp
        PMangTmp2 = PMangTmp
        diffAngTmp2 = diffAngTmp
        orderTmp2 = orderTmp
        hits = 0
        for i in range(len(GRangTmp)):  
            if (np.isnan(GRangTmp[i]) or np.isnan(PMangTmp[i]) or 
                diffAngTmp[i]>collAng or np.isinf(PMangTmp[i]) or 
                GRangTmp[i]>90.0 or PMangTmp[i]>90.0):
                # remove that point from array
                GRangTmp2=np.delete(GRangTmp2,i-hits)
                PMangTmp2=np.delete(PMangTmp2,i-hits)
                diffAngTmp2=np.delete(diffAngTmp2,i-hits)
                orderTmp2=np.delete(orderTmp2,i-hits)
                hits = hits + 1            
        GRang=np.append(GRang, GRangTmp2)            
        PMang=np.append(PMang, PMangTmp2)            
        diffAng=np.append(diffAng, diffAngTmp2)            
        order=np.append(order,orderTmp2)  # possible to use for later
    if info==True:
        print('tot number of pnts = ', len(GRang)*(int(fineRange/fineDelta)+1))
    return GRang, PMang
