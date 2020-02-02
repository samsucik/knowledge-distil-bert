import tensorflow as tf
import argparse, os, csv, re, glob
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--in_dir", default="CoLA.bak/distillation/logs", type=str, required=False,
                    help="Directory where the experiment-specific log dirs are found.")
parser.add_argument("--out_dir", default="analysis/logs", type=str, required=False,
                    help="Directory where the CSVs should be saved.")
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

existing_csvs = [f for f in os.listdir(args.out_dir) if os.path.isfile(os.path.join(args.out_dir, f)) and f.endswith(".csv")]
existing_log_dirs = [d for d in os.listdir(args.in_dir) if os.path.isdir(os.path.join(args.in_dir, d))]

for log_dir in existing_log_dirs:
    if "{}.csv".format(log_dir) in existing_csvs:
        print("Skipping", log_dir)
        continue
    print("Processing", log_dir)
    task_name = get_task_name(log_dir)
    metric_name = get_metric_name(task_name)
    metric_name_long = "eval_" + metric_name
    print("TASK_NAME: <{}>".format(task_name))

    log_file = list(glob.iglob(args.in_dir + "/" + log_dir + '/**/events.out.*', recursive=True))[0]
    stats = []
    rows = ["step", metric_name]
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

        out_file = os.path.join(args.out_dir, log_dir + ".csv")
        with open(out_file, "w", newline="") as f:
            f.write("{}\n".format(runtime))
            f.write("{}\n".format(",".join(rows)))
            writer = csv.writer(f)
            writer.writerows(stats)
    except Exception as e:
        print("Failed: {}".format(e.message))
