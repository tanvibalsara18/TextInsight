import os
from box.exceptions import BoxValueError
import yaml
from TextInsight.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: If an unexpected error occurs.

    Returns:
        ConfigBox: ConfigBox object containing the YAML file content.
    """
    try:
        # Check if the file is empty before attempting to load it
        if os.path.getsize(path_to_yaml) == 0:
            raise ValueError("YAML file is empty")

        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")

            # Ensure content is not None
            if content is None:
                raise ValueError("YAML file is empty or malformed")

            return ConfigBox(content)
    except ValueError as ve:
        logger.error(f"Error reading YAML file: {ve}")
        raise ve
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories to create.
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
