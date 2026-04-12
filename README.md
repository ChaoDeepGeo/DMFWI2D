# <div align="center">

# Learned diffusion model regularization for full waveform inversion
**Chao Li**<sup>1</sup> &nbsp;&nbsp;
**Yangkang Chen**<sup>1</sup>

<sup>1</sup> Bureau of Economic Geology, John A. and Katherine G. Jackson School of Geosciences, The University of Texas at Austin  

![Stars](https://img.shields.io/github/stars/ChaoDeepGeo/DLM-FWI?style=social)
![Forks](https://img.shields.io/github/forks/ChaoDeepGeo/DLM-FWI?style=social)
![Repo Size](https://img.shields.io/github/repo-size/ChaoDeepGeo/DLM-FWI)
![Last Commit](https://img.shields.io/github/last-commit/ChaoDeepGeo/DLM-FWI)
![Top Language](https://img.shields.io/github/languages/top/ChaoDeepGeo/DLM-FWI)

</div>

---

## Overview

Full-waveform inversion (FWI) estimates subsurface properties by iteratively minimizing the mismatch between simulated and recorded seismic data, but it can break down when an inaccurate starting model leads to cycle skipping. We introduce deep-learning-backed adaptive waveform inversion (DL-AWI), which uses a deep twin network to precondition observed and synthetic waveforms and embed them in a shared latent space, where an improved prior pair can be identified for stable data comparison. DL-AWI then evaluates the two signals using a ratio-based objective referenced to a zero-lag spike, improving robustness during early iterations. By learning a more favorable representation for matching, DL-AWI effectively broadens the update basin, accelerates convergence, and reduces the risk of being trapped in local minima. Synthetic experiments and a field example demonstrate that DL-AWI produces reliable inversions and remains stable even with poor initial models.


---

## Abstract

Full waveform inversion (FWI) iteratively improves the accuracy of the model by minimizing the discrepancies between the predicted and the observed data. However, FWI commonly suffers from cycle skipping when the initial model is poor, leading to an erroneous result. To mitigate this problem, we propose deep-learning-backed adaptive waveform inversion (DL-AWI), which introduces a deep twin neural network to precondition the waveforms and compare the ratio of two signals with a zero-lag spike, thereby enhancing the stability of the inversion process. DL-AWI can project the synthetic and observed signals into an extended latent space via several convolutional neural networks (CNNs) with shared weights, which can accelerate the data matching. Compared with classic FWI methods, the proposed DL-AWI provides a wider space for model updates, significantly decreasing the risk of being trapped in local minima. We use synthetic and field examples to validate its efficiency in subsurface model inversion, and the results show that DL-AWI is robust even when a poor initial model is provided.

---

## Framework

<p align="center">
  <img src="figures/DLAWI.png" width="850"/>
</p>

<p align="center">
  <b>Figure 1.</b> Overview of the proposed DL-AWI framework.
</p>

The workflow of DL-AWI consists of the following main steps:

1. Generate synthetic seismic data from the current velocity model.
2. Use a deep-learning-based matching module to generate extended synthetic data into a latent space for improved data fitting.
3. Compute the misfit between extended synthetic data and observed data.
4. Backpropagate the misfit to update the velocity model iteratively.

---

## Documents demonstration

- The Marmousi folder contains necessary code to reproduce the Marmousi result (main_dlawi.ipynb is ready to visialize the prilimary results).
- The Overthrus folder contains necessary code to reproduce the Overthrust result (main_dlawi.ipynb is ready to visialize the prilimary results).
- For classic AWI, please refer to Warner and Guasch, 2016, Adaptive waveform inversion: Theory, Geophysics, 81 (6): R429–R445.
- For SiameseFWI, please refer to Saad et al., 2024, SiameseFWI: A deep learning network for enhanced full waveform inversion. Journal of Geophysical Research: Machine Learning and Computation, 1, e2024JH000227.


---




## Result

<p align="center">
  <img src="figures/marminv.png" width="850"/>
</p>

<p align="center">
  <b>Figure 2.</b> Inverted Marmousi result of (a) Classic FWI, (b) Classic AWI, (c) SiameseFWI, and (d) DL-AWI. 
</p>

<p align="center">
  <img src="figures/overinv.png" width="850"/>
</p>

<p align="center">
  <b>Figure 3.</b> Inverted Overthrust result of (a) Classic FWI, (b) Classic AWI, (c) SiameseFWI, and (d) DL-AWI. 
</p>

---

## Features

- Robust against cycle skipping
- Improves inversion with poor initial models
- Compatible with conventional FWI workflows
- Free of complex adjoint source and gradient derivation and calculation.
- Easy to extend to acoustic, viscoacoustic, and elastic settings

---

## Installation

To set up the environment, run:

```bash
conda env create -f environment.yml
conda activate your_env_name
```

---

## Reference 

> Li et al., Learned diffusion model regularization for full waveform inversion.

### BibTex

```bibtex
@Article{lidmfwi,
AUTHOR = {Li, Chao and Chen, Yangkang},
TITLE = {Learned diffusion model regularization for full waveform inversion},
JOURNAL = {Geophysical prospecting},
VOLUME = {submitted}
}




```





