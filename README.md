# Fine-Tuning π₀.₅ on LIBERO using LeRobot

**Project:** Digital Image Processing / Robotics VLA Fine-Tuning  
**Model:** π₀.₅ Vision-Language-Action model  
**Dataset:** LIBERO via `HuggingFaceVLA/libero`  
**Framework:** Hugging Face LeRobot  

---

## 1. Project Overview

This project fine-tunes the π₀.₅ Vision-Language-Action model on the LIBERO robot manipulation dataset using Hugging Face LeRobot.

π₀.₅ is a pretrained VLA model that takes robot observations, language instructions, and robot state as input, and predicts continuous robot actions. The goal of this project is to adapt π₀.₅ to LIBERO-style language-conditioned manipulation tasks using supervised fine-tuning.

The current implementation focuses on building a reproducible fine-tuning pipeline:

- Set up LeRobot with CUDA support
- Download and load the LIBERO dataset
- Load a pretrained π₀.₅ checkpoint
- Run expert-only supervised fine-tuning
- Save and reload checkpoints
- Log and plot training loss
- Document setup, issues, and reproducibility steps

---

## 2. Fine-Tuning?

| Method | Used? | Explanation |
|---|---:|---|
| Supervised fine-tuning | Yes | The model learns from LIBERO demonstration trajectories |
| Offline imitation learning | Yes | Training uses existing demonstrations, not live environment interaction |
| Expert-only fine-tuning | Yes | Only the action expert / action-related components are trained |

The repository contains scripts, commands, plots, and documentation for reproducing π₀.₅ expert-only supervised fine-tuning on LIBERO. Large model checkpoints and datasets are excluded from GitHub and downloaded/generated locally using the README instructions.

The key training flag is:

```bash
--policy.train_expert_only=true



