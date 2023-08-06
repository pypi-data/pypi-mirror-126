from fds.utils import does_file_exist, execute_command, convert_bytes_to_string
from tests.it.helpers import IntegrationTestCase


class TestGit(IntegrationTestCase):

    def test_init_git(self):
        self.git_service.init()
        assert does_file_exist(f"{self.repo_path}/.git") is True

    def test_init_git_already_exists(self):
        execute_command(["git", "init"])
        assert does_file_exist(f"{self.repo_path}/.git") is True
        msg = self.git_service.init()
        assert msg == "git already initialized"

    def test_status(self):
        self.assertRaises(Exception, self.git_service.status)
        self.git_service.init()
        self.git_service.status()

    def test_add(self):
        self.git_service.init()
        super().create_fake_git_data()
        self.git_service.add(["."], [])
        output = execute_command(["git", "status"], capture_output=True)
        assert convert_bytes_to_string(output.stderr) == ""
        assert "new file:   git_data/file-0" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-1" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-2" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-3" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-4" in convert_bytes_to_string(output.stdout)

    def test_skip(self):
        self.git_service.init()
        super().create_fake_git_data()
        self.git_service.add(["."], ["./git_data"])
        output = execute_command(["git", "status"], capture_output=True)
        assert convert_bytes_to_string(output.stderr) == ""
        # This means untracked file
        assert "\n\tgit_data/\n\n" in convert_bytes_to_string(output.stdout)
        assert "new file:" not in convert_bytes_to_string(output.stdout)

    def test_add_one(self):
        self.git_service.init()
        super().create_fake_git_data()
        self.git_service.add(["git_data/file-0"], [])
        output = execute_command(["git", "status"], capture_output=True)
        assert convert_bytes_to_string(output.stderr) == ""
        assert "new file:   git_data/file-0" in convert_bytes_to_string(output.stdout)
        assert "Untracked files:" in convert_bytes_to_string(output.stdout)
        assert "file-1" in convert_bytes_to_string(output.stdout)
        assert "file-2" in convert_bytes_to_string(output.stdout)
        assert "file-3" in convert_bytes_to_string(output.stdout)
        assert "file-4" in convert_bytes_to_string(output.stdout)

    def test_add_multiple(self):
        self.git_service.init()
        super().create_fake_git_data()
        self.git_service.add(["git_data/file-0", "git_data/file-1", "git_data/file-3"], [])
        output = execute_command(["git", "status"], capture_output=True)
        assert convert_bytes_to_string(output.stderr) == ""
        assert "new file:   git_data/file-0" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-1" in convert_bytes_to_string(output.stdout)
        assert "new file:   git_data/file-3" in convert_bytes_to_string(output.stdout)
        assert "Untracked files:" in convert_bytes_to_string(output.stdout)
        assert "file-2" in convert_bytes_to_string(output.stdout)
        assert "file-4" in convert_bytes_to_string(output.stdout)

    def test_add_gitignore(self):
        self.git_service.init()
        super().create_fake_git_data()
        super().create_dummy_file(".gitignore", 100)
        self.git_service.add(["git_data/file-0"], [])
        output = execute_command(["git", "status"], capture_output=True)
        assert "new file:   git_data/file-0" in convert_bytes_to_string(output.stdout)
        assert "new file:   .gitignore" in convert_bytes_to_string(output.stdout)

    def test_commit(self):
        self.git_service.init()
        super().create_fake_git_data()
        self.git_service.add(["."], [])
        self.git_service.commit("Commit 1")
        output = execute_command(["git", "log", "--oneline"], capture_output=True)
        assert "Commit 1" in convert_bytes_to_string(output.stdout)

    def test_clone(self):
        self.git_service.clone(self.get_remote_url_for_test(), None)
        # Check git clone
        assert does_file_exist(f"{self.repo_path}/hello-world")

    def test_clone_with_dir(self):
        self.git_service.clone(self.get_remote_url_for_test(), "test")
        # Check git clone
        assert does_file_exist(f"{self.repo_path}/test")

    def test_get_repo_path(self):
        self.git_service.init()
        path = self.git_service.get_repo_path()
        assert path == self.repo_path
        self.create_dummy_folder("test_git")
        path = self.git_service.get_repo_path()
        assert path == self.repo_path
