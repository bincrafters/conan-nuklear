#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class NuklearConan(ConanFile):
    name = "nuklear"
    version = "1.0.0"
    url = "https://github.com/bincrafters/conan-nuklear"
    description = "A single-header ANSI C gui library"
    
    # Indicates License type of the packaged library
    license = "MIT"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/vurtun/nuklear"
        tools.get("{0}/archive/master.zip".format(source_url))
        extracted_dir = self.name + "-master"

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = self.source_subfolder
        self.copy(pattern="*.h", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
