# Fine-Tuning π₀.₅ on LIBERO using LeRobot

**Author:** Shaifalee Saxena  
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

## 2. What Kind of Fine-Tuning Is This?

This project uses:

> **Supervised offline imitation-learning fine-tuning**

More specifically:

| Method | Used? | Explanation |
|---|---:|---|
| Supervised fine-tuning | Yes | The model learns from LIBERO demonstration trajectories |
| Offline imitation learning | Yes | Training uses existing demonstrations, not live environment interaction |
| Expert-only fine-tuning | Yes | Only the action expert / action-related components are trained |
| Full fine-tuning | Not yet | Future comparison |
| LoRA / QLoRA / PEFT | No | `use_peft=false` |
| RL fine-tuning | No | No reward function or online rollout training is used |

The key training flag is:

```bash
--policy.train_expert_only=true
