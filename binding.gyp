{
    "targets": [
        {
            "target_name": "esptk",
            "sources": [
                "node_modules/esptk/src/espfile.cpp",
                "node_modules/esptk/src/record.cpp",
                "node_modules/esptk/src/subrecord.cpp",
                "string_cast.cpp",
                "index.cpp"
            ],
            "include_dirs": [
                "<!(node -p \"require('node-addon-api').include_dir\")",
                "node_modules/esptk/src"
            ],
            "dependencies": [
              "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            'cflags!': ['-fno-exceptions'],
            'cflags_cc!': ['-fno-exceptions'],
            'cflags_cc': ['-std=c++17'],
            'msbuild_settings': {
              'ClCompile': {
                'AdditionalOptions': ['-std:c++17']
              }
            },
            'conditions': [
                ['OS=="win"', {
                    'defines!': [
                        '_HAS_EXCEPTIONS=0'
                    ],
                    'defines': [
                        'BUILDING_NODE_EXTENSION'
                    ],
                    'libraries': [
                      '-DelayLoad:node.exe',
                    ],
                    'msvs_settings': {
                        'VCCLCompilerTool': {
                            'ExceptionHandling': 1,
                            'RuntimeLibrary': 0
                        },
                        "VCLibrarianTool": {
                          'AdditionalOptions': [ '/LTCG' ]
                        },
                        'VCLinkerTool': {
                          'LinkTimeCodeGeneration': 1
                        }
                    },
                    "msbuild_settings": {
                      "ClCompile": {
                        "AdditionalOptions": ["-std:c++17", "/MT"],
                        "RuntimeLibrary": "MultiThreaded"
                      }
                    }
                }],
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                    }
                }]
            ]
        }
    ]
}
