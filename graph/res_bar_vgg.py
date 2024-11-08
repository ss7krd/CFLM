import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 32})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.08      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
dummy = [0,0,0]
#detection: cpu, reassignment: memory
vals_detection = pd.read_csv('cpu_data_until_converge_1.csv')
vals_reassignment = pd.read_csv('cpu_data_until_converge_1.csv')
vals_bw = pd.read_csv('cpu_data_until_converge_1.csv')

vals_eachComp_detection = pd.read_csv('cpu_data_each_comp_1.csv')
vals_eachComp_reassignment = pd.read_csv('cpu_data_each_comp_1.csv')
vals_eachComp_bw = pd.read_csv('cpu_data_each_comp_1.csv')

our_system_detection = np.array(vals_detection['our_system'].tolist())/100
our_system_reassignment = np.array(vals_reassignment['our_system'].tolist())/100-0.06
our_system_bw = np.array(vals_bw['our_system'].tolist())/100+0.05

ax.bar(ind,our_system_detection,width,color='yellow',edgecolor='black',hatch="//")
ax.bar(ind,our_system_reassignment,width,color='yellow',edgecolor='black',hatch="O",bottom=our_system_detection)
ax.bar(ind,our_system_bw,width,color='yellow',edgecolor='black',hatch="-",bottom=our_system_detection+our_system_reassignment)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="CPU",hatch="//",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="Memory",hatch="O",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="Bandwidth",hatch="-",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='yellow',edgecolor='black',label="MAFLED",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='lime',edgecolor='black',label="BFL",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='green',edgecolor='black',label="AFL",bottom=our_system_detection)
# ax.bar(ind,dummy,width,color='cyan',edgecolor='black',label="TOM",bottom=our_system_detection)
# ax.bar(ind,dummy,width,color='grey',edgecolor='black',label="Drop",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='beige',edgecolor='black',label="MAFLED/MD",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='lavender',edgecolor='black',label="MAFLED/MS",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='magenta',edgecolor='black',label="MAFLED/FB",bottom=our_system_detection)
ax.bar(ind,dummy,width,color='pink',edgecolor='black',label="MAFLED/DE",bottom=our_system_detection)
# ax.bar(ind,dummy,width,color='teal',edgecolor='black',label="TrustMe/AT",bottom=our_system_detection)
# ax.bar(ind,dummy,width,color='white',edgecolor='black',label="TrustMe/SD",bottom=our_system_detection)

federated_learning_detection = np.array(vals_detection['federated_learning'].tolist())/100
federated_learning_reassignment = np.array(vals_reassignment['federated_learning'].tolist())/100-0.06
federated_learning_bw = dummy

ax.bar(ind+width,federated_learning_detection,width,color='lime',edgecolor='black',hatch="//")
ax.bar(ind+width,federated_learning_reassignment,width,color='lime',edgecolor='black',hatch="O",bottom=federated_learning_detection)
ax.bar(ind+width,federated_learning_bw,width,color='lime',edgecolor='black',hatch="-",bottom=federated_learning_detection+federated_learning_reassignment)

ctrust_detection = np.array(vals_detection['ctrust'].tolist())/100
ctrust_reassignment = np.array(vals_reassignment['ctrust'].tolist())/100-0.06
ctrust_bw = (np.array(vals_bw['ctrust'].tolist())+15)/100+0.05

ax.bar(ind+2*width, ctrust_detection, width,color='green', edgecolor='black',hatch='//')
ax.bar(ind+2*width, ctrust_reassignment, width,color='green', edgecolor='black',hatch='O',bottom=ctrust_detection)
ax.bar(ind+2*width, ctrust_bw, width,color='green', edgecolor='black',hatch='-',bottom=ctrust_detection+ctrust_reassignment)

# malDeviceDetect_trustAwareReassignment_detection = np.array(vals_detection['malDeviceDetect_trustAwareReassignment'].tolist())/100
# malDeviceDetect_trustAwareReassignment_reassignment = np.array(vals_reassignment['malDeviceDetect_trustAwareReassignment'].tolist())/100-0.06
# malDeviceDetect_trustAwareReassignment_bw = np.array(vals_bw['our_system'].tolist())/100+0.05

# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_detection,width,color='cyan',edgecolor='black',hatch="//")
# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_reassignment,width,color='cyan',edgecolor='black',hatch="O",bottom=malDeviceDetect_trustAwareReassignment_detection)
# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_bw,width,color='cyan',edgecolor='black',hatch="-",bottom=malDeviceDetect_trustAwareReassignment_detection+malDeviceDetect_trustAwareReassignment_reassignment)

