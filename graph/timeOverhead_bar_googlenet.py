import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 40})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.15    # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
dummy = [0,0,0,0,0,0]
#detection: cpu, reassignment: memory
vals_m = pd.read_csv('m_bar_googlenet.csv')
vals_cs = pd.read_csv('cs_bar_googlenet.csv')
vals_fd = pd.read_csv('fd_bar_googlenet.csv')
vals_de = pd.read_csv('de_bar_googlenet.csv')
# vals_m = pd.read_csv('cpu_data_each_comp_1.csv')
# vals_cs = pd.read_csv('cpu_data_each_comp_1.csv')
# vals_fd = pd.read_csv('cpu_data_each_comp_1.csv')

cflmd_m = np.array(vals_m['cflmd'].tolist())
cflmd_cs = np.array(vals_cs['cflmd'].tolist())*1.25
cflmd_fd = np.array(vals_fd['cflmd'].tolist())*1.25
cflmd_de = np.array(vals_de['cflmd'].tolist())*1.25

ax.bar(ind,cflmd_m,width,color=[(1,0.7,0)],edgecolor='black',hatch="//")
ax.bar(ind,cflmd_cs,width,color=[(1,0.7,0)],edgecolor='black',hatch="O",bottom=cflmd_m)
ax.bar(ind,cflmd_fd,width,color=[(1,0.7,0)],edgecolor='black',hatch="-",bottom=cflmd_m+cflmd_cs)
ax.bar(ind,cflmd_de,width,color=[(1,0.7,0)],edgecolor='black',bottom=cflmd_m+cflmd_cs+cflmd_fd)

ax.bar(ind,dummy,width,color='white',edgecolor='black',label="DS",hatch="//",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="US",hatch="O",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="FD",hatch="-",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='white',edgecolor='black',label="DE",bottom=cflmd_m)

ax.bar(ind,dummy,width,color=[(1,0.7,0)],edgecolor='black',label="CFLM",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='pink',edgecolor='black',label="FedCPF",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='cyan',edgecolor='black',label="LDF",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='darkgrey',edgecolor='black',label="CEFL",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='yellow',edgecolor='black',label="LGC",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='tomato',edgecolor='black',label="CFLM/DS",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='deepskyblue',edgecolor='black',label="CFLM/US",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='lime',edgecolor='black',label="CFLM/FD",bottom=cflmd_m)
ax.bar(ind,dummy,width,color='beige',edgecolor='black',label="CFLM/DE",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='teal',edgecolor='black',label="TrustMe/AT",bottom=cflmd_m)
# ax.bar(ind,dummy,width,color='white',edgecolor='black',label="TrustMe/SD",bottom=cflmd_m)

bfl_m = np.array(vals_m['bfl'].tolist())
bfl_cs = np.array(vals_cs['bfl'].tolist())*1.25
bfl_fd = np.array(vals_fd['bfl'].tolist())*1.25
bfl_de = np.array(vals_de['bfl'].tolist())*1.25

# ax.bar(ind+width,bfl_m,width,color='pink',edgecolor='black',hatch="//")
# ax.bar(ind+width,bfl_cs,width,color='pink',edgecolor='black',hatch="O",bottom=bfl_m)
# ax.bar(ind+width,bfl_fd,width,color='pink',edgecolor='black',hatch="-",bottom=bfl_m+bfl_cs)
# ax.bar(ind+width,bfl_de,width,color='pink',edgecolor='black',bottom=bfl_m+bfl_cs+bfl_fd)

afl_m = np.array(vals_m['afl'].tolist())
afl_cs = np.array(vals_cs['afl'].tolist())*1.25
afl_fd = (np.array(vals_fd['afl'].tolist()))*1.25
afl_de = (np.array(vals_de['afl'].tolist()))*1.25

# ax.bar(ind+2*width, afl_m, width,color='cyan', edgecolor='black',hatch='//')
# ax.bar(ind+2*width, afl_cs, width,color='cyan', edgecolor='black',hatch='O',bottom=afl_m)
# ax.bar(ind+2*width, afl_fd, width,color='cyan', edgecolor='black',hatch='-',bottom=afl_m+afl_cs)
# ax.bar(ind+2*width, afl_de, width,color='cyan', edgecolor='black',bottom=afl_m+afl_cs+afl_fd)

