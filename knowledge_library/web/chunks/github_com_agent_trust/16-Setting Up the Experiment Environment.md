## Setting Up the Experiment Environment
[](https://github.com/camel-ai/agent-trust#setting-up-the-experiment-environment)
To prepare the environment for conducting experiments, follow these steps using Conda:
To create a new Conda environment with all required dependencies as specified in the `environment.yaml` file, use:
```
conda env create -f environment.yaml
```

Alternatively, you can set up the environment manually as follows:
```
conda create -n agent-trust python=3.10
pip install -r requirements.txt
```
