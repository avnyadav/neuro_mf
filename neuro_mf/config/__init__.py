from neuro_mf.constant import *
import os
import yaml


def get_sample_model_config_yaml_file(export_dir: str) -> str:
    """
    author: https://github.com/avnyadav
    repo: https://github.com/avnyadav/neuro_mf
    export_dir: Location to export file
    =======================================

    This function generates model.yaml file
    return: File path of generated yaml file

    sample code:

    from neuro_mf.config import get_sample_model_config_yaml_file
    dir_name = r"d:\config"
    export_file_path=get_sample_model_config_yaml_file(export_dir="config")
    print(export_file_path)

    output: 'd:\\config\\model.yaml

    """
    try:
        model_config = {
            GRID_SEARCH_KEY: {
                MODULE_KEY: "sklearn.model_selection",
                CLASS_KEY: "GridSearchCV",
                PARAM_KEY: {
                    "cv": 3,
                    "verbose": 1
                }

            },
            MODEL_SELECTION_KEY: {
                "module_0": {
                    MODULE_KEY: "module_of_model",
                    CLASS_KEY: "ModelClassName",
                    PARAM_KEY:
                        {"param_name1": "value1",
                         "param_name2": "value2",
                         },
                    SEARCH_PARAM_GRID_KEY: {
                        "param_name": ['param_value_1', 'param_value_2']
                    }

                },
            }
        }
        os.makedirs(export_dir, exist_ok=True)
        export_file_path = os.path.join(export_dir, MODEL_CONFIG_FILE_NAME)
        with open(export_file_path, 'w') as file:
            yaml.dump(model_config, file)
        return export_file_path
    except Exception as e:
        raise e
