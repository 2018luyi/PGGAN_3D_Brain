""" config.py
"""
import argparse
import time

parser = argparse.ArgumentParser('PGGAN')

## general settings.
parser.add_argument('--train_data_root', type=str, default='/scratch/xzhou/mri/')
parser.add_argument('--random_seed', type=int, default=int(time.time()))
parser.add_argument('--n_gpu', type=int, default=1)             # for Multi-GPU training.
parser.add_argument('--model_name', type=str, default='P_G') # for different experiments, model name will be different for recording purpose
# P_G means use pixel norm (G) and group norm (D)
# B_G means use batch norm (G) and group norm (D)

## training parameters.
parser.add_argument('--lr', type=float, default=0.0002)         # learning rate.
parser.add_argument('--nc', type=int, default=1)                # color channel.
parser.add_argument('--nz', type=int, default=100)              # input dimension of noise.
parser.add_argument('--ngf', type=int, default=128)             # feature dimension of final layer of generator.
parser.add_argument('--ndf', type=int, default=128)             # feature dimension of first layer of discriminator.
parser.add_argument('--ncritic', type=int, default=5)           # train n time critic then train one time generator
parser.add_argument('--Lambda', type=int, default=10)           # weight in front of gradient penalty
parser.add_argument('--start_resl', type=int, default=2)        # 2 ** resl == size, start_resl = 2 means start size = 4
parser.add_argument('--max_resl', type=int, default=7)          # train til 128 resoltuion 2 ** 7
parser.add_argument('--eps_drift', type=float, default=0.001)   # coeff for the drift loss D(x) ** 2.

## network structure. G and D
parser.add_argument('--equal', type=bool, default=False)           # use of equalized-learning rate.
# network structure G
parser.add_argument('--G_batchnorm', type=bool, default=False)      # batch normalization
parser.add_argument('--G_pixelnorm', type=bool, default=True)     # pixel wise normalization
parser.add_argument('--G_leaky', type=bool, default=True)          # use of leaky relu instead of relu.
parser.add_argument('--G_tanh', type=bool, default=False)           # use of tanh at the end of the generator.
parser.add_argument('--G_upsam_mode', type=str, default='nearest') # upsample mode
# network structure D
parser.add_argument('--D_groupnorm', type=bool, default=True)    # batch normalization
parser.add_argument('--D_pixelnorm', type=bool, default=False)   # pixel wise normalization
parser.add_argument('--D_genedrop', type=bool, default=False)    # generalized drop out
parser.add_argument('--D_leaky', type=bool, default=True)        # use of leaky relu instead of relu.
parser.add_argument('--D_sigmoid', type=bool, default=False)     # use of sigmoid at the end of the discriminator.

## optimizer setting.
parser.add_argument('--optimizer', type=str, default='adam')        # optimizer type.
parser.add_argument('--beta1', type=float, default=0.0)             # beta1 for adam.
parser.add_argument('--beta2', type=float, default=0.99)            # beta2 for adam.

## model weights
parser.add_argument('--G_pth', type=str, default='./checkpoint_dir/P_G/G_6_10500.pth')       # save images every specified iteration.
parser.add_argument('--D_pth', type=str, default='./checkpoint_dir/P_G/D_6_10500.pth')      # display progress every specified iteration.

## parse and save config.
config, _ = parser.parse_known_args()