cfl_m = np.array(vals_m['cfl'].tolist())
cfl_cs = np.array(vals_cs['cfl'].tolist())*1.25
cfl_fd = (np.array(vals_fd['cfl'].tolist()))*1.25
cfl_de = (np.array(vals_de['cfl'].tolist()))*1.25

# ax.bar(ind+3*width, cfl_m, width,color='darkgrey', edgecolor='black',hatch='//')
# ax.bar(ind+3*width, cfl_cs, width,color='darkgrey', edgecolor='black',hatch='O',bottom=cfl_m)
# ax.bar(ind+3*width, cfl_fd, width,color='darkgrey', edgecolor='black',hatch='-',bottom=cfl_m+cfl_cs)
# ax.bar(ind+3*width, cfl_de, width,color='darkgrey', edgecolor='black',bottom=cfl_m+cfl_cs+cfl_fd)

lgc_m = np.array(vals_m['lgc'].tolist())
lgc_cs = np.array(vals_cs['lgc'].tolist())*1.25
lgc_fd = (np.array(vals_fd['lgc'].tolist()))*1.25
lgc_de = (np.array(vals_de['lgc'].tolist()))*1.25

# ax.bar(ind+4*width, lgc_m, width,color='yellow', edgecolor='black',hatch='//')
# ax.bar(ind+4*width, lgc_cs, width,color='yellow', edgecolor='black',hatch='O',bottom=lgc_m)
# ax.bar(ind+4*width, lgc_fd, width,color='yellow', edgecolor='black',hatch='-',bottom=lgc_m+lgc_cs)
# ax.bar(ind+4*width, lgc_de, width,color='yellow', edgecolor='black',bottom=lgc_m+lgc_cs+lgc_fd)

# malDeviceDetect_trustAwareReassignment_m = np.array(vals_m['malDeviceDetect_trustAwareReassignment'].tolist())/100
# malDeviceDetect_trustAwareReassignment_cs = np.array(vals_cs['malDeviceDetect_trustAwareReassignment'].tolist())/100-0.06
# malDeviceDetect_trustAwareReassignment_fd = np.array(vals_fd['our_system'].tolist())/100+0.05

# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_m,width,color='cyan',edgecolor='black',hatch="//")
# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_cs,width,color='cyan',edgecolor='black',hatch="O",bottom=malDeviceDetect_trustAwareReassignment_m)
# ax.bar(ind+3*width,malDeviceDetect_trustAwareReassignment_fd,width,color='cyan',edgecolor='black',hatch="-",bottom=malDeviceDetect_trustAwareReassignment_m+malDeviceDetect_trustAwareReassignment_cs)

# new_fl_m = vals_m['FL'].tolist()
# new_fl_cs = vals_cs['FL'].tolist()

# ax.bar(ind+3*width, new_fl_m, width,color='purple', edgecolor='black',hatch='/o', label='BFL1(D)')
# ax.bar(ind+3*width, new_fl_cs, width,color='palegreen', edgecolor='black',hatch='/o', label='BFL1(R)',bottom=new_fl_m)

# drop_m = np.array(vals_m['drop'].tolist())/100
# drop_cs = np.array(vals_cs['drop'].tolist())/100-0.06
# drop_fd = dummy#np.array(vals_fd['drop'].tolist())/100+0.05

# ax.bar(ind+4*width, drop_m, width, color='grey', edgecolor='black', hatch='//')
# ax.bar(ind+4*width, drop_cs, width, color='grey', edgecolor='black', hatch='O', bottom = drop_m)
# ax.bar(ind+4*width, drop_fd, width, color='grey', edgecolor='black', hatch='-', bottom = drop_m+drop_cs)
# rects4 = ax.bar(ind+width*3, drop, width, color = 'purple', edgecolor = 'black', hatch = '-', label = 'Drop')

#!!nicher parai change korte hobe


