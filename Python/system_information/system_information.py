import sys
import os

print("Fom sys module:")
print("argv:", sys.argv)
print("api_version:", sys.api_version)
print("base_exec_prefix:", sys.base_exec_prefix)
print("base_prefix:", sys.base_prefix)
print("byteorder:", sys.byteorder)
print("exec_prefix:", sys.exec_prefix)
print("executable:", sys.executable)
print("flags:", sys.flags)
print("float_info:", sys.float_info)
print("float_repr_style:", sys.float_repr_style)
print("hash_info:", sys.hash_info)
print("int_info:", sys.int_info)
print("maxsize:", sys.maxsize)
print("path:", sys.path)
print("platform:", sys.platform)
print("prefix:", sys.prefix)
print("stderr:", sys.stderr)
print("stdout:", sys.stdout)
print("stdin:", sys.stdin)
print("version:", sys.version)
print("version_info:", sys.version_info)

print("\n\nFom os module:")
print("curdir:", os.curdir)
print("cpu_count:", os.cpu_count())
print("environ:", os.environ)
print("getpid:", os.getpid())
print("getppid:", os.getppid)
print("get_exec_path:", os.get_exec_path())
print("getcwd:", os.getcwd())
print("getcwdb:", os.getcwdb())
print("path:", os.path)
print("name:", os.name)