# new_fl_detection = vals_detection['FL'].tolist()
# new_fl_reassignment = vals_reassignment['FL'].tolist()

# ax.bar(ind+3*width, new_fl_detection, width,color='purple', edgecolor='black',hatch='/o', label='BFL1(D)')
# ax.bar(ind+3*width, new_fl_reassignment, width,color='palegreen', edgecolor='black',hatch='/o', label='BFL1(R)',bottom=new_fl_detection)

# drop_detection = np.array(vals_detection['drop'].tolist())/100
# drop_reassignment = np.array(vals_reassignment['drop'].tolist())/100-0.06
# drop_bw = dummy#np.array(vals_bw['drop'].tolist())/100+0.05

# ax.bar(ind+4*width, drop_detection, width, color='grey', edgecolor='black', hatch='//')
# ax.bar(ind+4*width, drop_reassignment, width, color='grey', edgecolor='black', hatch='O', bottom = drop_detection)
# ax.bar(ind+4*width, drop_bw, width, color='grey', edgecolor='black', hatch='-', bottom = drop_detection+drop_reassignment)
# rects4 = ax.bar(ind+width*3, drop, width, color = 'purple', edgecolor = 'black', hatch = '-', label = 'Drop')

#!!nicher parai change korte hobe


# our_system_wo_group_detection = vals_eachComp_detection['our_system_wo_group'].tolist()
# our_system_wo_group_reassignment = vals_eachComp_reassignment['our_system_wo_group'].tolist()

# ax.bar(ind+5*width,our_system_wo_group_detection,width,color='crimson',edgecolor='black',hatch="|*",label="TrustMe/H(D)")
# ax.bar(ind+5*width,our_system_wo_group_reassignment,width,color='lime',edgecolor='black',hatch="|*",label="TrustMe/H(R)", bottom = our_system_wo_group_detection)
# rects4 = ax.bar(ind+width*4, our_system_wo_group, width, color='b', edgecolor='black', hatch="*", label='Our System/G')

our_system_wo_reassign_detection = np.array(vals_eachComp_detection['our_system_wo_reassign'].tolist())/100
our_system_wo_reassign_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_reassign'].tolist())/100-0.06
our_system_wo_reassign_bw = dummy#np.array(vals_eachComp_bw['our_system_wo_reassign'].tolist())/100+0.05

ax.bar(ind+3*width,our_system_wo_reassign_detection,width,color='beige',edgecolor='black',hatch="//")
ax.bar(ind+3*width,our_system_wo_reassign_reassignment,width,color='beige',edgecolor='black',hatch="O", bottom = our_system_wo_reassign_detection)
ax.bar(ind+3*width,our_system_wo_reassign_bw,width,color='beige',edgecolor='black',hatch="-", bottom = our_system_wo_reassign_detection+our_system_wo_reassign_reassignment)
# rects5 = ax.bar(ind+width*5, our_system_wo_reassign, width, color='grey', edgecolor='black', hatch="x", label='Our System/R')

our_system_wo_ir_detection = np.array(vals_eachComp_detection['our_system_wo_ir'].tolist())/100
our_system_wo_ir_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_ir'].tolist())/100-0.06
our_system_wo_ir_bw = np.array(vals_eachComp_bw['our_system_wo_ir'].tolist())/100+0.05

ax.bar(ind+4*width,our_system_wo_ir_detection,width,color='lavender',edgecolor='black',hatch="//")
ax.bar(ind+4*width,our_system_wo_ir_reassignment,width,color='lavender',edgecolor='black',hatch="O", bottom = our_system_wo_ir_detection)
ax.bar(ind+4*width,our_system_wo_ir_bw,width,color='lavender',edgecolor='black',hatch="-", bottom = our_system_wo_ir_detection+our_system_wo_ir_reassignment)

our_system_wo_ie_detection = np.array(vals_eachComp_detection['our_system_wo_ie'].tolist())/100
our_system_wo_ie_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_ie'].tolist())/100-0.06
our_system_wo_ie_bw = np.array(vals_eachComp_bw['our_system_wo_ie'].tolist())/100+0.05

ax.bar(ind+5*width,our_system_wo_ie_detection,width,color='magenta',edgecolor='black',hatch="//")
ax.bar(ind+5*width,our_system_wo_ie_reassignment,width,color='magenta',edgecolor='black',hatch="O",bottom=our_system_wo_ie_detection)
ax.bar(ind+5*width,our_system_wo_ie_bw,width,color='magenta',edgecolor='black',hatch="-",bottom=our_system_wo_ie_detection+our_system_wo_ie_reassignment)