# our_system_wo_group_m = vals_m['our_system_wo_group'].tolist()
# our_system_wo_group_cs = vals_cs['our_system_wo_group'].tolist()

# ax.bar(ind+5*width,our_system_wo_group_m,width,color='crimson',edgecolor='black',hatch="|*",label="TrustMe/H(D)")
# ax.bar(ind+5*width,our_system_wo_group_cs,width,color='yellow',edgecolor='black',hatch="|*",label="TrustMe/H(R)", bottom = our_system_wo_group_m)
# rects4 = ax.bar(ind+width*4, our_system_wo_group, width, color='b', edgecolor='black', hatch="*", label='Our System/G')

cflmd_m_m = np.array(vals_m['cflmd_m'].tolist())
cflmd_m_cs = np.array(vals_cs['cflmd_m'].tolist())*1.25
cflmd_m_fd = np.array(vals_fd['cflmd_m'].tolist())*1.25#np.array(vals_fd['cflmd_m'].tolist())/100+0.05
cflmd_m_de = np.array(vals_de['cflmd_m'].tolist())*1.25

ax.bar(ind+width,cflmd_m_m,width,color='tomato',edgecolor='black',hatch="//")
ax.bar(ind+width,cflmd_m_cs,width,color='tomato',edgecolor='black',hatch="O", bottom = cflmd_m_m)
ax.bar(ind+width,cflmd_m_fd,width,color='tomato',edgecolor='black',hatch="-", bottom = cflmd_m_m+cflmd_m_cs)
ax.bar(ind+width,cflmd_m_de,width,color='tomato',edgecolor='black', bottom = cflmd_m_m+cflmd_m_cs+cflmd_m_fd)
# rects5 = ax.bar(ind+width*5, cflmd_m, width, color='grey', edgecolor='black', hatch="x", label='Our System/R')

cflmd_cs_m = np.array(vals_m['cflmd_cs'].tolist())
cflmd_cs_cs = np.array(vals_cs['cflmd_cs'].tolist())*1.25
cflmd_cs_fd = np.array(vals_fd['cflmd_cs'].tolist())*1.25
cflmd_cs_de = np.array(vals_de['cflmd_cs'].tolist())*1.25

ax.bar(ind+2*width,cflmd_cs_m,width,color='deepskyblue',edgecolor='black',hatch="//")
ax.bar(ind+2*width,cflmd_cs_cs,width,color='deepskyblue',edgecolor='black',hatch="O", bottom = cflmd_cs_m)
ax.bar(ind+2*width,cflmd_cs_fd,width,color='deepskyblue',edgecolor='black',hatch="-", bottom = cflmd_cs_m+cflmd_cs_cs)
ax.bar(ind+2*width,cflmd_cs_de,width,color='deepskyblue',edgecolor='black', bottom = cflmd_cs_m+cflmd_cs_cs+cflmd_cs_fd)

cflmd_fd_m = np.array(vals_m['cflmd_fd'].tolist())
cflmd_fd_cs = np.array(vals_cs['cflmd_fd'].tolist())*1.25
cflmd_fd_fd = np.array(vals_fd['cflmd_fd'].tolist())*1.25
cflmd_fd_de = np.array(vals_de['cflmd_fd'].tolist())*1.25

ax.bar(ind+3*width,cflmd_fd_m,width,color='lime',edgecolor='black',hatch="//")
ax.bar(ind+3*width,cflmd_fd_cs,width,color='lime',edgecolor='black',hatch="O",bottom=cflmd_fd_m)
ax.bar(ind+3*width,cflmd_fd_fd,width,color='lime',edgecolor='black',hatch="-",bottom=cflmd_fd_m+cflmd_fd_cs)
ax.bar(ind+3*width,cflmd_fd_de,width,color='lime',edgecolor='black',bottom=cflmd_fd_m+cflmd_fd_cs+cflmd_fd_fd)

cflmd_de_m = np.array(vals_m['cflmd_de'].tolist())
cflmd_de_cs = np.array(vals_cs['cflmd_de'].tolist())*1.25
cflmd_de_fd = np.array(vals_fd['cflmd_de'].tolist())*1.25
cflmd_de_de = np.array(vals_de['cflmd_de'].tolist())*1.25

