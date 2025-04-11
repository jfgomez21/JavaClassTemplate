import os
import pathlib
import vim 

#TODO - determine base class for test classes

def jct_template():
    cwd = vim.eval("getcwd()")
    filename = vim.current.buffer.name
    is_windows = vim.eval("has('win32')") == '1'

    if is_windows:
        cwd = pathlib.Path(cwd).as_posix()
        filename = pathlib.Path(filename).as_posix()

    relative_name = filename.replace("{0}/".format(cwd), "")

    if not relative_name.startswith("src/"):
        index = relative_name.find("/src/")

        module_name = relative_name[:index]
        relative_name = relative_name[len(module_name) + 1:]

    base_name = os.path.basename(filename)
    class_name = base_name.replace(".java", "")
    
    is_test_package = relative_name.startswith("src/test/")
    is_test_class = is_test_package and class_name.startswith("Test") 

    if is_test_package:
        path = "src/test/java/"
    else:
        path = "src/main/java/"

    package_name = relative_name.replace(path, "").replace("/{0}".format(base_name), "").replace("/", ".")

    vim.current.buffer[0] = "package {0};".format(package_name)
    vim.current.buffer.append("")

    if is_test_class:
        vim.current.buffer.append("import org.junit.Test;")
        vim.current.buffer.append("")
        vim.current.buffer.append("import static org.junit.Assert.*;")
        vim.current.buffer.append("")
    
    vim.current.buffer.append("public class {0} {{".format(class_name))
    vim.current.buffer.append("\t")
    vim.current.buffer.append("}")

    vim.eval("cursor({0}, {1})".format(len(vim.current.buffer) - 1, 1))
