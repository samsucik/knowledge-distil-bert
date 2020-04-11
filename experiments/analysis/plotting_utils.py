import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines

leg_lw = 7

leg_kwargs = {
    "labelspacing": 0.1,
    "borderpad": 0.4, 
    "handletextpad": 0.5, 
    "borderaxespad": 0.3,
    "framealpha": 0.9,
    "columnspacing": 1.0,
    "handlelength": 1.0,
}
glue_tasks = ["CoLA", "SST-2", "Sara"]
glue_task_colours = {
    "CoLA": (0, 173, 118),
    "SST-2": (191, 115, 0),
    "Sara": (90, 23, 238),
    "pre-trained": (10, 10, 10),
}
glue_task_colours = {name: np.array(c)/255 for name, c in glue_task_colours.items()}

def unify_legend_outside(fig, axs, alternate_lws=[leg_lw], legcols=1, position="right", additional_handles=[]):
    ax = fig.add_subplot(1, 1, 1)
    ax.set_axis_off()
    handles, labels = axs.flatten()[-1].get_legend_handles_labels()
    n_handles_orig = len(handles)
    handles += additional_handles
    for h in additional_handles:
    	labels.append(h.get_label())
    legcols = legcols if legcols > 0 else len(handles)
    if position == "right":
    	legend = ax.legend(handles, labels, bbox_to_anchor=(1.0, 0.5), loc='center right', 
               bbox_transform=fig.transFigure, ncol=legcols, **leg_kwargs)
    elif position == "bottom":
    	legend = ax.legend(handles, labels, bbox_to_anchor=(0.5, 0.0), loc='lower center', 
               bbox_transform=fig.transFigure, ncol=legcols, **leg_kwargs)
    elif position == "top":
    	legend = ax.legend(handles, labels, bbox_to_anchor=(0.5, 1.0), loc='upper center', 
               bbox_transform=fig.transFigure, ncol=legcols, **leg_kwargs)
    else:
    	raise ValueError("Invalid legend position: {}".format(position))
    for i, legobj in enumerate(legend.legendHandles):
        if i < n_handles_orig:
        	legobj.set_linewidth(alternate_lws[i % len(alternate_lws)])
    for a in axs.flatten():
    	leg = a.get_legend()
    	if leg is not None:
    		leg.remove()

def add_overall_axislabel(fig, label, axis="y", side="left", pad=None):
    fig.add_subplot(111, zorder=0)
    ax = plt.gca()
    ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False, length=0)
    if axis == "y":
        ax.set_ylabel(label, labelpad=pad)
    else:
        ax.set_xlabel(label, labelpad=pad)
    despine(ax)
    ax.set_facecolor((0,0,0,0))

def smooth_series(x, N=5):
    return pd.Series(x).rolling(window=N).mean().iloc[N-1:].values

def despine(a):
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
    a.spines["bottom"].set_visible(False)
    a.spines["left"].set_visible(False)

def colour_subplot_gaps(fig, c="black"):
    fig.add_subplot(111, zorder=0)
    ax = plt.gca()
    ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False, length=0)
    ax.set_facecolor(c)
    despine(ax)
    return ax

def make_latex_label(model="BERT", role="student"):
	return "$\\text{" + model + "}_{\\text{" + ("S" if role == "student" else "T") + "}}$"

def new_legend_entry(c="black", label="label", marker=None, markersize=5, lw=3):
	handle = mlines.Line2D([], [], color=c, marker=marker,
	                     markersize=markersize, label=label, linewidth=lw)
	return handle
