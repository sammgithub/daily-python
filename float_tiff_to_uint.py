######### SERAJ Mostafa @UMBC #########
######## using gdal, numpy ############
#### convert from float tiff to png ###

from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean
from osgeo import gdal
import os

output_dir = '/output/dir/path/'

def convert(src, dest): ## src dest are the source and destnation
    
    ds = gdal.Open(src) ## the src is passed so that it can open from this src
    top = ds.GetRasterBand(1).ReadAsArray()
    top.shape
    print(top)
    top.min(), top.max()

    top_mul=top*10000
    print(top_mul)
    top_res=top_mul.astype(np.int16)
    print(top_res)

    fig, axes=plt.subplots(1,1, figsize=(30,15))
    axes.imshow(top, cmap='gray')

    fig, axes=plt.subplots(1,1, figsize=(30,15))
    axes.imshow(top_res, cmap='gray')

    [rows, cols] = top_res.shape

    driver = gdal.GetDriverByName("GTiff")
    # outdata = driver.Create(dest, cols, rows, 1, gdal.GDT_UInt16)
    outdata = driver.Create(dest, cols, rows, 1, gdal.GDT_Byte)

    outdata.SetGeoTransform(ds.GetGeoTransform())##sets same geotransform as input
    outdata.SetProjection(ds.GetProjection())##sets same projection as input
    outdata.GetRasterBand(1).WriteArray(top_res)
    outdata.GetRasterBand(1).SetNoDataValue(10000)##if you want these values transparent
    outdata.FlushCache() ##saves to disk!!

    # read = './converted_to_unit16.tif'
    # ds = gdal.Open(read)
    # read_new = ds.GetRasterBand(1).ReadAsArray()
    # print(read_new)

    # fig, axes=plt.subplots(1,1, figsize=(30,15))
    # axes.imshow(read_new, cmap='gray')

def main():
    files = list(os.scandir('/src/dir/path/'))
    for file in files:
        convert(file.path, f'{output_dir}{file.name}') ## '''file.path and file.name are file properties coming from os.scandir. test is python as>> os.scandir('.');file = next(os.scandir('.'));dir(file)<< it will show available options. AND <f'{output_dir}{file.name}> gives you the files in the same names in a new dest'''

main()
