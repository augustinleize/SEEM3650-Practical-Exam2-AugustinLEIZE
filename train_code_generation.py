
out_dir = 'out-code-python'
eval_interval = 250
eval_iters = 200
log_interval = 10

always_save_checkpoint = False

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256


n_layer = 7 
n_head = 5
n_embd = 380
dropout = 0.2

learning_rate = 1e-3
max_iters = 500 
lr_decay_iters = 500
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100