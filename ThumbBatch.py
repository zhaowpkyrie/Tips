from osgeo import gdal
import cv2
import numpy as np
import os
import tqdm


def create_thumbnail(input_file , output_file, nodata, ratio=0.1, background_color=[255, 255, 255]):
    # 打开tif文件
    dataset = gdal.Open(input_file)
    if dataset is None:
        print("Could not open input file")
        return
    # 获取图像的大小和波段数
    width = dataset.RasterXSize
    height = dataset.RasterYSize

    # 计算缩略图的大小
    new_width = int(width * ratio)
    new_height = int(height * ratio)

    options = "-of PNG -outsize %d %d -b 1 -b 2 -b 3" % (new_width, new_height)

    gdal.Translate(output_file, dataset, options=options)
    # 关闭文件
    dataset = None
    image = cv2.imread(output_file)

    if image is None:
        print("Could not open output file")
        return

    rows, cols, channels = image.shape
    for i in range(rows):
        for j in range(cols):
            if np.all(image[i, j] == nodata):
                for k in range(channels):
                    image[i, j, k] = background_color[k]
    cv2.imwrite(output_file, image)


if __name__ == '__main__':
    InputFoler = r"C:\Users\Administrator\桌面\ff"
    OutputFolder = r"D:\BaiduNetdiskDownload\oo"  #输出文件夹路径须为英文路径
    for file in tqdm.tqdm(os.listdir(InputFoler)):
        if file.endswith(".tif"):
            input_file = os.path.join(InputFoler, file)
            output_file = os.path.join(OutputFolder, file.split(".")[0] + "_thumb.png")
            create_thumbnail(input_file, output_file, nodata=0, ratio=0.1, background_color=[255,0, 255])

