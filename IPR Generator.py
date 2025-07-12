import numpy as np
import matplotlib.pyplot as g1

#Required Data
Q_IPR=250 #Stabilized Flow Rate
Pwf_IPR=2500 #Recorded Flowing Bottom_hole Pressure
Pr=3000 #Reservoir Pressure
Pb=2130 #Bubble Point Pressure
Qo_max = Q_IPR/(1 - 0.2*(Pwf_IPR/Pr) - 0.8*(Pwf_IPR/Pr)**2)

#Saturated Reservoir
if Pr<=Pb:
    Pwf_array = np.linspace(Pr, 0, 30)
    Qo_array = Qo_max*(1 - 0.2*(Pwf_array/Pr) - 0.8*(Pwf_array/Pr)**2)
    

#Understaturated Reservoir
else:
    if Pwf_IPR>Pb:
        J = Q_IPR/(Pr - Pwf_IPR)
        Qob = J*(Pr - Pb)
        Qo_1 = J*(Pr - np.linspace(Pr, Pb, 10))
        Qo_2 = Qob + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        Pwf_array = np.concatenate((np.linspace(Pr, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_array = np.concatenate((Qo_1,Qo_2[1:]))
    
    
       
    else:
        J = Q_IPR/((Pr - Pb) + (Pb/1.8)*(1 - 0.2*(Pwf_IPR/Pb) - 0.8*(Pwf_IPR/Pb)**2))
        Qob = J*(Pr - Pb)
        Qo_1 = J*(Pr - np.linspace(Pr, Pb, 10))
        Qo_2 = Qob + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        Pwf_array = np.concatenate((np.linspace(Pr, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_array = np.concatenate((Qo_1,Qo_2[1:]))
        
#Productivity Index
J=Q_IPR/(Pr-Pwf_IPR)
Q_array=J*(Pr-Pwf_array)

#Future IPR usimg First Approximation
Prf=2100
Qo_maxf=Qo_max*(Prf/Pr)*(0.2+0.8*(Prf/Pr))
#Saturated Reservoir
if Prf<=Pb:
    Pwf_array_new = np.linspace(Prf, 0, 30)
    Qo_array_new = Qo_maxf*(1 - 0.2*(Pwf_array_new/Prf) - 0.8*(Pwf_array_new/Prf)**2)
    

#Understaturated Reservoir
else:
    if Pwf_IPR>Pb:
        J = Q_IPR/(Prf - Pwf_IPR)
        Qob_new = J*(Prf - Pb)
        Qo_1_new = J*(Prf - np.linspace(Prf, Pb, 10))
        Qo_2_new = Qob_new + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        Pwf_array_new = np.concatenate((np.linspace(Prf, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_array_new = np.concatenate((Qo_1_new,Qo_2_new[1:]))
    
       
    else:
        J = Q_IPR/((Prf - Pb) + (Pb/1.8)*(1 - 0.2*(Pwf_IPR/Pb) - 0.8*(Pwf_IPR/Pb)**2))
        Qob_new = J*(Prf - Pb)
        Qo_1_new = J*(Prf - np.linspace(Prf, Pb, 10))
        Qo_2_new = Qob_new + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        Pwf_array_new = np.concatenate((np.linspace(Prf, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_array_new = np.concatenate((Qo_1_new,Qo_2_new[1:]))

#Future IPR usimg Second Approximation
PrF=2100
Qo_maxF=Qo_max*(PrF/Pr)**3
#Saturated Reservoir
if PrF<=Pb:
    PwF_array = np.linspace(PrF, 0, 30)
    Qo_Array_new= Qo_maxF*(1 - 0.2*(PwF_array/PrF) - 0.8*(PwF_array/PrF)**2)
    

#Understaturated Reservoir
else:
    if Pwf_IPR>Pb:
        J = Q_IPR/(PrF - Pwf_IPR)
        Qob_New = J*(PrF - Pb)
        Qo_1_New = J*(PrF - np.linspace(PrF, Pb, 10))
        Qo_2_New = Qob_New + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        PwF_array = np.concatenate((np.linspace(PrF, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_Array_new = np.concatenate((Qo_1_New,Qo_2_New[1:]))
    
       
    else:
        J = Q_IPR/((PrF - Pb) + (Pb/1.8)*(1 - 0.2*(Pwf_IPR/Pb) - 0.8*(Pwf_IPR/Pb)**2))
        Qob_New = J*(PrF - Pb)
        Qo_1_New = J*(Prf - np.linspace(PrF, Pb, 10))
        Qo_2_New = Qob_New + (J*Pb/1.8)*(1 - 0.2*(np.linspace(Pb, 0, 10)/Pb) - 0.8*(np.linspace(Pb, 0, 10)/Pb)**2)
        PwF_array = np.concatenate((np.linspace(PrF, Pb, 10), np.linspace(Pb, 0, 10)[1:]))
        Qo_Array_new = np.concatenate((Qo_1_New,Qo_2_New[1:]))

g1.plot(Qo_Array_new,PwF_array)
g1.plot(Qo_array_new,Pwf_array_new)
g1.plot(Q_array,Pwf_array)
g1.plot(Qo_array, Pwf_array)
g1.legend(["Second Approximation","First Approximation","Productivity Index","Current IPR"])
g1.xlabel("Q")
g1.ylabel("Pwf")

 

    