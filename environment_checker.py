import sys
import platform


print("=== AI Research Environment Checker ===")

print()
print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)

print()
print("Operating system:", platform.system())
print("Architecture:", platform.machine())

print()
print("Environment check complete.")