import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
from matplotlib import colors

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
grid_colour = np.array([1.0, 1.0, 1.0, 1.0])*0.85

def add_to_legend(ax, additional_handles=[], **kwargs):
    handles, labels = ax.get_legend_handles_labels()
    # n_handles_orig = len(handles)
    handles += additional_handles
    for h in additional_handles:
        labels.append(h.get_label())
    ax.legend(handles, labels, **kwargs)

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
        if side == "right":
            ax.yaxis.set_label_position("right")
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
    if model == "teacher":
        return "$\\text{BERT}_{\\text{T}}$"
    else:
        return "$\\text{" + model + "}_{\\text{" + ("S" if role == "student" else "T") + "}}$"

def new_legend_entry(c="black", label="label", marker=None, markersize=5, lw=3, ls="-"):
    handle = mlines.Line2D([], [], color=c, marker=marker,
                         markersize=markersize, label=label, linewidth=lw, ls=ls)
    return handle

def modify_cl(cl, modifier):
    cl = cl*modifier
    return np.array([max(0, min(c, 1.0)) for c in cl])

probing_baseline_colours = {"human": np.array(colors.to_rgb("paleturquoise")), 
                    "majority": np.array(colors.to_rgb("papayawhip")),
                    "morpho": np.array(colors.to_rgb("grey")),}
probing_baselines = {"majority": [20.0, 0.5, 17.9, 5.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0],
             "human": [100, 100, 84.0, 84.0, 98.0, 85.0, 88.0, 86.5, 81.2, 85.0],
             "conneau-best": [99.3, 88.8, 63.8, 89.6, 83.6, 91.5, 95.1, 95.1, 73.6, 76.2],
             "morpho-guessers": [None, None, None, None, None, 72.4, 62.52, 70.27, None, None]}
probing_task_names = ['Length', 'WordContent', 'Depth', 'TopConstituents', 'BigramShift', 'Tense', 'SubjNumber', 
              'ObjNumber', 'OddManOut', 'CoordinationInversion']
def make_probing_axis(ax, probing_task="Length"):
    yticks_major = np.arange(6)*20
    yticks_minor = np.arange(10)*10
    probing_task_idx = probing_task_names.index(probing_task)
    ax.set_yticks(yticks_major, minor=False)
    ax.set_yticks(yticks_minor, minor=True)
    ax.set_ylim(0, 100)
    xs_baseline = ax.get_xlim()
    ax.fill_between(xs_baseline, 0, probing_baselines["majority"][probing_task_idx], 
                    facecolor=probing_baseline_colours["majority"], zorder=0)
    ax.fill_between(xs_baseline, probing_baselines["human"][probing_task_idx], 100, 
                    facecolor=probing_baseline_colours["human"], zorder=0)
    for b in ["majority", "human"]:
        ax.axhline(probing_baselines[b][probing_task_idx], c=modify_cl(probing_baseline_colours[b], 0.9), zorder=0)
    ax.set_xlim(*xs_baseline)
    ax.grid(axis="y", color=grid_colour, which="both", zorder=1)
    ax.set_axisbelow(True)
    [s.set_linewidth(1.2) for s in [ax.spines[k] for k in ["top", "bottom"]]]
    [s.set_linewidth(1.2) for s in [ax.spines[k] for k in ["right", "left"]]]

import matplotlib.transforms as transforms
def annotate_range(vmin, vmax, label, ax, offset=-0.1, width=-0.1):
    # y-coordinates in axis coordinates,
    # x-coordinates in data coordinates
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    y = offset + 0.5 * width
    x = vmin + 0.5 * (vmax - vmin)
    ax.text(x, y, label,
            horizontalalignment='center', verticalalignment='top',
            clip_on=False, transform=trans)
