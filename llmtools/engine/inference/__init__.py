#from quant_cuda import matvmul2, matvmul3, matvmul4, matvmul8
from torch.utils.cpp_extension import CppExtension
quant_cuda = CppExtension(name='quant_cuda', sources=['cuda/quant_cuda.cpp'])