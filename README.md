# robot-learning-log

Programme intensif de 8 semaines (1-2h/jour) : du RL zéro aux World Models & VLA pour robotique.
MuJoCo pour la simulation, déploiement réel sur bras **SO101** (LeRobot).

Voir `programme-robot-learning.md` pour le détail théorie/exercice/checkpoint de chaque jour.
Une branche par semaine (`s1-rl-bases`, `s2-deep-rl`, ..., `s8-capstone`), mergée dans `main` une fois la semaine validée.

## Structure du repo

```
robot-learning-log/
├── README.md
├── programme-robot-learning.md      # programme complet, jour par jour
├── requirements.txt
├── s1-rl-bases/
│   ├── j1-bandits/
│   │   ├── bandit.py
│   │   └── README.md                # notes théorie + résultats + checkpoint
│   ├── j2-mdp/
│   ├── j3-bellman/
│   ├── j4-dp/
│   ├── j5-mc-td/
│   └── mini-projet-qlearning/
├── s2-deep-rl/
│   ├── j6-fonction-approx/
│   ├── j7-dqn/
│   ├── j8-dqn-ameliore/
│   ├── j9-reinforce/
│   ├── j10-actor-critic/
│   └── mini-projet-dqn-vs-a2c/
├── s3-mujoco-controle/
│   ├── j11-anatomie-mujoco/
│   ├── j12-dynamique/
│   ├── j13-pd-impedance/
│   ├── j14-cinematique/
│   └── mini-projet-trajectoire/
├── s4-rl-continu/
│   ├── j15-continu/
│   ├── j16-ppo/
│   ├── j17-sac/
│   ├── j18-ensembles-dynamique/
│   └── j19-mbpo/
├── s5-imitation-learning/
│   ├── j20-bc/
│   ├── j21-dagger/
│   ├── j22-collecte-so101/
│   ├── j23-act/
│   └── j24-diffusion-policy/
├── s6-world-models/
│   ├── j25-dynamique-latente/
│   ├── j26-dreamer/
│   ├── j27-tdmpc2/
│   ├── j28-incertitude/
│   └── mini-projet-world-model-reel/
├── s7-vla/
│   ├── j29-panorama-vla/
│   ├── j30-finetuning/
│   ├── j31-generalisation/
│   ├── j32-integration-wm-vla/
│   └── mini-projet-vla-deploiement/
└── s8-capstone/
    ├── design/
    ├── implementation/
    └── deploiement-final/
```

## Convention par jour

Chaque dossier `jN-nom/` contient :
- le code de l'exercice (from scratch sauf mention contraire dans le programme)
- un `README.md` court avec : ce que tu as compris (théorie en 3-5 lignes), résultat (courbe/métrique), le checkpoint du programme est-il atteint (✅/❌ + pourquoi).

## Checklist globale

- [ ] S1 — Bases du RL (bandits → Q-learning tabulaire)
- [ ] S2 — Deep RL (DQN → Actor-Critic)
- [ ] S3 — MuJoCo & contrôle robotique + Pont SO101 #1
- [ ] S4 — RL continu (PPO, SAC, MBPO) + Pont SO101 #2
- [ ] S5 — Imitation Learning (BC, DAgger, ACT, Diffusion Policy) + Pont SO101 #3
- [ ] S6 — World Models (Dreamer, TD-MPC2) + Pont SO101 #4
- [ ] S7 — VLA (fine-tuning, généralisation) + Pont SO101 #5
- [ ] S8 — Capstone

## Installation

Voir `requirements.txt`. Les dépendances sont groupées par phase du programme — pas besoin de tout installer dès le Jour 1 (voir commentaires dans le fichier).

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

`lerobot` (Semaine 3+) nécessite une installation séparée depuis le repo GitHub officiel (voir commentaire dans `requirements.txt`) car les versions évoluent vite et le paquet PyPI peut être en retard.
