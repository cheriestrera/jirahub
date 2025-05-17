from tkinter import Frame
from frontend.SignUpAdmin import SignUpAdminWindow  


class SceneManager:
    def __init__(self, root):
        self.root = root
        self.current_scene = None
        self.scenes = {}
    
    def register_scene(self, name, scene_class):
        self.scenes[name] = scene_class 
    
    def show_scene(self, name, *args, **kwargs):
        # Hide current scene
        if self.current_scene:
            self.current_scene.pack_forget()
        
        # Create and show new scene
        scene_class = self.scenes.get(name)
        if not scene_class:
            raise ValueError(f"Scene {name} not registered")
        
        self.current_scene = scene_class(self.root, *args, **kwargs)
        self.current_scene.pack(fill="both", expand=True)
        return self.current_scene