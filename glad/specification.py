from glad.parse import Specification, Require


class EGL(Specification):
    DISPLAY_NAME = 'EGL'

    API = 'https://raw.githubusercontent.com/KhronosGroup/EGL-Registry/master/api/'
    NAME = 'egl'


class GL(Specification):
    DISPLAY_NAME = 'OpenGL'

    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'gl'

    def _magic_require(self, api, profile):
        require = Specification._magic_require(self, api, profile)

        magic_blacklist = (
            'stddef', 'khrplatform', 'inttypes',  # gl.xml
        )
        requirements = [r for r in require.requirements if r not in magic_blacklist]
        return Require(api, profile, requirements)


class GLX(Specification):
    DISPLAY_NAME = 'GLX'

    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'glx'


class WGL(Specification):
    DISPLAY_NAME = 'WGL'

    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'wgl'


class Vulkan(Specification):
    DISPLAY_NAME = 'Vulkan'

    API = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Docs/1.0/src/spec/'
    NAME = 'vk'

    def _magic_require(self, api, profile):
        # magic_categories = (
        #     'define', 'basetype', 'handle'
        # )
        #
        # requirements = [name for name, types in self.types.items()
        #                 if any(t.api in (None, api) and t.category in magic_categories for t in types)]
        #
        # return Require(api, profile, requirements)
        return None

    def _magic_are_enums_blacklisted(self, enums_element):
        # blacklist everything that has a type
        return enums_element.get('type') in ('enum', 'bitmask')