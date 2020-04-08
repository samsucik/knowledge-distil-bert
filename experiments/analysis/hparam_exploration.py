log_files = {
    "lr": {
    # Learning algorithm and LR search: lr=5e-4
    "$5\\times10^{-3}$": ["distil-bert-CoLA-Jan15-16:29:04", "distil-bert-CoLA-Jan15-16:29:34", "distil-bert-CoLA-Jan15-16:29:47", "distil-bert-CoLA-Jan17-10:54:16", "distil-bert-CoLA-Jan17-10:54:23", "distil-bert-CoLA-Jan17-10:54:33"],
    "$1.5\\times10^{-3}$": ["distil-bert-CoLA-Jan16-09:37:40", "distil-bert-CoLA-Jan16-09:37:45", "distil-bert-CoLA-Jan16-09:37:49", "distil-bert-CoLA-Jan17-14:31:49", "distil-bert-CoLA-Jan17-14:32:57", "distil-bert-CoLA-Jan17-15:27:46"],
    "$5\\times10^{-4}$": ["distil-bert-CoLA-Jan15-16:22:30", "distil-bert-CoLA-Jan15-16:23:14", "distil-bert-CoLA-Jan15-16:23:19", "distil-bert-CoLA-Jan17-10:52:11", "distil-bert-CoLA-Jan17-10:52:18", "distil-bert-CoLA-Jan17-10:52:27"],
    "$1.5\\times10^{-4}$": ["distil-bert-CoLA-Jan16-00:45:07", "distil-bert-CoLA-Jan16-00:45:12", "distil-bert-CoLA-Jan16-09:09:56", "distil-bert-CoLA-Jan17-11:05:05", "distil-bert-CoLA-Jan17-11:06:22", "distil-bert-CoLA-Jan17-11:06:30"],
    "$5\\times10^{-5}$": ["distil-bert-CoLA-Jan15-16:41:24", "distil-bert-CoLA-Jan15-16:42:04", "distil-bert-CoLA-Jan15-23:38:24", "distil-bert-CoLA-Jan17-10:56:16", "distil-bert-CoLA-Jan17-10:56:24", "distil-bert-CoLA-Jan17-14:43:55"],
    "$1.5\\times10^{-5}$": ["distil-bert-CoLA-Jan16-00:47:07", "distil-bert-CoLA-Jan16-00:47:12", "distil-bert-CoLA-Jan16-00:47:30", "distil-bert-CoLA-Jan17-11:09:40", "distil-bert-CoLA-Jan17-11:10:08", "distil-bert-CoLA-Jan17-11:10:18"],
    "$5\\times10^{-6}$": ["distil-bert-CoLA-Jan15-16:44:39", "distil-bert-CoLA-Jan15-16:44:47", "distil-bert-CoLA-Jan15-16:44:58", "distil-bert-CoLA-Jan17-10:58:03", "distil-bert-CoLA-Jan17-10:58:09", "distil-bert-CoLA-Jan17-10:58:17"],
    "Adadelta, $1.0$": ["distil-bert-CoLA-Jan16-00:37:42", "distil-bert-CoLA-Jan16-00:37:50", "distil-bert-CoLA-Jan16-00:37:58", "distil-bert-CoLA-Jan17-10:37:31", "distil-bert-CoLA-Jan17-10:50:42", "distil-bert-CoLA-Jan17-10:50:57"],
    },
    "B": {
    # Batch size search: B=32
    "$32$": ["distil-bert-CoLA-Jan17-23:27:02", "distil-bert-CoLA-Jan17-23:27:26", "distil-bert-CoLA-Jan17-23:27:48"],
    "$50$": ["distil-bert-CoLA-Jan15-16:22:30", "distil-bert-CoLA-Jan15-16:23:14", "distil-bert-CoLA-Jan15-16:23:19", "distil-bert-CoLA-Jan17-10:52:11", "distil-bert-CoLA-Jan17-10:52:18", "distil-bert-CoLA-Jan17-10:52:27"],
    "$128$": ["distil-bert-CoLA-Jan17-23:28:55", "distil-bert-CoLA-Jan17-23:29:37", "distil-bert-CoLA-Jan17-23:30:35"],
    "$256$": ["distil-bert-CoLA-Jan17-23:32:15", "distil-bert-CoLA-Jan17-23:32:39", "distil-bert-CoLA-Jan17-23:33:03"],
    "$512$": ["distil-bert-CoLA-Jan17-23:36:20", "distil-bert-CoLA-Jan17-23:36:28", "distil-bert-CoLA-Jan17-23:36:39"],
    },
    "wp": {
    # Warmup proportion and lr decay: wp=0, decay
    "$0$": ["distil-bert-CoLA-Jan17-23:27:02", "distil-bert-CoLA-Jan17-23:27:26", "distil-bert-CoLA-Jan17-23:27:48"],
    "$0$, decay": ["distil-bert-CoLA-Jan18-12:47:13", "distil-bert-CoLA-Jan18-12:19:11", "distil-bert-CoLA-Jan18-12:19:25"],
    "$5$": ["distil-bert-CoLA-Jan18-12:23:19", "distil-bert-CoLA-Jan18-12:38:36", "distil-bert-CoLA-Jan18-12:38:46"],
    "$5$, decay": ["distil-bert-CoLA-Jan18-12:21:09", "distil-bert-CoLA-Jan18-12:22:01", "distil-bert-CoLA-Jan18-12:22:39"],
    "$10$": ["distil-bert-CoLA-Jan18-17:40:29", "distil-bert-CoLA-Jan18-17:40:44", "distil-bert-CoLA-Jan18-17:41:16"],
    "$10$, decay": ["distil-bert-CoLA-Jan18-12:28:34", "distil-bert-CoLA-Jan18-12:28:54", "distil-bert-CoLA-Jan18-17:39:44"],
    "$15$": ["distil-bert-CoLA-Jan18-17:45:54", "distil-bert-CoLA-Jan18-18:06:13", "distil-bert-CoLA-Jan18-18:09:09"],
    "$15$, decay": ["distil-bert-CoLA-Jan18-17:42:14", "distil-bert-CoLA-Jan18-17:42:42", "distil-bert-CoLA-Jan18-17:45:26"],
    },
    "embed-cola": {
    # Embedding type: word multichannel
    "word, multichannel": ["distil-bert-CoLA-Jan18-12:47:13", "distil-bert-CoLA-Jan18-12:19:11", "distil-bert-CoLA-Jan18-12:19:25"],
    "word, non-static": ["distil-bert-CoLA-Jan25-09:40:14", "distil-bert-CoLA-Jan25-09:40:18", "distil-bert-CoLA-Jan25-09:40:23",],
    "wordpiece, multichannel": ["distil-bert-CoLA-Jan19-00:12:33", "distil-bert-CoLA-Jan19-00:26:47", "distil-bert-CoLA-Jan19-00:27:35"],
    "wordpiece, non-static": ["distil-bert-CoLA-Jan19-00:25:02", "distil-bert-CoLA-Jan19-00:25:12", "distil-bert-CoLA-Jan19-00:25:57"],
    },
    "embed-sara": {
    # Embedding type: wordpiece multichannel
    "word, multichannel": ["distil-bert-Sara-Jan31-10:07:57", "distil-bert-Sara-Jan31-19:00:40", "distil-bert-Sara-Jan31-19:48:53"],
    "wordpiece, multichannel": ["distil-bert-Sara-Jan31-19:24:12"],
    },
    "embed-sst-2": {
    # Embedding type: word multichannel
    "word, multichannel": ["distil-bert-SST-2-Feb01-23:41:34", "distil-bert-SST-2-Feb01-21:32:49", "distil-bert-SST-2-Feb01-19:42:24"],
    "wordpiece, multichannel": ["distil-bert-SST-2-Feb01-19:40:33"],
    },
    "size-cola": {
    # Student size (CoLA):
    "LSTM=300, FC=400, L=1": ["distil-bert-CoLA-Jan18-12:47:13", "distil-bert-CoLA-Jan18-12:19:11", "distil-bert-CoLA-Jan18-12:19:25"],
    "LSTM=600, FC=800, L=1": ["distil-bert-CoLA-Jan20-15:27:08", "distil-bert-CoLA-Jan20-15:27:12", "distil-bert-CoLA-Jan20-15:27:17"],
    "LSTM=900, FC=1200, L=1": ["distil-bert-CoLA-Jan20-15:27:56", "distil-bert-CoLA-Jan20-15:28:00", "distil-bert-CoLA-Jan20-15:28:04"],
    "LSTM=1200, FC=1600, L=1": ["distil-bert-CoLA-Jan20-15:28:47", "distil-bert-CoLA-Jan20-15:28:50", "distil-bert-CoLA-Jan20-15:28:54"],
    "LSTM=1500, FC=2000, L=1": ["distil-bert-CoLA-Jan20-15:29:35", "distil-bert-CoLA-Jan20-15:29:37", "distil-bert-CoLA-Jan20-15:29:41"],
    
    "LSTM=300, FC=400, L=2": ["distil-bert-CoLA-Jan21-00:54:50", "distil-bert-CoLA-Jan21-00:54:41", "distil-bert-CoLA-Jan21-00:54:45"],
    "LSTM=600, FC=800, L=2": ["distil-bert-CoLA-Jan21-00:58:53", "distil-bert-CoLA-Jan21-01:00:43", "distil-bert-CoLA-Jan21-01:00:56"],
    "LSTM=900, FC=1200, L=2": ["distil-bert-CoLA-Jan21-09:08:51", "distil-bert-CoLA-Jan21-09:09:04", "distil-bert-CoLA-Jan21-09:09:08"],
    "LSTM=1200, FC=1600, L=2": ["distil-bert-CoLA-Jan21-09:10:20", "distil-bert-CoLA-Jan21-09:10:25", "distil-bert-CoLA-Jan21-09:10:45"],
    "LSTM=1500, FC=2000, L=2": ["distil-bert-CoLA-Jan21-09:11:59", "distil-bert-CoLA-Jan21-09:12:05", "distil-bert-CoLA-Jan21-09:14:17"],
    
    "LSTM=300, FC=400, L=3": ["distil-bert-CoLA-Jan21-09:17:10", "distil-bert-CoLA-Jan21-09:18:42", "distil-bert-CoLA-Jan21-10:59:59"],
    "LSTM=600, FC=800, L=3": ["distil-bert-CoLA-Jan21-11:01:09", "distil-bert-CoLA-Jan21-11:01:29", "distil-bert-CoLA-Jan21-11:02:02"],
    "LSTM=900, FC=1200, L=3": ["distil-bert-CoLA-Jan21-11:04:15", "distil-bert-CoLA-Jan21-11:04:40", "distil-bert-CoLA-Jan21-15:47:58"],
    "LSTM=1200, FC=1600, L=3": ["distil-bert-CoLA-Jan22-20:46:57", "distil-bert-CoLA-Jan22-20:47:02", "distil-bert-CoLA-Jan22-20:47:09",],
    "LSTM=1500, FC=2000, L=3": ["distil-bert-CoLA-Jan26-15:52:16", "distil-bert-CoLA-Jan26-15:52:46", "distil-bert-CoLA-Jan26-15:53:13"],
        
    "LSTM=300, FC=400, L=4": ["distil-bert-CoLA-Jan22-09:42:07", "distil-bert-CoLA-Jan22-09:42:15", "distil-bert-CoLA-Jan22-09:42:34"],
    "LSTM=600, FC=800, L=4": ["distil-bert-CoLA-Jan22-09:43:53", "distil-bert-CoLA-Jan22-09:43:55", "distil-bert-CoLA-Jan22-09:43:59",],
    "LSTM=900, FC=1200, L=4": ["distil-bert-CoLA-Jan22-20:49:39", "distil-bert-CoLA-Jan22-20:49:47", "distil-bert-CoLA-Jan22-20:49:50",],
    "LSTM=1200, FC=1600, L=4": ["distil-bert-CoLA-Jan24-10:10:39", "distil-bert-CoLA-Jan24-10:10:34", "distil-bert-CoLA-Jan24-10:10:36"],
    "LSTM=1500, FC=2000, L=4": ["distil-bert-CoLA-Jan26-15:53:57", "distil-bert-CoLA-Jan26-15:54:02", "distil-bert-CoLA-Jan26-15:53:52"],
        
    "LSTM=300, FC=400, L=5": ["distil-bert-CoLA-Jan22-09:51:35", "distil-bert-CoLA-Jan22-09:51:40", "distil-bert-CoLA-Jan22-09:51:54"],
    "LSTM=600, FC=800, L=5": ["distil-bert-CoLA-Jan22-20:51:12", "distil-bert-CoLA-Jan22-20:51:17", "distil-bert-CoLA-Jan22-20:51:25",],
    "LSTM=900, FC=1200, L=5": ["distil-bert-CoLA-Jan22-23:38:50", "distil-bert-CoLA-Jan22-23:40:55", "distil-bert-CoLA-Jan22-23:39:06",],
    "LSTM=1200, FC=1600, L=5": ["distil-bert-CoLA-Jan24-10:11:16", "distil-bert-CoLA-Jan24-10:11:12", "distil-bert-CoLA-Jan24-10:11:14"],
    "LSTM=1500, FC=2000, L=5": ["distil-bert-CoLA-Jan28-18:34:08", "distil-bert-CoLA-Jan28-18:54:54", "distil-bert-CoLA-Jan28-18:34:00"],
    },
    "size-sara": {
    # Student size (Sara):
    "LSTM=300, FC=400, L=1": ["distil-bert-Sara-Jan31-19:24:12"],
    "LSTM=150, FC=200, L=1": ["distil-bert-Sara-Feb01-10:23:06"],
    "LSTM=75, FC=100, L=1": ["distil-bert-Sara-Feb01-10:24:16"],
    "LSTM=37, FC=50, L=1": ["distil-bert-Sara-Feb01-10:25:21"],
    },
    "size-sst-2": {
    # Student size (SST-2):
    "LSTM=300, FC=400, L=1": ["distil-bert-SST-2-Feb01-23:41:34", "distil-bert-SST-2-Feb01-21:32:49", "distil-bert-SST-2-Feb01-19:42:24"],
    "LSTM=150, FC=200, L=1": ["distil-bert-SST-2-Feb02-23:06:55"],
    "LSTM=75, FC=100, L=1": ["distil-bert-SST-2-Feb02-23:08:41"],
    "LSTM=37, FC=50, L=1": ["distil-bert-SST-2-Feb02-23:09:34"],
    "LSTM=19, FC=25, L=1": ["distil-bert-SST-2-Feb03-09:23:05"],
    "LSTM=9, FC=13, L=1": ["distil-bert-SST-2-Feb04-08:52:36"],
    "LSTM=5, FC=6, L=1": ["distil-bert-SST-2-Feb04-08:52:09"],
    },
    "lr-bert-scratch": {
    # Learning rate search: lr=5e-4
    "$5\\times10^{-3}$": ["distil-bert-CoLA-Jan17-16:10:06"],
    "$1.5\\times10^{-3}$": ["distil-bert-CoLA-Jan17-15:57:10"],
    "$5\\times10^{-4}$": ["distil-bert-CoLA-Jan17-16:10:36"],
    "$1.5\\times10^{-4}$": ["distil-bert-CoLA-Jan17-16:12:47"],
    "$5\\times10^{-5}$": ["distil-bert-CoLA-Jan17-16:13:14"],
    "$1.5\\times10^{-5}$": ["distil-bert-CoLA-Jan17-16:19:46"],
    "$5\\times10^{-6}$": ["distil-bert-CoLA-Jan17-16:14:33"],
    },
    "wp-bert-scratch": {
    # Warmup proportion and lr decay: wp=20
    "$0$": ["distil-bert-CoLA-Jan18-11:57:42"],
    "$0$, decay": ["distil-bert-CoLA-Jan18-11:57:08"],
    "$5$": ["distil-bert-CoLA-Jan18-11:59:07"],
    "$5$, decay": ["distil-bert-CoLA-Jan18-11:58:22"],
    "$10$": ["distil-bert-CoLA-Jan18-12:08:07"],
    "$10$, decay": ["distil-bert-CoLA-Jan17-16:10:36"],
    "$15$": ["distil-bert-CoLA-Jan18-12:00:26"],
    "$15$, decay": ["distil-bert-CoLA-Jan18-11:59:56"],
    "$20$": ["distil-bert-CoLA-Jan18-12:12:15"],
    "$20$, decay": ["distil-bert-CoLA-Jan18-12:02:52"],
    },
    "B-bert-scratch": {
    # Batch size: B=256
    "$32$": ["distil-bert-CoLA-Jan19-10:04:57"],
    "$64$": ["distil-bert-CoLA-Jan19-10:05:42"],
    "$128$": ["distil-bert-CoLA-Jan19-10:06:41"],
    "$256$": ["distil-bert-CoLA-Jan18-12:12:15"],
    "$362$": ["distil-bert-CoLA-Jan19-11:09:55"],
    "$512$": ["distil-bert-CoLA-Jan23-09:55:20",],
    },
    "lr-bert": {
    # Learning rate search: lr=5e-4
    "$5\\times10^{-3}$": ["distil-bert-CoLA-Jan20-15:30:50"],
    "$1.5\\times10^{-3}$": ["distil-bert-CoLA-Jan20-15:33:44"],
    "$5\\times10^{-4}$": ["distil-bert-CoLA-Jan20-15:31:04"],
    "$1.5\\times10^{-4}$": ["distil-bert-CoLA-Jan20-15:33:55"],
    "$5\\times10^{-5}$": ["distil-bert-CoLA-Jan20-15:31:49"],
    "$1.5\\times10^{-5}$": ["distil-bert-CoLA-Jan20-15:34:05"],
    "$5\\times10^{-6}$": ["distil-bert-CoLA-Jan20-15:32:03"],
    },
    "wp-bert": {
    # Warmup proportion and lr decay: wp=15, decay
    "$0$": ["distil-bert-CoLA-Jan21-21:12:24",],
    "$0$, decay": ["distil-bert-CoLA-Jan21-20:50:51",],
    "$5$": ["distil-bert-CoLA-Jan21-23:14:47",],
    "$5$, decay": ["distil-bert-CoLA-Jan21-21:40:15",],
    "$10$": ["distil-bert-CoLA-Jan22-09:29:53",],
    "$10$, decay": ["distil-bert-CoLA-Jan20-15:31:04"],
    "$15$": ["distil-bert-CoLA-Jan22-09:31:03",],
    "$15$, decay": ["distil-bert-CoLA-Jan22-09:30:36",],
    "$20$": ["distil-bert-CoLA-Jan22-09:32:06",],
    "$20$, decay": ["distil-bert-CoLA-Jan22-09:31:31",],
    },
    "B-bert": {
    # Batch size: B=128
    "$32$": ["distil-bert-CoLA-Jan23-09:47:32"],
    "$64$": ["distil-bert-CoLA-Jan23-09:46:50",],
    "$128$": ["distil-bert-CoLA-Jan23-09:48:13",],
    "$256$": ["distil-bert-CoLA-Jan22-09:30:36",],
    "$512$": ["distil-bert-CoLA-Jan23-09:49:54",],
    },
    "embed-cola-bert": {
    # Embedding type: word multichannel
    "word, multichannel": ["distil-bert-CoLA-Jan24-10:07:52"],
    "word, non-static": ["distil-bert-CoLA-Jan24-10:07:32"],
    "wordpiece, multichannel": ["distil-bert-CoLA-Jan25-09:42:35"],
    "wordpiece, non-static": ["distil-bert-CoLA-Jan23-09:48:13",],
    },
    "embed-sara-bert": {
    # Embedding type: wordpiece non-static
    "word, multichannel": ["distil-bert-Sara-Jan31-09:34:12"],
    "wordpiece, non-static": ["distil-bert-Sara-Feb01-09:38:47"],
    },
    "embed-sst-2-bert": {
    # Embedding type: word multichannel
    "word, multichannel": ["distil-bert-SST-2-Feb01-19:47:00"],
    "wordpiece, non-static": ["distil-bert-SST-2-Feb01-19:44:54"],
    },
    "size-cola-bert": {
    # Size:
    "W=1, D=1": ["distil-bert-CoLA-Jan24-10:07:52"],
    "W=2, D=1": ["distil-bert-CoLA-Jan29-11:08:03"], # exploding distil-bert-CoLA-Jan25-10:02:01
    "W=3, D=1": ["distil-bert-CoLA-Jan29-11:17:12"], # exploding distil-bert-CoLA-Jan25-10:12:42
    "W=4, D=1": ["distil-bert-CoLA-Jan29-11:25:47"],
    # "W=5, D=1": ["distil-bert-CoLA-Feb02-10:42:58"], # exploding distil-bert-CoLA-Feb01-21:22:43
    "W=1, D=2": ["distil-bert-CoLA-Jan25-10:50:54"],
    "W=2, D=2": ["distil-bert-CoLA-Jan29-11:09:47"], # exploding distil-bert-CoLA-Jan25-10:18:53
    "W=3, D=2": ["distil-bert-CoLA-Jan29-11:18:20"],
    "W=4, D=2": ["distil-bert-CoLA-Jan29-11:38:07"],
    "W=5, D=2": [], # exploding distil-bert-CoLA-Feb01-21:51:43
    "W=1, D=3": ["distil-bert-CoLA-Jan29-13:58:24"],
    "W=2, D=3": ["distil-bert-CoLA-Jan29-14:42:48"],
    "W=3, D=3": ["distil-bert-CoLA-Jan29-11:23:24"],
    "W=4, D=3": ["distil-bert-CoLA-Jan29-11:38:51"], 
    },
    "size-sara-bert": {
    "W=1, D=1": ["distil-bert-Sara-Feb01-09:38:47"],
    "W=1, D=1/2": ["distil-bert-Sara-Feb02-11:31:12"],
    "W=1, D=1/3": ["distil-bert-Sara-Feb02-11:31:48"],
    "W=1, D=1/4": ["distil-bert-Sara-Feb03-09:18:48"],
    
    "W=1/2, D=1": ["distil-bert-Sara-Feb02-11:32:57"],
    "W=1/2, D=1/2": ["distil-bert-Sara-Feb02-11:33:27"],
    "W=1/2, D=1/3": ["distil-bert-Sara-Feb02-11:34:20"],
    "W=1/2, D=1/4": ["distil-bert-Sara-Feb03-09:17:40"],
    
    "W=1/3, D=1": ["distil-bert-Sara-Feb02-11:36:05"],
    "W=1/3, D=1/2": ["distil-bert-Sara-Feb02-11:36:39"],
    "W=1/3, D=1/3": ["distil-bert-Sara-Feb02-11:37:33"],
    "W=1/3, D=1/4": ["distil-bert-Sara-Feb03-09:16:28"],
    },
    "size-sst-2-bert": {
    "W=1, D=1": ["distil-bert-SST-2-Feb01-19:47:00"],
    "W=1, D=1/2": ["distil-bert-SST-2-Feb02-23:14:33"],
    "W=1, D=1/3": ["distil-bert-SST-2-Feb02-23:15:03"],
    "W=1, D=1/4": ["distil-bert-SST-2-Feb02-23:15:27"],
    
    "W=1/2, D=1": ["distil-bert-SST-2-Feb02-23:16:54"],
    "W=1/2, D=1/2": ["distil-bert-SST-2-Feb02-23:21:13"],
    "W=1/2, D=1/3": ["distil-bert-SST-2-Feb02-23:21:48"],
    "W=1/2, D=1/4": ["distil-bert-SST-2-Feb02-23:22:20"],
    
    "W=1/3, D=1": ["distil-bert-SST-2-Feb02-23:23:19"],
    "W=1/3, D=1/2": ["distil-bert-SST-2-Feb03-09:12:00"],
    "W=1/3, D=1/3": ["distil-bert-SST-2-Feb03-09:12:45"],
    "W=1/3, D=1/4": ["distil-bert-SST-2-Feb03-09:13:07"],
    
    "W=1/4, D=1": ["distil-bert-SST-2-Feb03-23:43:57"],
    "W=1/4, D=1/2": ["distil-bert-SST-2-Feb03-23:40:47"],
    "W=1/4, D=1/3": ["distil-bert-SST-2-Feb03-23:44:39"],
    "W=1/4, D=1/4": ["distil-bert-SST-2-Feb03-23:45:04"],
        
    "W=1/8, D=1": ["distil-bert-SST-2-Feb04-08:54:55"],
    "W=1/8, D=1/2": ["distil-bert-SST-2-Feb03-23:48:53"],
    "W=1/8, D=1/3": ["distil-bert-SST-2-Feb03-23:48:23"],
    "W=1/8, D=1/4": ["distil-bert-SST-2-Feb03-23:47:57"],
        
    "W=1/16, D=1": ["distil-bert-SST-2-Feb04-12:29:47"],
    "W=1/16, D=1/2": ["distil-bert-SST-2-Feb04-12:30:49"],
    "W=1/16, D=1/3": ["distil-bert-SST-2-Feb04-12:31:23"],
    "W=1/16, D=1/4": ["distil-bert-SST-2-Feb04-12:31:51"],
    },
    "size-cola-bert-params": {
        "W=1, D=1": [2.4, 5e-4],
        "W=2, D=1": [9.6, 1e-4],
        "W=3, D=1": [21.7, 8e-5],
        "W=4, D=1": [38.5, 7e-5],
        "W=1, D=2": [4.8, 5e-4],
        "W=2, D=2": [19.1, 8e-5],
        "W=3, D=2": [43, 5e-5],
        "W=4, D=2": [76.4, 4e-5],
        "W=1, D=3": [7.2, 1e-4],
        "W=2, D=3": [28.6, 7e-5],
        "W=3, D=3": [64.3, 5e-5],
        "W=4, D=3": [114.2, 4e-5],
    }
}
