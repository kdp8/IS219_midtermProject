import os
from dotenv import load_dotenv

load_dotenv()

class env:
    @staticmethod
    def get_history_file_path(env_var_name, default_filename):
        base_dir = os.environ.get(env_var_name)
        if not base_dir:
            base_dir = os.getcwd()
        os.makedirs(base_dir, exist_ok=True)
        return os.path.join(base_dir, default_filename)
