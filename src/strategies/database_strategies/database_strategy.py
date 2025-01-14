# interface class
import os
class DatabaseStrategy:
    def connect(self, *args, **kwargs):
        pass

    def backup(self, *args, **kwargs):
        pass

    def get_project_root(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Subir dos niveles para llegar a la raíz del proyecto
        project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
        return project_root