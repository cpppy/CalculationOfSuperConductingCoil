# -*- coding: cp936 -*-
import calcHeat
from numpy import *
import matplotlib.pyplot as plt
import pylab as pl

'''
I = calcHeat.electricCurrent(3.61)
print I
'''
ddtime = 0.001
time = 0
Qh = 0
Qc = 0
Jheat = 0
Q = 0
iend = 0

#�����������ڻ�ͼ
arrI = [0 for x in range(10000)]
arrB= [0 for x in range(10000)]
arrQh = [0 for x in range(10000)]
arrQc = [0 for x in range(10000)]
arrJheat = [0 for x in range(10000)]
arrQ = [0 for x in range(10000)]
arrtime = [0 for x in range(10000)]

print 'Qh                               Qc                              Jheat'

for i in range(10000):
    dt = ddtime
    #dt = (i)*ddtime   ����������ʹ���˻��㷨���ټ����
    time = time+dt
    print ' i = ',i,'   time = ',time
    arrtime[i] = time
    dIdt = abs(calcHeat.dIdt(time))
    dBdt = calcHeat.dmagneticFieldStrenth(dIdt)
    #������ļ���
    Jc = 1000*10000      #�˴�ӦѰ�ұ��ʽ����
    deff = 80*10**(-6)
    AscMultiLen = (80.42*416.9+52.78*487.6+30.16*1143.3+18.10*4350)*10**(-6)
    dQh = (2*Jc*deff*AscMultiLen*dBdt/(3*pi))*dt
    Qh = Qh + dQh
    arrQh[i] = Qh
    
    #�����ļ���
    nt = 0.1  #���ʱ�䳣�� Ԥ��Ϊ 0.1S
    u0 = 4*pi*10**(-7)
    Vsc = AscMultiLen
    dQc = (Vsc*nt*(dBdt**2)/u0)*dt
    Qc = Qc+dQc
    arrQc[i] = Qc

    #�����ȵļ���
    I = calcHeat.electricCurrent(time)   #�ĸ���Ȧ���ܵ���
    arrI[i] = I
    #troublelen = 400   #����δ֪(ʧ������)
    #temp =  220    #����δ֪��ʧ���¶ȣ�
    r = 2.1*10**(-9)    #�˴���������ƽ��ֵ��ʵ����Ҫ��ʽ r = calcHeat.RofCu(temp) ��ȷ��
    #R = troublelen*r/Acu
    s = pi*0.16*10**(-6) #����ͭϸ˿�Ľ����
    Ra = r*416.9/(80*s)  #��ȦA��ͭ�ĵ���
    Rb = r*487.6/(75*s)
    Rc = r*1143.3/(120*s)
    Rd = r*4350/(180*s)
    R = 1/((1/Ra)+(1/Rb)+(1/Rc)+(1/Rd))
    
    
    dJheat = (I**2)*R*dt
    Jheat = Jheat + dJheat
    arrJheat[i] = Jheat
    
    Qlast = Q
    print Qh,'   ',Qc,'   ',Jheat
    Q = Q+dQh+dQc+dJheat
    print Q
    arrQ[i] = Q
    B = calcHeat.Bvalue(I)
    #print B
    arrB[i] = B

    if Q-Qlast<0.01*Q*dt:
        iend = i
        break
print 'have been static'
print 'time= ',time
print Q
print 'R = ',R


#��ͼ����
fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)
ax1.plot(arrtime[:iend],arrI[:iend])
ax2.plot(arrtime[:iend],arrB[:iend])
ax3.plot(arrtime[:iend],arrQh[:iend])
ax4.plot(arrtime[:iend],arrQc[:iend])
ax5.plot(arrtime[:iend],arrJheat[:iend])
ax6.plot(arrtime[:iend],arrQ[:iend])

plt.show()
fig.savefig("docalcHeat.pdf")































