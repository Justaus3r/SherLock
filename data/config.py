args = {
    'im_size': 256,
    'batch_size': 128,
    'num_channels': 3,
    'malnet_tiny': False,
    'group': 'binary',  # options: binary, type, family
    'color_mode': 'rgb',  # options: rgb, grayscale

    'seed': 1,
    'devices': [0],

    'groups' : ['binary'], # binary, 'type', 'family'
    'data_dir': '/content/data_dir/',  # symbolic link directory
    'image_dir': '/content/dataset/malnet-images/',  # path where data is located
    'dataset_type': 'val', # all, train, test, val
    'symbolic': False


}
