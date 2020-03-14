import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset

class PandasDataset(Dataset):
    
    def __init__(self, df):
        self.df = df
    
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        return self.df.iloc[idx, :].values


class XYDataset(PandasDataset):
    
    def __getitem__(self, idx):
        X = self.df.values[idx, 1:]
        Y = self.df.values[idx, 0]
        return X, Y


def ensure_pytorch(pytorch_or_numpy, half=False):
    """Ensure output is a pytorch object.
    ndarray: as_tensor
    tensor, model, optimizer, ...: remains the same
    """
    if isinstance(pytorch_or_numpy, (np.ndarray)):
        pytorch_tns = torch.as_tensor(pytorch_or_numpy)
    else:
        pytorch_tns = pytorch_or_numpy
    if half:
        pytorch_tns = pytorch_tns.half()
    return pytorch_tns

def make_device(device_name='cuda', verbose=False, cpu_only=False, half=False, non_blocking=True):
    """
    Detect device_count and make (GPU, CPU) function pairs:
        1. GPU(pytorch_or_numpy): Ensure a tensor in the device you want
        2. CPU(pytorch_tensor): Copy back to memory and convert into np.ndarray
        3. device name
    Usage:
        GPU, CPU, device = make_device()
    Notes:
        If something can be done with pytorch, you won't convert then into numpy.
        So ``.numpy()`` is always called automatically
    """
    if device_name=='cpu': # device=cpu implies ``cpu_only`` mode
        cpu_only = True
    if torch.cuda.device_count()>0 and (not cpu_only):
        _GPU_single = lambda pytorch_or_numpy: ensure_pytorch(pytorch_or_numpy, half).to(device_name, non_blocking=non_blocking)
        _CPU_single = lambda pytorch_tensor: pytorch_tensor.cpu().data.numpy()
    else:
        device_name = 'cpu'
        _GPU_single = lambda pytorch_or_numpy: ensure_pytorch(pytorch_or_numpy, half)
        _CPU_single = lambda pytorch_tensor: pytorch_tensor.data.numpy()
    def _many_to_many(fn_single):
        def fn_many(*args):
            if len(args)==1:
                return fn_single(args[0])
            return [fn_single(arg) for arg in args]
        return fn_many
    return _many_to_many(_GPU_single), _many_to_many(_CPU_single), device_name