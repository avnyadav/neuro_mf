![image](https://user-images.githubusercontent.com/34875169/177150753-b68b0c66-3b15-4ecc-b168-1a77ebc3fc62.png)


neuro-ml is a open source library designed to avoid writing duplicate code.

You can use new model of scikit learn without writing any code.
Model training can be control by configuration file.
> # <center>neuro_mf.ModelFactory</center>

>class neuro_mf.ModelFactory(model_config_path:str) [source](https://github.com/avnyadav/neuro_mf/blob/main/neuro_mf/__init__.py#L33)

<hr>

Parameters:
```
model_config_path: location of model.yaml file

How to generate configuration file
It is very simple.
We will export sample model config file in config directory
You can use below python to export sample configuration file.

```python
from neuro_mf.config import get_sample_model_config_yaml_file

if __name__ == "__main__":
    export_file_path=get_sample_model_config_yaml_file(export_dir="config")

```
Check your config folder
You will find a file name as "model.yaml"

content of model.yaml

```yaml
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
Now update the content of model.yaml file with below content for testing.
```
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
  module_1:
    class: SVR
    module: sklearn.svm
    params:
      kernel: rbf
    search_param_grid:
      kernel:
      - poly
      - rbf
```


<hr>
Attributes:


``config: dict 
model.yaml file will be available as dict in this attribute
``

`` 
grid_search_cv_module: str 
Module of grid search cv from sklearn lib sklearn.model_selection
``

``
grid_search_class_name: str
``

``
grid_search_property_data:dict
``

``
models_initialization_config: dict
``

``
initialized_model_list:
All model instance will be available in this attribute once get_initialized_model_list has been invoked on model factory object
``

``
grid_searched_best_model_list
Once grid search has been done for all model then every model with their tuned paramter will be available in this attribute
``

Few of the function return type can be inferred using 
below named tuple

```
InitializedModelDetail = namedtuple("InitializedModelDetail",
                                    ["model_serial_number", "model", "param_grid_search", "model_name"])

GridSearchedBestModel = namedtuple("GridSearchedBestModel", ["model_serial_number",
                                                             "model",
                                                             "best_model",
                                                             "best_parameters",
                                                             "best_score",
                                                             ])

BestModel = namedtuple("BestModel", ["model_serial_number",
                                     "model",
                                     "best_model",
                                     "best_parameters",
                                     "best_score", ])

```

<hr>
Methods:

<table>
<tr>
<td>class_for_name(module_name, class_name)</td>
</tr>

<tr><td>execute_grid_search_operation(self, initialized_model: InitializedModelDetail, input_feature,
                                      output_feature)</td>
</tr>
<tr><td>get_best_model(self, X, y, base_accuracy=0.6) -> BestModel</td>
</tr>
<tr><td>get_best_model_from_grid_searched_best_model_list(grid_searched_best_model_list: List[GridSearchedBestModel],
                                                          base_accuracy=0.6
                                                          ) -> BestModel</td>
</tr>
<tr><td>get_initialized_model_list(self) -> List[InitializedModelDetail]</td>
</tr>

<tr><td>initiate_best_parameter_search_for_initialized_model(self, initialized_model: InitializedModelDetail,
                                                             input_feature,
                                                             output_feature) -> GridSearchedBestModel</td>
</tr>

<tr><td>initiate_best_parameter_search_for_initialized_models(self,
                                                              initialized_model_list: List[InitializedModelDetail],
                                                              input_feature,
                                                              output_feature) -> List[GridSearchedBestModel]</td>
</tr>

<tr><td>read_params</td>
</tr>

<tr><td>update_property_of_class</td>
</tr>
</table>



How to generate configuration file
It is very simple.
We will export sample model config file in config directory
You can use below python to export sample configuration file.

```python
from neuro_mf.config import get_sample_model_config_yaml_file

if __name__ == "__main__":
    export_file_path=get_sample_model_config_yaml_file(export_dir="config")

```
Check your config folder
You will find a file name as "model.yaml"

content of model.yaml

```yaml
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

Now update the content of model.yaml file with below content for testing.
```yaml
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
    module_1:
        class: SVR
        module: sklearn.svm
        params:
          kernel: rbf
        search_param_grid:
          kernel:
          - poly
          - rbf
```
Above configuration file contains information about two model Random Forest and Support Vector



get_best_model_function will return best model after comparison


Now Let's try to train a RandomForestRegressor
```python
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


