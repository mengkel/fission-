import wnutils as wx
import numpy as np


reactions = {}
reactions['Ac_273'] = wx.Reaction()
reactions['Ac_273'].reactants = ['ac273']
reactions['Ac_273'].products = ['mo128','ag143','n','n']
reactions['Ac_273'].source = 'single_rate'
reactions['Ac_273'].data = {'type': 'single_rate', 'rate': '20'}
 
reactions['Ac_273_1'] = wx.Reaction()
reactions['Ac_273_1'].reactants = ['ac273']
reactions['Ac_273_1'].products = ['mo126','ag144','n','n', 'n']
reactions['Ac_273_1'].source = 'single_rate'
reactions['Ac_273_1'].data = {'type': 'single_rate', 'rate': '30'}

reactions['Ac_273_2'] = wx.Reaction()
reactions['Ac_273_2'].reactants = ['ac273']
reactions['Ac_273_2'].products = ['mo127','ag145','n']
reactions['Ac_273_2'].source = 'single_rate'
reactions['Ac_273_2'].data = {'type': 'single_rate', 'rate': '40'}

reactions['Ac_273_3'] = wx.Reaction()
reactions['Ac_273_3'].reactants = ['ac273']
reactions['Ac_273_3'].products = ['nb125','cd147','n']
reactions['Ac_273_3'].source = 'single_rate'
reactions['Ac_273_3'].data = {'type': 'single_rate', 'rate': '10'}


t9 = [0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0,7.0, 10.0]
sef = list(np.ones(10))
rate = [1000, 1500, 2000, 3000, 3200, 3500, 3300, 3200, 3100, 3000]
rate1 = list(np.array(rate)*0.3)
rate2 = list(np.array(rate)*0.4)

reactions['Th_284'] = wx.Reaction()
reactions['Th_284'].reactants = ['th284','n']
reactions['Th_284'].products = ['cu92','zn96','ga96','n']
reactions['Th_284'].source = 'rate_table'
reactions['Th_284'].data = {'type': 'rate_table', 't9': t9, 'rate': rate1, 'sef': sef}

reactions['Th_284_1'] = wx.Reaction()
reactions['Th_284_1'].reactants = ['th284','n']
reactions['Th_284_1'].products = ['cu93','zn95','ga97']
reactions['Th_284_1'].source = 'rate_table'
reactions['Th_284_1'].data = {'type': 'rate_table', 't9': t9, 'rate': rate2,'sef': sef}

reactions['Th_284_2'] = wx.Reaction()
reactions['Th_284_2'].reactants = ['th284','n']
reactions['Th_284_2'].products = ['zr131','sn154']
reactions['Th_284_2'].source = 'rate_table'
reactions['Th_284_2'].data = {'type': 'rate_table', 't9': t9, 'rate': rate1,'sef': sef}

old_xml = wx.Xml('my_net.xml')
r = old_xml.get_reaction_data()

extended_xml = wx.New_Xml(xml_type = 'reaction_data')
fission_list = ['Ac_273', 'Ac_273_1', 'Ac_273_2', 'Ac_273_3', 'Th_284','Th_284_1','Th_284_2']

new_xml = wx.New_Xml(xml_type='reaction_data')
new_xml.set_reaction_data(reactions)
new_xml.write('new_reaction_data.xml')





#for i in range(len(fission_list)):
#    r[fission_list[i]] = reactions[fission_list[i]]

#extended_xml.set_reaction_data(r)
#extended_xml.write('reaction_with_fission.xml')

#xml = wx.Xml('reaction_with_fission.xml')
#xml.validate()


    











