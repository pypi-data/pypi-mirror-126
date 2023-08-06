
<div align="center">
    <img src="docs/banner.png" height=200 alt="banner"/>
</div>

-----
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/data-centric-ai/dcbench/CI)
![GitHub](https://img.shields.io/github/license/data-centric-ai/dcbench)
[![Documentation Status](https://readthedocs.org/projects/dcbench/badge/?version=latest)](https://dcbench.readthedocs.io/en/latest/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/data-centric-ai/dcbench/branch/main/graph/badge.svg?token=MOLQYUSYQU)](https://codecov.io/gh/data-centric-ai/dcbench)

A benchmark of  aspects of improving the quality of machine learning workflows.

[**Getting Started**](⚡️-Quickstart)
| [**What is dcbench?**](💡-what-is-dcbench)
| [**Docs**](https://dcbench.readthedocs.io/en/latest/index.html)
| [**Contributing**](CONTRIBUTING.md)
| [**Website**](https://www.datacentricai.cc/)
| [**About**](✉️-About)


## ⚡️ Quickstart

```bash
pip install dcbench
```

Using a Jupyter notebook or some other interactive environment, you can import the library 
and explore the data-centric problems in the benchmark:

```python
import dcbench
dcbench.problem_classes
```

## 💡 What is dcbench?
This is a benchmark that tests various data-centric aspects of improving the quality of machine learning workflows.

It features a growing list of *tasks*:

* Minimal data cleaning (`miniclean`)
* Task-specific Label Correction (`labelfix`)
* Discovery of validation Error Modalities (`errmod`)
* Minimal training dataset selection (`minitrain`)

Each task features a collection of *scenarios* which are defined by datasets and ML pipeline elements (e.g. a model, feature pre-processors, etc.)
## ⚙️ How does it work?
### `Problem`

This benchmark is a collection of *data-centric problems*. *What is a data-centric problem?* A useful analogy is: chess problems are to a full chess game as *data-centric* *problems* are to the full data-centric ML lifecycle. For example, many machine-learning workflows include a label cleaning phase where labels are audited and corrected. Therefore, our benchmark includes a collection of label cleaning *problems* each with a different dataset and set of sullied labels to be cleaned. 

The benchmark supports a diverse set of problems that may look very different from one another. For example, a slice discovery problem has different inputs and outputs than a data cleaning problem. To deal with this, we group problems by *problem class.*  In `dcbench`, each problem class is represented by a subclass of `Problem` (*e.g.* `SliceDiscoveryProblem`, `MiniCleanProblem`). The problems themselves are represented by instances of these subclasses. 

We can get a list all of the problem classes  in `dcbench` with:

```python
import dcbench
dcbench.problem_classes

# OUT: 
[SliceDiscoveryProblem, MiniCleanProblem]
```

`dcbench` includes a set of problems for each task. We can list them with: 

```python
from dcbench import SliceDiscoveryProblem
SliceDiscoveryProblem.instances

# Out: TODO, get the actual dataframe output here 
dataframe
```

We can get one of these problems with 

```python
problem = SliceDiscoveryProblem.from_id("eda4")
```

### `Artefact`

Each *problem* is made up of a set of artefacts: a dataset with labels to clean, a dataset and a model to perform error analysis on. In `dcbench` , these artefacts are represented by instances of `Artefact`. We can think of each `Problem` object as a container for `Artefact` objects. 

```python
problem.artefacts

# Out: 
{
	"dataset": CSVArtefact()
}

artefact: CSVArtefact = problem["dataset"]
```

Note that `Artefact` objects don't actually hold their underlying data in memory. Instead, they hold pointers to where the `Artefact` lives in [dcbench cloud storage](https://console.cloud.google.com/storage/browser/dcbench?authuser=1&project=hai-gcp-fine-grained&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false) and, if it's been downloaded,  where it lives locally on disk. This makes the `Problem` objects very lightweight.  

**Downloading to disk.** By default, `dcbench` downloads artefacts to `~/.dcbench/artefacts` but this can be configured in the dcbench settings TODO: add support for configuration. To download an `Artefact`  via the Python API, use `artefact.download()`. You can also download all the artefacts in a problem with `problem.download()`.

**Loading into memory.** `dcbench` includes loading functionality for each artefact type. To load an artefact into memory you can use `artefact.load()` . Note that this will also download the artefact if it hasn't yet been downloaded. 

Finally,  we should point out that `problem` is a Python mapping, so we can index it directly to load artefacts.  

```python
# this is equivalent to problem.artefacts["dataset"].load()
df: pd.DataFrame = problem["dataset"] 
```

## ✉️ About
`dcbench` is being developed alongside the data-centric-ai benchmark. Reach out to Bojan Karlaš (karlasb [at] inf [dot] ethz [dot] ch) and Sabri Eyuboglu (eyuboglu [at] stanford [dot] edu if you would like to get involved or contribute!)
