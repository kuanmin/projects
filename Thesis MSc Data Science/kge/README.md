# <img src="docs/source/images/logo/libkge-header-2880.png" alt="LibKGE: A knowledge graph embedding library" width="80%">

LibKGE is a PyTorch-based library for efficient training, evaluation, and
hyperparameter optimization of [knowledge graph
embeddings](https://ieeexplore.ieee.org/document/8047276) (KGE). It is highly
configurable, easy to use, and extensible. Other KGE frameworks are [listed
below](#other-kge-frameworks).

The key goal of LibKGE is to foster *reproducible research* into (as well as
meaningful comparisons between) KGE models and training methods. As we argue in
our [ICLR 2020 paper](https://github.com/uma-pi1/kge-iclr20)
(see [video](https://iclr.cc/virtual_2020/poster_BkxSmlBFvr.html)), the choice
of training strategy and hyperparameters are very influential on model performance,
often more so than the model class itself. LibKGE aims to provide *clean
implementations* of training, hyperparameter optimization, and evaluation
strategies that can be used with any model. Every potential knob or heuristic
implemented in the framework is exposed explicitly via *well-documented*
configuration files (e.g., see [here](kge/config-default.yaml) and
[here](kge/model/embedder/lookup_embedder.yaml)). LibKGE also provides the most
common KGE models and new ones can be easily added (contributions welcome!).

For link prediction tasks, rule-based systems such as
[AnyBURL](http://web.informatik.uni-mannheim.de/AnyBURL/) are a competitive
alternative to KGE.

## Table of contents

1. [Features](#features)
2. [Results and pretrained models](#results-and-pretrained-models)
3. [Quick start](#quick-start)
4. [Using LibKGE](#using-libkge)
5. [Currently supported KGE models](#currently-supported-kge-models)
6. [Adding a new model](#adding-a-new-model)
7. [Known issues](#known-issues)
8. [Changelog](CHANGELOG.md)
9. [Other KGE frameworks](#other-kge-frameworks)
10. [How to cite](#how-to-cite)

## Features

 - **Training**
   - Training types: negative sampling, 1vsAll, KvsAll
   - Losses: binary cross entropy (BCE), Kullback-Leibler divergence (KL),
     margin ranking (MR)
   - All optimizers and learning rate schedulers of PyTorch supported
   - Early stopping
   - Checkpointing
   - Stop (e.g., via `Ctrl-C`) and resume at any time
 - **Hyperparameter tuning**
   - Grid search, manual search, quasi-random search (using
     [Ax](https://ax.dev/)), Bayesian optimization (using [Ax](https://ax.dev/))
   - Highly parallelizable (multiple CPUs/GPUs on single machine)
   - Stop and resume at any time
 - **Evaluation**
   - Entity ranking metrics: Mean Reciprocal Rank (MRR), HITS@k with/without filtering
   - Drill-down by: relation type, relation frequency, head or tail
 - **Extensive logging**
   - Logging for training, hyper-parameter tuning and evaluation in machine
     readable formats to facilitate analysis
 - **KGE models**
   - All models can be used with or without reciprocal relations
   - [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf) ([code](kge/model/rescal.py), [config](kge/model/rescal.yaml))
   - [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) ([code](kge/model/transe.py), [config](kge/model/transe.yaml))
   - [DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf) ([code](kge/model/distmult.py), [config](kge/model/distmult.yaml))
   - [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf) ([code](kge/model/complex.py), [config](kge/model/complex.yaml))
   - [ConvE](https://arxiv.org/abs/1707.01476)  ([code](kge/model/conve.py), [config](kge/model/conve.yaml))
   - [RelationalTucker3](https://arxiv.org/abs/1902.00898)/[TuckER](https://arxiv.org/abs/1901.09590) ([code](kge/model/relational_tucker3.py), [config](kge/model/relational_tucker3.yaml))
   - [CP](https://arxiv.org/abs/1806.07297) ([code](kge/model/cp.py), [config](kge/model/cp.yaml))
   - [SimplE](https://arxiv.org/abs/1802.04868) ([code](kge/model/simple.py), [config](kge/model/simple.yaml))
   - [RotatE](https://arxiv.org/abs/1902.10197) ([code](kge/model/rotate.py), [config](kge/model/rotate.yaml))
 - **Embedders**
   - Lookup embedder ([code](kge/model/embedder/lookup_embedder.py), [config](kge/model/embedder/lookup_embedder.yaml))
   - Projection embedder ([code](kge/model/embedder/projection_embedder.py), [config](kge/model/embedder/projection_embedder.yaml))


## Results and pretrained models

We list some example results (w.r.t. filtered MRR and HITS@k) obtained with
LibKGE below. These results are obtained by running automatic hyperparameter
search as described [here](https://github.com/uma-pi1/kge-iclr20). They are not
necessarily the best results that can be achieved using LibKGE, but the results
are comparable in that a common experimental setup (and equal amount of work)
has been used for hyperparameter optimization for each model.

Note that we report performance numbers on the entire test set, **including the
triples that contain entities not seen during training**. This is not done
consistently throughout existing KGE implementations: some frameworks remove
unseen entities from the test set, which leads to a perceived increase in
performance (e.g., roughly add +3pp to our WN18RR MRR numbers for this method of
evaluation).

We also provide pretrained models for these results. Each pretrained model is
given in the form of a LibKGE checkpoint, which contains the model as well as
additional information (such as the configuration being used). See the
documentation below on how to use checkpoints.

#### FB15K-237 (Freebase)

|                                                                                                       |   MRR | Hits@1 | Hits@3 | Hits@10 |                                                                                      Config file |                                                                              Pretrained model |
|-------------------------------------------------------------------------------------------------------|------:|-------:|-------:|--------:|-------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------:|
| [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf)                                           | 0.356 |  0.263 |  0.393 |   0.541 |   [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-rescal.yaml) |    [1vsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-rescal.pt) |
| [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) | 0.313 |  0.221 |  0.347 |   0.497 |   [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-transe.yaml) |   [NegSamp-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-transe.pt) |
| [DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf)  | 0.343 |  0.250 |  0.378 |   0.531 | [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-distmult.yaml) | [NegSamp-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-distmult.pt) |
| [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf)                                           | 0.348 |  0.253 |  0.384 |   0.536 |  [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-complex.yaml) |  [NegSamp-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-complex.pt) |
| [ConvE](https://arxiv.org/abs/1707.01476)                                                             | 0.339 |  0.248 |  0.369 |   0.521 |    [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-conve.yaml) |     [1vsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/fb15k-237-conve.pt) |

#### WN18RR (Wordnet)

|                                                                                                       |   MRR | Hits@1 | Hits@3 | Hits@10 |                                                                                 Config file |                                                                        Pretrained model |
|-------------------------------------------------------------------------------------------------------|------:|-------:|-------:|--------:|--------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------:|
| [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf)                                           | 0.467 |  0.439 |  0.480 |   0.517 |   [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-rescal.yaml) |   [KvsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-rescal.pt) |
| [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) | 0.228 |  0.053 |  0.368 |   0.520 |   [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-transe.yaml) |  [NegSamp-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-transe.pt) |
| [DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf)  | 0.452 |  0.413 |  0.466 |   0.530 | [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-distmult.yaml) | [KvsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-distmult.pt) |
| [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf)                                           | 0.475 |  0.438 |  0.490 |   0.547 |  [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-complex.yaml) |  [1vsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-complex.pt) |
| [ConvE](https://arxiv.org/abs/1707.01476)                                                             | 0.442 |  0.411 |  0.451 |   0.504 |    [config.yaml](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-conve.yaml) |    [KvsAll-kl](http://web.informatik.uni-mannheim.de/pi1/iclr2020-models/wnrr-conve.pt) |

#### Wikidata5M (Wikidata)

LibKGE supports large datasets such as Wikidata5M (4.8M entities). The result
given below was found by automatic hyperparameter search similar to the one used
for the smaller datasets above, but with some values fixed (training with shared
negative sampling, embedding dimension: 128, batch size: 1024, optimizer:
Adagrad, regularization: weighted). We ran 30 pseudo-random configurations for
20 epochs, and then reran the configuration that performed best on validation
data for 200 epochs.

|                                                             |   MRR | Hits@1 | Hits@3 | Hits@10 |                                                                                    Config file |                                                                            Pretrained model |
|-------------------------------------------------------------|------:|-------:|-------:|--------:|-----------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------:|
| [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf) | 0.301 |  0.245 |  0.331 |   0.397 | [config.yaml](http://web.informatik.uni-mannheim.de/pi1/libkge-models/wikidata5m-complex.yaml) | [NegSamp-kl](http://web.informatik.uni-mannheim.de/pi1/libkge-models/wikidata5m-complex.pt) |

## Quick start

```sh
# retrieve and install project in development mode
git clone https://github.com/uma-pi1/kge.git
cd kge
pip install -e .

# download and preprocess datasets
cd data
sh download_all.sh
cd ..

# train an example model on toy dataset (you can omit '--job.device cpu' when you have a gpu)
kge start examples/toy-complex-train.yaml --job.device cpu

```

## Using LibKGE

LibKGE supports training, evaluation, and hyperparameter tuning of KGE models.
The settings for each task can be specified with a configuration file in YAML
format or on the command line. The default values and usage for available
settings can be found in [config-default.yaml](kge/config-default.yaml) as well
as the model- and embedder-specific configuration files (such as
[lookup_embedder.yaml](kge/model/embedder/lookup_embedder.yaml)).

#### Train a model

First create a configuration file such as:

```yaml
job.type: train
dataset.name: fb15k-237

train:
  optimizer: Adagrad
  optimizer_args:
    lr: 0.2

valid:
  every: 5
  metric: mean_reciprocal_rank_filtered

model: complex
lookup_embedder:
  dim: 100
  regularize_weight: 0.8e-7
```

To begin training, run one of the following:

```sh
# Store the file as `config.yaml` in a new folder of your choice. Then initiate or resume
# the training job using:
kge resume <folder>

# Alternatively, store the configuration anywhere and use the start command
# to create a new folder
#   <kge-home>/local/experiments/<date>-<config-file-name>
# with that config and start training there.
kge start <config-file>

# In both cases, configuration options can be modified on the command line, too: e.g.,
kge start <config-file> config.yaml --job.device cuda:0 --train.optimizer Adam
```

Various checkpoints (including model parameters and configuration options) will
be created during training. These checkpoints can be used to resume training (or any other job type such as hyperparameter search jobs).

#### Resume training

All of LibKGE's jobs can be interrupted (e.g., via `Ctrl-C`) and resumed (from one of its checkpoints). To resume a job, use:

```sh
kge resume <folder>

# Change the device when resuming
kge resume <folder> --job.device cuda:1
```

By default, the last checkpoint file is used. The filename of the checkpoint can be overwritten using ``--checkpoint``.


#### Evaluate a trained model

To evaluate trained model, run the following:

```sh
# Evaluate a model on the validation split
kge valid <folder>

# Evaluate a model on the test split
kge test <folder>
```

By default, the checkpoint file named ``checkpoint_best.pt`` (which stores the best validation result so far) is used. The filename of the checkpoint can be overwritten using ``--checkpoint``.

#### Hyperparameter optimization

LibKGE supports various forms of hyperparameter optimization such as grid search
or Bayesian optimization. The search type and search space are specified in the
configuration file. For example, you may use [Ax](https://ax.dev/) for SOBOL
(pseudo-random) and Bayesian optimization.

The following config file defines a search of 10 SOBOL trials (arms) followed by
20 Bayesian optimization trials:

```yaml
job.type: search
search.type: ax

dataset.name: wnrr
model: complex
valid.metric: mean_reciprocal_rank_filtered

ax_search:
  num_trials: 30
  num_sobol_trials: 10  # remaining trials are Bayesian
  parameters:
    - name: train.batch_size
      type: choice
      values: [256, 512, 1024]
    - name: train.optimizer_args.lr
      type: range
      bounds: [0.0003, 1.0]
    - name: train.type
      type: fixed
      value: 1vsAll
```

Trials can be run in parallel across several devices:

```sh
# Run 4 trials in parallel evenly distributed across two GPUs
kge resume <folder> --search.device_pool cuda:0,cuda:1 --search.num_workers 4

# Run 3 trials in parallel, with per GPUs capacity
kge resume <folder> --search.device_pool cuda:0,cuda:1,cuda:1 --search.num_workers 3
```

#### Export and analyze logs and checkpoints

Extensive logs are stored as YAML files (hyperparameter search, training,
validation). LibKGE provides a convenience methods to export the log data to
CSV.

```sh
kge dump trace <folder>
```

The command above yields CSV output such as [this output for a training
job](docs/examples/dump-example-model.csv) or [this output for a search
job](https://github.com/uma-pi1/kge-iclr20/blob/master/data_dumps/iclr2020-fb15k-237-all-trials.csv).
Additional configuration options or metrics can be added to the CSV files as
needed (using a [keys
file](https://github.com/uma-pi1/kge-iclr20/blob/master/scripts/iclr2020_keys.conf)).

Information about a checkpoint (such as the configuration that was used,
training loss, validation metrics, or explored hyperparameter configurations)
can also be exported from the command line (as YAML):

```sh
kge dump checkpoint <checkpoint>
```

Configuration files can also be dumped in various formats.
```sh
# dump just the configuration options that are different from the default values
kge dump config <config-or-folder-or-checkpoint>

# dump the configuration as is
kge dump config <config-or-folder-or-checkpoint> --raw

# dump the expanded config including all configuration keys
kge dump config <config-or-folder-or-checkpoint> --full

```

#### Help and other commands

```sh
# help on all commands
kge --help

# help on a specific command
kge dump --help
```

#### Use a pretrained model in an application

Using a trained model trained with LibKGE is straightforward. In the following
example, we load a checkpoint and predict the most suitable object for a two
subject-relations pairs: ('Dominican Republic', 'has form of government', ?) and
('Mighty Morphin Power Rangers', 'is tv show with actor', ?).

```python
import torch
from kge.model import KgeModel
from kge.util.io import load_checkpoint 

# download link for this checkpoint given under results above
checkpoint = load_checkpoint('fb15k-237-rescal.pt')
model = KgeModel.create_from(checkpoint)

s = torch.Tensor([0, 2,]).long()             # subject indexes
p = torch.Tensor([0, 1,]).long()             # relation indexes
scores = model.score_sp(s, p)                # scores of all objects for (s,p,?)
o = torch.argmax(scores, dim=-1)             # index of highest-scoring objects

print(o)
print(model.dataset.entity_strings(s))       # convert indexes to mentions
print(model.dataset.relation_strings(p))
print(model.dataset.entity_strings(o))

# Output (slightly revised for readability):
#
# tensor([8399, 8855])
# ['Dominican Republic'        'Mighty Morphin Power Rangers']
# ['has form of government'    'is tv show with actor']
# ['Republic'                  'Johnny Yong Bosch']
```

For other scoring functions (score_sp, score_po, score_so, score_spo), see [KgeModel](kge/model/kge_model.py#L455).


## Currently supported KGE models

LibKGE currently implements the following KGE models:

- [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf) ([code](kge/model/rescal.py), [config](kge/model/rescal.yaml))
- [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) ([code](kge/model/transe.py), [config](kge/model/transe.yaml))
- [DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf) ([code](kge/model/distmult.py), [config](kge/model/distmult.yaml))
- [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf) ([code](kge/model/complex.py), [config](kge/model/complex.yaml))
- [ConvE](https://arxiv.org/abs/1707.01476)  ([code](kge/model/conve.py), [config](kge/model/conve.yaml))
- [RelationalTucker3](https://arxiv.org/abs/1902.00898) ([code](kge/model/relational_tucker3.py), [config](kge/model/relational_tucker3.yaml))
- [CP](https://arxiv.org/abs/1806.07297) ([code](kge/model/cp.py), [config](kge/model/cp.yaml))
- [SimplE](https://arxiv.org/abs/1802.04868) ([code](kge/model/simple.py), [config](kge/model/simple.yaml))
- [RelationalTucker3](https://arxiv.org/abs/1902.00898)/[TuckER](https://arxiv.org/abs/1901.09590) ([code](kge/model/relational_tucker3.py), [config](kge/model/relational_tucker3.yaml))
- [RotatE](https://arxiv.org/abs/1902.10197) ([code](kge/model/rotate.py), [config](kge/model/rotate.yaml))

The [examples](examples) folder contains some configuration files as examples of how to train these models.

We welcome contributions to expand the list of supported models! Please see [CONTRIBUTING](CONTRIBUTING.md) for details and feel free to initially open an issue.

## Adding a new model or embedder

To add a new model to LibKGE, extend the
[KgeModel](https://github.com/uma-pi1/kge/blob/1c69d8a6579d10e9d9c483994941db97e04f99b3/kge/model/kge_model.py#L243)
class. A model is made up of a
[KgeEmbedder](https://github.com/uma-pi1/kge/blob/1c69d8a6579d10e9d9c483994941db97e04f99b3/kge/model/kge_model.py#L170)
to associate each subject, relation and object to an embedding, and a
[KgeScorer](https://github.com/uma-pi1/kge/blob/1c69d8a6579d10e9d9c483994941db97e04f99b3/kge/model/kge_model.py#L76)
to score triples given their embeddings.

The model implementation should be stored under
`<kge-home>/kge/model/<model-name>.py`, its configuration options under
`<kge-home>/kge/model/<model-name>.yaml` and its import has to be added to `<kge-home>/kge/model/__init__.py`.

The embdedder implementation should be stored under
`<kge-home>/kge/model/embedder/<embedder-name>.py`, its configuration options under
`<kge-home>/kge/model/embedder/<embedder-name>.yaml` and its import has to be added to `<kge-home>/kge/model/__init__.py`.

## Known issues

## Changelog

See [here](CHANGELOG.md).


## Other KGE frameworks

Other KGE frameworks:
 - [Graphvite](https://graphvite.io/)
 - [AmpliGraph](https://github.com/Accenture/AmpliGraph)
 - [OpenKE](https://github.com/thunlp/OpenKE)
 - [PyKEEN](https://github.com/SmartDataAnalytics/PyKEEN)

KGE projects for publications that also implement a few models:
 - [ConvE](https://github.com/TimDettmers/ConvE)
 - [KBC](https://github.com/facebookresearch/kbc)

PRs to this list are welcome.

## How to cite

If you use LibKGE, please cite the following publication:

```
@inproceedings{
  ruffinelli2020you,
  title={You {CAN} Teach an Old Dog New Tricks! On Training Knowledge Graph Embeddings},
  author={Daniel Ruffinelli and Samuel Broscheit and Rainer Gemulla},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://openreview.net/forum?id=BkxSmlBFvr}
}
```
