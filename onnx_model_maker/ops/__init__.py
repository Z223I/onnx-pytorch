import glob
import importlib
import os
import sys

import onnx
import numpy

from onnx_model_maker import mod_name
from onnx_model_maker import omm
from onnx_model_maker import OPSET_VER


modules = glob.glob(os.path.join(os.path.dirname(__file__), "op_ver_*.py"))
for m in modules:
  spec = importlib.util.spec_from_file_location(os.path.basename(m)[:-3], m)
  spec.loader.exec_module(importlib.util.module_from_spec(spec))


def Input(*args):
  inputs = []
  for i, a in enumerate(args):
    t = onnx.numpy_helper.from_array(a)
    vi = onnx.helper.make_tensor_value_info(f"_t_Input_{i}",
                                            t.data_type, t.dims)
    omm.model.graph.input.append(vi)
    inputs.append(vi.name)
  return inputs


def Output(*args):
  for i, a in enumerate(args):
    if type(a) == numpy.ndarray:
      t = onnx.numpy_helper.from_array(a)
      vi = onnx.helper.make_tensor_value_info(f"_t_Output_{i}", t.data_type,
                                              t.dims)
      omm.model.graph.output.append(vi)
    elif type(a) == str:
      vi = onnx.helper.make_empty_tensor_value_info(a)
      omm.model.graph.output.append(vi)
    elif type(a) == onnx.NodeProto:
      for o in a.output:
        vi = onnx.helper.make_empty_tensor_value_info(o)
        omm.model.graph.output.append(vi)
    else:
      raise Exception