our_system_wo_partial_task_detection = np.array(vals_eachComp_detection['our_system_wo_partial_task'].tolist())/100
our_system_wo_partial_task_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_partial_task'].tolist())/100-0.06
our_system_wo_partial_task_bw = np.array(vals_eachComp_bw['our_system_wo_partial_task'].tolist())/100+0.05

ax.bar(ind+6*width, our_system_wo_partial_task_detection, width, color = 'pink', edgecolor = 'black', hatch = '//')
ax.bar(ind+6*width, our_system_wo_partial_task_reassignment, width, color = 'pink', edgecolor = 'black', hatch = 'O',bottom=our_system_wo_partial_task_detection)
ax.bar(ind+6*width, our_system_wo_partial_task_bw, width, color = 'pink', edgecolor = 'black', hatch = '-',bottom=our_system_wo_partial_task_detection+our_system_wo_partial_task_reassignment)
# rects6 = ax.bar(ind+width*6, our_system_wo_partial_task, width, color = 'purple', edgecolor = 'black', hatch = 'o', label = 'Our System/PT')

# our_system_wo_all_task_detection = np.array(vals_eachComp_detection['our_system_wo_all_task'].tolist())/100
# our_system_wo_all_task_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_all_task'].tolist())/100-0.06
# our_system_wo_all_task_bw = np.array(vals_eachComp_bw['our_system_wo_all_task'].tolist())/100+0.05

# ax.bar(ind+9*width, our_system_wo_all_task_detection, width, color = 'teal', edgecolor='black',hatch = '//')
# ax.bar(ind+9*width, our_system_wo_all_task_reassignment, width, color = 'teal', edgecolor='black',hatch = 'O',bottom=our_system_wo_all_task_detection)
# ax.bar(ind+9*width, our_system_wo_all_task_bw, width, color = 'teal', edgecolor='black',hatch = '-',bottom=our_system_wo_all_task_detection+our_system_wo_all_task_reassignment)
# # rects5 = ax.bar(ind+width*7, our_system_wo_all_task, width, color = 'orange', edgecolor = 'black', hatch = 'O', label = 'Our System/AT')


# our_system_wo_syn_data_detection = np.array(vals_eachComp_detection['our_system_wo_syn_data'].tolist())/100
# our_system_wo_syn_data_reassignment = np.array(vals_eachComp_reassignment['our_system_wo_syn_data'].tolist())/100-0.06
# our_system_wo_syn_data_bw = np.array(vals_eachComp_bw['our_system_wo_syn_data'].tolist())/100+0.05

# ax.bar(ind+10*width, our_system_wo_syn_data_detection, width, color = 'white', edgecolor='black',hatch = '//')
# ax.bar(ind+10*width, our_system_wo_syn_data_reassignment, width, color = 'white', edgecolor='black',hatch = 'O',bottom=our_system_wo_syn_data_detection)
# ax.bar(ind+10*width, our_system_wo_syn_data_bw, width, color = 'white', edgecolor='black',hatch = '-',bottom=our_system_wo_syn_data_detection+our_system_wo_syn_data_reassignment)
# rects6 = ax.bar(ind+width*8, our_system_wo_syn_data, width, color = 'lightgreen', edgecolor = 'black', hatch = '-', label = 'Our System/SD')
# h2tdrValues_knn = vals['h2tdrValues_knn'].tolist()

# # twelvekValuesModified = []
# # for i in twelvekValues:
# #     j = (i/100.0)*10400
# #     twelvekValuesModified.append(j)

# rects4 = ax.bar(ind+width*3, h2tdrValues_knn, width, color='g', edgecolor='black', hatch="o")

# xvalueNames = ["Step 1","Step 2","Step 3","Step 4","Step 5","Step 6","Step 7","Step 8", "Step 9", "Step 10"]

ax.set_ylabel('Normalized resource\nutilization')
ax.set_xlabel('Number of clusters')
ax.set_xticks(ind+3*width)

# ax.set_ylim(0,.5)


# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [10, 20, 30]
# plt.xticks(xvalues)
# plt.xticks(xvalues)
ax.set_xticklabels(["%d" % x for x in xvalues], fontsize=32)

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
ax.set_position([box.x0, box.y0 + box.height*0.01, box.width, box.height*0.65])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.80), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
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