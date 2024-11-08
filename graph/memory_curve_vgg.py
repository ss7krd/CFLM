import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 36})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.09      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

stepX=[5, 10, 15, 20, 25, 30]
#DRAWING VERTICAL CHARTS
vals = pd.read_csv('training_time_data_until_converge.csv')
vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')

our_system = vals['our_system'].tolist()
# sixtykValuesModified = []
# for i in sixtykValues:
#     j = (i/100.0)*6415
#     sixtykValuesModified.append(j) 

# rects1 = ax.bar(ind, our_system, width, color='r', edgecolor='black', hatch="+", label="Our System")
ax.plot(stepX,our_system,c='r',marker="o",markersize=22,ls='-',label="MAFLED",fillstyle='full', linewidth = 4)

federated_learning = vals['federated_learning'].tolist()
ax.plot(stepX,federated_learning,c='b',marker="*",markersize=22,ls='-',label="BFL",fillstyle='full', linewidth = 4)
# fortykValuesModified = []
# for i in fortykValues:
#     j = (i/100.0)*7222
#     fortykValuesModified.append(j)

# rects2 = ax.bar(ind+width, federated_learning, width, color='b', edgecolor='black', hatch="*", label='Federated Learning')

ctrust = vals['ctrust'].tolist()
ax.plot(stepX, ctrust, c='purple', marker='H', markersize=22, ls='-', label='AFL', fillstyle='full', linewidth=4)

# malDeviceDetect_trustAwareReassignment = vals['malDeviceDetect_trustAwareReassignment'].tolist()
# ax.plot(stepX,malDeviceDetect_trustAwareReassignment,c='grey',marker="x",markersize=22,ls='-',label="TOM",fillstyle='full', linewidth = 4)
# twentyfourkValuesModified = []
# for i in twentyfourkValues:
#     j = (i/100.0)*8087
#     twentyfourkValuesModified.append(j)

# rects3 = ax.bar(ind+width*2, malDeviceDetect_trustAwareReassignment, width, color='grey', edgecolor='black', hatch="x", label='Trust-aware')


# new_fl = vals['FL'].tolist()
# ax.plot(stepX, new_fl, c='purple', marker='H', markersize=22, ls='-', label='BFL1', fillstyle='full', linewidth=4)


# drop = vals['drop'].tolist()
# ax.plot(stepX, drop, c='darkred', marker='h', markersize=22, ls='-', label='Drop', fillstyle='full', linewidth=4)
# rects4 = ax.bar(ind+width*3, drop, width, color = 'purple', edgecolor = 'black', hatch = '-', label = 'Drop')

#!!nicher parai change korte hobe


# our_system_wo_group = vals_eachComp['our_system_wo_group'].tolist()
# ax.plot(stepX,our_system_wo_group,c='crimson',marker="s",markersize=22,ls='-',label="TrustMe/H",fillstyle='full', linewidth = 4)
# rects4 = ax.bar(ind+width*4, our_system_wo_group, width, color='b', edgecolor='black', hatch="*", label='Our System/G')

# our_system_wo_reassign = vals_eachComp['our_system_wo_reassign'].tolist()
# ax.plot(stepX,our_system_wo_reassign,c='black',marker="D",markersize=22,ls='-',label="TrustMe/R",fillstyle='full', linewidth = 4)
# rects5 = ax.bar(ind+width*5, our_system_wo_reassign, width, color='grey', edgecolor='black', hatch="x", label='Our System/R')

our_system_wo_ir = vals_eachComp['our_system_wo_ir'].tolist()
ax.plot(stepX,our_system_wo_ir,c='pink',marker="<",markersize=22,ls='-',label="MAFLED/MD",fillstyle='full', linewidth = 4)

our_system_wo_ie = vals_eachComp['our_system_wo_ie'].tolist()
ax.plot(stepX,our_system_wo_ie,c='gold',marker=">",markersize=22,ls='-',label="MAFLED/MS",fillstyle='full', linewidth = 4)