def Abs(*args, **kwargs):
  schema = onnx.defs.get_schema("Abs",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Abs")(*args, **kwargs)


def Acos(*args, **kwargs):
  schema = onnx.defs.get_schema("Acos",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Acos")(*args, **kwargs)


def Acosh(*args, **kwargs):
  schema = onnx.defs.get_schema("Acosh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Acosh")(*args, **kwargs)


def Adagrad(*args, **kwargs):
  schema = onnx.defs.get_schema("Adagrad",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Adagrad")(*args, **kwargs)


def Adam(*args, **kwargs):
  schema = onnx.defs.get_schema("Adam",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Adam")(*args, **kwargs)


def Add(*args, **kwargs):
  schema = onnx.defs.get_schema("Add",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Add")(*args, **kwargs)


def And(*args, **kwargs):
  schema = onnx.defs.get_schema("And",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.And")(*args, **kwargs)


def ArgMax(*args, **kwargs):
  schema = onnx.defs.get_schema("ArgMax",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ArgMax")(*args, **kwargs)


def ArgMin(*args, **kwargs):
  schema = onnx.defs.get_schema("ArgMin",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ArgMin")(*args, **kwargs)


def ArrayFeatureExtractor(*args, **kwargs):
  schema = onnx.defs.get_schema("ArrayFeatureExtractor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ArrayFeatureExtractor")(*args, **kwargs)


def Asin(*args, **kwargs):
  schema = onnx.defs.get_schema("Asin",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Asin")(*args, **kwargs)


def Asinh(*args, **kwargs):
  schema = onnx.defs.get_schema("Asinh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Asinh")(*args, **kwargs)


def Atan(*args, **kwargs):
  schema = onnx.defs.get_schema("Atan",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Atan")(*args, **kwargs)


def Atanh(*args, **kwargs):
  schema = onnx.defs.get_schema("Atanh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Atanh")(*args, **kwargs)


def AveragePool(*args, **kwargs):
  schema = onnx.defs.get_schema("AveragePool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.AveragePool")(*args, **kwargs)


def BatchNormalization(*args, **kwargs):
  schema = onnx.defs.get_schema("BatchNormalization",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.BatchNormalization")(*args, **kwargs)


def Binarizer(*args, **kwargs):
  schema = onnx.defs.get_schema("Binarizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Binarizer")(*args, **kwargs)


def BitShift(*args, **kwargs):
  schema = onnx.defs.get_schema("BitShift",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.BitShift")(*args, **kwargs)


def Cast(*args, **kwargs):
  schema = onnx.defs.get_schema("Cast",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Cast")(*args, **kwargs)


def CastMap(*args, **kwargs):
  schema = onnx.defs.get_schema("CastMap",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.CastMap")(*args, **kwargs)


def CategoryMapper(*args, **kwargs):
  schema = onnx.defs.get_schema("CategoryMapper",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.CategoryMapper")(*args, **kwargs)


def Ceil(*args, **kwargs):
  schema = onnx.defs.get_schema("Ceil",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Ceil")(*args, **kwargs)


def Celu(*args, **kwargs):
  schema = onnx.defs.get_schema("Celu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Celu")(*args, **kwargs)


def Clip(*args, **kwargs):
  schema = onnx.defs.get_schema("Clip",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Clip")(*args, **kwargs)


def Compress(*args, **kwargs):
  schema = onnx.defs.get_schema("Compress",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Compress")(*args, **kwargs)


def Concat(*args, **kwargs):
  schema = onnx.defs.get_schema("Concat",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Concat")(*args, **kwargs)


def ConcatFromSequence(*args, **kwargs):
  schema = onnx.defs.get_schema("ConcatFromSequence",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ConcatFromSequence")(*args, **kwargs)


def Constant(*args, **kwargs):
  schema = onnx.defs.get_schema("Constant",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Constant")(*args, **kwargs)


def ConstantOfShape(*args, **kwargs):
  schema = onnx.defs.get_schema("ConstantOfShape",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ConstantOfShape")(*args, **kwargs)


def Conv(*args, **kwargs):
  schema = onnx.defs.get_schema("Conv",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Conv")(*args, **kwargs)


def ConvInteger(*args, **kwargs):
  schema = onnx.defs.get_schema("ConvInteger",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ConvInteger")(*args, **kwargs)


def ConvTranspose(*args, **kwargs):
  schema = onnx.defs.get_schema("ConvTranspose",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ConvTranspose")(*args, **kwargs)


def Cos(*args, **kwargs):
  schema = onnx.defs.get_schema("Cos",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Cos")(*args, **kwargs)


def Cosh(*args, **kwargs):
  schema = onnx.defs.get_schema("Cosh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Cosh")(*args, **kwargs)


def CumSum(*args, **kwargs):
  schema = onnx.defs.get_schema("CumSum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.CumSum")(*args, **kwargs)


def DepthToSpace(*args, **kwargs):
  schema = onnx.defs.get_schema("DepthToSpace",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.DepthToSpace")(*args, **kwargs)


def DequantizeLinear(*args, **kwargs):
  schema = onnx.defs.get_schema("DequantizeLinear",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.DequantizeLinear")(*args, **kwargs)


def Det(*args, **kwargs):
  schema = onnx.defs.get_schema("Det",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Det")(*args, **kwargs)


def DictVectorizer(*args, **kwargs):
  schema = onnx.defs.get_schema("DictVectorizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.DictVectorizer")(*args, **kwargs)


def Div(*args, **kwargs):
  schema = onnx.defs.get_schema("Div",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Div")(*args, **kwargs)


def Dropout(*args, **kwargs):
  schema = onnx.defs.get_schema("Dropout",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Dropout")(*args, **kwargs)


def DynamicQuantizeLinear(*args, **kwargs):
  schema = onnx.defs.get_schema("DynamicQuantizeLinear",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.DynamicQuantizeLinear")(*args, **kwargs)


def Einsum(*args, **kwargs):
  schema = onnx.defs.get_schema("Einsum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Einsum")(*args, **kwargs)


def Elu(*args, **kwargs):
  schema = onnx.defs.get_schema("Elu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Elu")(*args, **kwargs)


def Equal(*args, **kwargs):
  schema = onnx.defs.get_schema("Equal",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Equal")(*args, **kwargs)


def Erf(*args, **kwargs):
  schema = onnx.defs.get_schema("Erf",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Erf")(*args, **kwargs)


def Exp(*args, **kwargs):
  schema = onnx.defs.get_schema("Exp",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Exp")(*args, **kwargs)


def Expand(*args, **kwargs):
  schema = onnx.defs.get_schema("Expand",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Expand")(*args, **kwargs)


def EyeLike(*args, **kwargs):
  schema = onnx.defs.get_schema("EyeLike",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.EyeLike")(*args, **kwargs)


def FeatureVectorizer(*args, **kwargs):
  schema = onnx.defs.get_schema("FeatureVectorizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.FeatureVectorizer")(*args, **kwargs)


def Flatten(*args, **kwargs):
  schema = onnx.defs.get_schema("Flatten",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Flatten")(*args, **kwargs)


def Floor(*args, **kwargs):
  schema = onnx.defs.get_schema("Floor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Floor")(*args, **kwargs)


def GRU(*args, **kwargs):
  schema = onnx.defs.get_schema("GRU",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GRU")(*args, **kwargs)


def Gather(*args, **kwargs):
  schema = onnx.defs.get_schema("Gather",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Gather")(*args, **kwargs)


def GatherElements(*args, **kwargs):
  schema = onnx.defs.get_schema("GatherElements",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GatherElements")(*args, **kwargs)


def GatherND(*args, **kwargs):
  schema = onnx.defs.get_schema("GatherND",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GatherND")(*args, **kwargs)


def Gemm(*args, **kwargs):
  schema = onnx.defs.get_schema("Gemm",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Gemm")(*args, **kwargs)


def GlobalAveragePool(*args, **kwargs):
  schema = onnx.defs.get_schema("GlobalAveragePool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GlobalAveragePool")(*args, **kwargs)


def GlobalLpPool(*args, **kwargs):
  schema = onnx.defs.get_schema("GlobalLpPool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GlobalLpPool")(*args, **kwargs)


def GlobalMaxPool(*args, **kwargs):
  schema = onnx.defs.get_schema("GlobalMaxPool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GlobalMaxPool")(*args, **kwargs)


def Gradient(*args, **kwargs):
  schema = onnx.defs.get_schema("Gradient",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Gradient")(*args, **kwargs)


def Greater(*args, **kwargs):
  schema = onnx.defs.get_schema("Greater",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Greater")(*args, **kwargs)


def GreaterOrEqual(*args, **kwargs):
  schema = onnx.defs.get_schema("GreaterOrEqual",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.GreaterOrEqual")(*args, **kwargs)


def HardSigmoid(*args, **kwargs):
  schema = onnx.defs.get_schema("HardSigmoid",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.HardSigmoid")(*args, **kwargs)


def HardSwish(*args, **kwargs):
  schema = onnx.defs.get_schema("HardSwish",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.HardSwish")(*args, **kwargs)


def Hardmax(*args, **kwargs):
  schema = onnx.defs.get_schema("Hardmax",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Hardmax")(*args, **kwargs)


def Identity(*args, **kwargs):
  schema = onnx.defs.get_schema("Identity",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Identity")(*args, **kwargs)


def If(*args, **kwargs):
  schema = onnx.defs.get_schema("If",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.If")(*args, **kwargs)


def Imputer(*args, **kwargs):
  schema = onnx.defs.get_schema("Imputer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Imputer")(*args, **kwargs)


def InstanceNormalization(*args, **kwargs):
  schema = onnx.defs.get_schema("InstanceNormalization",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.InstanceNormalization")(*args, **kwargs)


def IsInf(*args, **kwargs):
  schema = onnx.defs.get_schema("IsInf",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.IsInf")(*args, **kwargs)


def IsNaN(*args, **kwargs):
  schema = onnx.defs.get_schema("IsNaN",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.IsNaN")(*args, **kwargs)


def LRN(*args, **kwargs):
  schema = onnx.defs.get_schema("LRN",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LRN")(*args, **kwargs)


def LSTM(*args, **kwargs):
  schema = onnx.defs.get_schema("LSTM",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LSTM")(*args, **kwargs)


def LabelEncoder(*args, **kwargs):
  schema = onnx.defs.get_schema("LabelEncoder",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LabelEncoder")(*args, **kwargs)


def LeakyRelu(*args, **kwargs):
  schema = onnx.defs.get_schema("LeakyRelu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LeakyRelu")(*args, **kwargs)


def Less(*args, **kwargs):
  schema = onnx.defs.get_schema("Less",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Less")(*args, **kwargs)


def LessOrEqual(*args, **kwargs):
  schema = onnx.defs.get_schema("LessOrEqual",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LessOrEqual")(*args, **kwargs)


def LinearClassifier(*args, **kwargs):
  schema = onnx.defs.get_schema("LinearClassifier",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LinearClassifier")(*args, **kwargs)


def LinearRegressor(*args, **kwargs):
  schema = onnx.defs.get_schema("LinearRegressor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LinearRegressor")(*args, **kwargs)


def Log(*args, **kwargs):
  schema = onnx.defs.get_schema("Log",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Log")(*args, **kwargs)


def LogSoftmax(*args, **kwargs):
  schema = onnx.defs.get_schema("LogSoftmax",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LogSoftmax")(*args, **kwargs)


def Loop(*args, **kwargs):
  schema = onnx.defs.get_schema("Loop",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Loop")(*args, **kwargs)


def LpNormalization(*args, **kwargs):
  schema = onnx.defs.get_schema("LpNormalization",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LpNormalization")(*args, **kwargs)


def LpPool(*args, **kwargs):
  schema = onnx.defs.get_schema("LpPool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.LpPool")(*args, **kwargs)


def MatMul(*args, **kwargs):
  schema = onnx.defs.get_schema("MatMul",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MatMul")(*args, **kwargs)


def MatMulInteger(*args, **kwargs):
  schema = onnx.defs.get_schema("MatMulInteger",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MatMulInteger")(*args, **kwargs)


def Max(*args, **kwargs):
  schema = onnx.defs.get_schema("Max",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Max")(*args, **kwargs)


def MaxPool(*args, **kwargs):
  schema = onnx.defs.get_schema("MaxPool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MaxPool")(*args, **kwargs)


def MaxRoiPool(*args, **kwargs):
  schema = onnx.defs.get_schema("MaxRoiPool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MaxRoiPool")(*args, **kwargs)


def MaxUnpool(*args, **kwargs):
  schema = onnx.defs.get_schema("MaxUnpool",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MaxUnpool")(*args, **kwargs)


def Mean(*args, **kwargs):
  schema = onnx.defs.get_schema("Mean",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Mean")(*args, **kwargs)


def MeanVarianceNormalization(*args, **kwargs):
  schema = onnx.defs.get_schema("MeanVarianceNormalization",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.MeanVarianceNormalization")(*args, **kwargs)


def Min(*args, **kwargs):
  schema = onnx.defs.get_schema("Min",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Min")(*args, **kwargs)


def Mod(*args, **kwargs):
  schema = onnx.defs.get_schema("Mod",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Mod")(*args, **kwargs)


def Momentum(*args, **kwargs):
  schema = onnx.defs.get_schema("Momentum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Momentum")(*args, **kwargs)


def Mul(*args, **kwargs):
  schema = onnx.defs.get_schema("Mul",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Mul")(*args, **kwargs)


def Multinomial(*args, **kwargs):
  schema = onnx.defs.get_schema("Multinomial",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Multinomial")(*args, **kwargs)


def Neg(*args, **kwargs):
  schema = onnx.defs.get_schema("Neg",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Neg")(*args, **kwargs)


def NegativeLogLikelihoodLoss(*args, **kwargs):
  schema = onnx.defs.get_schema("NegativeLogLikelihoodLoss",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.NegativeLogLikelihoodLoss")(*args, **kwargs)


def NonMaxSuppression(*args, **kwargs):
  schema = onnx.defs.get_schema("NonMaxSuppression",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.NonMaxSuppression")(*args, **kwargs)


def NonZero(*args, **kwargs):
  schema = onnx.defs.get_schema("NonZero",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.NonZero")(*args, **kwargs)


def Normalizer(*args, **kwargs):
  schema = onnx.defs.get_schema("Normalizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Normalizer")(*args, **kwargs)


def Not(*args, **kwargs):
  schema = onnx.defs.get_schema("Not",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Not")(*args, **kwargs)


def OneHot(*args, **kwargs):
  schema = onnx.defs.get_schema("OneHot",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.OneHot")(*args, **kwargs)


def OneHotEncoder(*args, **kwargs):
  schema = onnx.defs.get_schema("OneHotEncoder",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.OneHotEncoder")(*args, **kwargs)


def Or(*args, **kwargs):
  schema = onnx.defs.get_schema("Or",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Or")(*args, **kwargs)


def PRelu(*args, **kwargs):
  schema = onnx.defs.get_schema("PRelu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.PRelu")(*args, **kwargs)


def Pad(*args, **kwargs):
  schema = onnx.defs.get_schema("Pad",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Pad")(*args, **kwargs)


def Pow(*args, **kwargs):
  schema = onnx.defs.get_schema("Pow",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Pow")(*args, **kwargs)


def QLinearConv(*args, **kwargs):
  schema = onnx.defs.get_schema("QLinearConv",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.QLinearConv")(*args, **kwargs)


def QLinearMatMul(*args, **kwargs):
  schema = onnx.defs.get_schema("QLinearMatMul",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.QLinearMatMul")(*args, **kwargs)


def QuantizeLinear(*args, **kwargs):
  schema = onnx.defs.get_schema("QuantizeLinear",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.QuantizeLinear")(*args, **kwargs)


def RNN(*args, **kwargs):
  schema = onnx.defs.get_schema("RNN",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RNN")(*args, **kwargs)


def RandomNormal(*args, **kwargs):
  schema = onnx.defs.get_schema("RandomNormal",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RandomNormal")(*args, **kwargs)


def RandomNormalLike(*args, **kwargs):
  schema = onnx.defs.get_schema("RandomNormalLike",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RandomNormalLike")(*args, **kwargs)


def RandomUniform(*args, **kwargs):
  schema = onnx.defs.get_schema("RandomUniform",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RandomUniform")(*args, **kwargs)


def RandomUniformLike(*args, **kwargs):
  schema = onnx.defs.get_schema("RandomUniformLike",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RandomUniformLike")(*args, **kwargs)


def Range(*args, **kwargs):
  schema = onnx.defs.get_schema("Range",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Range")(*args, **kwargs)


def Reciprocal(*args, **kwargs):
  schema = onnx.defs.get_schema("Reciprocal",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Reciprocal")(*args, **kwargs)


def ReduceL1(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceL1",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceL1")(*args, **kwargs)


def ReduceL2(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceL2",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceL2")(*args, **kwargs)


def ReduceLogSum(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceLogSum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceLogSum")(*args, **kwargs)


def ReduceLogSumExp(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceLogSumExp",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceLogSumExp")(*args, **kwargs)


def ReduceMax(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceMax",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceMax")(*args, **kwargs)


def ReduceMean(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceMean",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceMean")(*args, **kwargs)


def ReduceMin(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceMin",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceMin")(*args, **kwargs)


def ReduceProd(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceProd",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceProd")(*args, **kwargs)


def ReduceSum(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceSum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceSum")(*args, **kwargs)


def ReduceSumSquare(*args, **kwargs):
  schema = onnx.defs.get_schema("ReduceSumSquare",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReduceSumSquare")(*args, **kwargs)


def Relu(*args, **kwargs):
  schema = onnx.defs.get_schema("Relu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Relu")(*args, **kwargs)


def Reshape(*args, **kwargs):
  schema = onnx.defs.get_schema("Reshape",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Reshape")(*args, **kwargs)


def Resize(*args, **kwargs):
  schema = onnx.defs.get_schema("Resize",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Resize")(*args, **kwargs)


def ReverseSequence(*args, **kwargs):
  schema = onnx.defs.get_schema("ReverseSequence",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ReverseSequence")(*args, **kwargs)


def RoiAlign(*args, **kwargs):
  schema = onnx.defs.get_schema("RoiAlign",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.RoiAlign")(*args, **kwargs)


def Round(*args, **kwargs):
  schema = onnx.defs.get_schema("Round",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Round")(*args, **kwargs)


def SVMClassifier(*args, **kwargs):
  schema = onnx.defs.get_schema("SVMClassifier",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SVMClassifier")(*args, **kwargs)


def SVMRegressor(*args, **kwargs):
  schema = onnx.defs.get_schema("SVMRegressor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SVMRegressor")(*args, **kwargs)


def Scaler(*args, **kwargs):
  schema = onnx.defs.get_schema("Scaler",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Scaler")(*args, **kwargs)


def Scan(*args, **kwargs):
  schema = onnx.defs.get_schema("Scan",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Scan")(*args, **kwargs)


def Scatter(*args, **kwargs):
  schema = onnx.defs.get_schema("Scatter",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Scatter")(*args, **kwargs)


def ScatterElements(*args, **kwargs):
  schema = onnx.defs.get_schema("ScatterElements",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ScatterElements")(*args, **kwargs)


def ScatterND(*args, **kwargs):
  schema = onnx.defs.get_schema("ScatterND",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ScatterND")(*args, **kwargs)


def Selu(*args, **kwargs):
  schema = onnx.defs.get_schema("Selu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Selu")(*args, **kwargs)


def SequenceAt(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceAt",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceAt")(*args, **kwargs)


def SequenceConstruct(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceConstruct",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceConstruct")(*args, **kwargs)


def SequenceEmpty(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceEmpty",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceEmpty")(*args, **kwargs)


def SequenceErase(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceErase",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceErase")(*args, **kwargs)


def SequenceInsert(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceInsert",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceInsert")(*args, **kwargs)


def SequenceLength(*args, **kwargs):
  schema = onnx.defs.get_schema("SequenceLength",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SequenceLength")(*args, **kwargs)


def Shape(*args, **kwargs):
  schema = onnx.defs.get_schema("Shape",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Shape")(*args, **kwargs)


def Shrink(*args, **kwargs):
  schema = onnx.defs.get_schema("Shrink",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Shrink")(*args, **kwargs)


def Sigmoid(*args, **kwargs):
  schema = onnx.defs.get_schema("Sigmoid",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sigmoid")(*args, **kwargs)


def Sign(*args, **kwargs):
  schema = onnx.defs.get_schema("Sign",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sign")(*args, **kwargs)


def Sin(*args, **kwargs):
  schema = onnx.defs.get_schema("Sin",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sin")(*args, **kwargs)


def Sinh(*args, **kwargs):
  schema = onnx.defs.get_schema("Sinh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sinh")(*args, **kwargs)


def Size(*args, **kwargs):
  schema = onnx.defs.get_schema("Size",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Size")(*args, **kwargs)


def Slice(*args, **kwargs):
  schema = onnx.defs.get_schema("Slice",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Slice")(*args, **kwargs)


def Softmax(*args, **kwargs):
  schema = onnx.defs.get_schema("Softmax",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Softmax")(*args, **kwargs)


def SoftmaxCrossEntropyLoss(*args, **kwargs):
  schema = onnx.defs.get_schema("SoftmaxCrossEntropyLoss",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SoftmaxCrossEntropyLoss")(*args, **kwargs)


def Softplus(*args, **kwargs):
  schema = onnx.defs.get_schema("Softplus",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Softplus")(*args, **kwargs)


def Softsign(*args, **kwargs):
  schema = onnx.defs.get_schema("Softsign",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Softsign")(*args, **kwargs)


def SpaceToDepth(*args, **kwargs):
  schema = onnx.defs.get_schema("SpaceToDepth",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SpaceToDepth")(*args, **kwargs)


def Split(*args, **kwargs):
  schema = onnx.defs.get_schema("Split",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Split")(*args, **kwargs)


def SplitToSequence(*args, **kwargs):
  schema = onnx.defs.get_schema("SplitToSequence",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.SplitToSequence")(*args, **kwargs)


def Sqrt(*args, **kwargs):
  schema = onnx.defs.get_schema("Sqrt",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sqrt")(*args, **kwargs)


def Squeeze(*args, **kwargs):
  schema = onnx.defs.get_schema("Squeeze",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Squeeze")(*args, **kwargs)


def StringNormalizer(*args, **kwargs):
  schema = onnx.defs.get_schema("StringNormalizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.StringNormalizer")(*args, **kwargs)


def Sub(*args, **kwargs):
  schema = onnx.defs.get_schema("Sub",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sub")(*args, **kwargs)


def Sum(*args, **kwargs):
  schema = onnx.defs.get_schema("Sum",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Sum")(*args, **kwargs)


def Tan(*args, **kwargs):
  schema = onnx.defs.get_schema("Tan",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Tan")(*args, **kwargs)


def Tanh(*args, **kwargs):
  schema = onnx.defs.get_schema("Tanh",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Tanh")(*args, **kwargs)


def TfIdfVectorizer(*args, **kwargs):
  schema = onnx.defs.get_schema("TfIdfVectorizer",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.TfIdfVectorizer")(*args, **kwargs)


def ThresholdedRelu(*args, **kwargs):
  schema = onnx.defs.get_schema("ThresholdedRelu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ThresholdedRelu")(*args, **kwargs)


def Tile(*args, **kwargs):
  schema = onnx.defs.get_schema("Tile",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Tile")(*args, **kwargs)


def TopK(*args, **kwargs):
  schema = onnx.defs.get_schema("TopK",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.TopK")(*args, **kwargs)


def Transpose(*args, **kwargs):
  schema = onnx.defs.get_schema("Transpose",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Transpose")(*args, **kwargs)


def TreeEnsembleClassifier(*args, **kwargs):
  schema = onnx.defs.get_schema("TreeEnsembleClassifier",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.TreeEnsembleClassifier")(*args, **kwargs)


def TreeEnsembleRegressor(*args, **kwargs):
  schema = onnx.defs.get_schema("TreeEnsembleRegressor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.TreeEnsembleRegressor")(*args, **kwargs)


def Trilu(*args, **kwargs):
  schema = onnx.defs.get_schema("Trilu",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Trilu")(*args, **kwargs)


def Unique(*args, **kwargs):
  schema = onnx.defs.get_schema("Unique",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Unique")(*args, **kwargs)


def Unsqueeze(*args, **kwargs):
  schema = onnx.defs.get_schema("Unsqueeze",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Unsqueeze")(*args, **kwargs)


def Upsample(*args, **kwargs):
  schema = onnx.defs.get_schema("Upsample",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Upsample")(*args, **kwargs)


def Where(*args, **kwargs):
  schema = onnx.defs.get_schema("Where",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Where")(*args, **kwargs)


def Xor(*args, **kwargs):
  schema = onnx.defs.get_schema("Xor",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.Xor")(*args, **kwargs)


def ZipMap(*args, **kwargs):
  schema = onnx.defs.get_schema("ZipMap",
                                max_inclusive_version=OPSET_VER,
                                domain="")
  return getattr(sys.modules[f"{mod_name}.ops"], 
                 f"v{schema.since_version}.ZipMap")(*args, **kwargs)


__all__ = ["Input", "Output", "Abs", "Acos", "Acosh", "Adagrad", "Adam", "Add", "And", "ArgMax", "ArgMin", "ArrayFeatureExtractor", "Asin", "Asinh", "Atan", "Atanh", "AveragePool", "BatchNormalization", "Binarizer", "BitShift", "Cast", "CastMap", "CategoryMapper", "Ceil", "Celu", "Clip", "Compress", "Concat", "ConcatFromSequence", "Constant", "ConstantOfShape", "Conv", "ConvInteger", "ConvTranspose", "Cos", "Cosh", "CumSum", "DepthToSpace", "DequantizeLinear", "Det", "DictVectorizer", "Div", "Dropout", "DynamicQuantizeLinear", "Einsum", "Elu", "Equal", "Erf", "Exp", "Expand", "EyeLike", "FeatureVectorizer", "Flatten", "Floor", "GRU", "Gather", "GatherElements", "GatherND", "Gemm", "GlobalAveragePool", "GlobalLpPool", "GlobalMaxPool", "Gradient", "Greater", "GreaterOrEqual", "HardSigmoid", "HardSwish", "Hardmax", "Identity", "If", "Imputer", "InstanceNormalization", "IsInf", "IsNaN", "LRN", "LSTM", "LabelEncoder", "LeakyRelu", "Less", "LessOrEqual", "LinearClassifier", "LinearRegressor", "Log", "LogSoftmax", "Loop", "LpNormalization", "LpPool", "MatMul", "MatMulInteger", "Max", "MaxPool", "MaxRoiPool", "MaxUnpool", "Mean", "MeanVarianceNormalization", "Min", "Mod", "Momentum", "Mul", "Multinomial", "Neg", "NegativeLogLikelihoodLoss", "NonMaxSuppression", "NonZero", "Normalizer", "Not", "OneHot", "OneHotEncoder", "Or", "PRelu", "Pad", "Pow", "QLinearConv", "QLinearMatMul", "QuantizeLinear", "RNN", "RandomNormal", "RandomNormalLike", "RandomUniform", "RandomUniformLike", "Range", "Reciprocal", "ReduceL1", "ReduceL2", "ReduceLogSum", "ReduceLogSumExp", "ReduceMax", "ReduceMean", "ReduceMin", "ReduceProd", "ReduceSum", "ReduceSumSquare", "Relu", "Reshape", "Resize", "ReverseSequence", "RoiAlign", "Round", "SVMClassifier", "SVMRegressor", "Scaler", "Scan", "Scatter", "ScatterElements", "ScatterND", "Selu", "SequenceAt", "SequenceConstruct", "SequenceEmpty", "SequenceErase", "SequenceInsert", "SequenceLength", "Shape", "Shrink", "Sigmoid", "Sign", "Sin", "Sinh", "Size", "Slice", "Softmax", "SoftmaxCrossEntropyLoss", "Softplus", "Softsign", "SpaceToDepth", "Split", "SplitToSequence", "Sqrt", "Squeeze", "StringNormalizer", "Sub", "Sum", "Tan", "Tanh", "TfIdfVectorizer", "ThresholdedRelu", "Tile", "TopK", "Transpose", "TreeEnsembleClassifier", "TreeEnsembleRegressor", "Trilu", "Unique", "Unsqueeze", "Upsample", "Where", "Xor", "ZipMap"]