import tensorflow as tf
import argparse, os, csv, re

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default="CoLA.bak/distillation/tensorboard", type=str, required=False,
                    help="Directory where the experiment-specific TF events dir is found.")
parser.add_argument("--file", default="tb_Jan03_15-36-42_letha04.inf.ed.ac.uk", type=str, required=False,
                    help="File name (it's really a directory which contains a single tfevent file).")
args = parser.parse_args()

files = [f for f in os.listdir(os.path.join(args.dir, args.file)) if os.path.isfile(os.path.join(args.dir, args.file, f))]
if len(files) == 1:
    tfevent_file = os.path.join(args.dir, args.file, files[0])
else:
    raise ValueError("Found {} files but expected exactly one to exist within {}/{}.".format(len(files), args.dir, args.file))

stats = []
rows = ["step", "mcc"]
for e in tf.compat.v1.train.summary_iterator(tfevent_file):
    for v in e.summary.value:
        if v.tag == "eval_mcc":
            stats.append([e.step, v.simple_value])
        if v.tag == "config/text_summary":
            config = str(v.tensor.string_val[0])[12:-2].split(", ")
            [print(l) for l in config]

out_file = os.path.join("analysis", args.file + ".csv")
with open(out_file, "w", newline="") as f:
    f.write("{}\n".format(",".join(rows)))
    writer = csv.writer(f)
    writer.writerows(stats)
