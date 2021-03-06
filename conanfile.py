from conans import ConanFile, CMake, tools
import os


class ToluappConan(ConanFile):
    name = "toluapp"
    version = "1.0.93"
    license = "MIT"
    author = "konrad.no.tantoo"
    url = "https://github.com/KonradNoTantoo/toluapp_conan"
    description = "tolua++ is an extension of toLua, a tool to integrate C/C++ code with Lua."
    topics = ("conan", "lua", "code binding")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    folder_name = "{}-{}".format(name, version)
    requires = ["lua/5.1.5@utopia/testing"]


    def source(self):
        tools.get("https://github.com/LuaDist/toluapp/archive/1.0.93.tar.gz")
        tools.replace_in_file("{}/CMakeLists.txt".format(self.folder_name), "project ( toluapp C )",
                              '''project ( toluapp C )
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')


    def configure_cmake(self):
        cmake = CMake(self)

        if self.settings.compiler != "Visual Studio":
            # toluapp's FindLua.cmake forgets dl system lib
            # we have to override LUA_LIBRARIES for linkage to work
            cmake.definitions["LUA_LIBRARIES"] = "lua;dl;m"
            if self.settings.arch != "x86":
                cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"

        cmake.configure(source_folder=self.folder_name)
        return cmake


    def build(self):
        cmake = self.configure_cmake()
        cmake.build()


    def package(self):
        cmake = self.configure_cmake()
        cmake.install()


    def package_info(self):
        self.cpp_info.libs = ["toluapp"]
        bindir = os.path.join(self.package_folder, "bin")
        self.output.info("Appending to PATH environment variable: {}".format(bindir))
        self.env_info.path.append(bindir)
