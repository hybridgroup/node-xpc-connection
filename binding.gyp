{
  'targets': [
    {
      'target_name': "binding",
      'conditions': [
        ['OS=="mac"', {
          'sources': [
            'src/XpcConnection.cpp'
          ],
          # cflags on OS X are stupid and have to be defined like this
          'defines': [
            '_FILE_OFFSET_BITS=64',
            '_LARGEFILE_SOURCE'
          ],
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-Wall',
              '-ObjC++'
            ]
          }
        }]
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
