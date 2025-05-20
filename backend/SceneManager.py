from tkinter import Frame
from frontend.SignUpAdmin import SignUpAdminWindow  


class SceneManager:
    def __init__(self, root):
        self.root = root
        self.current_scene = None
        self.scenes = {}
        self.scene_instances = {}
    
    def register_scene(self, name, scene_class):
        self.scenes[name] = scene_class 
    
    def get_scene(self, name):
        return self.scene_instances.get(name)
    
    def show_scene(self, name, *args, **kwargs):
        if self.current_scene:
            self.current_scene.pack_forget()
        
        scene_class = self.scenes.get(name)
        if not scene_class:
            raise ValueError(f"Scene {name} not registered")
        
        self.current_scene = scene_class(self.root, *args, **kwargs)
        self.current_scene.pack(fill="both", expand=True)
        self.scene_instances[name] = self.current_scene
        return self.current_scene