our_system_wo_partial_task = vals_eachComp['our_system_wo_partial_task'].tolist()
ax.plot(stepX, our_system_wo_partial_task, c = 'cyan', marker = '+', markersize = 22, ls = '-', label = "MAFLED/FB", fillstyle = 'full', linewidth = 4)
# rects6 = ax.bar(ind+width*6, our_system_wo_partial_task, width, color = 'purple', edgecolor = 'black', hatch = 'o', label = 'Our System/PT')

our_system_wo_all_task = vals_eachComp['our_system_wo_all_task'].tolist()
ax.plot(stepX, our_system_wo_all_task, c = 'orange', marker = '1', markersize = 22, ls = '-', label = "MAFLED/DE", fillstyle = 'full', linewidth = 4)
# rects5 = ax.bar(ind+width*7, our_system_wo_all_task, width, color = 'orange', edgecolor = 'black', hatch = 'O', label = 'Our System/AT')


# our_system_wo_syn_data = vals_eachComp['our_system_wo_syn_data'].tolist()
# ax.plot(stepX, our_system_wo_syn_data, c = 'g', marker = 'H', markersize = 22, ls = '-', label = "TrustMe/SD", fillstyle = 'full', linewidth = 4)
# rects6 = ax.bar(ind+width*8, our_system_wo_syn_data, width, color = 'lightgreen', edgecolor = 'black', hatch = '-', label = 'Our System/SD')
# h2tdrValues_knn = vals['h2tdrValues_knn'].tolist()

# # twelvekValuesModified = []
# # for i in twelvekValues:
# #     j = (i/100.0)*10400
# #     twelvekValuesModified.append(j)

# rects4 = ax.bar(ind+width*3, h2tdrValues_knn, width, color='g', edgecolor='black', hatch="o")

# xvalueNames = ["Step 1","Step 2","Step 3","Step 4","Step 5","Step 6","Step 7","Step 8", "Step 9", "Step 10"]

ax.set_ylabel('Memory (MB)')
ax.set_xlabel('Number of clusters')
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [5, 10, 15, 20, 25, 30]
# plt.xticks(xvalues)
plt.xticks(xvalues)
ax.set_xticklabels(["%d" % x for x in xvalues], fontsize=36)

# ax.set_ylim(70, 100)
ytickvalues = []
# for i in range(70, 105, 10):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=36)
# ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('iWash', 'WristWash', 'H2DTR-NN', 'H2DTR-kNN'), loc=1, fontsize=28 )

# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our System', 'Federated Learning', 'Malicious Device Detection+Trust-aware Reassignment'), loc=1, fontsize=28)

# ax.legend(loc=1)
# plt.title("Categorization of Errors in Critical Cases")
# def autolabel(rects):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
#                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)

# plt.show()

#DRAWING HORIZONTAL CHARTS
# our_lexicon_bangla = [9.8, 1.33]
# rects1 = ax.barh(ind, our_lexicon_bangla, width, color='r', edgecolor='black', hatch=patterns[0])
# our_lexicon_romanized = [9.9, 1.27]
# rects2 = ax.barh(ind+width, our_lexicon_romanized, width, color='g', edgecolor='black', hatch=patterns[1])
# google_lexicon = [14.8, 1.88]
# rects3 = ax.barh(ind+width*2, google_lexicon, width, color='b', edgecolor='black', hatch=patterns[9])

# ax.set_xlabel('Percentage')
# ax.set_yticks(ind+width)
# ax.set_yticklabels( ('WER %', 'PER %') )
# # ax.set_xlim(0,25)
# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our lexicon Bangla', 'Our lexicon romanized', 'Google lexicon') )

# # def autolabel(rects):
# #     for rect in rects:
# #         h = rect.get_height()
# #         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
# #                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0, box.y0 + box.height*0.03, box.width, box.height*0.75])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.55), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='32', ncol=4, handleheight=2.2, labelspacing=0.0, frameon=False) 
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          # fancybox=True, shadow=True, ncol=5)
# plt.legend(frameon=False)
# leg.get_frame().set_linewidth(0.0)
# fig.tight_layout()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
# figure = plt.gcf()  # get current figure
# figure.set_size_inches(50, 30)
# plt.savefig("/home/sudipta/Desktop/image_filename_test.png")
plt.show()