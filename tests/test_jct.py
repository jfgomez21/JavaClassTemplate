import unittest

import vim
import jct

class TestJct(unittest.TestCase):
    def setUp(self):
        vim.current.buffer.clear()
        vim.current.buffer.append("")

    def assert_vim_buffer(self, expected):
       #self.assertEqual(len(expected), len(vim.current.buffer))

       for i in range(len(expected)):
           self.assertEqual(expected[i], vim.current.buffer[i])

    def test_jct_template(self):
       jct.jct_template()

       expected = [
            "package abc;",
            "",
            "public class Main {",
            "\t",
            "}"
       ]

       self.assert_vim_buffer(expected)

    def test_jct_template_with_test_class(self):
        vim.set_cwd("/path/to/your/project", "src/test/java/abc/TestMain.java")

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "import org.junit.Test;",
            "",
            "import static org.junit.Assert.*;",
            "",
            "public class TestMain {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_class_in_test_package(self):
        vim.set_cwd("/path/to/your/project", "src/test/java/abc/Main.java")

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "public class Main {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_module(self):
        vim.set_cwd("/path/to/your/project", "module-name/src/main/java/abc/Main.java")

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "public class Main {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_module_and_test_class(self):
        vim.set_cwd("/path/to/your/project", "module-name/src/test/java/abc/TestMain.java")

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "import org.junit.Test;",
            "",
            "import static org.junit.Assert.*;",
            "",
            "public class TestMain {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_windows(self):
        vim.set_cwd("C:/path/to/your/project", "src/main/java/abc/Main.java")
        vim.set_win32(True)

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "public class Main {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)


