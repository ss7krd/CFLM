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

N = 2
ind = np.arange(2)  # the x locations for the groups
width = 0.08      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]


#DRAWING VERTICAL CHARTS
vals = pd.read_csv('accuracy_trainingTime_bar_real_lstm.csv')
# vals = pd.read_csv('accuracy_trainingTime_data_each_comp_real.csv')

cflmd = vals['cflmd'].tolist()
rects1 = ax.bar(ind[0], cflmd[0]-0.2, width, color=[(1,0.7,0)],edgecolor='black',label="CFLMD")

bfl = vals['bfl'].tolist()
rects2 = ax.bar(ind[0]+width, bfl[0]-0.2, width, color='pink',edgecolor='black',label="FedCPF")

afl = vals['afl'].tolist()
ax.bar(ind[0]+width*2, afl[0]-0.2, width, color = 'cyan', edgecolor='black', label="LDF")

cfl = vals['cfl'].tolist()
rects3 = ax.bar(ind[0]+width*3, cfl[0]-0.2, width, color='darkgrey',edgecolor='black',label="CEFL")

# new_fl = vals['FL'].tolist()
# rects4 = ax.bar(ind[0]+width*3, new_fl[0], width, color='purple', edgecolor='black',hatch='/o', label="BFL1")

lgc = vals['lgc'].tolist()
rects1 = ax.bar(ind[0]+width*4, lgc[0]-0.2, width, color='yellow', edgecolor='black', label="LGC")

# cflmd_wo_group = vals['cflmd_wo_group'].tolist()
# rects2 = ax.bar(ind[0]+width*5, cflmd_wo_group[0], width, color='crimson',edgecolor='black',hatch="|*",label="TrustMe/H")

cflmd_m = vals['cflmd_m'].tolist()
rects3 = ax.bar(ind[0]+width*5, cflmd_m[0]-0.2, width, color='tomato',edgecolor='black',label="CFLMD/M")

cflmd_cs = vals['cflmd_cs'].tolist()
rects4 = ax.bar(ind[0]+width*6, cflmd_cs[0]-0.2, width, color='deepskyblue',edgecolor='black',label="CFLMD/CS")

cflmd_fd = vals['cflmd_fd'].tolist()
rects1 = ax.bar(ind[0]+width*7, cflmd_fd[0]-0.2, width, color='lime',edgecolor='black',label="CFLMD/FD")

cflmd_de = vals['cflmd_de'].tolist()
rects2 = ax.bar(ind[0]+width*8, cflmd_de[0]-0.2, width,color = 'beige', edgecolor = 'black', label = "CFLMD/DE")

# cflmd_wo_all_task = vals['cflmd_wo_all_task'].tolist()
# rects3 = ax.bar(ind[0]+width*9, cflmd_wo_all_task[0], width, color = 'orange', edgecolor='black',hatch = 'o-', label = "TrustMe/AT")

# cflmd_wo_syn_data = vals['cflmd_wo_syn_data'].tolist()
# rects4 = ax.bar(ind[0]+width*10, cflmd_wo_syn_data[0], width, color = 'g', edgecolor='black',hatch = 'O|', label = "TrustMe/SD")





# vals = pd.read_csv('accuracy_trainingTime_data_until_convergence_real.csv')
# vals = pd.read_csv('accuracy_trainingTime_data_each_comp_real.csv')

# cflmd = vals['cflmd'].tolist()
# rects1 = ax.bar(ind[0], cflmd[0], width, color='r',edgecolor='black',hatch="+")

# bfl = vals['bfl'].tolist()
# rects2 = ax.bar(ind[0]+width, bfl[0], width, color='b',edgecolor='black',hatch="*")

# afl = vals['afl'].tolist()
# ax.bar(ind[0]+width*2, afl[0], width, color = 'purple', edgecolor='black', hatch="/o")

# cfl = vals['cfl'].tolist()
# rects3 = ax.bar(ind[0]+width*3, cfl[0], width, color='grey',edgecolor='black',hatch="x")

# # new_fl = vals['FL'].tolist()
# # rects4 = ax.bar(ind[0]+width*3, new_fl[0], width, color='purple', edgecolor='black',hatch='/o', label="BFL1")

# lgc = vals['lgc'].tolist()
# rects1 = ax.bar(ind[0]+width*4, lgc[0], width, color='darkred', edgecolor='black', hatch='\\|')

# # cflmd_wo_group = vals['cflmd_wo_group'].tolist()
# # rects2 = ax.bar(ind[0]+width*5, cflmd_wo_group[0], width, color='crimson',edgecolor='black',hatch="|*",label="TrustMe/H")

# cflmd_m = vals['cflmd_m'].tolist()
# rects3 = ax.bar(ind[0]+width*5, cflmd_m[0], width, color='black',edgecolor='white',hatch="-\\")

# cflmd_cs = vals['cflmd_cs'].tolist()
# rects4 = ax.bar(ind[0]+width*6, cflmd_cs[0], width, color='pink',edgecolor='black',hatch="+o")

