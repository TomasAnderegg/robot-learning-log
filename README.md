# robot-learning-log

Intensive 8-week program (1-2h/day): from zero RL to World Models & VLA for robotics.
MuJoCo for simulation, real deployment on an **SO101** arm (LeRobot).

See `programme-robot-learning.md` for the full theory/exercise/checkpoint breakdown of each day.
One branch per week (`w1-rl-basics`, `w2-deep-rl`, ..., `w8-capstone`), merged into `main` once the week is validated.

## Repo structure

```
robot-learning-log/
├── README.md
├── programme-robot-learning.md      # full program, day by day
├── requirements.txt
├── w1-rl-basics/
│   ├── d1-bandits/
│   │   ├── bandit.py
│   │   └── README.md                # theory notes + results + checkpoint
│   ├── d2-mdp/
│   ├── d3-bellman/
│   ├── d4-dp/
│   ├── d5-mc-td/
│   └── mini-project-qlearning/
├── w2-deep-rl/
│   ├── d6-function-approx/
│   ├── d7-dqn/
│   ├── d8-dqn-improved/
│   ├── d9-reinforce/
│   ├── d10-actor-critic/
│   └── mini-project-dqn-vs-a2c/
├── w3-mujoco-control/
│   ├── d11-mujoco-anatomy/
│   ├── d12-dynamics/
│   ├── d13-pd-impedance/
│   ├── d14-kinematics/
│   └── mini-project-trajectory/
├── w4-continuous-rl/
│   ├── d15-continuous/
│   ├── d16-ppo/
│   ├── d17-sac/
│   ├── d18-dynamics-ensembles/
│   └── d19-mbpo/
├── w5-imitation-learning/
│   ├── d20-bc/
│   ├── d21-dagger/
│   ├── d22-so101-data-collection/
│   ├── d23-act/
│   └── d24-diffusion-policy/
├── w6-world-models/
│   ├── d25-latent-dynamics/
│   ├── d26-dreamer/
│   ├── d27-tdmpc2/
│   ├── d28-uncertainty/
│   └── mini-project-real-world-model/
├── w7-vla/
│   ├── d29-vla-landscape/
│   ├── d30-finetuning/
│   ├── d31-generalization/
│   ├── d32-wm-vla-integration/
│   └── mini-project-vla-deployment/
└── w8-capstone/
    ├── design/
    ├── implementation/
    └── final-deployment/
```

## Per-day convention

Each `dN-name/` folder contains:
- the exercise code (from scratch unless the program says otherwise)
- a short `README.md` with: what you understood (3-5 lines of theory), result (plot/metric), whether the program's checkpoint was met (✅/❌ + why).

## Overall checklist

- [ ] W1 — RL fundamentals (bandits → tabular Q-learning)
- [ ] W2 — Deep RL (DQN → Actor-Critic)
- [ ] W3 — MuJoCo & robotic control + SO101 Bridge #1
- [ ] W4 — Continuous RL (PPO, SAC, MBPO) + SO101 Bridge #2
- [ ] W5 — Imitation Learning (BC, DAgger, ACT, Diffusion Policy) + SO101 Bridge #3
- [ ] W6 — World Models (Dreamer, TD-MPC2) + SO101 Bridge #4
- [ ] W7 — VLA (fine-tuning, generalization) + SO101 Bridge #5
- [ ] W8 — Capstone

## Installation

See `requirements.txt`. Dependencies are grouped by program phase — no need to install everything on Day 1 (see comments in the file).

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

`lerobot` (Week 3+) requires a separate install from the official GitHub repo (see comment in `requirements.txt`) since versions move fast and the PyPI package can lag behind.
