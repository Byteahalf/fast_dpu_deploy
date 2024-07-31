import torch
from pytorch_nndct.apis import Inspector
from pytorch_nndct.apis import torch_quantizer, dump_xmodel
import logging
import os

from models.common import DetectMultiBackend

imgsz = 640
gs = 32
batch_size = 8


target = "0x101000016010407"
logger = logging.getLogger()
device = torch.device('cpu')
path = "runs/train/exp/weights/best.pt"
model = DetectMultiBackend(path, device=device)
optimize = 1
model.eval()
model.to(device)

in_tensor = torch.rand([8, 3, 640, 640])
in_tensor.to(device)
inspector = Inspector(target)
inspector.inspect(model, in_tensor, device=device)

in_tensor = torch.rand([8, 3, 640, 640])
in_tensor.to(device)
quantizer = torch_quantizer("calib", model, (in_tensor), device=device)
quant_model = quantizer.quant_model
quant_model(in_tensor)
quantizer.export_quant_config()


in_tensor = torch.rand([1, 3, 640, 640])
in_tensor.to(device)
quantizer = torch_quantizer("test", model, (in_tensor), device=device)
quant_model = quantizer.quant_model
quant_model(in_tensor)
quantizer.export_xmodel()
quantizer.export_onnx_model()

os.system("vai_c_xir -x quantize_result/DetectMultiBackend_int.xmodel -a arch.json -o quantize_result/ -n dpu")

os.system("xir svg quantize_result/dpu.xmodel out.svg")