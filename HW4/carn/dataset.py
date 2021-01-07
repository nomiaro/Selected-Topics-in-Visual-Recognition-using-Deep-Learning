import os
import glob
import h5py
import random
import numpy as np
from PIL import Image
import torch.utils.data as data
import torchvision.transforms as transforms

def random_crop(hr, lr, size, scale):
    h, w = lr.shape[:-1]
    x = random.randint(0, w-size)
    y = random.randint(0, h-size)

    hsize = size*scale
    hx, hy = x*scale, y*scale

    crop_lr = lr[y:y+size, x:x+size].copy()
    crop_hr = hr[hy:hy+hsize, hx:hx+hsize].copy()

    return crop_hr, crop_lr


def random_flip_and_rotate(im1, im2):
    if random.random() < 0.5:
        im1 = np.flipud(im1)
        im2 = np.flipud(im2)

    if random.random() < 0.5:
        im1 = np.fliplr(im1)
        im2 = np.fliplr(im2)

    angle = random.choice([0, 1, 2, 3])
    im1 = np.rot90(im1, angle)
    im2 = np.rot90(im2, angle)

    # have to copy before be called by transform function
    return im1.copy(), im2.copy()


def rescale_img(img_in, scale):
    size_in = img_in.size
    new_size_in = tuple([int(x * scale) for x in size_in])
    img_in = img_in.resize(new_size_in, resample=Image.BICUBIC)
    return img_in


class TrainDataset(data.Dataset):
    def __init__(self, path, size, scale):
        super(TrainDataset, self).__init__()

        self.size = size
        #h5f = h5py.File(path, "r")
        
        #self.hr = [v[:] for v in h5f["HR"].values()]
        self.hr = [os.path.join(path, x) for x in os.listdir(path)]
        # perform multi-scale training
        '''
        if scale == 0:
            self.scale = [2, 3, 4]
            self.lr = [[v[:] for v in h5f["X{}".format(i)].values()] for i in self.scale]
        else:
            self.scale = [scale]
            self.lr = [[v[:] for v in h5f["X{}".format(scale)].values()]]
        
        h5f.close()
        '''
        self.scale = [scale]

        self.transform = transforms.Compose([
            transforms.ToTensor()
        ])

    def __getitem__(self, index):
        size = self.size

        hr_image = Image.open(self.hr[index]).convert('RGB')
        lr_image = hr_image.resize((int(hr_image.size[0]/self.scale[0]),int(hr_image.size[1]/self.scale[0])), Image.BICUBIC)
        hr = np.array(hr_image)
        lr = np.array(lr_image)

        item = [(hr, lr)]
        item = [random_crop(hr, lr, size, self.scale[i]) for i, (hr, lr) in enumerate(item)]
        item = [random_flip_and_rotate(hr, lr) for hr, lr in item]
        
        return [(self.transform(hr), self.transform(lr)) for hr, lr in item]

    def __len__(self):
        return len(self.hr)
        

class TestDataset(data.Dataset):
    def __init__(self, dirname, scale):
        super(TestDataset, self).__init__()

        #self.name  = dirname.split("/")[-1]
        self.lr = [os.path.join(dirname, x) for x in os.listdir(dirname)]
        self.scale = scale
        
        '''
        if "DIV" in self.name:
            self.hr = glob.glob(os.path.join("{}_HR".format(dirname), "*.png"))
            self.lr = glob.glob(os.path.join("{}_LR_bicubic".format(dirname), 
                                             "X{}/*.png".format(scale)))
        else:
            all_files = glob.glob(os.path.join(dirname, "x{}/*.png".format(scale)))
            self.hr = [name for name in all_files if "HR" in name]
            self.lr = [name for name in all_files if "LR" in name]

        self.hr.sort()
        self.lr.sort()
        '''

        self.transform = transforms.Compose([
            transforms.ToTensor()
        ])

    def __getitem__(self, index):
        #hr = Image.open(self.hr[index])
        lr = Image.open(self.lr[index])

        #hr = hr.convert("RGB")
        lr = lr.convert("RGB")
        hr = rescale_img(lr, self.scale)
        filename = self.lr[index].split("/")[-1]

        return self.transform(hr), self.transform(lr), filename

    def __len__(self):
        return len(self.lr)
