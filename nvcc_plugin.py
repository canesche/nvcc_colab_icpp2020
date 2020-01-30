from nvcc.nvcc import NVCCPlugin as NVCC_V1

def load_ipython_extension(ip):
    nvcc_plugin = NVCC_V1(ip)
    ip.register_magics(nvcc_plugin)
