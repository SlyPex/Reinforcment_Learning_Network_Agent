<h1 align="center">Autonomous Network Defender Agent using Reinforcement Learning</h2>

<div align="center">
  <img src="https://img.shields.io/github/commit-activity/t/SlyPex/Reinforcment_Learning_Network_Agent" alt="GitHub commit activity">
  <img src="https://img.shields.io/github/contributors/SlyPex/Reinforcment_Learning_Network_Agent" alt="Contributers">
  <img alt="GitHub License" src="https://img.shields.io/github/license/SlyPex/Reinforcment_Learning_Network_Agent">
</div>

This is a Mini-Project for our RL course at the University, the objective is to get familiar with RL core concepts.

> Ain't much. but it's honest work.

## Description
### Environment
According to the specifications of the Mini-Project, the Environment should be defined from scratch, since [gymnasium](https://gymnasium.farama.org/) has an implementation of [Environment](https://gymnasium.farama.org/api/env/) class which can be suitable as a super class for the defined environment in this Mini-Project

### Observation Space
In the context of this project the dataset [NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd) is considered to be the base Environment, each row from the dataset is considered as a state.
### Action Space
Dataset has a target class which classes each sample into _Normal_ or _Anomaly_, Relying on this the Action Space is defined as follows:

- `Allow` which corresponds to `Normal`
- `Deny` which corresponds to `Anomaly`

### Reward Function
Simply, if the agent allows/denies a normal/anomaly traffic respectively it get rewarded +1 otherwise it gets 0.

## Usage
First clone this project either by:
  - Git command:
```sh
git clone https://github.com/SlyPex/Reinforcment_Learning_Network_Agent.git
```
- Github CLI:
```sh
gh repo clone SlyPex/Reinforcment_Learning_Network_Agent
```
Next `cd` into the project directory and install the required libraries using : 

```sh
pip install -r requierments.txt
```

Then open up the Jupyter Notebook [agent_training.ipynb](./notebooks/agent_training.ipynb) file and run all the cells to train the agent.