# cflmd_fd = vals['cflmd_fd'].tolist()
# rects1 = ax.bar(ind[0]+width*7, cflmd_fd[0], width, color='gold',edgecolor='black',hatch="x*")

# cflmd_de = vals['cflmd_de'].tolist()
# rects2 = ax.bar(ind[0]+width*8, cflmd_de[0], width,color = 'cyan', edgecolor = 'black', hatch = 'o')

# cflmd_wo_all_task = vals['cflmd_wo_all_task'].tolist()
# rects3 = ax.bar(ind[0]+width*9, cflmd_wo_all_task[0], width, color = 'orange', edgecolor='black',hatch = 'o-')

# cflmd_wo_syn_data = vals['cflmd_wo_syn_data'].tolist()
# rects4 = ax.bar(ind[0]+width*10, cflmd_wo_syn_data[0], width, color = 'g', edgecolor='black',hatch = 'O|')






# ax2.bar(ind[1], cflmd[1], width, color='r', edgecolor='black', hatch="+")

# ax2.bar(ind[1]+width, bfl[1], width, color='b', edgecolor='black', hatch="*")

# ax2.bar(ind[1]+width*2, cfl[1], width, color='grey', edgecolor='black', hatch="x")

# ax2.bar(ind[1]+width*3, lgc[1], width, color = 'purple', edgecolor = 'black', hatch = '-')




cflmd = vals['cflmd'].tolist()
rects1 = ax2.bar(ind[1], cflmd[1]*0.75, width, color=[(1,0.7,0)],edgecolor='black',label="TrustMe")

bfl = vals['bfl'].tolist()
rects2 = ax2.bar(ind[1]+width, bfl[1]*0.75, width, color='pink',edgecolor='black',label="BFL")

afl = vals['afl'].tolist()
ax2.bar(ind[1]+width*2, afl[1]*0.75, width, color = 'cyan', edgecolor='black', label="afl")

cfl = vals['cfl'].tolist()
rects3 = ax2.bar(ind[1]+width*3, cfl[1]*0.75, width, color='darkgrey',edgecolor='black',label="TOM")

# new_fl = vals['FL'].tolist()
# rects4 = ax2.bar(ind[1]+width*3, new_fl[1], width, color='purple', edgecolor='black',hatch='/o', label="BFL1")

lgc = vals['lgc'].tolist()
rects1 = ax2.bar(ind[1]+width*4, lgc[1]*0.75, width, color='yellow', edgecolor='black', label="lgc")

# cflmd_wo_group = vals['cflmd_wo_group'].tolist()
# rects2 = ax2.bar(ind[1]+width*5, cflmd_wo_group[1], width, color='crimson',edgecolor='black',hatch="|*")

cflmd_m = vals['cflmd_m'].tolist()
rects3 = ax2.bar(ind[1]+width*5, cflmd_m[1]*0.75, width, color='tomato',edgecolor='black')

cflmd_cs = vals['cflmd_cs'].tolist()
rects4 = ax2.bar(ind[1]+width*6, cflmd_cs[1]*0.75, width, color='deepskyblue',edgecolor='black')

cflmd_fd = vals['cflmd_fd'].tolist()
rects1 = ax2.bar(ind[1]+width*7, cflmd_fd[1]*0.75, width, color='lime',edgecolor='black')

cflmd_de = vals['cflmd_de'].tolist()
rects2 = ax2.bar(ind[1]+width*8, cflmd_de[1]*0.75, width,color = 'beige', edgecolor = 'black')

# cflmd_wo_all_task = vals['cflmd_wo_all_task'].tolist()
# rects3 = ax2.bar(ind[1]+width*9, cflmd_wo_all_task[1]/1.5, width, color = 'orange', edgecolor='black',hatch = 'o-')

# cflmd_wo_syn_data = vals['cflmd_wo_syn_data'].tolist()
# rects4 = ax2.bar(ind[1]+width*10, cflmd_wo_syn_data[1]/1.5, width, color = 'g', edgecolor='black',hatch = 'O|')

ax.set_ylabel('Accuracy')

ax.set_xticks(ind+4*width)
ax.set_xticklabels(['Accuracy','Training time'])

# ax.set_xlabel('Increase in number of malicious devices after each 20 iterations')

# ax.set_ylim(0,4500)

# ax.set_xticks(ind+1.5*width)

#ax.set_xticklabels(vals['error_type'].tolist())

#xvalues = [5, 10, 15, 20, 25, 30]

# xvalues = [1, 2, 3, 4, 5, 6]

# plt.xticks(xvalues)

# ax.set_xticklabels(["%d%%" % x for x in xvalues], fontsize=36)

ax.set_ylim(75, 100)
# ax2.set_ylim(40, 200)

ytickvalues = []
for i in range(75, 101, 5):
	ytickvalues.append(i)
ax.set_yticks(ytickvalues)
ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=36)


ax2.set_ylabel('Training time (min)')
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
ax.set_position([box.x0, box.y0 + box.height*0.02, box.width*0.98, box.height*0.75])
#bbox_to_anchor=(0.5, 1.6)
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.55), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
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