import torch
from denoising_diffusion_pytorch.denoising_diffusion_pytorch_only_over import num_to_groups, Trainer, Unet, GaussianDiffusion
from torchvision import transforms as T, utils
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import io
import hydra
from omegaconf import DictConfig
import os
import sys

#################this manuscript is used to test the diffusion model for filtering for a casual model

def myprediff(cfg,inputv,ws1,ws2,tartime,pmin,pmax):
 
   
    
    model = Unet(
        dim = 64,
        channels=1,
        dim_mults = (1, 2, 8),
        flash_attn = False
    )


    
    diffusion = GaussianDiffusion(
        model,
        image_size = 100,
        timesteps = 1000,           # number of steps
        sampling_timesteps = 100,   # number of sampling timesteps (using ddim for faster inference [see citation for ddim paper])
        auto_normalize = False,
        is_working_with_fwi = 7,
        **cfg
        # True for conditional generation
    )
    
    
    # result_folder should be the address where you store model-300.pt
    # folder should be the address where you store normalized_fwi.pt (normalized to [-1, 1]) via linear transform
    trainer = Trainer(
        diffusion_model=diffusion, 
        #results_folder = cfg.result_folder_path, 
        #folder = cfg.training_data_path, 
        results_folder = '/home/lcgeo/geo/dlmfwi_diffusion/diffusion_model', 
        folder ='/home/lcgeo/geo/dlmfwi_diffusion/diffusion_model/normalized_fwi.pt' , 
        train_batch_size = 16
    )
    
    
    trainer.load(300) # load model-300.pt

    
 

    
    kimg = inputv.clone()
   
    trainer.ema.ema_model.input_vel = kimg.clone()
    
    
    trainer.ema.ema_model.ws1 = ws1
    trainer.ema.ema_model.ws2 = ws2
    trainer.ema.ema_model.tartime = tartime
    trainer.ema.ema_model.pmin = pmin
    trainer.ema.ema_model.pmax = pmax
    
    #begin to conduct SGDS
    #all_images_list = list(map(lambda n: trainer.ema.ema_model.sample(batch_size=n), batches))
    #sys.exit()
    
    with torch.no_grad():
            vel_reg= trainer.ema.ema_model.sample(batch_size=1).clone()
            
   
  
   
    return vel_reg



   

   
    
       
      
       
       
 

