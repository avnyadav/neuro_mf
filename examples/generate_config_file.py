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