ax.bar(ind+4*width, cflmd_de_m, width, color = 'beige', edgecolor = 'black', hatch = '//')
ax.bar(ind+4*width, cflmd_de_cs, width, color = 'beige', edgecolor = 'black', hatch = 'O',bottom=cflmd_de_m)
ax.bar(ind+4*width, cflmd_de_fd, width, color = 'beige', edgecolor = 'black', hatch = '-',bottom=cflmd_de_m+cflmd_de_cs)
ax.bar(ind+4*width, cflmd_de_de, width, color = 'beige', edgecolor = 'black',bottom=cflmd_de_m+cflmd_de_cs+cflmd_de_fd)
# rects6 = ax.bar(ind+width*6, cflmd_de, width, color = 'purple', edgecolor = 'black', hatch = 'o', label = 'Our System/PT')

# our_system_wo_all_task_m = np.array(vals_m['our_system_wo_all_task'].tolist())/100
# our_system_wo_all_task_cs = np.array(vals_cs['our_system_wo_all_task'].tolist())/100-0.06
# our_system_wo_all_task_fd = np.array(vals_fd['our_system_wo_all_task'].tolist())/100+0.05

# ax.bar(ind+9*width, our_system_wo_all_task_m, width, color = 'teal', edgecolor='black',hatch = '//')
# ax.bar(ind+9*width, our_system_wo_all_task_cs, width, color = 'teal', edgecolor='black',hatch = 'O',bottom=our_system_wo_all_task_m)
# ax.bar(ind+9*width, our_system_wo_all_task_fd, width, color = 'teal', edgecolor='black',hatch = '-',bottom=our_system_wo_all_task_m+our_system_wo_all_task_cs)
# # rects5 = ax.bar(ind+width*7, our_system_wo_all_task, width, color = 'orange', edgecolor = 'black', hatch = 'O', label = 'Our System/AT')


# our_system_wo_syn_data_m = np.array(vals_m['our_system_wo_syn_data'].tolist())/100
# our_system_wo_syn_data_cs = np.array(vals_cs['our_system_wo_syn_data'].tolist())/100-0.06
# our_system_wo_syn_data_fd = np.array(vals_fd['our_system_wo_syn_data'].tolist())/100+0.05

# ax.bar(ind+10*width, our_system_wo_syn_data_m, width, color = 'white', edgecolor='black',hatch = '//')
# ax.bar(ind+10*width, our_system_wo_syn_data_cs, width, color = 'white', edgecolor='black',hatch = 'O',bottom=our_system_wo_syn_data_m)
# ax.bar(ind+10*width, our_system_wo_syn_data_fd, width, color = 'white', edgecolor='black',hatch = '-',bottom=our_system_wo_syn_data_m+our_system_wo_syn_data_cs)
# rects6 = ax.bar(ind+width*8, our_system_wo_syn_data, width, color = 'lightgreen', edgecolor = 'black', hatch = '-', label = 'Our System/SD')
# h2tdrValues_knn = vals['h2tdrValues_knn'].tolist()

# # twelvekValuesModified = []
# # for i in twelvekValues:
# #     j = (i/100.0)*10400
# #     twelvekValuesModified.append(j)

# rects4 = ax.bar(ind+width*3, h2tdrValues_knn, width, color='g', edgecolor='black', hatch="o")

# xvalueNames = ["Step 1","Step 2","Step 3","Step 4","Step 5","Step 6","Step 7","Step 8", "Step 9", "Step 10"]

ax.set_ylabel('Time overhead (sec)')
ax.set_xlabel('Number of devices')
ax.set_xticks(ind+2*width)

# ax.set_ylim(0,.5)


# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [100,200,300,400,500,600]
# plt.xticks(xvalues)
# plt.xticks(xvalues)
ax.set_xticklabels(["%d" % x for x in xvalues], fontsize=40)

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
ax.set_position([box.x0, box.y0 + box.height*0.01, box.width, box.height*0.70])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.65), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='40', ncol=3, handleheight=1.5, labelspacing=0.0, frameon=False) 
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