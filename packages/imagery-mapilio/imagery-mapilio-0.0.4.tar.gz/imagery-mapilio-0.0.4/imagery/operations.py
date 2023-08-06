import os
import numpy as np
import cv2

from helper.generator import Generator
from calculation.pixel import Pixel
from imagery.postprocessor import PostProcessor
from addict import Dict

class Operation:

    @staticmethod
    def image_write(outPath: str, image: np.ndarray, name: str):
        name_output = f"{name}.jpeg"
        cv2.imwrite(os.path.join(outPath, name_output), image, [cv2.IMWRITE_JPEG_QUALITY, 80])

    @staticmethod
    def image_action(**kwargs) -> (str, np.ndarray, float):
        """

        Args:
            image:
            finalBox: detected object bounding box
            class_name: detected objects category name
            writePaths: where will it write
            rgb_mask:
            copyImage:
            config:
            score:
            file_id: specif prediction dir id

        Returns:
            write local directory, detected objects as a array, pca angle
        """
        params = Dict(kwargs)

        xmin, ymin, xmax, ymax = [int(item) for item in params.finalBox]
        image_pca, image_rgb = PostProcessor.image_coloring(params.image, params.rgb_mask)
        detectedObject_pca = image_pca[ymin:ymax, xmin:xmax]
        # detectedObject = image_rgb[ymin:ymax, xmin:xmax]
        detectedObject = params.copyImage[ymin:ymax, xmin:xmax] # if detectedObject dont want color open this
        del image_pca
        angle_pca = Pixel.get_angle_pca(detectedObject_pca)

        if params.config.processedimageWrite:
            cX = int((xmin + xmax) / 2)
            cY = int((ymin + ymax) / 2)

            cv2.putText(image_rgb, params.class_code, (cX, cY),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.putText(image_rgb, str(params.score), (cX + 10, cY + 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            cv2.putText(image_rgb, params.objectId, (cX + 20, cY + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            cv2.rectangle(image_rgb, (xmin, ymin), (xmax, ymax), (255, 0, 255), thickness=2)

        imageNumber = os.path.basename(params.writePaths[1]).split(".")[0]
        imageSaveType = os.path.basename(params.writePaths[1]).split(".")[1]
        saveName = imageNumber + "_{}.".format(Generator.unique_matchId_generator()) + imageSaveType
        detectedObjectPath = os.path.join("Exports", params.file_id, "ObjectsImage", saveName)
        cv2.imwrite(detectedObjectPath, detectedObject)

        del params.copyImage

        return detectedObjectPath, image_rgb, angle_pca

    @staticmethod
    def image_read_rgb(detectedObjectPath: str) -> np.ndarray:
        return cv2.imread(detectedObjectPath)

    @staticmethod
    def image_read_rgb_as_gray(detectedObjectPath: str) -> np.ndarray:
        return cv2.imread(detectedObjectPath, 0)