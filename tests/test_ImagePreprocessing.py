import unittest
import scr.ImagePreprocessing as ip
from cv2 import cv2
import os

class TestImagePreprocessing(unittest.TestCase):

    def testgetHorizontalProjectionSegmentationPoints_1(self):
        filepath = './data/testimg/testimg_1.png'
        img = ip.imgReadAndConvert(filepath)
        H_Start, H_End = ip.getHorizontalProjectionSegmentationPoints(img)
        self.assertEqual(len(H_Start), 1)
        self.assertEqual(len(H_End), 1)

    def testgetHorizontalProjectionSegmentationPoints_2(self):
        filepath = './data/testimg/testimg_2.png'
        img = ip.imgReadAndConvert(filepath)
        H_Start, H_End = ip.getHorizontalProjectionSegmentationPoints(img)
        self.assertEqual(len(H_Start), 1)
        self.assertEqual(len(H_End), 1)

    def testgetHorizontalProjectionSegmentationPoints_3(self):
        filepath = './data/testimg/testimg_3.png'
        img = ip.imgReadAndConvert(filepath)
        H_Start, H_End = ip.getHorizontalProjectionSegmentationPoints(img)
        self.assertEqual(len(H_Start), 3)
        self.assertEqual(len(H_End), 3)

    def testgetVerticalProjectionSegmentationPoints_1(self):
        filepath = './data/testimg/testimg_1.png'
        img = ip.imgReadAndConvert(filepath)
        W_Start, W_End = ip.getVerticalProjectionSegmentationPoints(img)
        self.assertEqual(len(W_Start), 4)
        self.assertEqual(len(W_End), 4)

    def testgetVerticalProjectionSegmentationPoints_2(self):
        filepath = './data/testimg/testimg_2.png'
        img = ip.imgReadAndConvert(filepath)
        W_Start, W_End = ip.getVerticalProjectionSegmentationPoints(img)
        self.assertEqual(len(W_Start), 12)
        self.assertEqual(len(W_End), 12)

    def testgetVerticalProjectionSegmentationPoints_3(self):
        filepath = './data/testimg/testimg_3.png'
        img = ip.imgReadAndConvert(filepath)
        W_Start, W_End = ip.getVerticalProjectionSegmentationPoints(img)
        self.assertEqual(len(W_Start), 1)
        self.assertEqual(len(W_End), 1)

    def testProjectionSegmentation_1(self):
        filepath = './data/testimg/testimg_1.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        self.assertEqual(len(imgs), 4)
        self.assertEqual(len(Position), 4)

    def testProjectionSegmentation_2(self):
        filepath = './data/testimg/testimg_2.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        self.assertEqual(len(imgs), 12)
        self.assertEqual(len(Position), 12)

    def testProjectionSegmentation_3(self):
        filepath = './data/testimg/testimg_3.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        self.assertEqual(len(imgs), 6)
        self.assertEqual(len(Position), 6)

    def testImgStandardize_1(self):
        filepath = './data/testimg/testimg_1.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        standard_imgs = ip.imgStandardize(imgs,Position)
        self.assertEqual(len(standard_imgs), 4)
        for i in range(len(standard_imgs)):
             h,w =standard_imgs[i]['segment_img'].shape[:2]
             self.assertEqual(h,32)
             self.assertEqual(w,32)

    def testImgStandardize_2(self):
        filepath = './data/testimg/testimg_2.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        standard_imgs = ip.imgStandardize(imgs,Position)
        self.assertEqual(len(standard_imgs), 12)
        for i in range(len(standard_imgs)):
             h,w =standard_imgs[i]['segment_img'].shape[:2]
             self.assertEqual(h,32)
             self.assertEqual(w,32)

    def testImgStandardize_3(self):
        filepath = './data/testimg/testimg_3.png'
        img = ip.imgReadAndConvert(filepath)
        imgs, Position = ip.projectionSegmentation(img)
        standard_imgs = ip.imgStandardize(imgs,Position)
        self.assertEqual(len(standard_imgs), 6)
        for i in range(len(standard_imgs)):
             h,w =standard_imgs[i]['segment_img'].shape[:2]
             self.assertEqual(h,32)
             self.assertEqual(w,32)

    def testGroundTruthParser_1(self):
        ground_truth = [r'$1\pm 134 \div \pi$']
        gt_list = ip.groundTruthParser(ground_truth)
        self.assertEqual(len(gt_list),7)

    def testGroundTruthParser_2(self):
        ground_truth = [r'$1\pm 20- 173$']
        gt_list = ip.groundTruthParser(ground_truth)
        self.assertEqual(len(gt_list),8)

    def testReadCharacterListFromInkmlFile_1(self):
        filepath = './data/testimg/testinkml_1.inkml'
        gt = ip.readCharacterListFromInkmlFile(filepath)
        self.assertEqual(len(gt),9)

    def testReadCharacterListFromInkmlFile_2(self):
        filepath = './data/testimg/testinkml_2.inkml'
        gt = ip.readCharacterListFromInkmlFile(filepath)
        self.assertEqual(len(gt),5)

    def testReadCharacterListFromInkmlFile_3(self):
        filepath = './data/testimg/testinkml_3.inkml'
        gt = ip.readCharacterListFromInkmlFile(filepath)
        self.assertEqual(len(gt),4)