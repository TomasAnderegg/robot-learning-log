# robot-learning-log

Intensive 8-week program (1-2h/day, +3 optional bonus days): from zero RL to World Models & VLA for robotics.
MuJoCo for simulation, real deployment on an **SO101** arm (LeRobot).
Reading list cross-checked with NUS [CS 6283 — Robot Learning in the Era of Foundation Models](https://jiafei1224.github.io/cs6283.github.io/#reading).

Full day-by-day breakdown (theory/exercise/checkpoint): `programme-robot-learning.md`.
Setup: `requirements.txt`. One branch per week (`w1-rl-basics` → `w8-capstone`).

---

## Week 1 — RL fundamentals, from zero

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 1 | What is RL? | Agent-environment loop, bandits, ε-greedy, regret | 📄 [Sutton & Barto ch.2](http://incompleteideas.net/book/RLbook2020.pdf) · 🎥 [David Silver — Lecture 1: Intro to RL](https://www.youtube.com/watch?v=2pWv7GOvuf0) | Code a k-armed bandit + ε-greedy agent from scratch, plot regret |
| 2 | MDP formalism | States, actions, transitions, rewards, γ, return | 📄 [Sutton & Barto ch.3](http://incompleteideas.net/book/RLbook2020.pdf) · 🎥 [David Silver — Lecture 2: MDPs](https://www.youtube.com/watch?v=lfHX2hHRMVQ) | Hand-code a gridworld MDP (`step`/`reset`) |
| 3 | Value functions & Bellman | V(s), Q(s,a), Bellman expectation/optimality | 📄 Sutton & Barto ch.3.5-3.8 · 🎥 David Silver Lecture 2 (2nd half) | Iterative Bellman backup to compute V(s) on your gridworld |
| 4 | Dynamic Programming | Policy Iteration, Value Iteration | 📄 [Sutton & Barto ch.4](http://incompleteideas.net/book/RLbook2020.pdf) · 🎥 [David Silver — Lecture 3: DP](https://www.youtube.com/watch?v=Nd1-UUMVfz4) | Implement both, compare convergence speed |
| 5 | Monte Carlo & TD | Model-free prediction, bootstrapping | 📄 [Sutton & Barto ch.5-6](http://incompleteideas.net/book/RLbook2020.pdf) · 🎥 [David Silver — Lecture 4: Model-Free Prediction](https://www.youtube.com/watch?v=PnHCvfgC_ZA) | MC estimation of V(s), then TD(0), compare |
| Mini-project | Tabular Q-learning | ε-greedy control, off-policy TD | 📄 Sutton & Barto ch.6.5 · 🎥 [David Silver — Lecture 5: Model-Free Control](https://www.youtube.com/watch?v=0g4j2k_Ggc4) | Q-learning from scratch on `FrozenLake`/`Taxi-v3` |

## Week 2 — Deep RL

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 6 | Function approximation | Why tabular fails, NN as Q-approximator | 🎥 [David Silver — Lecture 6: Value Function Approximation](https://www.youtube.com/watch?v=UoPei5o4fps) | Replace your Q-table with a small MLP on FrozenLake |
| 7 | DQN | Experience replay, target network | 📄 [Mnih et al. 2015, Nature](https://www.nature.com/articles/nature14236) · 🎥 [CS285 (Levine) — DQN lecture, Fall 2020 playlist](https://youtube.com/playlist?list=PL_iWQOsE6TfURIIhCrlt-wj9ByIVpbfGc) | DQN from scratch on `CartPole-v1` |
| 8 | Improving DQN | Double DQN, Dueling DQN | 📄 [Van Hasselt et al. 2016 — Double DQN](https://arxiv.org/abs/1509.06461) · 📄 [Wang et al. 2016 — Dueling DQN](https://arxiv.org/abs/1511.06581) | Implement one improvement, compare |
| 9 | Policy gradients | REINFORCE, policy gradient theorem | 📄 Sutton & Barto ch.13 · 🎥 [David Silver — Lecture 7: Policy Gradient](https://www.youtube.com/watch?v=KHZVXao4qXs) | REINFORCE from scratch on CartPole/LunarLander |
| 10 | Actor-Critic | Baseline, advantage function | 🎥 CS285 (Levine) — Actor-Critic lecture, same playlist | A2C from scratch |
| Mini-project | DQN vs Actor-Critic | Value-based vs policy-based trade-offs | — | Train both on `LunarLander-v2`, compare |

## Week 3 — MuJoCo & robotic control

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 11 | MuJoCo anatomy | MJCF, `mj_step`, bodies/joints/actuators | 📄 [MuJoCo documentation](https://mujoco.readthedocs.io/) | Load an arm model, sinusoidal joint motion |
| 12 | Arm dynamics | Lagrange equation, gravity compensation | 📄 [Modern Robotics, ch.8 (Lynch & Park)](https://hades.mech.northwestern.edu/images/7/7f/MR.pdf) | Compare with/without gravity, measure `qfrc_bias` |
| 13 | PD & impedance control | Joint-space PD, Cartesian impedance | 📄 Modern Robotics ch.11 | PD controller from scratch, tune Kp/Kd |
| 14 | Kinematics (FK/IK) | Homogeneous transforms, numerical IK | 📄 Modern Robotics ch.3 & 6 · 📎 [cuRobo (CS6283)](https://arxiv.org/pdf/2310.17274) | Numerical IK solver from scratch |
| Bonus | Grasping fundamentals | Grasp representation & generation | 📄 [6-DOF GraspNet (CS6283)](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mousavian_6-DOF_GraspNet_Variational_Grasp_Generation_for_Object_Manipulation_ICCV_2019_paper.pdf) | Script a top-down grasp, compare to learned grasping |
| Mini-project + SO101 Bridge #1 | Cartesian trajectory | IK + PD combined | — | Circle/line trajectory in sim + first real teleoperation |
| Bonus | Deep perception for manipulation | Perception as action maps, multi-task vision policies | 📄 [Transporter Networks](https://arxiv.org/pdf/2010.14406) · 📄 [PerAct (CS6283)](https://peract.github.io/paper/peract_corl2022.pdf) | Design doc: vision-based pick/place vs scripted IK |

## Week 4 — Continuous RL for robotics

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 15 | Discrete → continuous | Gaussian policies, reparameterization | 🎥 CS285 — Continuous control lecture | Adapt your A2C to `Pendulum-v1`/`Reacher` |
| 16 | PPO | Clipped surrogate objective, GAE | 📄 [Schulman et al. 2017 — PPO](https://arxiv.org/abs/1707.06347) · 🎥 [OpenAI Spinning Up — PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) | PPO from scratch on `Reacher` |
| 17 | SAC | Entropy regularization, off-policy | 📄 [Haarnoja et al. 2018 — SAC](https://arxiv.org/abs/1801.01290) · 📎 [Learning Dexterous In-Hand Manipulation (CS6283)](https://arxiv.org/pdf/1808.00177) · 📎 [Human-in-the-Loop RL (CS6283)](https://arxiv.org/pdf/2410.21845) | SAC from scratch on a manipulation task |
| 18 | Model-based RL | Dynamics ensembles, uncertainty | 📄 [Janner et al. 2019 — MBPO](https://arxiv.org/abs/1906.08253) | Train a dynamics ensemble on collected trajectories |
| 19 | MBPO loop | Imagined rollouts | 📄 MBPO paper (same as above) · 🎥 CS285 — Model-based RL lecture | Full MBPO loop, compare to pure SAC |
| SO101 Bridge #2 | Sim2real gap | — | — | Deploy PPO/SAC reaching policy, document the gap |

## Week 5 — Modern Imitation Learning

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 20 | Behavior Cloning | Supervised learning, compounding error | 📎 [Implicit Behavioral Cloning (CS6283)](https://arxiv.org/pdf/2109.00137) · 📎 [End-to-End Visuomotor Policies, Levine et al. (CS6283)](https://arxiv.org/pdf/1504.00702) | Train BC, observe drift |
| 21 | DAgger | Iterative data aggregation | 📄 [Ross et al. 2011 — DAgger](https://arxiv.org/abs/1011.0686) | DAgger vs BC comparison |
| 22 | Real data collection | LeRobot dataset format | 📄 [LeRobot docs](https://huggingface.co/docs/lerobot) | Collect 20-50 demos on SO101 |
| 23 | ACT | Action chunking, CVAE, transformer | 📄 [Zhao et al. 2023 — ACT/ALOHA (CS6283)](https://arxiv.org/pdf/2304.13705) · 🎥 [ALOHA project page (videos)](https://tonyzhaozh.github.io/aloha/) | Train ACT on your SO101 dataset |
| 24 | Diffusion Policy | Denoising diffusion over action sequences | 📄 [Chi et al. 2023 — Diffusion Policy (CS6283)](https://arxiv.org/pdf/2303.04137) · 🎥 [Cheng Chi — LeRobot Research Presentation #2](https://www.youtube.com/watch?v=M03sZFfW-qU) | Train Diffusion Policy, compare to ACT |
| SO101 Bridge #3 | Real deployment | — | — | Deploy ACT/Diffusion Policy, measure success rate |

## Week 6 — World Models

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 25 | Latent dynamics | Encoder → latent state → dynamics | 📄 [Hafner et al. 2019 — PlaNet](https://arxiv.org/abs/1811.04551) | Simplified RSSM-style latent model |
| 26 | Dreamer | RSSM, actor/critic in imagined latent space | 📄 [Hafner et al. 2020 — Dream to Control](https://arxiv.org/abs/1912.01603) · 📄 [Hafner et al. 2023 — Dreamer v3 (Nature)](https://www.nature.com/articles/s41586-025-08744-2) · 🎥 [TalkRL — Danijar Hafner on Dreamer v3](https://www.talkrl.com/episodes/danijar-hafner-2) | Adapt Dreamer on a MuJoCo task |
| 27 | TD-MPC2 | Decoded planning vs amortized policy | 📄 [Hansen et al. 2023 — TD-MPC2](https://arxiv.org/abs/2310.16828) | Extend Day 18-19 model into TD-MPC2 |
| 28 | Uncertainty & robustness | Ensemble uncertainty for cautious planning | (ties back to your own [[paws-jumping]]/RWM work) | Penalize uncertain trajectories in planning |
| Mini-project + SO101 Bridge #4 | Real-data world model | — | — | World model on SO101 data, closed-loop planning on real arm |

## Week 7 — VLA & multimodal policies

| Day | Course | Theory | Resources | Exercise |
|---|---|---|---|---|
| 29 | VLA landscape | VLM backbone + action tokenization | 📄 [Kim et al. 2024 — OpenVLA](https://arxiv.org/abs/2406.09246) · 📄 [Brohan et al. 2023 — RT-2](https://arxiv.org/abs/2307.15818) · 📎 [MolmoAct2 (CS6283, 2026)](https://arxiv.org/pdf/2605.02881) · 📎 [Native Video-Action Pretraining (CS6283, 2026)](https://arxiv.org/pdf/2607.08639) | Comparison diagram across SmolVLA/OpenVLA/RT-2/2026 SOTA |
| Bonus | Data & benchmarks | Cross-embodiment datasets | 📎 [DROID (CS6283)](https://arxiv.org/pdf/2403.12945) · 📎 [Open X-Embodiment / RT-X (CS6283)](https://arxiv.org/pdf/2310.08864) | Compare your SO101 dataset scale to DROID/OpenX |
| 30 | Fine-tuning | Language-conditioned fine-tuning | 📄 [LeRobot / SmolVLA docs](https://huggingface.co/docs/lerobot) | Fine-tune SmolVLA on SO101 dataset |
| 31 | Generalization | Zero-shot/few-shot evaluation | 📄 [LIBERO benchmark](https://arxiv.org/abs/2306.03310) | Evaluate on unseen variations |
| 32 | VLA + world model | Prediction for planning/replanning | (design exercise, no single paper) | Architecture sketch: world model as VLA verifier |
| Mini-project + SO101 Bridge #5 | Final VLA deployment | — | — | Deploy on real SO101, final method comparison |

## Week 8 — Capstone

Design → implement → deploy. No new theory — you're combining what you've already learned. See `programme-robot-learning.md` for the day-by-day breakdown.

---

## Legend
📄 = paper/reading · 🎥 = video · 📎 = added from the [CS 6283](https://jiafei1224.github.io/cs6283.github.io/#reading) reading list

## Installation

```bash
python -m venv .venv   # or: conda create -n robot-learning python=3.11
source .venv/bin/activate
pip install -r requirements.txt
```

See `requirements.txt` for phase-grouped dependencies and install notes (swig for `gymnasium[box2d]`, `lerobot` install-from-source, etc.).
