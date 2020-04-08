import tensorflow as tf
import argparse, os, csv, re, glob
import numpy as np
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("--in_dir", default="CoLA.bak/distillation/logs", type=str, required=False,
                    help="Directory where the experiment-specific log dirs are found.")
parser.add_argument("--out_dir", default="analysis/logs", type=str, required=False,
                    help="Directory where the CSVs should be saved.")
parser.add_argument("--task", default=None, type=str, required=False,
                    help="The task, one of [cola, sst-2, sara].")
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
existing_log_dirs = [os.path.abspath(d) for d in os.listdir(args.in_dir) if os.path.isdir(os.path.join(args.in_dir, d))]
if len(existing_log_dirs) == 0:
    print("Didn't find any log dirs inside {}, considering it to be a log dir itself.".format(args.in_dir))
    existing_log_dirs = [os.path.abspath(args.in_dir)]

for log_dir in existing_log_dirs:
    if "{}.csv".format(log_dir) in existing_csvs:
        print("Skipping", log_dir)
        continue
    print("Processing", log_dir)
    task_name = args.task if args.task is not None else get_task_name(log_dir)
    metric_name = get_metric_name(task_name)
    metric_name_long = "eval_" + metric_name
    columns_to_extract = [metric_name_long]
    columns_to_extract = [metric_name_long, "grad_norm", "learning_rate/lr"]
    print("TASK_NAME: <{}>".format(task_name))

    log_files = list(glob.iglob(log_dir + '/**/events.out.*', recursive=True))
    if len(log_files) == 0:
        print("Skiping {}: no tfevents file found.".format(log_dir))
        continue
    log_file = log_files[0]
    stats = {k: [] for k in columns_to_extract}
    rows = [metric_name]
    rows = [metric_name, "grad_norm", "lr"]
    times = []
    try:
        for e in tf.compat.v1.train.summary_iterator(log_file):
            times.append(e.wall_time)
            for v in e.summary.value:
                if v.tag in columns_to_extract:
                    stats[v.tag].append(v.simple_value)
                if v.tag == "config/text_summary":
                    config = str(v.tensor.string_val[0])[12:-2].split(", ")
                    for l in config:
                        print(l)
        start_time = np.min(times)
        end_time = np.max(times)
        runtime = (end_time - start_time)/3600
        print("Runtime: {:.2f}h.".format(runtime))

        stats_to_write = list(itertools.zip_longest(*[stats[c] for c in columns_to_extract]))
        print("Stats to write", stats_to_write[:10])
        out_file = os.path.join(args.out_dir, log_dir + ".csv")
        with open(out_file, "w", newline="") as f:
            f.write("{}\n".format(runtime))
            f.write("{}\n".format(",".join(rows)))
            writer = csv.writer(f)
            writer.writerows(stats_to_write)
            # print(out_file)
    except Exception as e:
        print("Failed: {}, {}".format(e, type(e)))
