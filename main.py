import base64
import gradio as gr

def sentence_builder(API,file):

    return API , {"name":API}


iface = gr.Interface(
    sentence_builder,
    [
        gr.inputs.Radio(["VBHC", "EKYC", "Full OCR"]),
        "file",
    ],
    ["image","json"]
)

if __name__ == "__main__":
    iface.launch()