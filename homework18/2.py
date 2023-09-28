import sys
import io

original_stdout = sys.stdout
string_io_buffer = io.StringIO()
sys.stdout = string_io_buffer
print("Це виведено у буфер")
output_content = string_io_buffer.getvalue()
sys.stdout = original_stdout

print("Зміст буфера:")
print(output_content)
