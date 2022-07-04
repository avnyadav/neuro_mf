![image](https://user-images.githubusercontent.com/34875169/177150753-b68b0c66-3b15-4ecc-b168-1a77ebc3fc62.png)

neuro-ml is a open source library designed to avoid writing duplicate code.

You can use new model of scikit learn without writing any cod.
Model training can be control by configuration file

How to generate configuration file

It is very simple. 

We will export sample model config file in config directory

You can use below command to export sample configuration

```commandline
from neuro_mf.config import get_sample_model_config_yaml_file

if __name__ == "__main__":
    export_file_path=get_sample_model_config_yaml_file(export_dir="config")

```
Check your config folder
You will find a file name as "model.yaml"

content of model.yaml
```commandline
grid_search:
  class: GridSearchCV
  module: sklearn.model_selection
  params:
    cv: 3
    verbose: 1
model_selection:
  module_0:
    class: ModelClassName
    module: module_of_model
    params:
      param_name1: value1
      param_name2: value2
    search_param_grid:
      param_name:
      - param_value_1
      - param_value_2
```

Now update the content of model.yaml file with below content
for testing
```commandline
grid_search:
  class: GridSearchCV
  module: sklearn.model_selection
  params:
    cv: 3
    verbose: 1
model_selection:
  module_0:
    class: RandomForestRegressor
    module: sklearn.ensemble
    params:
      n_estimators: 200
      criterion: squared_error
    search_param_grid:
      n_estimators:
      - 150
      - 200
      - 250
      max_depth:
      - 2
      - 5
      - 6
      
```

Now Let's try to train a RandomForestRegressor
```commandline
import os

from neuro_mf.config import get_sample_model_config_yaml_file
from neuro_mf import ModelFactory

if __name__ == "__main__":
    # export_dir=get_sample_model_config_yaml_file(export_dir="config")
    export_file_path = os.path.join("config", "model.yaml")
    model_factory = ModelFactory(model_config_path=export_file_path)
    x = None  # input feature
    y = None  # target feature
    best_model = model_factory.get_best_model(x, y, base_accuracy=0.9)
    print(best_model.best_model)
    print(f"best score:{best_model.best_score}")

```


