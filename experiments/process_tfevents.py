import tensorflow as tf
import argparse, os, csv, re, glob

parser = argparse.ArgumentParser()
parser.add_argument("--in_dir", default="CoLA.bak/distillation/logs", type=str, required=False,
                    help="Directory where the experiment-specific log dirs are found.")
parser.add_argument("--out_dir", default="analysis/logs", type=str, required=False,
                    help="Directory where the CSVs should be saved.")
args = parser.parse_args()

existing_csvs = [f for f in os.listdir(args.out_dir) if os.path.isfile(os.path.join(args.out_dir, f)) and f.endswith(".csv")]
existing_log_dirs = [d for d in os.listdir(args.in_dir) if os.path.isdir(os.path.join(args.in_dir, d))]

for log_dir in existing_log_dirs:
    if "{}.csv".format(log_dir) in existing_csvs:
        print("Skipping", log_dir)
        continue
    print("Processing", log_dir)
    log_file = list(glob.iglob(args.in_dir + "/" + log_dir + '/**/events.out.*', recursive=True))[0]
    stats = []
    rows = ["step", "mcc"]
    for e in tf.compat.v1.train.summary_iterator(log_file):
        for v in e.summary.value:
            if v.tag == "eval_mcc":
                stats.append([e.step, v.simple_value])
            if v.tag == "config/text_summary":
                config = str(v.tensor.string_val[0])[12:-2].split(", ")
                [print(l) for l in config]

    out_file = os.path.join(args.out_dir, log_dir + ".csv")
    with open(out_file, "w", newline="") as f:
        f.write("{}\n".format(",".join(rows)))
        writer = csv.writer(f)
        writer.writerows(stats)
