import tensorflow as tf
import argparse, os, csv, re, glob
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--in_dir", default="CoLA.bak/distillation/logs", type=str, required=False,
                    help="Directory where the experiment-specific log dirs are found.")
parser.add_argument("--exp_dir", type=str, required=True,
                    help="Experiment-specific directory.")
args = parser.parse_args()

def get_metric_name(task_name):
    if task_name == "cola": return "mcc"
    elif task_name == "sst-2": return "acc"
    elif task_name == "sara": return "f1-micro"
    else: raise ValueError(task_name)
def get_task_name(s):
    s = s.split("/")[-1]
    if "SST-2" in s: return "sst-2"
    if "Sara" in s: return "sara"
    if "CoLA" in s: return "cola"
    raise ValueError(s)

task_name = get_task_name(args.exp_dir)
metric_name = get_metric_name(task_name)
metric_name_long = "eval_" + metric_name
print("TASK_NAME: <{}>".format(task_name))

log_file = list(glob.iglob(args.in_dir + "/" + args.exp_dir + '/**/events.out.*', recursive=True))[0]
stats = []
times = []
try:
    for e in tf.compat.v1.train.summary_iterator(log_file):
        times.append(e.wall_time)
        for v in e.summary.value:
            if v.tag == metric_name_long:
                stats.append([e.step, v.simple_value])
            if v.tag == "config/text_summary":
                config = str(v.tensor.string_val[0])[12:-2].split(", ")
                for l in config:
                    print(l)
    start_time = np.min(times)
    end_time = np.max(times)
    runtime = (end_time - start_time)/3600
    print("Runtime: {:.2f}h.".format(runtime))
    stat_vals = np.array(stats)[:,1]
    best_metric_value = np.amax(stat_vals)
    best_metric_step = stats[np.argmax(stat_vals)][0]
    print("Best metric value: {} in step {}.".format(best_metric_value, best_metric_step))
except Exception as e:
    print("Failed: {}".format(e))
