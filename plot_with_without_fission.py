import wnutils.xml as wx
import matplotlib.pyplot as plt

xml = wx.Xml('with_fission7.xml')
xml_no_fission = wx.Xml('no_fission7.xml')
ya = xml.get_abundances_vs_nucleon_number(zone_xpath='[last()]')
ya_no_fission = xml_no_fission.get_abundances_vs_nucleon_number(zone_xpath='[last()]')
plt.plot(ya[0], label = 'with fission')
plt.plot(ya_no_fission[0], label = 'without fission')
plt.yscale('log')
plt.xlim([0,300])
plt.ylim([1.e-20, 1])
plt.xlabel('A, Mass Number')
plt.ylabel('Abundance per Nucleon')
plt.legend(loc='upper right')
plt.show()
plt.savefig('with_without_f1.png')
