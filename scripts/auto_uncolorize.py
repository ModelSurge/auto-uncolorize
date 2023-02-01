import gradio as gr
import modules.scripts as scripts
import sys


base_dir = scripts.basedir()
sys.path.append(base_dir)


class AutoBackupScript(scripts.Script):
    def title(self):
        return "Uncolorize"

    def ui(self, is_img2img):
        is_active_checkbox = gr.Checkbox(value=False, label='Save image as black and white', interactive=True)
        return [is_active_checkbox]

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess_image(self, p, pp, script_active_checkbox, *script_args):
        if not script_active_checkbox:
            return

        pp.image = pp.image.convert('L')
