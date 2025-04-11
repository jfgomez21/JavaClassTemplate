import unittest

import vim
import jct

class TestJct(unittest.TestCase):
    def setUp(self):
        vim.current.buffer.clear()
        vim.current.buffer.append("")

        vim.clear_base_test_classes()

    def assert_vim_buffer(self, expected):
       for i in range(min(len(expected), len(vim.current.buffer))):
           self.assertEqual(expected[i], vim.current.buffer[i])
        
       self.assertEqual(len(expected), len(vim.current.buffer))

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

    def test_jct_template_with_base_test_class(self):
        vim.set_cwd("/path/to/your/project", "src/test/java/abc/def/TestMain.java")
        vim.set_base_test_classes("", "abc.AbstractBaseTest")

        jct.jct_template()

        expected = [
            "package abc.def;",
            "",
            "import abc.AbstractBaseTest;",
            "import org.junit.Test;",
            "",
            "import static org.junit.Assert.*;",
            "",
            "public class TestMain extends AbstractBaseTest {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_module_name_and_base_test_class(self):
        vim.set_cwd("/path/to/your/project", "services-module/src/test/java/abc/def/TestMain.java")
        vim.set_base_test_classes("services-module", "abc.AbstractBaseTest")

        jct.jct_template()

        expected = [
            "package abc.def;",
            "",
            "import abc.AbstractBaseTest;",
            "import org.junit.Test;",
            "",
            "import static org.junit.Assert.*;",
            "",
            "public class TestMain extends AbstractBaseTest {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)

    def test_jct_template_with_base_test_class_in_same_package(self):
        vim.set_cwd("/path/to/your/project", "src/test/java/abc/TestMain.java")
        vim.set_base_test_classes("", "abc.AbstractBaseTest")

        jct.jct_template()

        expected = [
            "package abc;",
            "",
            "import org.junit.Test;",
            "",
            "import static org.junit.Assert.*;",
            "",
            "public class TestMain extends AbstractBaseTest {",
            "\t",
            "}"
        ]

        self.assert_vim_buffer(expected)
