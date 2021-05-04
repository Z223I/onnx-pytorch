# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v4.Concat")
def Concat(inputs, **kwargs):
  _inputs = []
  for i in (inputs, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Concat"]
  omm.op_counter["Concat"] += 1
  node = onnx.helper.make_node("Concat",
                               _inputs, [f"_t_Concat_{idx}"],
                               name=f"Concat_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node
